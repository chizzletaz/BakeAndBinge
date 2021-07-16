Go to the [README file](https://github.com/chizzletaz/BakeAndBinge/blob/master/README.md)

# **Testing**
## Table of Contents
- [Testing User stories](#testing-user-stories)  
    * [First time users](#first-time-users)
    * [General users](#general-users)
    * [Regular users](#regular-users)
- [Testing Developer stories](#developer-stories)
    * [Admin/site owner](#adminsite-owner)
- [Manual testing features](#manual-testing-features)
- [Code Validation](#code-validation)  
- [Testing browser compatibility](#testing-browser-compatibility)  
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
- When a user is logged in, they are redirected to their own profile page or they can use the 'Profile' link to go to their profile page.
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
- When the user clicks the three dots icon on the right, they get more information about the product.
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

**Subscription option**  
Expected:   
The user is subscribed to the newsletter when the user fills in the subscription form correctly.

Testing:
1. Go to the footer of any page (except register or login).
2. Don't fill in an email address and click 'Subscribe'.
3. Confirm that a warning message appears.  
   Result:  
        A 'Subcription successfull' message appears.  
   Fix:   
        Add 'required' to the input field.  
   Result:  
        A warning message appears.
4. Fill in an invalid email address.
5. Confirm that a warning message appears.
6. Fill in a valid email address.
7. Confirm that the message 'Subscription successful!' appears.
8. Fill in the same email address.
9. Confirm that the message 'Apparently you've subscribe already. This email already exists.' appears.

Result:  
The user is subscribed to the newsletter when the user fills in the subscription form correctly.

**Register functionality**  
Expected:   
The user can register to the website by filling in the register form correctly.

Testing:
1. Go to the register page by clicking the 'register here' button on the landing page or click on the register link in the navbar.
2. Don't fill in the register form.
3. Confirm that a warning message appears.
4. Only fill in the username.
5. Confirm that a warning message appears.
6. Only fill in the password.
7. Confirm that a warning message appears.
8. Fill in a unique username and password.
9. Confirm that the message 'Registration succesful!' appears.
10. Log out by clicking the logout button in the navbar.
11. Repeat steps 1 and 8.
12. Confirm that the message 'This username already exists, try another username.' appears.

Result:  
The user can register to the website by filling in the register form correctly.

**Login functionality**  
Expected:   
The user can log in to the website by filling in the login form correctly.

Testing:
1. Go to the login page by clicking on the login link in the navbar.
2. Don't fill in the login form.
3. Confirm that a warning message appears.
4. Only fill in the username.
5. Confirm that a warning message appears.
6. Only fill in the password.
7. Confirm that a warning message appears.
8. Fill in a wrong username and password.
9. Confirm that the message 'Incorrect username and/or password, try again.' appears.
10. Fill in your username and password.
11. Confirm you are redirected to your profile page and the message 'welcome, *your username*' appears.

Result:  
The user can log in to the website by filling in the login form correctly.

**Logout functionality**  
Expected:   
The user is logged out when they click on the logout link in the navbar.

Testing:
1. Log in.
2. Click the logout button in the navbar.
3. Confirm that a warning modal appears with the message 'Are you sure you want to log out?'.
4. Click 'No'.
5. Confirm you are still logged in and are kept on the current page.
6. Repeat steps 2 and 3.
7. Click 'Yes'.
8. Confirm you are logged out from the website and a message 'You have been logged out' appears.
9. Confirm you are redirected to the login page.

Result:  
The user is logged out when they click on the logout link in the navbar.

**CTA button**  
Expected:   
The user is redirected to the register page when they click on the 'REGISTER HERE' button.

Testing:
1. Go to the landing page.
2. Click the 'REGISTER HERE' button.
3. Confirm you are redirected to the register page.

Result:  
The user is redirected to the register page when they click on the 'REGISTER HERE' button.

**Search bar**  
Expected:  
The user can go to the search bar and search recipes by keyword.

Testing:
1. On the landing page, click the 'BROWSE RECIPES' button.
2. Confirm you are redirected to the recipes page and that you see the search bar.
3. Go to any other page (except register or login).
4. Click the search icon.
5. Confirm you are redirected to the recipes page and that you see the search bar.
6. Fill in the keyword 'strawberry' in the search bar.
7. Confirm that a recipe for strawberry cake appears.
8. Fill in the keyword 'test'in the search bar.
9. Confirm that the message 'Sorry, no results were found.' appears.

Result:  
The user can go to the search bar and search recipes by keyword.

**Category buttons**  
Expected:  
The user can use the category buttons on the recipes page to display the recipes by category.

Testing:
1. On the recipes page click the 'Cookies' button.
2. Confirm that only recipes with category 'Cookies' are displayed.
3. Repeat steps 1 and 2 for the other categories.
4. On the recipes page click on the 'All' button.
5. Confirm that all recipes are displayed.

Result:  
The user can use the category buttons on the recipes page to display the recipes by category.

**Error 404 handler page**  
Expected:  
The user gets a error 404 page when a page can't be displayed and can get back by clickin a button.

Testing:
1. Go to any page.
2. In the browser's address bar, remove one or more characters and press enter.
3. Confirm a message 404 page is shown, without navbar and footer.
4. Confirm there is a button 'click here to get back' at the bottom of the page.
5. Click the button and confirm you are redirected to the home page of the website.

Result:  
The user gets a error 404 page when a page can't be displayed and can get back by clickin a button.

**Collapsible on shop page**  
Expected:  
The user can get more information about a shop product when they click on the three dots icon.

Testing:
1. Go to the shop page by clicking the shop link in the navbar.
2. Click on the three dots icon in one of the shop products.
3. Confirm that a text with more information about the product is shown.  
    Result:  
    On smaller screen sizes (< 326px ), the text doesn't scroll all the way up and is cut off.  
    Fix:   
    Due to the fact that I used the 'medium' attribute of Materialize on the cards, the max height is 400px.
    Change the height to 450px.  
    Result:  
    All the information text is shown.
4. Click on the cross icon.
5. Confirm that the text disappears and the image of the product is shown.

Result:  
The user can get more information about a shop product when they click on the three dots icon.

**Modal for how to add a new recipe**  
Expected:  
A modal with info on how to add a recipe pops up, when the user clicks the 'how to add a new recipe' button.

Testing:
1. Log in.
2. On the profile page, click the plus icon
3. Confirm a modal pops up with information on how to add a new recipe.
4. Click on the 'DONE' button.
5. Confirm the modal closes.
6. Repeat step 2.
7. Click outside the modal.
8. Confirm the modal closes.

Result:  
A modal with info on how to add a recipe pops up, when the user clicks the 'how to add a new recipe' button.

**Confirmation modal**  
Expected:  
A modal asking the user to confirm their action pops up, when the user clicks a 'delete' or 'logout' button.

Testing:
1. Log in.
2. Click the log out button in the navbar.
3. Confirm a modal pops up that asks 'Are you sure you want to log out?'.
4. Click 'Yes'.
5. Log in as admin.
6. Click the 'DELETE' button on one of the recipes.
7. Confirm a modal pops up that asks 'Are you sure you want to delete this recipe?'.
8. Click 'no'.
9. Go to the categories page by clicking the 'manage categories' link in the navbar.
10. Click on the "DELETE' button of one of the categories.
11. Confirm a modal pops up that asks 'Are you sure you want to delete this category?'.
12. Click 'no'.

Result:  
A modal asking the user to confirm their action pops up, when the user clicks a 'delete' or 'logout' button.

**Social icons**  
Expected:  
The user is redirected to the respective social media page, when they click on a social media icon.

Testing:
1. Go to the footer of any page.
2. Click on a social media icon.
3. Confirm you are redirected to that social media page.
4. Confirm that the page is opened in a new window.
5. Repeat steps 2, 3 and 4 for the other icons.

Result:  
The user is redirected to the respective social media page, when they click on a social media icon.

**Contact form**  
Expected:  
The user can send the site owner a message by filling in the contact form.

Testing:
1. Go to the contact page by clicking the 'contact' link in the navbar.
2. Don't fill in the contact form.
3. Confirm that a warning message appears.
4. Fill in the contact form except for the firstname and click the 'SUBMIT' button.
5. Confirm that a warning message appears.
6. Repeat steps 4 and 5 for the lastname, email address and message inputs.
7. Fill in the complete contact form and click the 'SUBMIT' button.
8. Confirm that the message 'Your message has been sent' is shown.
9. Confirm you are redirected to the home page.

Result:  
The user can send the site owner a message by filling in the contact form.

#### CRUD (Create, Read, Update, Delete) functionality.

**Add recipe**  
Expected:  
A new recipe is added when the user fills in the add recipe form.

Testing:
1. Log in.
2. Click the plus icon.
3. Confirm you are redirected to the add recipe page.
4. Click the 'CANCEL' button at the bottom of the page.
5. Confirm you are redirected to your profile page.
6. Fill on the recipe form, except the recipe title.
7. Confirm a warning message appears.
8. Repeat steps 6 and 7 for the other inputs that are marked 'required'.
9. Fill in the recipe form and the click 'ADD' button.
10. Confirm that a message appears with 'Your recipe has been added.'
11. Confirm you are redirected to you profile page.
12. Confirm that the recipe you added is added to your profile page.

Result:  
A new recipe is added when the user fills in the add recipe form.

**Add category**  
Expected:  
A new category is added when the admin fills in the add category form.

Testing:
1. Log in as admin.
2. Click on the 'manage categories' link in the navbar.
3. Click on the plus icon.
4. Confirm you are redirected to the 'add a new category' page.
5. Enter a category name and click the 'ADD CATEGORY' button.
6. Confirm you are redirected to the categories page.
7. Confirm your new category is added.

Result:  
A new category is added when the admin fills in the add category form.

**Edit recipe**  
Expected:  
An existing recipe is edited when the user fills in the edit recipe form.

Testing:
1. Log in.
2. On your profile page, click the 'EDIT' button of one of your recipes.
3. Confirm you are redirected to the edit recipe page.
4. Confirm the form is prefilled with the data of the existing recipe.
5. Change any of the input fields.
6. Click the 'EDIT RECIPE' button.
7. Confirm you are redirected to your profile page.
8. Click on the 'GO TO RECIPE' button of the edited recipe.
9. Confirm that your change is shown in the recipe.

Result:  
An existing recipe is edited when the user fills in the edit recipe form.

**Edit category**  
Expected:  
An existing category is edited when the admin fills in the edit category form.

Testing:
1. Log in as admin.
2. Click on the 'manage categories' link in the navbar.
3. Click the 'EDIT' button of one of your categories.
4. Confirm you are redirected to the edit category page.
5. Change the category name and click the 'EDIT CATEGORY' button.
6. Confirm you are redirected to the categories page.
7. Confirm your chosen category is edited. 

Result:  
An existing category is edited when the admin fills in the edit category form.

**Delete recipe**  
Expected:  
A recipe is deleted when the user clicks on the 'DELETE' button of a recipe.

Testing:
1. Log in.
2. On your profile page, click the 'DELETE' button of one of your recipes (tip: create a test recipe first with only the required input fields).
3. Confirm a modal pops up with the message 'Are you sure you want to delete this recipe?'
4. Click 'YES'.
5. Confirm you are redirected to your profile page.
6. Confirm the recipe is deleted.

Result:  
A recipe is deleted when the user clicks on the 'DELETE' button of a recipe.

**Delete category**  
Expected:  
A category is deleted when the user clicks on the 'DELETE' button of a category.

Testing:
1. Log in as admin.
2. Click on the 'manage categories' link in the navbar.
3. Click the 'DELETE' button of one of your categories.
4. Confirm a modal pops up with the message 'Are you sure you want to delete this category?'
5. Click 'YES'.
6. Confirm you are redirected to the categories page.
7. Confirm your chosen category is deleted.

Result:  
A category is deleted when the user clicks on the 'DELETE' button of a category.


---
## Code validation
### HTML
[W3C Markup Validation Service](https://validator.w3.org/) is used to check for markup validity of the web document.
Bacause Flask Jinja template is used on all HTML pages, the source code is taken from the rendered pages to be tested.  
How to validate the rendered page:  
- Use the source code of the rendered page
    - Right click on the page
    - Click 'show source code'
    - Copy all HTML
    - Paste into the validator.        
Or  
- Enter the url of the heroku live link.  
However, when authentication is used, the live link can't be used to validate the page.

Running the code through the validator gives:  
#### For index.html:
- 4 errors and 1 warning shown  
![html index error](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/validation/html-index.png)
1. Element h4 not allowed as child of element ul in this context.  
Fix: According to HTML5 spec, you can't have header tags as children within a ```<ul></ul>```, you can only have ```<li>``` elements as children. So you should populate it with ```<li></li>```, then insert your content within each list, so wrap the h4 in <li></li>
Credit: Mike Hanslo @ https://stackoverflow.com/questions/29079953/element-h4-not-allowed-as-child-of-element-ul-in-this-context
2. Section lacks heading.   
Fix: change section into div.
3. Start tag a seen but an element of the same type was already open.  
I originally only had the 'go to recipe'-button acting as an anchor tag. Later I added an anchor tag to the whole card, but forgot to remove the anchor tag of the button. This resulted in an anchor tag inside another anchor tag.   
Fix: change the the anchor tag of the button to a button tag and remove the href.
This gives another error: The element button must not appear as a descendant of the a element.  
Fix: Change button tag to p tag with button class.
> Note: Since similar cards are used on the recipes and profile pages pages, these errors will be fixed there as well.

#### For recipes.html:
- No errors or warnings to show.
![html recipes error](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/validation/html-recipes.png)

#### For recipe.html:
- 2 different errors are shown:
![html recipe error](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/validation/html-recipe.png)
1. Named character reference was not terminated by a semicolon. (Or & should have been escaped as &amp;.)
I forgot to add the ; after $nbsp to indicate a space.  
Fix: add semi-colon after $nbsp.
2. Element br not allowed as child of element ul in this context. According to HTML5 spec, you can only have ```<li>``` elements as children. I used the ```<br>``` element to add padding between each ingredient and step.
But ul elements can only have ```<li>``` elements as children.  
Fix: remove the br element and add an empty li (```<li></li>```)

#### For contact.html:
- 1 error and 1 warning are shown
![html contact error](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/validation/html-contact.png)
1. Duplicate ID email.
I used 'email' for the ID and name in the contact form. But 'email' is already used for ID and name in the subcribe form in the footer.   
Fix: change the ID and name to 'contactemail'.
2. The warning is gone after fixing error 1.

#### For shop.html:
- 3 errors are shown
![html shop error](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/validation/html-shop.png)
1.  End tag main seen, but there were open elements.
I forgot to close 2 div's.   
Fix: See below at number 2.
2. Unclosed element div.
I forgot to close 2 div's.  
Fix: add closing div element.

#### For register.html:
- No errors or warnings to show.
![html register error](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/validation/html-register.png)

#### For login.html: 
- No errors or warnings to show.
![html login error](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/validation/html-login.png)

#### For profile.html:
![html profile error](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/validation/html-profile.png)
- 4 errors are shown.
1. Element div not allowed as child of element ul in this context.  
The div element belongs to a modal. According to HTML5 spec, you can only have ```<li>``` elements as children. 
Fix: put the modal structure outside of the ul.
2. Start tag a seen but an element of the same type was already open.  
I wrapped the the whole card in an anchor tag, so the whole card can be used to open a recepe.
However on the profile page, 2 more anchor tags are added as edit and delete button. This results in anchor tags within anchor tags.  
Fix: keep the card-action div outside the first anchor tag.
After fixing the mistakes, other errors suddenly appear.
![html further profile error](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/validation/html-profile2.png)
3. Duplicate ID modal1.  
There is a duplication of the modal that asks the user for confirmation on deleting a recipe.
However, since the recipes are rendered by looping, the modals are duplicated as well. 
Fix: use Jinja to add the loop index at every loop, so the modal has a unique ID every time. 

#### For add_recipe.html:
- No errors or warnings to show.
![html add recipe error](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/validation/html-add-recipe.png)

#### For edit_recipe.html:
- 4 errors are shown.
 ![html edit recipe error](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/validation/html-edit-recipe.png)
 1. The ID's for 'inputIngredientRow' are not unique because of the way they are created with javascript:
 ```
    // add ingredient row
    $("#addRowIngredient").click(function () {
        var html = `
        <div class="row mb0" id="inputIngredientRow">
            <div class="input-field col s12 mb0">
                <textarea id="ingredient" name="ingredient[]" class="materialize-textarea" required></textarea>
                <label for="ingredient">Ingredient</label>
                <i id="removeRowIngredient" class="far fa-trash-alt prefix right"></i>    
            </div>`;

        $('#newRowIngredient').append(html);
    });
    // remove ingredient row
    $(document).on('click', '#removeRowIngredient', function () {
        $(this).closest('#inputIngredientRow').remove();
    });
 ```
 Fix: use parent('div) instead of closest('#inputIngredientRow'). This way the id="inputIngredientRow" doesn't have to be used.

2. The ID's for 'inputStepRow' are not unique because of the way they are created with javascript.  
Fix: see above at number 1.

3. The ID's for 'ingredient' are not unique because of the way they are created with javascript.  
Fix: use Jinja to add the loop index at every loop, so the modal has a unique ID every time.

4. The ID's for 'step' are not unique because of the way they are created with javascript.  
Fix: use Jinja to add the loop index at every loop, so the modal has a unique ID every time.

#### For categories.html:
- 1 error and 1 warning are shown 4 times
![html categories error](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/validation/html-categories.png)
1. Duplicate ID modal4.
use Jinja to add the loop index at every loop, so the modal has a unique ID every time. 

#### For add_category.html:
- No errors or warnings to show.
![html add category error](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/validation/html-add-recipe.png)

#### For edit_category.html: 
- No errors or warnings to show.
![html edit category error](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/validation/html-add-recipe.png)

#### For 403.html:  
I don't know how to test this page.

#### For 404.html:
- No errors or warnings to show.
![html 404 errorhandler error](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/validation/html-add-recipe.png)

#### For 405.html:  
I don't know how to test this page.

---
### CSS  
[W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) is used to check the CSS of the web document.
Running the code through the validator gives:
#### For style.css:
- No errors are found.  
![style.css validation](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/validation/css-style.png)

---
### Javascript  
[JSHint](https://jshint.com/) is used to check the validity of the Javascript of the web document.  
It is recommended to add **```/* jshint esversion: 6 */```** at the top of the .js file to tell JSHint that your code uses ECMAScript 6 specific syntax.      
Running the code through the validator gives:
#### For style.js:
- No errors or warnings are shown. 
---
### Python  
[PEP8 online](http://pep8online.com/) is used to check the python code for PEP8 requirements.
#### For app.py:
Before checking the app.py file, I tried to remove as many mistakes beforehand, such as extra whitespaces, maximum
code line length of 72, correct line breaks, etc.   
Nevertheless, there were a lot of issues that I missed.
- Several notifications  
![pep8 python notifications](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/validation/python-pep8.png)  
After fixing the notifications, I get an All right message.
![All right message pep8](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/validation/python-pep8-after.png)

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

---
Issue: I don't want to show the header and footer on the error handler pages.
Idea: use 'hide_nav=True' for rendering in app.py and Jinja condition on the error handler pages:
```
{% if not hide_nav %}{% extends "base.html" %}{% endif %}
```
However, this leaves out everything including the links in the head tag. This means you have to add some of the links again on the error handler page.
I've decided to not extend the base and make a 'normal' page setup for each error handler page, leaving out the header and footer.
