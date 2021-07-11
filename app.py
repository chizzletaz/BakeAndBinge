import os
from flask import (
    Flask, flash, render_template, redirect, 
    request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date
if os.path.exists("env.py"):
    import env

# create an instance of Flask:
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# create an instance of PyMongo:
mongo = PyMongo(app)


# HOME
@app.route("/")
@app.route("/home")
def home():
    recipes = list(mongo.db.recipes.find().sort("date_added", -1).limit(6))
    # Credit for the relations between collections using ObjectId: my mentor, Antonio Rodriguez
    # Since in the recipe collection, the category_name is stored as the ObjectId of the 
    # category_name in the category collection, we have to convert the ObjectId-number
    # of the category name to the category name itself
    for recipe in recipes:
        category = mongo.db.categories.find_one({'_id': ObjectId(recipe['category_name'])})
        recipe['category_name'] = category['category_name']
        user = mongo.db.users.find_one({'_id': ObjectId(recipe['created_by'])})
        recipe['created_by'] = user['username']

    # Getting all the category names 
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("index.html", recipes=recipes, categories=categories)


# SEARCH
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    for recipe in recipes:
        category = mongo.db.categories.find_one({'_id': ObjectId(recipe['category_name'])})
        recipe['category_name'] = category['category_name']

        user = mongo.db.users.find_one({'_id': ObjectId(recipe['created_by'])})
        recipe['created_by'] = user['username']

    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("recipes.html", recipes=recipes, categories=categories)


# FILTER ON CATEGORY
@app.route("/recipes_filter/<category_name>")
def recipes_filter(category_name):
    # Get the category that is queried 
    category = mongo.db.categories.find_one({'category_name': category_name})
    # and find all the recipes with that category
    recipes = list(mongo.db.recipes.find({'category_name': category['_id']}))
    
    for recipe in recipes:
        # convert the category_name ObjectId to the name
        recipe['category_name'] = category['category_name']

        # convert the created_by ObjectId to the name
        user = mongo.db.users.find_one({'_id': ObjectId(recipe['created_by'])})
        recipe['created_by'] = user['username']

    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("recipes.html", recipes=recipes, categories=categories)


# REGISTER
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if the username already exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        
        if existing_user:
            flash("This username already exists, try another username")
            return redirect(url_for('register'))

        register = {
            "username" : request.form.get("username").lower(),
            "password" : generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session ' cookie
        session['user'] = request.form.get('username').lower()
        flash('Registration succesful!')
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


# LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        #check if the username exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        
        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session['user'] = request.form.get("username").lower()
                    flash("welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
                    
            else:
                # invalid password match
                flash("Incorrect username and/or password, try again.")
                return redirect(url_for('login'))

        else:
            #username doesn't exist
            flash("Incorrect username and/or password, try again.")
            return redirect(url_for('login'))

    return render_template("login.html")


# PROFILE PAGE
@app.route('/profile/<username>', methods=["GET", "POST"])
def profile(username):
    # get the session user's name from the database
    user = mongo.db.users.find_one(
        {"username": session["user"]})
    
    if session['user']:
        # get recipes from this user
        recipes = list(mongo.db.recipes.find(
            {"created_by": user["_id"]}).sort("date_added", -1))
        
        for recipe in recipes:
            # convert category_name ObjectId to the name
            category = mongo.db.categories.find_one(
                {'_id': ObjectId(recipe['category_name'])})
            recipe['category_name'] = category['category_name']
        
            # convert created_by ObjectId to the name
            recipe['created_by'] = user['username']

        categories = mongo.db.categories.find().sort("category_name", 1)
        return render_template("profile.html", recipes=recipes, username=username, categories=categories)

    flash("You don't have an account yet (or aren't logged in). Please register (or login).")
    return redirect(url_for('register'))


# LOGOUT
@app.route("/logout")
def logout():
    if session['user']:
        #remove user from session cookies
        flash("You have been logged out")
        session.pop('user')
        return redirect(url_for("login"))

    return redirect(url_for('home'))


# ALL RECIPES
@app.route("/recipes")
def recipes():
    recipes = list(mongo.db.recipes.find())
    
    for recipe in recipes:
        # convert category_name ObjectId to the name
        category = mongo.db.categories.find_one(
            {'_id': ObjectId(recipe['category_name'])})
        recipe['category_name'] = category['category_name']

        # convert created_by ObjectId to the name
        user = mongo.db.users.find_one(
            {'_id': ObjectId(recipe['created_by'])})
        recipe['created_by'] = user['username']

    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("recipes.html", recipes=recipes, categories=categories)


# INDIVIDUAL RECIPE
@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    # convert created_by ObjectId to the name
    user = mongo.db.users.find_one({'_id': ObjectId(recipe['created_by'])})
    recipe['created_by'] = user['username']

    # convert category_name ObjectId to the name
    category = mongo.db.categories.find_one({'_id': ObjectId(recipe['category_name'])})
    recipe['category_name'] = category['category_name']
    
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("recipe.html", recipe=recipe, categories=categories)


# ADD RECIPE
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if session['user']:

        if request.method == "POST":

            user = mongo.db.users.find_one({'username': session["user"]})
            recipe = {
                "category_name": ObjectId(request.form.get("category_name")),
                "recipe_title": request.form.get("recipe_title"),
                "recipe_description": request.form.get("recipe_description"),
                "recipe_image": request.form.get("recipe_image"),
                "prep_time": request.form.get("prep_time"),
                "bake_time": request.form.get("bake_time"),
                "total_time": request.form.get("total_time"),
                "servings": request.form.get("servings"),
                "tools": request.form.get("tools"),
                "ingredients": request.form.getlist("ingredient[]"),
                "steps": request.form.getlist("step[]"),
                "tips": request.form.get("tips"),
                "created_by": ObjectId(user['_id']),
                # credit specific time format: https://www.programiz.com/python-programming/datetime/current-datetime
                "date_added": date.today().strftime("%d %B %Y") 
            }
            mongo.db.recipes.insert_one(recipe)
            flash("Your recipe has been added.")
            return redirect(url_for('profile', username=session["user"]))

        categories = list(mongo.db.categories.find().sort("category_name", 1))
        return render_template("add_recipe.html", categories=categories)

    flash("Action denied. You don't have an account yet (or aren't logged in). Please register (or login).")
    return redirect(url_for('register'))


# EDIT RECIPE
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if session['user']:

        # find the current recipe
        recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        # convert created_by ObjectId to the name
        user = mongo.db.users.find_one({'_id': ObjectId(recipe['created_by'])})
        recipe['created_by'] = user['username']
        
        # check if the recipe is made by the user
        if session['user'].lower() == recipe['created_by'].lower():

            if request.method == "POST":
                user = mongo.db.users.find_one({'username': session["user"]})
                submit = {
                    "category_name": ObjectId(request.form.get("category_name")),
                    "recipe_title": request.form.get("recipe_title"),
                    "recipe_description": request.form.get("recipe_description"),
                    "recipe_image": request.form.get("recipe_image"),
                    "prep_time": request.form.get("prep_time"),
                    "bake_time": request.form.get("bake_time"),
                    "total_time": request.form.get("total_time"),
                    "servings": request.form.get("servings"),
                    "tools": request.form.get("tools"),
                    "ingredients": request.form.getlist("ingredient[]"),
                    "steps": request.form.getlist("step[]"),
                    "tips": request.form.get("tips"),
                    "created_by": ObjectId(user['_id']),
                    # credit specific time format: https://www.programiz.com/python-programming/datetime/current-datetime
                    "date_added": date.today().strftime("%d %B %Y") 
                }
                mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
                flash("Your recipe has been updated.")
                return redirect(url_for("recipes"))

            recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
            # convert category_name ObjectId to the name
            category = mongo.db.categories.find_one({'_id': ObjectId(recipe['category_name'])})
            recipe['category_name'] = category['category_name']
            
            categories = list(mongo.db.categories.find().sort("category_name", 1))
            return render_template("edit_recipe.html", recipe=recipe, categories=categories)

        flash("Action denied. This isn't your recipe.")
        return redirect(url_for('profile', username=session["user"]))

    flash("You don't have an account yet (or aren't logged in). Please register (or login).")
    return redirect(url_for('register'))


# DELETE RECIPE
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    if session['user']:

        # find the current recipe
        recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        # convert created_by ObjectId to the name
        user = mongo.db.users.find_one({'_id': ObjectId(recipe['created_by'])})
        recipe['created_by'] = user['username']

        # check if the recipe is made by the user
        if session['user'].lower() == recipe['created_by'].lower():
            # mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
            flash("Your recipe has been deleted.")
            return redirect(url_for('profile', username=session["user"]))
        
        else:
            flash("Action denied. This is not your recipe")
            return redirect(url_for('profile', username=session["user"]))

    flash("You don't have an account yet (or aren't logged in). Please register (or login).")
    return redirect(url_for('register'))


# MANAGE CATEGORIES
@app.route("/categories")
def categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


# ADD CATEGORY
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if session['user']:

        if session['user'].lower() == 'admin':

            if request.method == "POST":
                category = {
                    "category_name": request.form.get("category_name")
                }
                mongo.db.categories.insert_one(category)
                flash("New category has been added.")
                return redirect(url_for('categories'))

            return render_template("add_category.html")

        flash("Access denied. You don't have permission for this page.")
        return redirect(url_for('home'))

    flash("Access denied. You don't have permission for this page.")
    return redirect(url_for('home'))


# EDIT CATEGORY
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if session['user']:

        if session['user'].lower() == 'admin':

            if request.method == "POST":
                submit = {
                    "category_name": request.form.get("category_name")
                }
                mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
                flash('Category has been updated.')
                return redirect(url_for('categories'))

            category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
            return render_template("edit_category.html", category=category)
        
        flash("Access denied. You don't have permission for this page.")
        return redirect(url_for('home'))

    flash("Access denied. You don't have permission for this page.")
    return redirect(url_for('home'))
    

# DELETE CATEGORY
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    if session['user']:
        if session['user'] == 'admin'.lower():
            mongo.db.categories.remove({"_id": ObjectId(category_id)})
            flash("Category has been deleted.")
            return redirect(url_for('categories'))
        
        flash("Access denied. You don't have permission for this page.")
        return redirect(url_for('profile', username=session["user"]))

    flash("Access denied. You don't have permission for this page.")
    return redirect(url_for('home'))


# CONTACT
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash('Your message has been sent')
        return redirect(url_for('home'))

    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("contact.html", categories=categories)


# SUBSCRIBE
@app.route("/subscribe", methods=["GET", "POST"])
def subscribe():
    if request.method == "POST":
        # check if the email already exists in the database
        existing_email = mongo.db.subscribe.find_one(
            {"email": request.form.get("email").lower()})

        if existing_email:
            flash("Apparently you've subscribe already. This email already exists.")
            return redirect(url_for('home'))

        subscribe = {
            "email" : request.form.get("email").lower(),
        }
        mongo.db.subscribe.insert_one(subscribe)
        flash('Subscription succesful!')
        return redirect(url_for('home'))


@app.route("/shop")
def shop():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("shop.html", categeries=categories)


# ERROR HANDLERS
@app.errorhandler(403)
def forbidden_access(e):
    return render_template('/error_handlers/403.html'), 403


@app.errorhandler(404)
def page_not_found(e):
    return render_template('/error_handlers/404.html'), 404


@app.errorhandler(500)
def internal_error(e):
    return render_template('/error_handlers/500.html'), 500


# APP INITIALISATION
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)
