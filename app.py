import os
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_PASS")

app.config["MONGO_DBNAME"] = 'cook_book'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)

@app.route('/')
@app.route('/recipe')
def recipe():
    return render_template("index.html", page_title="Home Page", recipes=mongo.db.recipes.find())


@app.route('/search')
def search():
    query = request.args.get["results"]
    results = mongo.db.recipes.find({"recipes" : {"$regex": query}})
    return render_template("index.html", recipes=results)


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    bases = mongo.db.bases.find()
    meats = mongo.db.meats.find()
    sauces = mongo.db.sauces.find()
    spices = mongo.db.spices.find()
    vegetables = mongo.db.vegetables.find()
    return render_template("editrecipe.html", recipes=recipe, bases=mongo.db.bases.find(), meats=mongo.db.meats.find(), sauces=mongo.db.sauces.find(), spices=mongo.db.spices.find(), vegetables=mongo.db.vegetables.find(), page_title="Results")

@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'Recipe':request.form.get('Recipe'),
        'Cuisine':request.form.get('Cuisne'),
        'Description':request.form.get('Description'),
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