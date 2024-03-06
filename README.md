# James Dunne Coaching - A Communication Coaching Website
<img src="static/images/screen_01.png" ><br>
<hr>

## Overview
This project is designed and developed as a platform for a communications coaching business. User's are able to purchase access to educational videos in single units or sets of videos. They are also able to purchase tokens which are used to book one to one online coaching sessions. All these functionalities are available to any user with an account. <br>
The website was created for private clients to manage their coaching sessions, B2C, but there is no reason that businesses wouldn't also use a client profile, B2B; a single member of an HR department could distribute session tokens to many members of a company through the gifting mechanic. <br>
**James Dunne Coaching - cookbook building website** was developed using Python (Django), HTML, CSS and JavaScript by storing the data in a PostgreSQL database.
<br><br>
The fully deployed project can be accessed at [this link](https://jdcoaching-49c095ee8d82.herokuapp.com/).<br><br>


## Site Features :
- Single Payment system (not subscription), using Stripe. Users can pay by card or using ApplePay or GooglePay.
- Discount code functionality
- Purchasing video tutorial access and session tokens
- Session calendar booking system
- Newsletter sign-up modal
- Confidentiality procedures displayed
- After session review form for testimonials
- Testimonials side scroller
- About the Coach Section
- Contact form for in-person sessions
- A resources section
- Login with email, username or social accounts links, namely Facebook and Google 
- Bookings should be able to push an appointment to Google calendar of client or outlook calendar.
- A video conferencing tool or an emailed video link for GoogleChat/Zoom/Teams. (Potentially offer FaceTime as an alternative option for IPhone users). 
- Its own domain
- Fully accessible with hidden features for users with disabilities, image tags and text on all features for clients with screen readers.
- Gifting functionality
- links to social accounts
- code of conduct page


## Business Plan & Analysis :
- After **discussion with a coach** currently working in the industry it's clear this is a **premium service**, generally expected to be more expensive than psychotherapy sessions for example which have a continuous expectation of repeated sessions, Communications Coaching is more often a sort of finishing schooling, sometimes a single session is all that is required to teach the necessary skill or technique to solve a clients specific challenge. Most commonly a **short set of 5 or 6 sessions** is what clients settle on. They iterate and perfect communication techniques by taking what they have learned in a session back into their lives, trying it out, then returning to the coach with the result for further development, practice and advice. This model means that clients have a much shorter half-life in communication coaching than in other comparable coaching industries. 

- **Video tutorials** are purposefully affordable, designed to encourage sign up to online or in-person coaching sessions. They are an introduction to the coaches voice and style. 
- Some customers will be satisfied with videos, this acts as **passive income** for the coach and filters favourable clients who are familiar and already like coach’s style.
- Video tutorials are 25 minutes each. They are released in **Tutorial Series**. Access to Tutorials and Tutorial Series can be **purchased individually or bundles**.

- €10 for a single video tutorial, €25 a bundle of three or €50 for Tutorial Series of 6 or more videos. This is considered relatively cheap as the clients who usually require this service are already successful in their field and looking to hone their interpersonal skills to a fine point. (Pricing is difficult from the persepective of the coach, too high and you alienate a portion of your client-base, too low and you undervalue yourself. We have to balance self-valuation with accessibility. Openly addressing this low cost in the content can be most confident thing to do. Stating that videos have been made affordable because session are where the majority of progress is made).

- **E-sessions** start at €120 for a single session. This reduces depending on the number of session **tokens** purchased at one time.

- My discussion with a working coach made it clear that there is a large range of pricing based on the client themselves. **Students** looking for interview preparation are given vastly reduced rates compared to **CEOs** of large companies or **civil servants** working in politics for example. In the cash-in-hand analog world this is simple, the coach changes the rate by simply saying a lower or higher number in the moment and agreeing this with the client. When we try to systematize this for the **online business** we need a discreet method for this so that clients paying higher prices do not feel that the price is unfair or inflated. My solution to this is a dynamic system for the Coach User to generate and distribute discount codes.
- **Discount codes** need to work cleanly and effectively so they can be distributed on **social media**, in **newsletters**, in **direct communications**. We can also use the account registration process to filter the users and target which grade of discount is sent to them in emails, or even inside on-site advertisements. 

- A **newsletter with subscription** option needs to open once with a pop-up including offer of discount. Newsletter is distributed with each new set of videos, or major event. I believe a policy of **minimizing spamming** registered clients will encourage retainment of this client-base.

- Online “**E-Session**” slots. Clients can book these appointments and pre-pay by purchasing tokens. The client redeems the tokens by booking a time slot for an appointment. The Coach must keep these appointments and block out unavailability ahead of time to avoid cancellations or clashes. This is achieved with a **calendar booking system**. Similar to the AirBnB booking model.
- The coach will offer first session free after sign-up for a **discovery and assessment** chat. Usually 15 minutes. 
- **Discovery sessions** are a chance to engage with a new client. A method of connecting with a tentative potential client. It's important to acknowledge that some, certainly not all, but some clients are interested because they feel they are lacking in confidence, this trait itself means they may struggle to reach out. Knowing that a proportion of the Coaches target market is skittish is important. These people need to be shown that this is a safe, trustworthy, reliable service, even more than other clients. The first interaction needs to be made easy, the coach approachable and the service is clearly confidential. **Confidentiality is key** to this industry. 

- **Contact form** for In-person sessions. This is a more intimate and ultimately extranious service but it is an extension of the business and needs to be available. 

- Selling tickets to **group sessions** is also a great way to offer an affordable entry for tentative clients. Now it’s likely early on that anyone booking may find themselves in a one-to-one. This can be made clear that it’s a potential on quieter weeks and a bonus for them if they are so lucky to get a private session at a discounted group rate. 

- **About Section** needs to address the history of the coach and blend every story with how that relates to the type of coaching being offered. 

- **Testimonials** (unfortunetly fabricated, currently) are a chance for helpful, honest and precise advertising of the service being provided. We can create a form for these to be recorded electronically after sessions. Asking professional colleagues of the coach for one liner quotes is also effective. 

- **Resources section**; this is where the coach can show their knowledge and keenness to impart confidence and wisdom on the client. Can be a list of book, sites, videos. Must not redirect to other coaches unless agreed with other coach previously and not funneling business away. Good to inform, no point shooting self in the foot. 

- **Pathing**; un-authorised users can browse all content and videos without playing them while not logged in. Only logged in accounts can access the videos they have paid for.
Account page of users shows previous purchases and session bookings. Some taster content needs to be available. 

- **Gifting**; session or session bundles as well as video access can be purchased as a gift. This does not authorise the buyer account but generates a code and email sent to a target email address. This is sent to the recipient email. The recipient can create an account and cash in the gift of videos or sessions which will be debited to their account.

- **Business Services**; it’s good to advertise B2B services but we will keep this to a contact form with a brief About Section describing the business courses. No business will buy online and it distracts/intimidates private clients. 

- Only authorised accounts are able to purchase products. All the coaches **payments are contained** to the single platform. No cash or transfers to negotiate. The calendar organises their schedule and leaves room for moving or rebooking sessions.
- Keeping cash out of the equation feels **more professional** and keeps the coaches interactions **focused on the client**. Also avoids issues with clients forgetting to pay or not bringing cash on the day. Everything is automated and upfront.
- If the coach needs to rebook, there needs to be a process for this. The client account is refunded a session, an email is sent, and they are able to rebook a free slot in the calendar. 

## Rules : <br>
**Clear rules and boundaries** are key for keeping the interactions **smooth and professional** and supporting the client's feeling of trust. 
- Clients can **cancel** up to 24 hours before a session. Session token is **refunded** and they can book again. 
- **Cancellations** within 24 hours from the booked session slot and the token is consumed.
- More than 15 minutes **lateness** will result in cancellation. No reason, no problem, this is a no-blame platform. Valid reason given via email then coach can refund token at own discretion. (Simple tool for this in site will be included). 
- If client buys several session and then doesn’t want the remainder after a session it is fine to **refund** these. No point being stingey if it costed coach no more time. No refund on gifted sessions. 
- Session must be used within 12 months or they will be **cancelled**. This encourages use.

## Aesthetics, Vibe & Feeling :
### Confidence / Clarity / impact 
- Practicing what you preach is important. Messages and processes need to be extra clear and effective.
- There is a tendency towards some pushy salesmanship from some coaches site. This could be a culture thing within subsets of the industry. Driving with negative fear building statements (“you don’t know what you’re missing”, “can you afford not to take this course”). But I really don’t like this and think there is a gentle pragmatic approach that allows the client to come to you willingly or walk off if they feel it’s not right. 
- This positive gentle approach also fosters a more positive community, client retention and recommendations by word of mouth. 
- Aesthetically there needs to be a clear brand image. A logo and continuation in the typography. 
- Classy, legible, soothing tones. I like off-white skin tones with a single bolder brand colour lightly sprinkled in. 
- A three word mantra for a tag line. This defines your brand. They are the words the client says to their friend across the water cooler.
- A Trustworthy, Quality service, Approachable by all.

## CONTENT TYPES :
Content always needs to include a practical tips for the client. What can they do to improve. It's easy to wax lyrical about confidence and communicating when talking to a camera. We are naturally used to aback and forth interaction, this is when we conversationally handover useful tips organically. However defining this as a media policy encourages the coach and content editor to remember that this is not a standard conversation and they need to impart useful advice as if the user had already expressed their problem and requested specific assistance in the area the video is focusing on. <br>
#### example of problem behaviour / description of why people do this / practical solutions 

### Example Video Tutorial Series: 
    - Confidence Vocal Techniques
    - Clarity in Body Language
    - Managing Confrontation 
    - Business Communication 
    - Confident Lifestyle Choices
    - Communicating in Close Relationships
    - Parenting - Communicating with Children
    - Women in Business - Dealing with Challenges
    - Successful Interview Technique
    - Managing People with Clarity
    - Impact Public Speaking
    - Feeling Comfortable in Social Settings
    - First Impressions with Gravity

### Standards: 
- Video quality needs to be high, sound quality needs to be immaculate, setting should be calming and focused on coach. No AI blur effects. Waist to head unless legs are needed for content. Looking at the lense. Should feel natural, like a one to one. 
- These are tasters for clients to feel a little of what coach’s E-session feel like. They should feel satisfied with the content and keen absorbers should want to feel comfortable with wanting to ask more questions, this is what sessions are for. 
- Complex videos should be book ended with an acknowledgment that this is an overview and that watchers who find the content helpful but feel they need more should reach out for their free discovery chat which came included with their account, don’t push bookings or further payments. Clients and coach need to speak and see how coach can help first.
- Always remember this is a human interaction in which we are overcoming the distance caused by the camera.

## Coaching Differentiation:
There are many different types of coaching and often the same coach can offer several forms of coaching based on their skill set. These types of coaching are umbrella terms for groups of skills and techniques as well as types of interactions the coach and client expect to have with each other. <br>
This is another way to separate price brackets. We can either keep the price of a token the same and clients can exchange a token for any type of session booking, the price differentiated with discount codes or there are different types of session tokens as well as discount codes. This seems to me to be a more effective way of handling. Different coaching session types can also have an effect of the booking system, longer or shorter session slots for example. The coach will be able to see on their schedule the type of coaching sessions they have for the day ahead.<br>
Session type examples:
- Communication Coaching
- Confidence Coaching
- Mindset Coaching
- Vocal Coaching
- Interview Coaching
- Corporate Interaction Coaching
- Management Coaching
- Parenting Coaching
- Role Playing Session
- 6-Week Confident Course
The last example is a bundle course. The purchase buys 6 tokens, for one session each week. <br>
The Coach should be able to book slots for clients and manage tokens in user accounts.  

## Social Media Theory:
### Instgram Post Schedule:
- Rotate one of each of these types of posts daily: <br><br>

- Video with useful tip taken while walking
- Board with quote from someone coach admires and a break down of what that means to them in the post notes
- Board advert for coaching session or the site (boiler plate post notes)
- Video snippet from an interview with coach
- Board advice for specific client demographic in need of coaching for communicating
- Board advert for tutorial videos
- Video direct to camera with advice of the week ( this is optional at coaches discretion )
Rinse & Repeat <br>

#### Instagram content details:
- We will always include an extensicve list of keywords hidden within videos and images for search engine optimization to reach the largest number of relevant users connect by the social platforms algorithm.
- A backlog of this content can be made so that posting is a 5 minute activity for the coach each morning or every other morning. 
- Creating an account which is connected to as many organisations and groups as possible to increase reach of content to users who are interested is key to this social media strategy. 


## UX
This site was created respecting the Five Planes Of Website Design:<br>
### Strategy<hr>
**User Stories:** <br>

|   EPIC                                |ID|                                User Story                                                   |
| :-------------------------------------|--|:------------------------------------------------------------------------------------------- |
|**CONTENT AND NAVIGATION**             |  ||
|                                       |1A| As a user, I want to see a nav menu so I can easily navigate through website content|
|                                       |1B| As a user, I want to understand the purpose of the site|
|                                       |1C| As a user, I want the website to have a nice and intuitive design which I recognise|
|**USER REGISTRATION/AUTENTHICATION**   |  ||
|                                       |2A| As a user, I want to be able to register on the website|
|                                       |2B| As a user, I want to be able to authenticate using only email and password|
|                                       |2C| As a user, I want to be able to log out at any time|
|**COOKBOOKS**                          |  ||
|                                       |3A| As a logged-in user, I want to be able to search through existing recipes|
|                                       |3B| As a logged-in user, I want to be able to make my own collection of recipes which I can come back to|
|                                       |3C| As a logged-in user, I want to be able to make my cookbooks Public or Private|
|**SHARING**                            |  ||
|                                       |4A| As a logged-in user, I want to be able to share a recipe with a friend easily|
|                                       |4B| As a logged-in user, I want to be able to share just the ingredients to a friend easily|
|**USER PROFILE**                       |  ||
|                                       |5A| As a logged-in user, I want to view a list of my cookbooks|
|                                       |5B| As a logged-in user, I want to be able to edit my cookbooks|
|                                       |5C| As a logged-in user, I want to be able to add new recipes|
|                                       |5D| As a logged-in user, I want to be able to create my own variations of existing recipes|
|                                       |5E| As a logged-in user, I want to write a short bio about myself on my profile|
|**REVIEWS**                            |  ||
|                                       |6A| As a logged-in user, I want to leave a review on public recipes|
|                                       |6B| As a logged-in user, I want to be able to delete reviews on my own recipes|
|**CONTACT**                            |  ||
|                                       |7A| As a user, I want to see the websites contact details to raise an issue|

**Project Goal:**<br>
Create a website for collecting and sharing recipes which is useful, enjoyable and attractive for the largest range of users.

**Project Objectives:**<br> 
* To create a website with a simple and intuitive User Experience;
* To add content which is relevant and informative;
* To differentiate between user accounts and an admin account for non-code literate business content management;
* To implement fully functional features that will ease logged-in user's experience with the site and help them to integrate it's use into their lifestyle;
* To make the website available and functional on every device.<br><br>

### Scope<hr>
**Simple and intuitive User Experience**<br>
* Ensure the navigation menu is visible and functional at any stage of using the site;
* Ensure every page has a relevant name which fits its content;
* Ensure the users will get visual feedback when navigating through pages;
* Ensure the users will get visual feedback when navigating through recipes collections;
* Create a design which does not confuse users and matches a singluar brand image.

**Relevant content**<br>
* Recipes have clear instrustions, ingredients and descriptions;
* Menu and cookbook navigations blocks are clear and well designed;
* Create a scrollable page which shows all the recipes in the database;
* Create a section beneath each recipe with customer reviews for full transparency.

**Features for upgraded experience**<br>
* Create a favouriting system for prioritizing specific recipes in a cookbook;
* Create a business profile option for professional chefs to sell their cookbooks on the platform;
* Create a search function which includes food genres to allow groupings and style searches;
* Create a link with existing cupboard contents tracking apps so that ingredients needed lists can be generated with an awareness of what is already in the user's kitchen;
* The ability for future users to add whole cookbooks from other users collections.

**Different client and admin Accounts**<br>
* Admin accounts are able to block accounts for abusing the platform;
* Admin accounts can delete database entries which do not meet basic format compliances;
* Client accounts can create their own recipes, manage their own collections and create variant copies of other user recipes. They can also write reviews on any public recipes.

**Responsiveness**<br>
* Create a responsive design for desktop, tablet and mobile devices.<br><br>

### Structure<hr>
The structure of the website is divided into six pages; with content depending on account specifications <br>
-The **Home** page is visible for new and returning users, it includes an about section and buttons to register or login;<br>
-**Register/Login** is a pop-up overlay on top of the Home page;<br>
-**Logout** feature is a modal that helps user exit their current account;<br>
-The **Nav Menu** is the same across all pages however it is simplified before logging in;<br>
-The **Kitchen** page is only visible for the logged-in clients and displays the logged-in users collection of Cookbooks and Dishes along with a brief bio of the user;<br>
-The **Dish Wall** is the main display and acts as the home page for logged in users. It displays a scrollable gallery of Dish-Tiles from the database;<br>
-The **Create** page has two sub-pages, Create-Cookbook and Create-Dish;<br>
-The **Create-Cookbook** page allows users to name their book, rite a brief description and pic a cover;<br>
-The **Create-Dish** page allows users to create a recipe or Dish-Tile to add to the database;<br>
-**Contact Us** contains information visible to any users, even without registering;<br>
-The **Dish Tile** pages contain a recipe and display all it's details and reviews;<br>
_**Manage Features** allow an admin user to edit content generated by standard users.<br>

### Skeleton<hr>
**Wireframes**<br>
The wireframes for mobile and desktop were created with [Balsamiq](https://balsamiq.com/) tool and can be viewed [here](static/images/Wireframes.png)<br>

**Database**<br>
The project uses the PostgreSQL relational database for storing the data.<br>
Two diagrams were made to represent the relation between the tables

## Agile Methodology
This project was developed using the Agile methodology. User stories were central in planning steps taken. User stories were broken down into acceptance criteria and these were checked off using githubs project KanBan board functionality. These can all be seen publicly attached to this repo. Some acceptance criteria were beyond the scope of the educational project and timeline so have not been met. However they were retained to make it clear the greater goal for the project and to give context to what has already been built; compromises have been made where possible so that absolutely no core functionality for this first iteration and base version of the design have been left out.<br> 
<img src="static/images/screen_02.png" >
<br>

## Features
### Existing Features<hr>
#### Create, Read, Update, Delete
Creation of 

<img src="static/images/screen_03.png" >

#### Client Profiles
The users' accounts have been created using the **django allauth** module. This way, information about the current user can be accessed from the template and displayed for the user to access the site. The client profile model contains a bio, a profile picture. These are displayed on the user's profile. The profile can be edited easily and is accessed on the view_clientprofile page along with all the user's other content, such as their bookings, booking tokens, and video sets, for easy access and management.<br>

### Testing
## Manual Testing
Each user experience function was tested thoroughly by manually logging in as a non-admin user and attempting to take the steps to create content, read content, edit content and delete content. This is true for reviews, recipes and cookbooks as well as user profiles. 

The defensive programming has also been tested manually. By finding the url of a particular post, then logging out, and attempting to access this same url. The @login_required decorator on the views for post_details stops unauthorised users from accessing anything other than the index, which only shows a welcome and prompt for registering and the about and contact pages. The @login_required addition to settings allows us to set a specified redirect for any unauthorised attempt to any accepted url and view which uses this decorator. My setting simply returns the attempt to the index. 

<img src="static/images/screen_04.png" >

The admin functionalities, for creating, editing, deleting, authorizing and managing all models in the database has been thoroughly tested in the making of the site. 

All the forms used in the site have been thoroughly tested for non-valid attempts and valid attempts with unusual entries. The slug generator in particular caused some unfortunate bugs when spaces and non-alphanumeric characters were used which had to be handled in the views.py file with several methods to remove any non-alpha characters and spaces as well as adding a distinct number to each newly generated string. This was all thanks to manual testing. 

Image uploads have all been tested.

## Django Testing

All forms and views were tested for validation and unvalid responses.

## Validator Testing 
[JsHint](https://jshint.com/) - used for validating the javascript code<br>Reports [here](static/images/testing_01.png) and [here](static/images/testing_02.png)<br><br>
[PEP8 Validator](https://www.pythonchecker.com/) - used for validating the python code<br>Report example [here](static/images/testing_04.png)<br><br>
[HTML - W3C HTML Validator](https://validator.w3.org/#validate_by_uri+with_options) - used for validating the HTML<br><br>
[CSS - Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_uri) - used for validating the CSS<br>Report [here](static/images/testing_05.png)<br><br>
[W.A.V.E.](https://wave.webaim.org/) - for testing accessibility<br>Report example [here](static/images/testing_03.png)<br><br>
LightHouse - for testing performance<br>Report[here](static/images/testing_06.png)<br>

## Unfixed Bugs

There are no unfixed bugs that I am aware of at this time. My aim was to have everything which is included working smoothly before submission, rather than adding lots of extra features which were not properly tested or unfinished and beyond the requirements of the prokect scope. 

## Responsive Layout and Design
The project design has been adapted to all types of devices using Bootstrap predefined breakpoints and Chrome's DevTools to digitally test the platform across a number of devices. Three specific media queries were added to solve minor layout issues at specific breakpoints.

**Tested devices:**

    - iPhone SE 
    - iPhone XR 
    - iPhone 12 Pro
    - iPhone 14 Pro Max
    - Pixel 7
    - Samsung Galaxy S8+ 
    - Samsung Galaxy S20 Ultra
    - Ipad Mini
    - Ipad Air 
    - Ipad Pro 
    - Surface Pro 7
    - Surface Pro Duo 
    - Galaxy Fold
    - Samsung Galaxy A51/71 
    - Nest Hub
    - Nest Hub Max

## Tools Used

[GitHub](https://github.com/) - used for hosting the source code of the program<br>
[GitPod](https://gitpod.io/workspaces) - Used as an IDE for the remained of the project, fantastic tool<br>
[Visual Studio](https://code.visualstudio.com/) - for holding code snippets while new method were tested<br>
[Heroku](https://dashboard.heroku.com/) - used for deploying the project<br>
[Balsamiq](https://balsamiq.com/wireframes/) - for creating the wireframes<br>
[Favicon.io](https://favicon.io/) - used for generating the website favicon<br>
[Font Awesome](https://fontawesome.com/) - used for the icons<br>
[Bootstrap5](https://getbootstrap.com/) - for adding predifined styled elements and creating responsiveness<br>
[Google Fonts](https://fonts.google.com/) - for typography<br>
[JsHint](https://jshint.com/) - used for validating the javascript code<br>
[PEP8 Validator](http://pep8online.com/) - used for validating the python code<br>
[HTML - W3C HTML Validator](https://validator.w3.org/#validate_by_uri+with_options) - used for validating the HTML<br>
[CSS - Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_uri) - used for validating the CSS<br>
[Chrome Del Tools](https://developer.chrome.com/docs/devtools/) - for debugging the project<br>
[W.A.V.E.](https://wave.webaim.org/) - for testing accessibility<br>
[Cloudinary](https://cloudinary.com/) - for storing static data<br>
[LightHouse] - for testing performance<br>

### Python packages

* asgiref==3.7.2
* cloudinary==1.36.0
* crispy-bootstrap5==0.7
* dj-database-url==0.5.0
* dj3-cloudinary-storage==0.0.6
* Django==4.2.10
* django-allauth==0.57.2
* django-cloudinary-storage==0.3.0
* django-crispy-forms==2.1
* django-formtools==2.5.1
* django-summernote==0.8.20.0
* gunicorn==20.1.0
* oauthlib==3.2.2
* psycopg2==2.9.9
* PyJWT==2.8.0
* python3-openid==3.2.0
* requests-oauthlib==1.3.1
* sqlparse==0.4.4
* urllib3==1.26.18
* whitenoise==5.3.0

## Deployment

### Deploy on Heroku
 1. Create Pipfile 
 
 In the terminal enter the command ` pip3 freeze > requirements.txt`, and a file with all requirements will be created. 
 
 2. Setting up Heroku

    * Go to the Heroku website (https://www.heroku.com/) 
    * Login to Heroku and choose *Create App* 
    * Click *New* and *Create a new app*
    * Choose a name and select your location
    * Go to the *Resources* tab 
    * From the Resources list select *Heroku Postgres*
    * Navigate to the *Deploy* tab
    * Click on *Connect to Github* and search for your repository
    * Navigate to the *Settings* tab
    * Reveal Config Vars and add your Cloudinary, Database URL (from Heroku-Postgres) and Secret key.    

3. Deployment on Heroku

    * Go to the Deploy tab.
    * Choose the main branch for deploying and enable automatic deployment 
    * Select manual deploy for building the App 
    
The live link can be found here - https://jdcoaching-49c095ee8d82.herokuapp.com/

<hr>

## Credits
### Content
* The content of the website is taken from several websites. 
### Media
* All images have been. 
* The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)
### Code
* The method for applying infinite scroll came from [here](https://simpleisbetterthancomplex.com/tutorial/2017/03/13/how-to-create-infinite-scroll-with-django.html)
* The initial approach for the dish wall layout came from [here](https://github.com/sobriquette/pinclone/tree/master)
* The core of the method for using index counters in a For Loop to give the varied sizes came from [here](https://copyprogramming.com/howto/python-index-counter-in-django-template-forloop)
* The lesson on how to shorten long titles and excerpts to "..." [here](https://stackoverflow.com/questions/29925447/how-to-display-at-the-end-of-a-very-long-title-bootstrap)
* Some of the early building blocks of the site and a helpful guide was [here](https://www.freecodecamp.org/news/how-to-create-a-portfolio-website-using-html-css-javascript-and-bootstrap/)
* After issues with the infinite scroll this was very helpful [here](https://refine.dev/blog/what-is-htmx/#installing-htmx)

## Acknowledgements
- Code Institute for the knowledge and all the tutor support.<br><br>
<hr>