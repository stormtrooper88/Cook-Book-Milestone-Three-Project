import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'cook_book'
app.config["MONGO_URI"] = 'mongodb+srv://root:Rundle18@myfirstcluster-6cjbt.mongodb.net/cook_book?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/recipe')
def recipe():
    return render_template("index.html", page_title="Home Page")

@app.route('/browse')
def browse():
    return render_template("browse.html", page_title="Browse")

@app.route('/addrecipe')
def addrecipe():
    bases = mongo.db.bases.find()
    meats = mongo.db.meats.find()
    sauces = mongo.db.sauces.find()
    spices = mongo.db.spices.find()
    vegetables = mongo.db.vegetables.find()
    return render_template("addrecipe.html", page_title="Add A Recipe", bases=mongo.db.bases.find(), meats=mongo.db.meats.find(), sauces=mongo.db.sauces.find(), spices=mongo.db.spices.find(), vegetables=mongo.db.vegetables.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            debug=True)