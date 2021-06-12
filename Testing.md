# Bugs
Issue: SOLVED
The 'Recipes' dropdown menu in the navbar doesn't adapt to the width of the text inside and a vertical scroll bar is displayed.
Furthermore, when clicking on the 'Recipes', the name disappears. 
Solution: according to the documentation of Materialize, you can change the ![constrainWidth](https://github.com/chizzletaz/GrandmasBakingCollection/blob/master/static/images/README/contrainwidth.png).
add: { constrainWidth: false } as an option to $(".dropdown-trigger").dropdown() (the dropdown trigger in the javascript file).

Extra: looking at the other options, I added ![coverTrigger](https://github.com/chizzletaz/GrandmasBakingCollection/blob/master/static/images/README/covertrigger.png), so the dropdown menu will display below the trigger. And ![hover](https://github.com/chizzletaz/GrandmasBakingCollection/blob/master/static/images/README/hover.png), so the dropdown menu will open on hover.
  
---
Issue:
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
