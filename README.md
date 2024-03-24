# DevOps Coursework assignment 1 - E-Shop eCommerce Webstore

This repository contains the source code for the E-Shop eCommerce webstore, a full stack web application developed as a portfolio project for The ATU - Donegal. The website can be viewed at (https://e-commerce-web-shop.onrender.com).

# Overview

Welcome to [E-Shop](https://e-commerce-web-shop.onrender.com)
This Website is an e-Commerce Webstore that was designed and developed as an Portfolio Project for The DevOps Coursework assignment 1 at ATU - Donegal.

E-Shop is a demo e-commerce platform showcasing a wide range of affordable, full-stock cloth products and to a diverse and growing target audience. The project demonstrates the developer's proficiency in creating a comprehensive e-commerce solution, with an appealing design, intuitive navigation, and responsive layout.

Please note that this project is for assessment purposes only and does not accept real credit or debit card payments. Any purchases or bookings made on the website will not be fulfilled.

The project is for assessment purposes only and will not accept any genuine credit or debit card payments and any purchases or booking made will not be fullfilled. The [E-Shop](https://e-commerce-web-shop.onrender.com) is a full stack, E-commerce, web application offering affordable, full ctock products and solutions to a growing and diverse target audience.

- User Interface and Design: The website features a visually appealing and modern design, making it easy for users to browse and navigate the site. The layout is responsive, ensuring that the website looks great on various devices, including desktops, laptops, tablets, and smartphones.

- Product Catalog: E-Shop offers a wide range of cloth products and solutions, organized into different categories for easy browsing. Users can explore various sections to find the items they're looking for.
  
- User Accounts and Authentication: E-Shop has implemented user account creation and authentication, allowing users to create profiles, save their preferences, and view their order history. This feature demonstrates the developer's ability to integrate essential user management components in an e-commerce platform.
  
- Shopping Cart and Checkout: The website incorporates a shopping cart system that enables users to add products to their cart, review their selections, and proceed to the checkout process. Though it doesn't accept real credit or debit card payments, the website demonstrates the developer's understanding of integrating a seamless and secure checkout experience.
  
- Performance and Optimization: The E-Shop website is built with performance in mind, ensuring fast load times and an optimized user experience. This aspect showcases the developer's knowledge of best practices in web development and their ability to create a high-performing e-commerce platform.

Overall, the E-Shop is a well-rounded e-commerce web application that demonstrates the developer's expertise in full stack web development, specifically in the context of e-commerce. The website is an excellent portfolio project that highlights their proficiency in various aspects of web development, from front-end design to back-end functionality, and provides a strong foundation for potential future projects.

Please use the link below to view the deployed project. If you wish to make a mock purchase, you can use the following details:

Test credit cart detailes:

- Card Number: 4032032685528157
- Exp Date: Any (future) date using the format MM/YY
- CVN = any 3 digit number
- ZIP code = any 5 numerals
- Mobile: 203-550-1340


Test PayPal detailes:

Email: kingmon@gmail.com

Password: **********


Any payments made using an actual payment card will fail and the card will not be charged. No orders made will be fulfilled.


## Project goals

The primary goals of the E-Shop e-commerce webstore project are:

1. **Portfolio Showcase:** Demonstrate the developer's skills and capabilities in full-stack web development, specifically in the context of e-commerce, as part of The DevOps Coursework assignment 1 at ATU - Donegal.
   
2. **User Experience:** Create a visually appealing, responsive, and user-friendly web application that offers an intuitive browsing and shopping experience for a diverse and growing target audience.

3. **Product Catalog:** Design a comprehensive product catalog with a wide range of home products and solutions, organized into categories for easy browsing and navigation.
   
4. **User Accounts and Authentication:** Integrate user account creation and authentication features, enabling users to create profiles, save their preferences, and view their order history.
   
5. **Shopping Cart and Checkout:** Develop a seamless shopping cart system and a simulated checkout process that demonstrates the understanding and implementation of a secure and user-friendly e-commerce transaction flow.
   
6. **Performance and Optimization:** Optimize the website for performance and fast load times, ensuring a smooth and enjoyable user experience.
   
7. **Scalability and Extensibility:** Build a solid foundation that allows for future expansion and refinement, making it possible to add new features, products, and functionalities as the platform grows.

<hr>

## UX (User Experience)

### User stories

#### First time visitor goals

As a first time visitor, I want:
* to easily understand the main purpose of the site.
* to be able to easily navigate throughout the site.
* to be able to register a user account to access all content without restrictions.
* to be able to log out of my user account.
       
        
#### Returning and frequent user goals

As a returning user, I want:
* to sign in to my user account.
* to make a service checkout.
* to view my purchase details. 
* to edit my purchase details or delete them.
* to create an account, edit and delete them.
* to sign out of my account to keep my account safe.
* to be able to reserve an items in the busket for a later come back, view items details and make changes in shopping cart and delete my items from it.


#### Site Administrator goals
As a Site Administrator I would like to be able to create, view, edit and delete products and create, edite, delete categories.

### Agile tools

The GitHub Projects section was used as a [Kanban board](https://github.com/users/SergiyKochenko/projects/15) for the development of this project, which made it possible to break down the project execution into subtasks and make it easier to complete and track project progress.


## Design Structure

The site was based on my expepience from the CodeInstitute. The look of the site, color scheme, font, logo and image for the home page were made by myself from the template.

<hr>

## Environment and Settings
- Environment Variables: Utilizes django-environ to manage environment variables, ensuring sensitive information like database credentials and secret keys aren't hard-coded in the source code.
- Base Directory Setup: Establishes a base directory (BASE_DIR) for the project, which is used to construct paths to various resources and configurations.
- Security Settings: Includes settings for keeping the secret key secure and configuring CSRF trusted origins.
## Applications and Middleware
- Installed Applications: Lists Django's default apps and additional apps specific to the e-commerce functionality (store, cart, account, payment) as well as utility apps like mathfilters and crispy_forms for form styling.
- Middleware Configuration: Specifies the middleware components that are activated in the Django project, which includes security, session, authentication, and message middleware among others.
## URLs and Templates
- Root URL Configuration: Points to ecommerceshop.urls as the module that handles the project's URL configurations.
- Templates Configuration: Defines the settings for template handling, including the directories where templates are stored and the context processors that add additional context to templates globally.
## Database Configuration
- Database Settings: Initially, it shows a default configuration using SQLite, then it's overridden by PostgreSQL settings from environment variables, demonstrating the project's readiness for production deployment with a scalable database.
## Authentication and Authorization
- Password Validators: Lists validators for user passwords to enforce security practices, such as minimum length and common password checks.
## Internationalization
- Language and Timezone: Sets the default language to English (US) and timezone to UTC, with options enabled for internationalization and timezone support.
## Static and Media Files
- Static and Media Settings: Configures URLs and directories for serving static files and user-uploaded media, including integration with AWS S3 for storage.
## Email Configuration
- Email Backend: Sets up Django to use SMTP for email sending, with settings for the host, port, and authentication details pulled from environment variables.
## Cloud Storage
- AWS S3 Integration: Provides settings for using AWS S3 for file storage, including credentials, bucket name, and domain configuration.
## Administrative Customizations
- Admin Styling: Adjusts the path for admin static files to ensure the admin interface is styled correctly.

<hr>

## Tools used

- [Google Fonts:](https://fonts.google.com/) Was used to to incorporate font styles.  
- [Font Awesome](https://fontawesome.com/): was used to create the icons used on the website.
- [Bootstrap](https://getbootstrap.com/) Was used to create the front-end design.
- [Gitpod:](https://Gitpod.io/) Gitpod was used as IDE to commit and push the project to GitHub.
- [GitHub:](https://github.com/) Was used as a version control system to manage the code
- [Freelogoservices:](https://www.freelogoservices.com/) Was used for creating logo
- [TinyPNG:](https://www.figma.com/) Was used to reduce the size and weight of images and optimizing interaction with the site
- [Color Palette Generator:](https://mybrandnewlogo.com/color-palette-generator) Was used to select colors of the web site.
- [Pip3](https://pypi.org/project/pip/): is the package manager to install Python modules and libraries.
- [Gunicorn](https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/gunicorn/): "Green Unicorn" is a Python Web Server Gateway to translate HTTP Requests for Python to understand.
- [Spycopg2](https://pypi.org/project/psycopg2/): PostgreSQL database adapter so I can manage the Database in Python.
- [Cloudinary](https://cloudinary.com/): the image hosting service used to upload images and other media.
- [VSCode](https://code.visualstudio.com/): the IDE used to develop the website.
- [Chrome Developer Tools](https://developer.chrome.com/docs/devtools/open/): was used to debug the website.
- [W3C Validator](https://validator.w3.org/): was used to validate HTML5 code for the website.
- [W3C CSS validator](https://jigsaw.w3.org/css-validator/): was used to validate CSS code for the website.
- [Github Projects and Kanban board](https://) was used to track the progress of the project in general and of every application in the project.
- [Free grammar checker](https://www.zoho.com/writer/free-grammar-checker.html)
- [Free formatter HTML](https://www.freeformatter.com/html-formatter.html#before-output): was used to format HTML5 code for the website.
- [Free cleancss CSS3](https://www.cleancss.com/css-beautify/): was used to format CSS3 code for the website.
- [Free black vercel](https://black.vercel.app/): was used to format python code for the website.
- [JSHint](https://jshint.com/): was used to validate Java Script code for the website.
<br>


##  Deployment

The project was developed using Visual Studio, the project code is stored on GitHub, and then deployed to [Render](https://render.com/).
To deploy, follow these steps:


1. Sign Up/Login: First, sign up for an account on Render or log in if you already have one.

2. Connect to GitHub/GitLab: Render supports automatic deployments from GitHub and GitLab. You'll need to connect your Render account to your GitHub or GitLab account. This allows Render to access your repository.

3. Create a New Web Service: Once logged in, go to your dashboard and click on the "New +" button, then select "Web Service". This starts the process of creating a new web service for your website.

4. Select Your Repository: You will be prompted to select the repository where your website code is stored. Choose the repository you wish to deploy.

5. Configure Your Web Service:

- Branch: Select the branch you want to deploy.
- Build Command: This is the command Render will run to build your website. It might be something like npm run build for Node.js projects.
- Start Command: This is the command that starts your website, such as npm start for Node.js.
- Environment: Choose the environment (such as Node, Python, Ruby) that matches your project.
- Root Directory: If your project is not in the root of your repository, specify the directory.

6. Environment Variables: If your project needs environment variables (like API keys), you can add them in the Environment tab.

7. Deploy: After configuring your web service, click the "Create Web Service" button. Render will then clone your repository, run the build command, and deploy your website.

8. Custom Domain (Optional): After your web service is up and running, you can add a custom domain through the "Settings" tab of your web service. Render provides automatic HTTPS for custom domains.

9. Automatic Deployments: By default, Render will automatically deploy your website on each push to the selected branch of your connected repository. You can adjust these settings in the "Settings" tab.

10. After successful deployment message in the page top left corner click the button labeled 'Open app' and you can access live app.


### Forking the GitHub Repository

To use this code and make changes without affecting the original code, it is possible to 'fork' the code on the GitHub repository through the following steps:

1. Create  or log into your GitHub account.
2. Go to the GitHub [repository](https://github.com/SergiyKochenko/E-Shop).
3. Click the 'Fork' button in the upper right-hand corner of the page.
A copy of the repository will be available in your own repository.


### Making a Local Clone
1. Log in to GitHub and locate the GitHub Repository
2. Under the repository name choose button "Code",  click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open your development editor of choice and open a terminal window in a directory of your choice
5. Type *git clone*, and then paste the URL you copied in Step 3.

``> git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY``

Press Enter. 

Your local clone will be created.

For more information follow this [link](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop).

<br/>

## Manual Testing

#### Device Testing

The Project was tested using a multi-device emulator with different display sizes in the Google Chrome Developer Dashboard.
The following devices have been tested:

- Nest HubMax (Desktop)
- iPad Pro (Tablet)
- iPad Air (Tablet)
- iPad Mini (Tablet)
- Galaxy Tab S4 (Tablet)
- Nexus 7 (Mobile)
- Nokia N9 (Mobile)
- iPhone 12 Pro Max (Mobile)
- iPhone 5/SE (Mobile)
- iPhone 4 (Mobile)

#### Browsers Tested

Testing has been carried out on the  following browsers: 
  - Google Chrome
  - Firefox
  - Microsoft Edge
  - Safari iOS

The site was constantly tested during the process of creating the site in the Visual Studio Code Environment and the deployed site on Render was also tested in terms of user experience.
The available functionality and user experience is reflected in the table below.

| Goals/actions  | As a guest | As a logged user  | Result | Comment |
|--|:--:|:--:|:--:|--|
| User can use menu and navigating through pages | &check; | &check; | Pass | Click on menu item redirects to appropriate page |
| User can see the home page | &check; | &check; | Pass | |
| User can see the Pricing page | &check; |&check;  |  Pass| |
| User can see the Sign Up page | &check; |&check;  |  Pass| |
| User can see the Login page  | &check; |&check;  |  Pass| |
| User can see the Logout page  | &check; |&check;  |  Pass| |
| User can click the Create an account button  | &check; |&check;  |  Pass| Redirects to the page with a message that the user must register or log in for guest or shows up form for authorized user |
| User can see the Register page | &cross; | &check;  | Pass |A page is displayed with a message that the user must register or log in  |
| User can fill fields in the form the Register page | &cross; | &check;  | Pass |This page and form are available only to authorized users |
| User can see the Dashboard page   | &cross; | &check;  | Pass | This page is available only to an authorized users|
| User can see the Prifile manage page  | &cross;  | &check;  | Pass | This page is available only to authorized users|
| User can Update account form on the Profile management page  | &cross;  | &check;  | Pass |This page is available only to authorized users ||
| User can Delete an accuont form on the Profile management page  |  &cross; | &check;  |Pass  | This page is available only to authorized users |
| User can see the Manage shipping page click on the Manage shipping button from the dashboard  |  &check; | &check;  |Pass  | This page is available only to authorized users |
| User can Update shipping address from on the Manage shipping page  |  &cross; | &check;  |Pass  | This page is available only to authorized users |
| User can select category items from nav-bar on the dropdown menu  |  &cross; | &check;  |Pass  | This page is available only to authorized users |
| User can add items to the busket  |  &cross; | &check;  |Pass  | This page is available only to authorized users |
| User can update items in the busket  |  &cross; | &check;  |Pass  | This page is available only to authorized users |
| User can delete items from the busket  |  &cross; | &check;  |Pass  | This page is available only to authorized users |
| User can procced to chechout  |  &cross; | &check;  |Pass  | This page is available only to authorized users |
| User can pay by PayPal, Debit or Credit Card  |  &cross; | &check;  |Pass  | This page is available only to authorized users |
| Admin can create service, edit and delete from admin site  |  &cross; | &check;  |Pass  | This page is available only for authorized admin |
| Admin can create user, update and delete from admin panel  |  &cross; | &check;  |Pass  | This page is available only for authorized admin |
| Admin can approve or delete user from admin panel  |  &cross; | &check;  |Pass  | This page is available only for authorized admin |
| |

### Testing CRUD functionality:
 - Each of the features were tested multiple times to ensure that numerous new items could be added, and that each items had the ability to be updated, edited and delete by the user that submitted it.
 - If an item is submitted by user, the update/delete buttons appear on the page of Shopping cart.
 - Each of the features were tested multiple times to ensure that numerous new products could be submitted, and that each item had the ability to be updated, edited and delete by the user that submitted it.
 - If a item is submitted by another user, the particular ID item list with update/delete buttons do not appear on the page. This page is available only to authorized users.
<br/>


<hr>

# Credits:

### Code

The structure and the code of the project was based on my knowledge, with support Google search, Youtube, Slack, Stack Overflow and more:
  * Hello Django - I created CRUD functionalities based on previous experience of my projects.
  * From I think  therefore I blog -  I borrowed confirmation messages code and also followed the site deployment steps outlined here. 

Date picker field and minimum date validator learned from [here](https://gist.github.com/stasyao/99376eb0cf0ad3599f9737c421b5210e#part_4).

[Official Django Documentation](https://docs.djangoproject.com/en/4.1/ref/) was researched for code expressions  and code functionalities.
Django [choices fields](https://docs.djangoproject.com/en/4.1/ref/models/fields/).

Stack Overflow was used intensively for research into code functionalities and problem solving. 


### Content

The site home page is taken from internet searches template. I slightly changed the look of the home page and tried to keep the rest of the pages in the same style.


### Media

Images were all open source and free to use from my owen collections.

### Acknowledgment

- Atlantic Technological University for supporting all our group and for  individual support in all circumstances.
- All the tutorial videos (especially the Dr. Shane Wilso's blogs) which helped me to understand how it all comes together.
- The tutor support team at Atlantic Technological University for their support.
- To my friends who participated in testing my application.
- Dr. Shane Wilso, for helping me.
- Class mates for helping me.





