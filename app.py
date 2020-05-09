import os
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.secret_key = 'some_secret'

app.config["MONGO_DBNAME"] = 'cook_book'
app.config["MONGO_URI"] = 'mongodb+srv://root:Rundle18@myfirstcluster-6cjbt.mongodb.net/cook_book?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/recipe')
def recipe():
    return render_template("index.html", page_title="Home Page", recipes=mongo.db.recipes.find())

@app.route('/search')
def search():
    query = request.form['recipes']
    text_results = mongo.db.command('text', 'posts', search=query, limit=SEARCH_LIMIT)
    doc_matches = (res['obj'] for res in text_results['results'])
    return render_template("index.html", results=results)


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("editrecipe.html", recipes=recipe, page_title="Results")

@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'Recipe':request.form.get('Recipe'),
        'Cuisine':request.form.get('Cuisne'),
        'base':request.form.get('base'),
        'meat':request.form.get('meat'),
        'sauce':request.form.get('sauce'),
        'spice':request.form.get('spice'),
        'vegetable':request.form.get('vegetable'),
        'Instructions':request.form.get('Instructions')
    })
    return redirect(url_for('recipe'))

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('recipe'))

@app.route('/addrecipe')
def addrecipe():
    bases = mongo.db.bases.find()
    meats = mongo.db.meats.find()
    sauces = mongo.db.sauces.find()
    spices = mongo.db.spices.find()
    vegetables = mongo.db.vegetables.find()
    return render_template("addrecipe.html", page_title="Add A Recipe", bases=mongo.db.bases.find(), meats=mongo.db.meats.find(), sauces=mongo.db.sauces.find(), spices=mongo.db.spices.find(), vegetables=mongo.db.vegetables.find())

@app.route('/addrecipe_add', methods=['POST'])
def addrecipe_add():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    if request.method == "POST":
         flash("Thank you for adding your recipe!"),
    return redirect(url_for('recipe'))




if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            debug=True)