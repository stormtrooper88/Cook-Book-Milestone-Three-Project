<h1>Cookbook-Milestone-three-project</h1>


This project aims to show my work using the skills learnt in the data fundamentals module along with past modules that I have completed. I have created a cookbook in which users can add, edit and delete their recipes.
The aim is for the user to submit their recipes so that they can later visit their recipe. When they do this, they can edit the recipe or delete it. The recipes will be shown on the homepage so that others are able to see what has already been submitted and those users can eventually replicate these recipes and add their own or edit those already on there. 

<h3>Why this Project?</h3>

I have created this project for the Data Centric Development Milestone Project of Code Institute’s Full Stack Software Development course. The project was to create an online cookbook. This would need to include both front and back end code to allow users to add, edit and delete new recipes. It would also need to include a functionality for users to locate recipes using a short description. 
The Front-End display and functionality use CSS, HTML, and JavaScript. On the Back-End functionality I have used Flask, MongoDB and Python. 

<h2>UX</h2>

<h3>User Stories</h3>

•	As the user, I wish to go to the home page and see the different options available to me.

•	As the user I would like to be able to press on the add recipe button and be taken to the add a recipe page. 

•	As the user, I would like to be able to create a recipe with the following options: recipe, cuisine, a brief description, bases, spices, meat, sauces, vegetables and finally give my instructions to those trying to create my dish. 

•	As a user, I want to be able to see a short description of this recipe so I can distinguish it from other recipes. 

•	As a user, I want to be able to submit this recipe so that it shows up on the home page for others to see my recipe. 

•	As a user, I want to be able to edit a recipe on the website as I made a mistake and need to change the original work. 

•	As a user, I can click on the edit button and it will take me to my original recipe for me to fix my mistakes.

•	As a user, I want the changes to be saved so that if I return to that recipe, the changes I made will be shown.

•	As a user, I want to be able to a delete a recipe on the website by pressing the delete button. 


<h3>Wireframes</h3>

I worked on my wireframes before starting to create the website. I made several wireframes using Balsamiq focusing on the home page, the browser page and the add, edit and delete page. I also create the same page but changed them, so it suited the device the user was using These files. 

https://github.com/stormtrooper88/Cook-Book-Milestone-Three-Project/blob/master/wireframes/Cooking%20recipes%20websiteupdated.pdf

<h2>Features</h2>

<h3>Existing Features</h3>

Add a recipe

Here the user can add a recipe with the following fields required before they can submit. These are: recipe, cuisine, recipe description, base, meat, sauce, spice, vegetable and instructions. The base, meat, sauce, spice, vegetable can be multiple selections rather than one simple choice. I have added a require to each field so that the user cannot submit the recipe without filling out all the fields. Once the user has submitted their recipe, the recipe will be loaded onto a MongoDB database of collections and stored there. The user will then be sent back to the homepage where they will get a responsive message thanking them for adding a recipe. 

Edit a recipe

Here the user can edit their recipe by changing any of the fields named in add a recipe. They can then submit the changes they have made. These changes will then be saved in the database on MongoDB. 

Delete a recipe

Here the user can delete the recipe they have created.

<h3>Features Left to Implement</h3>

•	A feature I would have liked to have added is a search bar. I did include one, but I did not have the time to get running with the database in MongoDB. 

•	A feature I would have liked to include is to add pages as the recipes grow over time, so they do not cluster. 

<h3>Technologies Used</h3>

•	CSS

•	Flask

•	HMTL

•	Javascript

•	Python

•	Materalize

•	MongoDB

<h3>Testing</h3>

1.	Adding a recipe: 

i.	I went to the "Add a recipe" button which will load up and the addrecipe html.

ii.	I tried to submit the empty form which verified that an error message about the required fields appears.

iii. I tried to submit without completing each section of the form to verify that an error appears on the fields missed out. 

iv.	I tried to submit the form with all inputs valid and verify that a success message appears which it does whilst sending the user back to the homepage with a “thank you for adding your recipe!” message and their recipe with a short description. 

2.	Editing a recipe: 

i.	I went to the "EDIT" button which will load up and the editrecipe html.

ii.	Here I was able to edit the recipe as I wished and then submitted the changes which took me back to the homepage.

iii.	Here I was able to see the changes made by noticing a change when filling out the short description field. 

3.	Deleting a recipe: 

i.	On the homepage there is a red button called “DELETE”.

ii.	Once I clicked on this, the page refreshed, and the recipe was removed. 


<h3>Database Schema</h3>

The database in MongoDB is structured with several collections: bases, meats, recipes, sauces, spices and vegetables. Within each collection of bases, meats, sauces, spices and vegetables, the user can pick different options which allow them to be precise and choose several different options. 
The recipe that the user creates will be stored in recipes with all the other collections being found there along with a description and instructions. The recipe is then shown on the homepage as a description with an option to either edit or delete it. 


<h3>Deployment</h3>

<h4>Heroku</h4>

For the deployment of Heroku I used the config vars:

•	IP = 0.0.0.0

•	PORT = 5000

https://tcb-cookbook-milestone-project.herokuapp.com/

There are no differences between the development and deployed version. This was run using Python3. 

<h4>Github</h4>

To clone the code used in this project you can do as following: 

to run the code locally then you can clone my git repository and run it an editor such as Visual Studio Code. 

Simply past git clone https://github.com/stormtrooper88/Cook-Book-Milestone-Three-Project into your terminal. Once you have done this you will want to stop the connection with the GitHub repository. You do this by typing into your terminal git remote rm origin. Alternatively, you can press the “clone or download” button on the link above that will allow you to clone the work. 

<h3>Credits</h3>

<h4>Content</h4>

•	All content is of my own work through the videos provided by Code Institute’s  task manager mini project and Thorin & Co project. 

<h3>Media</h3>

•	No photos or videos were used within this project.

<h3>Acknowledgements</h3>

•	I would like to acknowledge the tutor that now extends to my time zone and their patience with my questions. 

•	I would also like to acknowledge my mentor, Dick, who has helped me throughout the course and the support system in place at code institute. 


