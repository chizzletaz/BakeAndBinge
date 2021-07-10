Go to the [README file](https://github.com/chizzletaz/BakeAndBinge/blob/master/README.md)

# **Testing**
## Table of Contents
- [Testing User stories](#testing-user-stories)  
    * [First time users](#first-time-users)
    * [Regular users](#regular-users)
    * [Returning users](#returning-users)
- [Testing Developer stories](#developer-stories)
    * [Admin/site owner](#adminsite-owner)
- [Manual testing features](#manual-testing-features)
- [Code Validation](#code-validation)  
- [Testing across web browsers](#testing-across-web-browsers)  
- [Testing Responsiveness](#testing-responsiveness)  
- [Bugs and Problems](#bugs-and-problems)  
***

## Testing user stories
### First time users:
**1. As a first time user, I want to navigate easily across the website.**
- The user can navigate the website by using the links in the navbar.  
![navbar image](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/navbar.png) 
- The user can return to the landing page by clicking the logo or clicking the Home button in the navbar.  
![navbar2 image](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/navbar2.png) 
- The user can use buttons on the page to navigate to certain pages, e.g. 'Go to recipe'-button to go to the indivudual recipe page.  
<img src="https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/go-to-recipe.png" alt="go to recipe image" width="400"/>


**2. As a first time user, I want to browse the recipes, so I can find inspiration for a recipe.**
 - The landing page has a 'Browse recipes'-button, which directs the user to the recipes page.  
  <img src="https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/browse-recipes.png" alt="browse recipes image" width="400"/>   
 - The recipes page has buttons (for large screens) or a dropdown-menu (for smaller screens) to browse
 per category. (see General users 3)

**3. As a user, I want to know how to add a recipe.**
- When a user is logged in, they are redirected to their own profile page or they can use the button to go to their profile page.
- On this page there is a button with a question mark. 
![how to add button image](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/how-to-add-button.png)  
- When the user clicks this button, a modal pops up with an explanation on how to add a recipe. 
- The explanation consists of the ‘add recipe’ form with explanatory text.
![how to add modal image](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/how-to-add-modal.png)

### General users:  
**1. As a user, I want to be able to use the website on different screen sizes.**
- This website is designed to be responsive, so the users can play on a mobile device, a tablet or a desktop for different view screens. 
- When the size of the window is changed, the content adapts responsively.

**2. As a user, I want to search recipes by keyword(s), so I can find recipes more purposefully.**
- On the recipe page there is a search bar, where the user can enter keywords to search the recipes.
![search bar image](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/searchbar.png)
- The user can go to the recipes page by clicking the ‘browse recipes’ button on the landing page or use the search icon in the navbar to be redirected to the recipes page.  
![search options image](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/search-options.png)  


**3. As a user, I want to filter recipes by category, so I narrow down my search and/or search per category.**
- On the recipes page, the user can select a category to filter by that category.
- On large screens (> 992px) there are individual buttons.  
![category large image](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/category-large.png) 
- On smaller screens (< 992px) there is a dropdown menu to select a category.  
<img src="https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/category-small.png" alt="category small image" width="400"/>

**4. As a user, I want to sort the recipes by date, popularity, alphabet, so I can better choose a recipe.**  
This is a feature left to implement.

**5. As a user, I want to see if a recipe is gluten free, vegan, etc so I can find out quickly if it matches my diet.**  
This is a feature left to implement.

**6. As a user, I want to be able to delete my profile, if I no longer wish to use the website.**  
This is a feature left to implement.

### Regular users:
**1. As a regular user, I want to have my own page, so I can manage my own recipes.**
- When a user registers or logs in, they are redirected to their own profile page. 
- On this page, the use can manage (add, edit or delete) their recipes (see below).
- The user can go to their profile page by clicking the 'Profile' link in the navbar.  
![profile image](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/profile-page.png) 

 **2. As a regular user, I want to add my own recipes, so I can share them with others on the website.**
- When a user is logged in they can add a new recipe by going to their profile page and click the ‘add a new recipe’ button.
![add recipe image](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/add-recipe-button.png) 

**3. As a regular user, I want to edit and delete my own recipes, so I can keep my recipes up to date.**
- When a user is logged in they can edit or delete their own recipes, by going to their profile page and click on the ‘edit’ or ‘delete’ button of the recipe they want to edit or delete.  
![edit delete buttons image](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/edit-delete-recipe.png) 

**4. As a regular user, I want to contact the site owner in case I have questions or remarks.**
- The navbar has a link to the contact page. 
![contact link image](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/contact-link.png) 
- On the contact page, the user can fill in the form to contact the site owner.


**5. As a regular user, I want to be able to rate other recipes.**  
This is a feature left to implement.

**6. As a regular user, I want to be able to save other people's recipes.**  
This is a feature left to implement.

**7. As a regular user, I want to be able to share recipes.**  
This is a feature left to implement.

**8. As a regular user, I want to get the latest news and updates.** 
- The footer has a subscribe form, where the user can enter their email address to get the latest news and updates.  
![footer image](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/footer.png) 

## Developer stories:
### Admin/site owner:
**1. As a site owner, I want to promote certain baking tools, in order to increase commission on the sales.**
- The navbar has a link to the shop page.   
![shop link image](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/shop-link.png) 
- This page has cards with info on baking tools. 
- When the user clicks the ‘buy now’ button, they are redirected to an external page where they can buy the item.  
![buy now image](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/buy-now.png) 

**2. As a site owner, I want to be able to have access to the recipes categories and the option to manage them.**
- When the site owner logs in as admin, they have an extra link in the navbar to manage categories. 
![manage categories image](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/manage-categories.png)  
- When they click on this link, the categories page is opened. 
- On this page the admin can create a new category, edit or delete an existing category.  
![create edit delete categories image](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/CRUD-admin.png) 

**3. As a site owner, I want users to register and login, before they can add, edit or delete their recipes.** 
- A user has to register or log to add, edit or delete. (see above 'Regular users 1, 2 and 3')

## Manual testing features
**Navigation to the landing page:**  
Expected: The logo text and the home button direct the user to the landing page.  
Testing:
1. Go to any page but the landing page.  
2. Click on ‘Triviata’-text at the top of the page and verify you are directed to the landing page.
3. Go to any page but the landing page.
4. Click on the button with the house-icon and verify you are directed to the landing page.

Result: The logo text and the home button direct the user to the landing page.

---
## Code validation
[W3C Markup Validation Service](https://validator.w3.org/) is used to check for markup validity of the web document.
Bacause Flask Jinja template is used on all HTML pages, the source code is taken from the rendered pages to be tested.
How to validate the rendered page:
Use the source code of the rendered page
- Right click on the page
- Click 'show source code'
- Copy all HTML
- Paste into the validator.
Or
Enter the url of the heroku live link.

Running the code through the validator gives:  
### For index.html:
- 4 errors and 1 warning shown  
![html index error](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/validation/html-index.png)
1. Element h4 not allowed as child of element ul in this context.
Fix: According to HTML5 spec, you can't have header tags as children within a <ul></ul>, you should populate it with <li></li>, then insert your content within each list, so wrap the h4 in <li></li>
Credit: Mike Hanslo @ https://stackoverflow.com/questions/29079953/element-h4-not-allowed-as-child-of-element-ul-in-this-context
2. Section lacks heading. 
Fix: change section into div.
3. Start tag a seen but an element of the same type was already open.
I originally only had the 'go to recipe'-button acting as an anchor tag. Later I added an anchor tag to the whole card, but forgot to remove the anchor tag of the button. This resulted in an anchor tag inside another anchor tag. 
Fix: change the the anchor tag of the button to a button tag and remove the href.
This gives another error: The element button must not appear as a descendant of the a element.
Fix: Change button tag to p tag with button class.
> Note: Since similar cards are used on the recipes and profile pages pages, these errors will be fixed there as well.

**The recipes page:**

**The recipe page:**

**The contact page:**

**The shop page:**

**The register page:**

**The login page:** 

**The profile page:**

**The add recipe page:**

**The edit recipe page:**
 
**The categories page:** 

**The add category page:**

**The edit category page:** 

**The 403 error handler page:**

**The 404 error handler page:**

**The 500 error handler page:**

---
[W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) is used to check the CSS of the web document.
Running the code through the validator gives:
### For style.css:
- No errors are found.  
![style.css validation](assets/img/examples/css-style.png)

---
[JSHint](https://jshint.com/) is used to check the validity of the Javascript of the web document.    
Running the code through the validator gives:
### For start.js:
- No errors, just some warnings about semi-colons and an error 'Expected an assignment or function call and instead saw an expression.'  
![start.js validation](assets/img/examples/js-start.png)

---
## Testing browser compatibility
I've tested the site on Safari, Chrome and Mozilla Firefox.
The testing was done by checking all elements, functionalities and links.
No issues arose during testing.  

---
## Testing responsiveness
To test the responsiveness of the  website, I've used [Chrome Dev Tools](https://github.com/chizzletaz/MilestoneProject1/blob/master/assets/img/extra/responsiveness_chrome_dev_tools.png) and [Responsinator](https://www.responsinator.com/) to test the site at different screen resolutions.   
The testing was done on widths down to a screen resolution of 280px. All the elements on each page were checked.  
The following issues arose:
- Issue: At a width of 280px, the size of the buttons on the landing page go outside the screen.   
![button responsive wrong](assets/img/examples/responsive-button-wrong.png)

## Bugs and problems

Issue: SOLVED  
The 'Recipes' dropdown menu in the navbar doesn't adapt to the width of the text inside and a vertical scroll bar is displayed.  
Furthermore, when clicking on the 'Recipes', the name disappears.  

Fix: according to the documentation of Materialize, you can change the ![constrainWidth](https://github.com/chizzletaz/GrandmasBakingCollection/blob/master/README/images/contrainwidth.png).  
add: { constrainWidth: false } as an option to $(".dropdown-trigger").dropdown() (the dropdown trigger in the javascript file).  

Extra: looking at the other options, I added ![coverTrigger](https://github.com/chizzletaz/GrandmasBakingCollection/blob/master/README/images/covertrigger.png), so the dropdown menu will display below the trigger.   
And ![hover](https://github.com/chizzletaz/GrandmasBakingCollection/blob/master/README/images/hover.png), so the dropdown menu will open on hover.  

> UPDATE: I removed hover from the dropdown menu, cause on mobile devices the dropdown didn't work.
  
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

    input id="step" name="step[]" type="text" class="validate">
    <label for="step">Instruction</label>
```
This seemed to solve the problem.

---
Issue: SOLVED  
The Jinja condition to only show the edit and delete buttons for the user that created the recipe, doesn't work.
```
    {% if session.user|lower == recipe.created_by|lower %} 
        <div class="card-action">
            <a class="btn" href="{{ url_for('edit_recipe', recipe_id=recipe._id) }}">Edit Recipe</a>
            <a class="btn right" href="#">Delete Recipe</a>
        </div>
    {% endif %}
```
Fix: In the recipes collection, the 'created_by' name is stored as the ObjectId of that name in the user collection.
To use the condition, the 'created_by' has to be converted to the name. 
Add to recipes() in app.py:
```
    user = mongo.db.users.find_one(
        {'_id': ObjectId(recipe['created_by'])})
    recipe['created_by'] = user['username']
```
---
Issue: SOLVED  
On the recipe page, I can't get the icons and text of the times and servings aligned on [1 line](https://github.com/chizzletaz/GrandmasBakingCollection/blob/master/README/images/icons_recipe_before.png).  

Idea: use the [collections component](https://github.com/chizzletaz/GrandmasBakingCollection/blob/master/README/images/icons_recipe_after.png) of Materialize.

---
Issue: partially SOLVED  
When displaying the recipes on the index, recipes and profile page, the cards 
[aren't](https://github.com/chizzletaz/GrandmasBakingCollection/blob/master/README/images/cards_unequal.png) equal height.  

Fix: Apparently Materialize doesn't support flexblox [acburst](https://github.com/Dogfalo/materialize/issues/2089)
Another partial solution is given by [bilalkhan891](https://github.com/Dogfalo/materialize/issues/2089)
Now each row has the height of the [largest card](https://github.com/chizzletaz/GrandmasBakingCollection/blob/master/README/images/cards_equal.png).

---
Issue: SOLVED  
When selecting recipes by category and only 1 recipe displays, the recipe is displayed on the right side of the page.  

Fix: Upon inspecting the page, the margin-left of .row .col is set to auto. Changing it to margin-right: auto, moves the recipe 
to the left. However this is a custom CSS by Materialize. I wasn't able to override this CSS, but by adding margin-right: auto
to the columns of class 'equal-right':
```
.equal-col .col {
    margin-right: auto;
}
```
The recipe is displayed in the middle. When 2 recipes are shown, the recipes are equallty distributed over the width.
I find this visually more pleasing. So I didn't try to adjust the CSS to align the recipes to the right.

