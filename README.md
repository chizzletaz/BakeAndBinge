# Bake and Binge
![Preview image](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/preview.png)

Like many others, I've always loved baking and cooking. Over the years you try out new recipes and share the result with your family and friends.
When the recipe is a hit you often you get the question: 'Can I get the recipe?'.
Usually you scribble the recipe down on a piece of paper. You collect them and put them on a pile.
I have a lot of those papers lying in the kitchen as well and I also lost some of the recipes, because I lost the piece of paper.  
So wouldn't it would be much easier to add your recipe online and share it that way? No more scribbling, no more loose papers!
That way you can bake good recipes and binge them at the same time!

I have narrowed the recipes down to only baking recipes, in order to reduce the amount and difficulty of programming and design options.   
For the CSS-framework I opted to work with Materialize instead of Bootstrap. Both to learn to work with another framework and to show that I can work with other frameworks.

#### A live version can be viewed [here](https://bake-and-binge.herokuapp.com)

# Table of Content
- [User Experience (UX)](#user-experience-ux)  
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
    * [Forking this GitHub Repository](#forking-this-github-repository)
    * [Cloning this GitHub Repository](#cloning-this-github-repository)
- [Credits](#credits)

***
# **User Experience (UX)**
## **Strategic level**

The target audience are users that want to search or browse recipes and add their own. By adding their own recipe, they can share it with others.  
With this website I want to create a website for people to find and try out nice recipes and give them the opportunity to add their own. This way users can share their recipes online.   
With this project I also hope to show my knowledge and application of the added coding skills I’ve learned, i.e. Python, using Flask and MongoDB, as well as using a different CSS-framework, namely Materialize.

### **User stories:**  
*First time users:*
- As a first time user, I want to navigate easily across the site.
- As a first time user, I want to browse the recipes, so I can find inspiration for a recipe.  
- As a first user, I want to know how to add a recipe.

*General users:*
- As a user, I want to be able to use the website on different screen sizes. 
- As a user, I want to search recipes by keyword(s), so I can find recipes more purposefully. 
- As a user, I want to filter recipes by category, so I narrow down my search and/or search per category. 
- As a user, I want to sort the recipes by date, popularity, alphabet, so I can better choose a recipe. 
- As a user, I want to see if a recipe is gluten free, vegan, etc so I can find out quickly if it matches my diet.
- As a user, I want to be able to delete my profile, if I no longer wish to use the website. 

*Regular users:*
- As a regular user, I want to have my own page, so I can manage my own recipes. 
- As a regular user, I want to add my own recipes, so I can share them with others on the website.
- As a regular user, I want to edit and/or delete my own recipes, so I can keep my recipes up to date. 
- As a regular user, I want to contact the site owner in case I have questions or remarks. 
- As a regular user, I want to be able to rate other recipes. 
- As a regular user, I want to be able to save other people's recipes.
- As a regular user, I want to be able to share recipes. 
- As a regular user, I want to get the latest news and updates. 

### **Developer stories**
*Admin/site owner:*
- As a site owner, I want to promote certain baking tools, in order to increase commission on the sales.
- As a site owner, I want to be able to have access to the recipes categories and the option to manage them.
- As a site owner, I want users to register and login, before they can add, edit or delete their recipes.

## **Scope level**
I've opted for an MVP (Minimal Viable Project) and work my way up from there.  
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
3. An option to save a recipe.
4. An explanation on how to add recipes.
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
- The user get's a feedback when an error has occurred (warning text or via error handlers).

### **The pages**
        FRONTEND  
The website will have 13 pages plus 3 error handler pages. Each page will have a navbar and a footer, except for the error handler pages.

The navbar links are shown depending on whether a user is logged in or not and if the user is the admin or not.   
The main navbar has links to home, shop, contact, recipes (dropdown menu to search by category), register, login and a search icon.  
When a user is logged in, the register and login links are hidden and a profile link and logout link are shown.  
When the user is admin, an extra link for managing categories is shown.  

The footer has a section to subscribe to the newsletter and links to socials.

#### Description of the pages

- **The landing page/home page:** *(index.html - route: /, /home)*  
The main page has the main navbar. Below that a hero image and a short explanation for the site. Beneath that are the latest recipes.

- **The recipes page:** *(recipes.html - route: /recipes)*  
On this page all the recipes are shown. For large screens there are buttons to filter the recipes by category (route: /recipes/< category_name >). For smaller screens, there is a select input.   
There is a search bar which leads to this same page with the results of the search (route: /search). From there the user can go to an individual recipe page. 

- **The recipe page:** *(recipe.html - route: /recipe/< recipe_id >)*  
This is the page were individual recipes are shown. 

- **The contact page:** *(contact.html - route: /contact)*  
This page has a contact form to ask questions or give remarks.

- **The shop page:** *(shop.html - route: /shop)*  
This page has an overview of items that the user can purchase. The links lead to an external website, which opens up in a new window.

- **The register page:** *(register.html - route: /register)*  
This page has a register form where the user can register and create an account. After registration the user is redirected to their own profile page. There is a button to go to the login page, if a user already has an account.

- **The login page:** *(login.html - route: /login)*  
This page has a login form where users that have an account can login. After login the user will be redirected to their own profile page. There is a button to the register page, in case the user has no account.

- **The profile page:** *(profile.html - route: /profile/< username >*  
This is the personal profile page of the user. Recipes that the user has added themselves are displayed here. There is an edit and a delete button for each recipe. There is also a button that opens a modal with an explanation on how to add a new recipe. When the user is logged in, the navbar has extra links for profile and logout. The links for register and login are not shown.

- **The add recipe page:** *(add_recipe.html - route: /add_recipe)*  
This page has a form where the user can add new recipes. When submitted, the user is redirected to their profile page. There is a cancel button to abort the action, the user will be redirected to their own profile page.

- **The edit recipe page:** *(edit_recipe.html - route: /edit_recipe)*  
This page has a pre-filled form where the user can edit their own recipe. When submitted, the user is redirected to their profile page. There is a cancel button to abort the action, the user will be redirected to their own profile page.
 
- **The categories page:** *(categories.html - route: /categories)*   
This is an admin only page. This page has an overview of the existing categories. The admin can add, edit or delete categories by clicking the respective buttons.

- **The add category page:** *(add_category.html - route: /add_category)*   
This page is admin only and has and option to add a new category. There is a cancel button to abort the action, the user will be redirected to categories page.

- **The edit category page:** *(edit_category.html - route: /edit_category)*  
This page is admin only and has a prefilled form to change an existing category. There is a cancel button to abort the action, the user will be redirected to categories page.

- **The 403 error handler page:** *(403.html - errorhandler: 403)*  
This page is shown in case of forbidden access.

- **The 404 error handler page:** *(403.html - errorhandler: 404)*  
This page is shown in case no page is found.

- **The 500 error handler page:** *(403.html - errorhandler: 500)*  
This page is shown in case of an internal service error.


Below is a chart of the webpages and their mutual connections:  
![pages chart](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/Recipe_pages.png)

        BACKEND

Below are examples of the database collections:  
**category collections:**  
![database category collections](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/DB_category.png)  
**recipe collections:**  
![database recipe collections](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/DB_recipe.png)  
**subscribe collections:**  
![database subscribe collections](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/DB_subscribe.png)  
**users collections:**  
![database users collections](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/DB_users.png)

## **Skeleton Level**
### Wireframes
- [Wireframes for Home Page](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/wireframes/landing.pdf)  
- [Wireframes for Recipes Page](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/wireframes/recipes.pdf)  
- [Wireframes for Recipe Page](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/wireframes/recipe.pdf)  
- [Wireframes for Contact Page](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/wireframes/contact.pdf)  
- [Wireframes for Shop Page](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/wireframes/shop.pdf)  
- [Wireframes for Register Page](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/wireframes/register.pdf)  
- [Wireframes for Login Page](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/wireframes/login.pdf)
- [Wireframes for Profile Page](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/wireframes/profile.pdf)  
- [Wireframes for Add Recipe Page](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/wireframes/add_recipe.pdf)  
- [Wireframes for Edit Recipe Page](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/wireframes/edit_recipe.pdf)  
- [Wireframes for Categories Page](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/wireframes/categories.pdf)  
- [Wireframes for Add Category Page](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/wireframes/add_category.pdf)  
- [Wireframes for Edit Category Page](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/wireframes/edit_category.pdf)  


## **Service Level**

### **Colors**
To ensure that colours match well, I've choosen to use the colours of Materialize.  
In food, bright colours signify flavours such as sweets and desserts - pink is expecially associated with baking and sweets.
Therefore the main colour is pink. As a contrasting colour I've chosen green.

![colourB&B](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/coloursB&B.png)  

- ![#ff4081](https://via.placeholder.com/15/ff4081/000000?text=+) #ff4081 is used as the main colour and is the pink accent-2 colour of Materialize.
This colour is used for buttons that have to stand out, shadow-text and the underline of the links upon hovering.  
- ![#fce4ec](https://via.placeholder.com/15/fce4ec/000000?text=+) #fce4ec is the pink lighten-5 colour on Materialize. This colour is used for the background of the modals.    
- ![#009688](https://via.placeholder.com/15/009688/000000?text=+) #009688 is the standard button colour of Materialize. I've kept this colour for the less important buttons (the submit button in the footer and the info button on the profile page).  
- ![#80cbc4](https://via.placeholder.com/15/80cbc4/000000?text=+) #80cbc4 is the teal lighten-3 colour on Materialize. This colour is used for the background colour of the flash messages.
- ![#fefefa](https://via.placeholder.com/15/fefefa/000000?text=+) #fefefa is used as the background colour. It is a slightly off white colour and emphasizes a simple and clean design.  
- ![#66bb6a](https://via.placeholder.com/15/66bb6a/000000?text=+) #66bb6a is used for the border of the edit buttons.  
- ![#d32f2f](https://via.placeholder.com/15/d32f2f/000000?text=+) #d32f2f is used for the border of the delete and cancel buttons.  

### **Typography** 
For the title(h1) and the logo, I've used Kaushan Script. This is a handwritten font, which adds a more unique and homemade feeling.  
> ![example of kaushan script text](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/kaushan-script.png)  

To keep the design consistent, I've decided to use one font-family: Noto.  
Noto fonts are intended to be visually harmonious across multiple languages, with compatible heights and stroke thicknesses.

For the other headers (h2 to h5) I've used Noto Serif. 
> ![example of noto serif text](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/noto-serif.png)  

For the rest of the text I've used Noto Sans, this is a sans serif font, which are well suited for displaying text on computer screens.  

> ![example of noto sans text](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/noto-sans.png)  
---
# **Features**

## **Existing Features**

- **Responsiveness** on all viewports, which allow users to use the website on all devices.
- A **navigation bar**, which allows users to easily navigate the website. On devices below 992px, the navbar collapses into a hamburger menu, to reduce the real estate and create a cleaner, calmer look.
- A **subscription option**, which allows users to subscribe to the newsletter, by entering their email address in the subscribe card. 

- **Recipe cards**, which allow users to see information about a recipe. By clicking on the recipe, the user is redirected to the recipe page.
- **Register functionality**, which allows users to create an account, by filling in the register form. 
- **Login functionality**, which allows users to log in their account, by filling in the login form. 
- **Logout functionality**, which allows users to log out of their account, by clicking the logout button.
- A **CTA (Call to Action button) button**, which allows users to register to the website (incase they are not logged in).
- A **search bar**, which allows users to search recipes, by entering a keyword in the search bar.
- **Category buttons**, which allow users to filter recipes by category, by clicking on the corresponding button.
- **Error handler pages**, which handle *'forbidden access'*, *'page not found'* and *'internal server'* errors, by giving users information on the error that has occurred and redirect the user back to the home page.
- A **collapsible**, which allows users to get more information about a product on the shop page, by clicking on the three dots icon.

**Modals** 
- A modal for how to add a recipe, which gives users information on how to add a new recipe.
- A confirmation modal as a defensive programming tool, which allows users to confirm to delete a recipe or category (in case of admin) or to log out.

**Icons**
- Social media icons, which allow users to go to the corresponding social platform, by clicking on the social icon.
- Icons as a visual aid, which allow users to quickly and intuitively see what is meant. E.g. a cross-icon to signify a delete function, a plus-icon to signify to add a recipe or category or an @-icon to enter an email address.

**Forms**
- A form that allows users to get in contact with the website owner, by filling in the form.
- A form that allows users to add a new recipe, by filling in the form on the add-recipe page.
- A form that allows users to edit a recipe, by editing the prefilled recipe form on the edit-recipe page.
- A form that allows the admin to add a new category, by filling in the form on the add-category page.
- A form that allows the admin to edit a category, by editing the prefilled form on the edit-category page.

**CRUD (Create, Read, Update, Delete) functionality**  
*Create:*  
- Logged in users can create new recipes.
- Admin can create new categories.  

*Read:*  
- All users can search and view recipes.  

*Update:*
- Logged in users can edit their own recipes.
- Admin can edit categories.

*Delete:*
- Logged in users can delete their own recipes.
- Admin can delete categories.

## **Features left to implement**
- **Rating/liking recipes** by other users.
- **Sharing recipes** via social media, email or other communication forms.
- A **save option** to save other users' recipes.
- **Deleting a profile**, when a user doesn't want to use the account anymore.
- A **sort option**, so users can sort by attribute (alphabetically, time, rating, etc).
- An **add labels** option to add labels about (e.g. vegan, gluten free) to recipes.
- **Pagination**, in case the number of recipes gets too large. It would be more user friendly to have pagination.
- **Reset password**, in case the user has lost their password and wants to reset it.
---
# **Technologies used**

### **Languages used**  
- [HTML5](https://en.wikipedia.org/wiki/HTML) for markup.  
- [CSS](https://en.wikipedia.org/wiki/CSS) for styling.
- [Javascript](https://en.wikipedia.org/wiki/JavaScript) for interactivity.
- [Python3](https://www.python.org/) for backend programming.

### **Frameworks and libraries used**   
- [Materialize v1.0.0](https://materializecss.com/) a frontend-framework with precoded code-snippets, like navigation bar, modals, and to help with the responsiveness of the website.
- [jQuery](https://jquery.com/), a javascript library for easier DOM traversing and manipulation and shortening of javascript. 	
- [Google fonts](https://fonts.google.com/) for the fonts used on the website. 
- [Font Awesome](https://fontawesome.com/) for the icons used on the website. 
- [Flask](https://flask.palletsprojects.com/en/2.0.x/) is a micro Python web application framework. 
- [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) is a fast, expressive, extensible templating engine for Python.

### **Tools and Programmes used**
- [Balsamiq](https://balsamiq.com/) for making the wireframes. 
- [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
 to debug and checking/testing the website.
- [Git](https://git-scm.com/) for version control.  
- [GitHub](https://github.com/) for storing the files and version control of the website.  
- [Visual Studio Code](https://code.visualstudio.com/) for coding (IDE) the website.
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) for the cloud database.
- [Heroku](https://www.heroku.com/) a cloud platform for deploying the website.
- [W3C Markup Validation Service](https://validator.w3.org/) to check for markup validity.
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) to check the CSS-code.
- [JSHint](https://jshint.com/) to check the Javascript code.
- [PEP8 checker](http://pep8online.com/) to check the python code for PEP8 requirements. 
- [Favicon]( http://antifavicon.com/) to make the favicon for the website.
- [Coolors](https://coolors.co/) to make the colour scheme.
---
# **Testing**
For testing results, see [Testing.md](https://github.com/chizzletaz/BakeAndBinge/blob/master/Testing.md)

---
## **Deployment**
Heroku is used to deploy this application, since GitHub can only deploy static websites.

This application was developed using VSCode as IDE, commited to Git and pushed to GitHub.
The GitHub repository is linked to the Heroku App via automatic deployment (see below).
Every time commits and pushes are sent to GitHub, the Heroku App is updated shortly after.

### Deployment to Heroku
Before we deploy our Heroku application, we need to setup some files that Heroku needs to run the app.  
1. **Create a 'requirements.txt' file**  
    A requirements.txt file contains a list of the Python dependencies that our project needs in order to run successfully.  
    First, we need to tell Heroku which applications and dependencies are required to run our app:
    1. In the terminal window of the IDE type: **pip3 freeze --local > requirements.txt**
    2. Then type: **git add -A**
    3. Then type: **git commit -m “Add requirements.txt”**

2. **Create a Heroku 'Procfile'**  
    The Procfile is what Heroku looks for to know which file runs the app, and how to run it.
    1. In the terminal window of the IDE type: **echo web: python app.py > Procfile**
    2. Then type: **git add Procfile**
    3. Then type: **git commit -m “Add Profile.”**
    4. Then type: **git push**  

    > The Procfile might add a blank line at the bottom, and sometimes this can cause problems, when running our app on Heroku, so just delete that line and save the file.

3. **Create a Heroku App**
    1. Create a new app by clicking the ‘New’ button.
    ![new Heroku app button](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/new-app.png)
    2. Give a unique name and set region to your nearest region.
    ![name and region input](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/name-region.png)
    3. Click ‘Create App’

4. **Setup automatic deployment from GitHub/Connect Heroku app to GitHub.**  
    1. Go to the Deploy tab.  
    ![deploy tab](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/deploy.png)  
    2. Under 'Deployment method', Click on 'Connect to GitHub'.
    ![connect to github button](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/connect-to-github.png)
    3. Under 'Connect to GitHub', enter the GitHub repository name and click ‘Search’.
    ![search repository name](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/search-repo.png)
    4. Click 'Connect'.
    ![connect repository name](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/connect-repo.png)


    Before enabling automatic deployment, the hidden variables like IP, PORT, secret key etc., need to be added to Heroku.  
5. **Add config vars to Heroku**    
    1. Go to the Settings tab.  
    ![setting tab](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/settings.png)  
    2. Click on 'Reveal Config Vars'.  
    ![Config vars tab](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/config-vars.png)  
    3. Enter the values of the config vars.
    ![setting tab](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/config-vars-values.png)  

    > Tip: copy the secret key from the env.py file and enter as the value for the secret key.  

    4. Go back to the Deploy Tab.  
    5. Scroll down to Automatic deploys and click the ‘Enable Automatic Deploys’ button.  
    ![enable automatic deploy button](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/automatic-deploy.png)
    6. Click on ‘Deploy Branch’.
    ![deploy branch button](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/deploy-branch.png)
    7. When Heroku has finished building the application, the following message should appear:
    ![succesful deployment](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/succesful-deploy.png)
---
### Forking this GitHub Repository
A fork is a copy of a repository. Forking a repository allows you to freely experiment with changes without affecting the original project.
To achieve this follow these steps:
1. Login to GitHub and follow this link to [the GitHub Repository](https://github.com/chizzletaz/BakeAndBinge).
2. At the top right of the page, click on the fork button.  
![fork button](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/forking.png)
3. You now have a copy of the repository in your GitHub account.

### Cloning this GitHub repository
1. Log in to GitHub and follow this link to [the GitHub Repository](https://github.com/chizzletaz/BakeAndBinge)
2. Click on the ‘Code’ button 
![Code button](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/github-clone.png)
3. To clone using HTTPS, copy the link that is displayed by clicking on the copy icon 
![save icon](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/github-copy.png).
4. Open a terminal in your preferred IDE (e.g. VSCode or Atom)
5. Use  the ‘git clone’ command and add the link that you copied in step 3.
6. Or for VSCode: click 'Explorer' or 'Shift + CMD + E'. 
7. Click the button 'Clone Repository', add the url you copied above and hit enter.
8. A clone will be created locally.

For more info on how to clone a repository check [here](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

---
# **Credits**
### code
- Specific time representation of [datetime](https://www.programiz.com/python-programming/datetime/current-datetime)  
- Jinja condition depending on route [yuxiaoy](https://stackoverflow.com/questions/62853545/if-statement-to-determine-which-route-is-used-in-jinja-template-flask)  
- Better aligning the recipe cards [bilalkhan891](https://github.com/Dogfalo/materialize/issues/2089)  
- [Hide](https://jinja.palletsprojects.com/en/3.0.x/tricks/) navbar and footer on error handler pages.

### Content
Recipes:
- [Twix pie](https://veganwifey.com/een-vegan-twix-taart/)  
- [Artisan bread](https://sallysbakingaddiction.com/homemade-artisan-bread/#tasty-recipes-80079-jump-target)  
- [Almond cookies](https://www.foodless.nl/amandelkoekjes-met-citroen/)  

The other recipes are my own or come from my own collection of recipes written on a piece of paper.  

### Media
- Shop items and [links](https://www.lecreuset.ie/en_IE/)  
- Pink background on landing page - Photo by <a href="https://unsplash.com/@sharonmccutcheon?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Sharon McCutcheon</a> on <a href="https://unsplash.com/s/photos/baking?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
- Bake background - Photo by <a href="https://unsplash.com/@nate_dumlao?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Nathan Dumlao</a> on <a href="https://unsplash.com/s/photos/baking?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>  

- Error 500 image - <a href="https://www.freepik.com/free-photos-vectors/website">Website vector created by stories - www.freepik.com</a>  
- Error 403 image - <a href='https://www.freepik.com/free-photos-vectors/website'>Website vector created by stories - www.freepik.com</a>  
- Error 404 image - <a href='https://www.freepik.com/free-photos-vectors/technology'>Technology vector created by freepik - www.freepik.com</a>
- [Colour codes](https://usbrandcolors.com/tech/) of social media icons.
---
# Acknowledgements
I want to thank my mentor Antonio Rodriguez for guiding me through this project and helping me with some solutions.
Especially with the relations between collections on MongoDB and the development of the corresponding python code for the functions in the app.py file.  
I want to thank Tutor support at CI and fellow Slack members for answering my questions.