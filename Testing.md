# Bugs
Issue: SOLVED
The 'Recipes' dropdown menu in the navbar doesn't adapt to the width of the text inside and a vertical scroll bar is displayed.
Furthermore, when clicking on the 'Recipes', the name disappears. 
Solution: according to the documentation of Materialize, you can change the ![constrainWidth](https://github.com/chizzletaz/GrandmasBakingCollection/blob/master/static/images/README/contrainwidth.png).
add: { constrainWidth: false } as an option to $(".dropdown-trigger").dropdown() (the dropdown trigger in the javascript file).

Extra: looking at the other options, I added ![coverTrigger](https://github.com/chizzletaz/GrandmasBakingCollection/blob/master/static/images/README/covertrigger.png), so the dropdown menu will display below the trigger. And ![hover](https://github.com/chizzletaz/GrandmasBakingCollection/blob/master/static/images/README/hover.png), so the dropdown menu will open on hover.
  
---
Issue: SOLVED
I used Jinja to add categories dynamically to the 'add recipe page', by adding
    categories = mongo.db.categories.find().sort("category_name", 1)
to the add_recipe() function.
I wanted to dynamically add the categories to the navbar as well. However, this time it worked for the navbar, but not for the 
select option on the 'add recipe' page. 
Fix: I remembered from the Task Manager Walkthrough that I'm looping over the categories list twice.
This means that the first (navbar) iterate over the list, it unpacks and leaves it empty afterwards. 
Also the list that comes from the find() method, isn't a actual list, but a Mongo Cursor Object.
By wrapping the find() method in a Python list(), the list can be used again.

---
Issue: SOLVED
Due to the relational connection of category_name in recipes (the category_name in the recipe collection has the value of the
ObjectId of category_name in the categories collection), the preloading of the category_name on the 'edit_recipe' page is not working as used in the Task Manager Walkthrough.
```
{% for category in categories %}
    {% if category.category_name == recipe.category_name %}
        <option value="{{ category._id }}">{{ category.category_name }} selected</option>
    {% else %}
        <option value="{{ category._id }}">{{ category.category_name }}</option>
    {% endif %}
{% endfor %}
```
Fix: The category_name in the Categories collection has to be connected to the category_id in the Recipe collection.
Add this to the "GET" method of the recipe() function:
```
try:
    category = mongo.db.categories.find_one({'_id': ObjectId(recipe['category_name'])})
    recipe['category_name'] = category['category_name']
except Exception as e:
    print('Exception %s' % str(e))
    pass
```

---
Issue: SOLVED
When adding a new recipe, the ingredients and the instructions aren't stored.
I used 'ingredients' and 'steps' for the id, label and name:
```
<input id="ingredients" name="ingredients[]" type="text" class="validate">
<label for="ingredients">Ingredient</label>

<input id="steps" name="steps[]" type="text" class="validate">
<label for="steps">Instruction</label>
```
Fix:
I changes the id, label and name to 'ingredient' and 'step':
```
<input id="ingredient" name="ingredient[]" type="text" class="validate">
<label for="ingredient">Ingredient</label>

<input id="step" name="step[]" type="text" class="validate">
<label for="step">Instruction</label>
```
This seemed to solve the problem.

---
Issue:
The Jinja condition to only show the edit and delete buttons for the user that created the recipe, doesn't work.
```
{% if session.user|lower == recipe.created_by|lower %} 
    <div class="card-action">
        <a class="btn" href="{{ url_for('edit_recipe', recipe_id=recipe._id) }}">Edit Recipe</a>
        <a class="btn right" href="#">Delete Recipe</a>
    </div>
{% endif %}
```
Issue: SOLVED
On the recipe page, I can't get the icons and text of the times and servings aligned on [1 line](https://github.com/chizzletaz/GrandmasBakingCollection/blob/master/static/images/README/icons_recipe_before.png).
Idea: use the [collections component](https://github.com/chizzletaz/GrandmasBakingCollection/blob/master/static/images/README/icons_recipe_after.png). of Materialize.

