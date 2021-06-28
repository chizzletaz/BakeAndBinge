#Bake and Binge
![Preview image](https://grandmas-baking-collection.herokuapp.com)

Like many others, I've always loved baking and cooking. Over the years you try out new recipes and share the result with your family and friends.
When the recipe is a hit you often you get the question: 'Can you give me the recipe?'.
Usually you scribble the recipe down on a piece of paper. I have a lot of those papers lying in the kitchen.
But it would be much easier to add your recipe online and share is that way. No more scribbling, no more loose papers. 

### A live version can be viewed [here](https://chizzletaz.github.io/GrandmasBakingCollection/)

# Table of Content
- [User Experience (UX)](#user-experience-(ux))  
	* [Strategic level](#strategic-level)
        * [User stories](#user-stories)
        * [Developer stories](#developer-stories)  
	* [Scope level](#scope-level) 
        * [Requirements](#requirements) 
	* [Structure level](#structure-level)
        * [Interaction Design and Information Design](#interaction-design-and-information-design)
        * [The pages](#the-pages)
	* [Skeleton level](#skeleton-level)
        * [Wireframes](#wireframes) 
        * [Update](#update) 
	* [Service Level](#service-level)
        * [Colors](#colors)
        * [Typography](#typography)
- [Features](#features)
    * [Existing Features](#existing-features)
    * [Features left to implement](#features-left-to-implement)
- [Technologies Used](#technologies-used)
    * [Languages](#languages-used)
    * [Frameworks and libraries](#frameworks-and-libraries-used)
    * [Tools and Programmes](#tools-and-programmes-used)
- [Testing](#testing)
- [Deployment](#deployment)
    * [Deploying to GitHub Pages](#deploying-to-github-pages)
    * [Making a Local Clone](#making-a-local-clone)
- [Credits](#credits)

***
# **User Experience (UX)**
## **Strategic level**

The target audience are users that want to search recipes and add their own.
I want to create a website for people to find nice recipes and give them the opportunity to add their own. 
With this project I also hope to show my knowledge and application of the added coding skills I’ve learning, i.e. Python, using Flask and MongoDB.

### **User stories:**  
*First time users:*
- As a first time user, I want to navigate easily across the site. —> nav bar, nav buttons.
- As a first time user, I want to browse the recipes, so I can find inspiration for a recipe. —> recipe page with all recipes + browse per category.

*General users:*
- As a user, I want to be able to use the website on different screen sizes. —> responsive design
- As a user, I want to search recipes by keyword(s), so I can find recipes more purposefully. —> search option
- As a user, I want to filter recipes by category, so I narrow down my search and/or search per category. —> filter buttons or select option
- As a user, I want to sort the recipes by date, popularity, alphabet, so I can better choose a recipe. —> sort buttons.
- As a user, I want to see if a recipe is gluten free, vegan, etc so I can find out quickly if it matches my diet. -> labels for gluten free, vegan, etc.
- As a user, I want to know how to add a recipe. -> How to add a new recipe explanation.

*Regular users:*
- As a regular user, I want to have my own page, so I can manage my own recipes. —> register/login functionality.
- As a regular user, I want to add my own recipes, so I can share them with others on the website. —> add recipe page + functionality
- As a regular user, I want to edit and delete my own recipes, so I can keep my recipes up to date. —> edit/delete page + functionality.
- As a regular user, I want to contact the site owner in case I have questions or remarks. —> contact page.
- As a regular user, I want to be able to rate other recipes. —> rating functionality
- As a regular user, I want to be able to share recipes. —> share functionality
- As a regular user, I want to get the latest news and updates. -> sign up for newsletter

### **Developer stories**
*Admin/site owner:*
- As a site owner, I want to promote certain baking tools, in order to increase commission on the sales.
- As a site owner, I want to be able to have access to the recipes categories and the option to manage them. —> admin functionality.
- As a site owner, I want users to register and login, before they can add, edit or delete their recipes. —> register/login functionality.
- As a site owner, I want to give the user a pleasant site experience, so they will come back another time.

## **Scope level**
I've opted for a MVP (Minimal Viable Project) again and work my way up from there.
Based on the user stories the minimal requirements for this project are:

### **Requirements**
1. A navbar and good navigation buttons.
2. A responsive design.
3. A page with all the recipes.
4. A search option to search the recipes.
5. An option to filter by category.
6. An option to subscribe to the newsletter.
7. An option to register and login/logout.
8. A profile page when users log in. 
9. Options to Create, Read, Edit and Delete (CRUD) recipes.
10. A shop page to promote baking tools.
11. An option for the user to contact the site’s owner.
12. An Admin page with admin only functionality.

**Extra requirements:** 
1. An option to rate recipes.
2. An option to share recipes.
3. An option to save a recipe to the users profile page.
4. An explanation how to add recipes.
5. An option to delete a profile.
6. An option to sort by attribute (alphabetically, time, rating)
7. An option to add labels (e.g. vegan, gluten free) to recipes.

## **Structure Level**
### **Interaction Design and Information Design**
The overall look is kept the same on each page as much as possible, to enhances single-use-learning:
- Header and footer are kept mostly the same on each page.
- Buttons are styled in the same way.
- The use of colours are kept the same on each page.

The navigation is kept simple and consistent:
- A responsive navigation bar at the top of the page.
- A landing page with clearly indicating the options for first time users.
- The logo at the top of the page is also the link to the home page.
- Buttons can be used to navigate.

The information provided should be easily visible:
- Visual aids are used, like icons and complementary colours.
- The amount of information is kept to a minimum.

The user is given feedback, in order to enhance a pleasant user experience:
- The user get’s a visual feedback during certain actions (e.g. focussing on, clicking on, hovering over buttons and links).
- Flash messages are used to confirm actions.
- Modal pop ups are used as defensive programming, i.e. prompting the user if they are sure of their action.
- The user get's a feedback when an error as occurred (warning text or via error handlers).

### **The pages**
**FRONTEND**  
The website will have 13 pages plus 3 error handler pages. Each page will have a navbar and a footer, except for the error handler pages. 
The navbar links are depending on whether a user is logged in or not and if the user is the admin. 

**The landing page/home page:** *(index.html - route: /, /home)*  
The main page has a navbar with links for home, shop, recipes (dropdown menu to search by category), register, login and a search icon.
Below that an hero image and a short explanation for the site.
Beneath that are the latest recipes and lastly a section to subscribe to the newsletter.

**The recipes page:** *(recipes.html - route: /recipes)*  
On this page all the recipes are shown. For large screens there are buttons to filter the recipes by category (route: /recipes/< category_name >). For smaller screens, there is a select input. 
There is a search bar which leads to this same page with the results of the search (route: /search). 
From there the user can go to an individual recipe page. 

**The recipe page:** *(recipe.html - route: /recipe/< recipe_id >)*  
This is the page were individual recipes are shown. 

**The contact page:** *(contact.html - route: /contact)*  
This page has a contact form to ask questions or give remarks.

**The shop page:** *(shop.html - route: /shop)*  
This page has an overview of items that the user can purchase. The links lead to an external website, which opens up in a new window.

**The register page:** *(register.html - route: /register)*  
This page has a register form where the user can register and create an account. After registration the user is led to their own profile page.

**The login page:** *(login.html - route: /login)*
This page has a login form where users that have an account can login. After login the user will be redirected to their own profile page. When the user has no account, they are redirected to the register page.

**The profile page:** *(profile.html - route: /profile/< username >*  
This is the personal profile page of the user. Recipes that the user has added themselves are displayed here. There is an edit and delete button for each recipe. There is also a button to add a new recipe. When the user is logged in, the navbar has extra links for profile and logout. The links for register and login are not shown.

**The add recipe page:** *(add_recipe.html - route: /add_recipe)*  
This page has a form where the user can add new recipes. When submitted, the user is redirected to their profile page. There is a cancel button to abort the action, the user will be redirected to their own profile page.

**The edit recipe page:** *(edit_recipe.html - route: /edit_recipe)*  
This page has a pre-filled form where the user can edit their own recipe. When submitted, the user is redirected to their profile page. There is a cancel button to abort the action, the user will be redirected to their own profile page.
 
**The categories page:** *(categories.html - route: /categories)* 
This is an admin only page. This page has an overview of the existing categories. The admin can add, edit or delete categories by clicking the respective buttons.

**The add category page:** *(add_category.html - route: /add_category)* 
This page is admin only and has and option to add a new category. There is a cancel button to abort the action, the user will be redirected to categories page.

**The edit category page:** *(edit_category.html - route: /edit_category)*  
This page is admin only and has and option to change an existing category. There is a cancel button to abort the action, the user will be redirected to categories page.

**The 403 error handler page:** *(403.html - errorhandler: 403)*
This page shows in case of forbidden access.

**The 404 error handler page:** *(403.html - errorhandler: 404)*
This page shows in case no page is found.

**The 500 error handler page:** *(403.html - errorhandler: 500)*
This page shows in case of an internal service error.


Below is a chart of the webpages and their mutual connections:
![pages chart](https://github.com/chizzletaz/GrandmasBakingCollection/blob/master/static/images/README/Recipe_pages.png)

**BACKEND**

Below are examples of the database collections:
![database category collections](https://github.com/chizzletaz/GrandmasBakingCollection/blob/master/static/images/README/DB_category.png)
![database recipe collections](https://github.com/chizzletaz/GrandmasBakingCollection/blob/master/static/images/README/DB_recipe.png)
![database subscribe collections](https://github.com/chizzletaz/GrandmasBakingCollection/blob/master/static/images/README/DB_subscribe.png)
![database users collections](https://github.com/chizzletaz/GrandmasBakingCollection/blob/master/static/images/README/DB_users.png)

## **Skeleton Level**
### Wireframes
![Wireframes for Home Page](https://github.com/chizzletaz/GrandmasBakingCollection/blob/master/static/images/wireframes/landing.pdf)
![Wireframes for Recipes Page](https://github.com/chizzletaz/GrandmasBakingCollection/blob/master/static/images/wireframes/recipes.pdf)
![Wireframes for Recipe Page](https://github.com/chizzletaz/GrandmasBakingCollection/blob/master/static/images/wireframes/recipe.pdf)
![Wireframes for Contact Page](https://github.com/chizzletaz/GrandmasBakingCollection/blob/master/static/images/wireframes/contact.pdf)
![Wireframes for Shop Page](https://github.com/chizzletaz/GrandmasBakingCollection/blob/master/static/images/wireframes/shop.pdf)
![Wireframes for Register Page](https://github.com/chizzletaz/GrandmasBakingCollection/blob/master/static/images/wireframes/register.pdf)
![Wireframes for Login Page](https://github.com/chizzletaz/GrandmasBakingCollection/blob/master/static/images/wireframes/login.pdf)
![Wireframes for Profile Page](https://github.com/chizzletaz/GrandmasBakingCollection/blob/master/static/images/wireframes/profile.pdf)
![Wireframes for Add Recipe Page](https://github.com/chizzletaz/GrandmasBakingCollection/blob/master/static/images/wireframes/add_recipe.pdf)
![Wireframes for Edit Recipe Page](https://github.com/chizzletaz/GrandmasBakingCollection/blob/master/static/images/wireframes/edit_recipe.pdf)
![Wireframes for Categories Page](https://github.com/chizzletaz/GrandmasBakingCollection/blob/master/static/images/wireframes/categories.pdf)
![Wireframes for Add Category Page](https://github.com/chizzletaz/GrandmasBakingCollection/blob/master/static/images/wireframes/add_category.pdf)
![Wireframes for Edit Category Page](https://github.com/chizzletaz/GrandmasBakingCollection/blob/master/static/images/wireframes/edit_category.pdf)
## **Service Level**

### **Colors**

### **Typography** 
# **Features**

## **Existing Features**

## **Features left to implement**
\
# **Technologies used**

### **Languages used**  
- [HTML5](https://en.wikipedia.org/wiki/HTML) for markup  
- [CSS](https://en.wikipedia.org/wiki/CSS) for styling
- [Javascript](https://en.wikipedia.org/wiki/JavaScript) for  interactivity

### **Frameworks and libraries used**   
- [Bootstrap v5.0](https://getbootstrap.com/)  for precoded code-snippets, like navigation bar, modals, carousel and to help with the responsiveness of the website.
- [jQuery](https://jquery.com/), a javascript library for easier DOM traversing and manipulation and shortening of javascript. 	
- [Google fonts](https://fonts.google.com/) for the fonts used in the website. 
- [Open Trivia Database](https://opentdb.com/api_config.php?ref=public-apis), an API that provides questions and answers for this project.
- [Font Awesome](https://fontawesome.com/) for the icons used on the website.  

### **Tools and Programmes used**
- [Balsamiq](https://balsamiq.com/) for making the wireframes. 
- [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
 to debug and checking/testing the website.
- [Git](https://git-scm.com/) for version control.  
- [GitHub](https://github.com/) for storing and deploying the website.  
- [GitPod](https://www.gitpod.io/) for coding (IDE) the website.  
- [Visual Studio Code](https://code.visualstudio.com/) for trying out code (IDE), due to limited usage time on gitpod.
- [W3C Markup Validation Service](https://validator.w3.org/) to check for markup validity
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) to check the CSS-code.
- [JSHint](https://jshint.com/) to check the Javascript code.
- [Favicon]( http://antifavicon.com/) to make the favicon for the website.

# **Testing**
For testing results, see [Test.md](Test.md)

## **Deployment**

### Deploying to GitHub pages
To deploy this website to GitHub, I followed the these steps:

1. Login to GitHub.com.
2. Go to repositories on the left side and click on the repository named: chizzletaz/Triviata
![repository](/assets/img/examples/github-repositories.png)
3. In the repository click on the ‘Settings’-tab at the top.
![Settings-tab](assets/img/examples/github-settings.png)
4. Scroll down to ‘GitHub Pages’ section
![GitHub Pages section](assets/img/examples/github-pages.png).
5. Under ‘Source’ you see the word ‘None’ with a dropdown menu: select ‘master’
![master](assets/img/examples/github-master.png).
6. Click ‘Save’ and scroll back down to GitHub Pages. 
Here you will find the URL of the deployed website
![URL of the deployed website](assets/img/examples/github-url.png).

Every time commits and pushes are sent to GitHub, the GitHub Pages site is updated shortly after.

For more information about deploying to GitHub Pages check [here](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)

### Forking the GitHub Repository
A fork is a copy of a repository. Forking a repository allows you to freely experiment with changes without affecting the original project.
Do achieve this follow these steps:
1. Login to GitHub.com and follow this link to [the GitHub Repository](https://github.com/chizzletaz/Triviata).
2. At the top right of the page, click on the fork button.
![fork button](assets/img/examples/forking.png)
3. You now have a copy of the repository in your GitHub account.

### Making a Local Clone
1. Follow this link to [the GitHub Repository](https://github.com/chizzletaz/Triviata)
2. Click on the ‘Code’ button 
![Code button](assets/img/examples/github-clone.png)
3. To clone using HTTPS, copy the link that is displayed by clicking on the copy icon ![save icon](assets/img/examples/github-copy.png).
4. Open a terminal in your preferred IDE (e.g. VSCode or Atom)
5. Use  the ‘git clone’ command and add the link that you copied in step 3.
6. A clone will be created locally.

For more info on how to clone a repository check [here](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

# **Credits**
### code
Specific time representation of [datetime](https://www.programiz.com/python-programming/datetime/current-datetime)  
Jinja condition depending on route [yuxiaoy](https://stackoverflow.com/questions/62853545/if-statement-to-determine-which-route-is-used-in-jinja-template-flask)  
Better aligning the recipe cards [bilalkhan891](https://github.com/Dogfalo/materialize/issues/2089)

### Content

### Media
Shop items and [links](https://www.lecreuset.ie/en_IE/)  
Bake background - Photo by <a href="https://unsplash.com/@nate_dumlao?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Nathan Dumlao</a> on <a href="https://unsplash.com/s/photos/baking?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>  
error 500 image - <a href="https://www.freepik.com/free-photos-vectors/website">Website vector created by stories - www.freepik.com</a>  
error 403 image - <a href='https://www.freepik.com/free-photos-vectors/website'>Website vector created by stories - www.freepik.com</a>  
error 404 image - <a href='https://www.freepik.com/free-photos-vectors/technology'>Technology vector created by freepik - www.freepik.com</a>

# Acknowledgements