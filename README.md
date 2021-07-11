<h1 align="center"><a>https://newirishlife.herokuapp.com/</a></h1>

Web-based travel guide for providing correct information for a fresh start on Irish grounds.
Finding work, a place to stay, where to buy good cheap food in Ireland. 
All of this can be difficult in the beginning but with the correct preparation,
advice, and planning this task can be made a lot easier.
New Irish Life is a great starting point.

![Website Main Mockup](https://github.com/tsokac2/newirishlife/blob/main/static/wireframes/W4_Main.jpg)

## Contents
* [User Experience Design (UX)](#UX)
    * [User Story](#User-Story)
    * [Design process](#Design-process)
* [Features](#FEATURES)
    * [Home](#HOME)
    * [Trip](#TRIP)
    * [Work](#WORK)
    * [Life](#LIFE)
    * [Tips](#TIPS)
    * [Sign Up](#SIGN-UP)
    * [Login](#LOGIN)
    * [Profile](#PROFILE)
    * [Add Tip](#ADD-TIP)

* [Technologies used](#TECHNOLOGIES-USED)
* [Testing](#TESTING)
* [Deployment](#DEPLOYMENT)
* [Credits](#Credits)

****

# UX
<h2 align="center">Story</h2>
<h3 align="center">Four years ago, one Croatian landed in Ireland.
There was a lot of info about life in Ireland on the internet, but not essentials information in one place.
</h3>
<h2 align="center">Well, not anymore!</h2>


## Project Goals
This project is my final project for the Code Institute's Full stack development programme. The main goal of this project is to create an e-commerce site using Django framework, which is hosted with AWS as well as implementing a fully functional payment system with Stripe.

## Site Owner Goals
* Provide the users with a professional e-commerce online shop to allow secure purchases.
* Make a profit selling traditional Irish souvenirs.
* Promote Ireland and the Irish way of living.


## User Story
User stories are presented for 3 different User types:
* **First Visitor**
* **Active User**
* **Superuser**


### First Visitor
* As a new Irish resident, I want all **NECESSARY AND IMPORTANT** information for my **[New Irish Life](https://newirishlife.herokuapp.com/)** in one place and available from any device connected to the internet, so I can organize my life in a fun and simple way.
* Visibly accessible **Main Menu** configure for any screen size with quick access to all website sections. 
* In the **Trip** section, I want to have quick access to the most popular online travel brands and quick link options to chose from.
* The **Trip** section will contain custom configurated Google Maps API with some options for bus, train, or tram stations with visible markers in different colors for the fastest navigation.
* I the **Work** section, I want to have quick access to the most popular recruitment websites and quick link options to chose from.
* I the **Life** section, I want to have quick access to the most up-to-date rental website,  most popular Irish mobile network providers, most popular grocery shop brands, and quick link options to chose from.
* In the **Shop** section, I want to have the option to sort and search all displayed products by categories, prices, and keywords including quick links for the different product categories, ability to purchase _without_ a User Login process.
* In the **Shop/checkout** section visible option to create a User Profile and save delivery information.
* I want to have the ability to create my profile for the full **[New Irish Life](https://newirishlife.herokuapp.com/)** user experience (UX).
* In the **Footer** section, I want to have main section links with the Newsletter User form following by Social media links/logo icons.
* I want to stay up-to-date with all fresh information regarding work and lifestyle by subscribing to my email for newsletter services without creating the User Profile account.
* Browsing through the website I want to have access to each URL directly so it feels like a single app website.
* I want to receive a friendly message if I try to access a **URL** that doesn't exist or I don't have access to instead of the default browser **404** messages.


### Active User
* I want to have the ability to register with my _Email Address_ or _User Name_, and _Password_ strength of my choice with error validation notifications for non-valid input.
* I want to receive a link for the _User Email_ confirmation process into my mailbox.
* I want to Login with my _Username or Email_ and _Password_ with an error validation notification for non-valid input.
* I want to have the option _"Remember Me"_ for my login credentials.
* As an **Active User**, I want to have the option to reset my _Login credentials_.
* On my profile page I want to have the following features listed:
    * My Full name
    * My Full name
    * My Username
    * My Email
    * My Profile image
    * My Phone Number
    * Full Address
    * Ability to **Edit** and **Update** all my profile details.
    * List of my orders history, if none a quick link for the **[SHOP](https://newirishlife.herokuapp.com/products/)** section.
    * Orders history card has to contain a _Link/order_ number with full order details, _Order Date_, _Item Quantity + Item Name_, _Total_ amount spent per order. 
    * Ability to **Delete** my profile with a confirmation message.


### Superuser
* As a Superuser access, I want to have the ability to access the admin console.
* As a Superuser I want to have the ability to upload a new product for the **[SHOP](https://newirishlife.herokuapp.com/products/)** section with success confirmation messages. 
* As a Superuser I want to have direct links displayed for _Edit_ and _Delete_ products on the products detail page.
* As a Superuser I want to have the ability to **Delete** existing products with a confirmation message.

### Testing User Stories from User Experience (UX)
* **MAIN MENU** - As a _First Visitor_, I want to easily understand the main menu and links for different website sections:
    * Upon entering the site user can see a clear navigation bar and site logo.
    * Each menu link is self-explanatory and as a _First Visitor_, the user can understand the main purpose of the link section.
    * The main menu is visible in the **Footers** section with a _"mirror image"_ of the top main menu navigation links.

* Definition by **[HOME](https://newirishlife.herokuapp.com/)** section - As a _First Visitor_, I want to easily understand the main purpose of the site and my benefit of the **[New Irish Life](https://newirishlife.herokuapp.com/)**:
    * The main purpose is represented with a short introduction paragraph and a _"HERO"_ image gallery.
    * Website content is pointed with four visual design cards for the top section of the site.
    * Footer is well structured and offers links for the main site section and full operating **Newsletter** form service.
    * Users can share **[New Irish Life](https://newirishlife.herokuapp.com/)** on four social media links presented in the bottom part of the footer.
    * The main navigation menu and footer are replicated through all main sections of the website.

* Definition by **[TRIP](https://newirishlife.herokuapp.com/trip)** section - As a _First Visitor_, I want to easily understand section purpose with a short and fun intro paragraph and slide-show intro gallery:
    * Users can choose the most popular online travel brands to organize in card elements.
    * Each card element contains the main link, the brand website screenshot, the _"Quick links..."_ option, and a brand description.
    * Users can have access to the best Irish public transportation services.
    * Users can navigate through embedded **[Google Maps API](https://newirishlife.herokuapp.com/trip)** with colorful markers representing the most important bus stations, train stations, and tram stations in Dublin, Ireland.

* Definition by **[WORK](https://newirishlife.herokuapp.com/work)** section - As a  _First Visitor_, I want to easily understand how to start a job search process with the best possible preparation for the Irish work market:
    * Users can quickly understand where to start the job search process.
    * Users can understand what kind of **[CV](https://newirishlife.s3.eu-west-1.amazonaws.com/static/downloads/Tomislav+Sokac_CV.pdf)** template is necessary for a successful job search mission.
    * Users can find the best option for online education with the best offers.

* Definition by **[LIFE](https://newirishlife.herokuapp.com/life)** section - As a _First Visitor_, I want to easily find the best online rental marketplaces, the most popular mobile networks provider, and large-chain grocery shops:
    * Users can choose one of the four most popular Irish online rental portals with quick links for share accommodation or buy options.
    * Users can quickly decide for best mobile network providers regarding broadband speed, bill pay offers, TV broadband offers.
    * Users can check the four largest grocery shop chains with previous user reviews, best deals, work offerings.

* Definition by **[LOGIN](https://newirishlife.herokuapp.com/accounts/login/)** section -  I want to easily login with my _email-or-username_ or and _password_ and be redirected to the HOME page with an updated menu with access to the **Profile** page and success login message:
    * If the user is not registered there is a **["Create profile"](https://newirishlife.herokuapp.com/accounts/signup/)** link for the registration process form. 
    * If the user forgot login credentials she/he can reset the password with the **["Forget Password?"](https://newirishlife.herokuapp.com/accounts/password/reset/)** link.
    * If the user enters incorrect credentials, the login form will prompt a login _error_ message.
    * Users have an option to save login credentials with the **"Remember me"** check box.
    * The **[LOGIN](https://newirishlife.herokuapp.com/accounts/login/)** section contains quick _"cards"_ overview of the site and short introduction paragraph and a _"HERO"_ image gallery.

* Definition by **[SIGNUP](https://newirishlife.herokuapp.com/accounts/signup/)** section - I want to easily register with my _email_, _username_, and _password_ with a minimum of 8 characters of my choice and be redirected to the **Confirmation** link page with a message to **![CONFIRM](wireframe link)** my email address:
    * If the user is registered there is a **[LOGIN](https://newirishlife.herokuapp.com/accounts/login/)** link for register users.
    * For a successful registration process user must enter the following:

        | **Registration Form** |
        --- | 
        E-mail address |
        E-mail address confirmation |
        Username |
        Password |
        Password (again) |
   
    * The **[SIGNUP](https://newirishlife.herokuapp.com/accounts/signup/)** section contains quick _"cards"_ overview of the site and short introduction paragraph and a _"HERO"_ image gallery.

* Definition by **[PROFILE](https://newirishlife.herokuapp.com/accounts/login/)**  section - On my **Profile** page I want to have the option to **UPDATE** my profile details, **LOGOUT** from my profile and **DELETE** my profile:
    * User ![Profile Details]( wireframe image ) are listed in the following order:
        * Profile image
        * Full Name (If updated)
        * Username
        * Email 
        * Create profile date
    * User update form contains the following fields:
    * The user has an option to update profile details.

        | **Profile Update Form** |
        --- | 
        Full name |
        Phone number |
        Street address 1 |
        Street address 2 |
        City |
        County |
        Postcode |
        Country |

    * Users can see Orders history details on the right side of the profile page.
    * Order history details contain the following details:
        * Link Order number for full order details
        * Order data
        * Order Items
        * Total amount spent


* Definition by **[SHOP](https://newirishlife.herokuapp.com/products/)** section - As a _First Visitor_, I want to see all listed products that **[New Irish life](https://newirishlife.herokuapp.com)** is offering with corresponding product categories:
    * Users can quickly browse through the **[SHOP](https://newirishlife.herokuapp.com/products/)** section and view products and products categories.
    * Users can select one of five categories from the categories menu and browse only that type of product.
    * Users can sort all products by the following queries with a sort _dropdown menu_.
    * Users can search for a product by using a _search bar_ with the specific _keyword_ of their choice.
    * Users can quickly understand what is product _name_, _price_, _rating_, and _product categories_ from the product detail card.
    * If the user is a **SUPERUSER** then the _superuser_ has the option to ["Add New Product"]( wireframe link).


* Definition by **[PRODUCT DETAIL](https://newirishlife.herokuapp.com/products/4/)** section - As a _First Visitor_, I want to understand quickly what kind of type of product is on the selected **[PRODUCT DETAIL](https://newirishlife.herokuapp.com/products/4/)** page:
    * Users can view 3 product images browsing through image gallery thumbnails.
    * Users can view _product name_, _rating_, _special offer_, _product price_, chose _product quantity_, view product _description_.
    * Users have two options, a **["Keep Shopping"](https://newirishlife.herokuapp.com/products/)** link to browse different products or an **["Add To Bag"](https://newirishlife.herokuapp.com/bag/)** option for the browsed product.
    * If the user is a **SUPERUSER** then the _superuser_ has the option to **"EDIT"** or to **"DELETE"** browsed product.


* Definition by **[BAG](https://newirishlife.herokuapp.com/bag/)** section -  As a _First Visitor_, I want to view my **[BAG](https://newirishlife.herokuapp.com/bag/)** items by clicking on the BAG link in the menu:
    * Users can view items they "Add to Bag" with the following item(s) details:
        * _Item Name_
        * _Item Image_
        * _Item SKU Number_
        * _Item Price_
        * _Item Description_
        * _Quantity_
    * Users have the option to update item Quantity to **"Add"** or **"Deduct"** item quantity from the shopping **[BAG](https://newirishlife.herokuapp.com/bag/)**.
    * Users can easily view the **"Grand Total"** amount of their shipping **[BAG](https://newirishlife.herokuapp.com/bag/)**.
    * Users can easily understand delivery charges according to of amount they are planning to spend.
    * Users can completely remove the item from shopping **[BAG](https://newirishlife.herokuapp.com/bag/)** by pressing red **"X"** in the top right corner of the item details card.
    * Users have the option to **"Keep Shopping"** or to **"Checkout"** requested items from shopping **[BAG](https://newirishlife.herokuapp.com/bag/)**. 


* Definition by **CHECKOUT** section - As a _First Visitor_, I want to **CHECKOUT** securely with my valid credit card:
    * For the successful CHECKOUT process user must enter the following details:

        | **Details** |
        --- | 
        Full name * |
        Email Address * |
        | **Shipping Details** |
        Phone number *  |
        Street address 1 * |
        Street address 2 |
        Town or City * |
        County |
        Postal Code * |
        Country * |

        | **Payment details** |
        --- | 
        Card Number * |
        Expiry Date * |
        CVC Number * |
    
    * Users have the option to **["Adjust Bag"](https://newirishlife.herokuapp.com/bag/)** which will redirect them to their **["BAG"](https://newirishlife.herokuapp.com/bag/)** or **"Complete Order"** if all the details are correct will charge their card for the **Grand Total**  **["BAG"](https://newirishlife.herokuapp.com/bag/)** amount.
    * Users can view **"SUMMARY"** of their requested items with the following details:
        * Total number or ordering items
        * Item Main Image
        * Item Name
        * Item Quantity
        * Item Price
        * Item Details Link
    * If the user is a **"Register"** user then there is a checkbox to **_"Save this delivery information to my profile"_**
    * If the user is not a "Register" user the there are 2 options:
        * **[Create an account](https://newirishlife.herokuapp.com/accounts/signup/)**
        * **[Login](https://newirishlife.herokuapp.com/accounts/login/)**
    
    **_NOTE: This is a school project, hence the products are NOT for "real-world" order purposes. For testing the payment process please use the following test card details:_**

    | **Test Card Details** |
    --- | 
    Card Number:  **4242 4242 4242 4242** |
    Expiry Date: any valid date ex. **02/25** |
    CVC Number: any 3 digits number ex. **555** |


* Definition by **CHECKOUT SUCCESS** section - As a _First Visitor_, I want to see all order details with **_"Checkout success message"_**:
    * If the checkout process was successful user will receive an email Confirmation for Order Number - ![Email example](wireframe link).
    * Users can quickly view orders details on generated order **"CHECKOUT SUCCESS"** page.
    * Users can view the following order details on the **CHECKOUT SUCCESS** page:
        * _Order Number_
        * _Order Date_
        * _Order Details_
        * _Delivery addrress_
        * _Billing Info_
    * Users have a link to go back to the **[SHOP](https://newirishlife.herokuapp.com/products/)** section and continue shopping.


* Definition by **ADD NEW PRODUCT** section -  As a _Superuser_, I want to have the ability to "Add New Product" in a **[SHOP](https://newirishlife.herokuapp.com/products/)** section:
    * Superusers can **"Add New Product"** by entering the following inputs fields:
        * _Product Category_
        * _Product SKU Number_
        * _Product Name_
        * _Product Description_
        * _Product Price_
        * _Product Sales Price_
        * _Product Rating_
        * _Product Image 1_ - Mani image
        * _Product Image 2_
        * _Product Image 3_
    * Superusers will receive form validation errors if inputs fields are not valid.
    * If the **"Add New Product"** process is completed, the superuser will be redirected to the _new dded product_ detail page to review added product detail page.


* Definition by **EDIT PRODUCT** section -   As a _Superuser_, I want to have an ability to **"EDIT"** product that is already listed in a **[SHOP](https://newirishlife.herokuapp.com/products/)** section:
    * Superusers can **"EDIT"** by _updating_ the following inputs fields:
        * _Product Category_
        * _Product SKU Number_
        * _Product Name_
        * _Product Description_
        * _Product Price_
        * _Product Sales Price_
        * _Product Rating_
        * _Product Image 1_ - Mani image
        * _Product Image 2_
        * _Product Image 3_
    * Superusers will receive form validation errors if inputs fields are not valid.
    * If the **"EDIT"** process is completed successfully, the superuser will be redirected to the _edited product_ detail page to review product updates.
    * Superuser has an option to **"DELETE"** product with the **_"Are you sure you want to delete product?_"** confirmation option.

### Design process

**1.** Draft basic UX sections:
* **[HOME](https://newirishlife.herokuapp.com/)**
* **[TRIP](https://newirishlife.herokuapp.com/trip)**
* **[WORK](https://newirishlife.herokuapp.com/work)**
* **[LIFE](https://newirishlife.herokuapp.com/life)**
* **[LOGIN](https://newirishlife.herokuapp.com/accounts/login/)**
* **[SIGNUP](https://newirishlife.herokuapp.com/accounts/signup/)**
* **[PROFILE](https://newirishlife.herokuapp.com/accounts/login/)**
* **[SHOP](https://newirishlife.herokuapp.com/products/)**
* **[PRODUCT DETAIL](https://newirishlife.herokuapp.com/products/4/)**
* **[BAG](https://newirishlife.herokuapp.com/bag/)**

**2.** Brief list of all pop-ups, alert messages, email layouts and their front-end placement.

**3.** List all color pallets - usage - background color, font color, border.

**4.** List all font styles for best UX, regarding user profile details, movie quotes, post titles, and descriptions.

**5.** A list of free images from the free-image web platforms for each project section.

**6.** Draft web-page layout using Adobe Photoshop and Balsamiq for the main layout and Adobe Illustrator for layout components such as Logo, borders, navigation elements.

**7.** List possible Fowtawesome Icon for best UX in picture experiences and a draft of custom icons.

**8.** Plan Python and Django apps implementation into the project.

**9.** List Semantic Mark-up to structure HTML code.

**10.** List CSS folder structure for SASS Pre-processor configuration.

**11.** List of preferable Django packages for website front-end and backend performance.

**12.** Plan Django apps installation and main usage per website section.

**13.** Plan Django Templates structure and static files structure.

**14.** Plan database Django Forms and Models structure for the following website sections:
* **[SIGNUP](https://newirishlife.herokuapp.com/accounts/signup/)**
* **[SHOP](https://newirishlife.herokuapp.com/products/)** section products details
* User **[PROFILE](https://newirishlife.herokuapp.com/accounts/login/)** section
* Shopping **[BAG](https://newirishlife.herokuapp.com/bag/)** Checkout
* **Add New Product** - (Superuser access only)

**15.** Create and configure **[Amazon S3](https://aws.amazon.com/s3/?nc2=h_ql_prod_fs_s3)** bucket for website static files structure and purposes.

**16.** Plan and implement **[Google Maps API](https://developers.google.com/maps/gmp-get-started#quickstart)** for orientation purposes.

**17.** Plan and implement **[Emailjs API](https://dashboard.emailjs.com/sign-in)** service for Newsletter form.

**18.** Take notes for all major development issue, their solutions, challenges, project credits, and SLACK community guidance.

### Wireframes
* **[HOME](https://newirishlife.herokuapp.com/)** section general idea - for Large and Small screens devices - **[View](https://github.com/tsokac2/newirishlife/blob/main/static/wireframes/W4_Home.png)**
* **[TRIP](https://newirishlife.herokuapp.com/trip)**, **[WORK](https://newirishlife.herokuapp.com/work)**, and **[LIFE](https://newirishlife.herokuapp.com/life)** sections general idea - for Large and Small screens devices - **[View](https://github.com/tsokac2/newirishlife/blob/main/static/wireframes/W4_Trip.png)**
* **[TRIP GOOGLE MAPS](https://newirishlife.herokuapp.com/trip)** section general idea - for Large and Small screens devices **[View](https://github.com/tsokac2/newirishlife/blob/main/static/wireframes/W4_Google_Maps.png)**
* **[SIGNUP](https://newirishlife.herokuapp.com/accounts/signup/)** section general idea - for Large and Small screens devices - **[View](https://github.com/tsokac2/newirishlife/blob/main/static/wireframes/W4_Signup.png)**
* **[LOGIN](https://newirishlife.herokuapp.com/accounts/login/)** section general idea - for Large and Small screens devices - **[View](https://github.com/tsokac2/newirishlife/blob/main/static/wireframes/W4_Login.png)**
* **[SHOP](https://newirishlife.herokuapp.com/products/)** section general idea - for Large and Small screens devices - **[View](https://github.com/tsokac2/newirishlife/blob/main/static/wireframes/W4_Shop.png)**
* **[PRODUCT DETAIL](https://newirishlife.herokuapp.com/products/11/)** section general idea - for Large and Small screens devices - **[View](https://github.com/tsokac2/newirishlife/blob/main/static/wireframes/W4_Product_Detail.png)**
* **[BAG](https://newirishlife.herokuapp.com/bag/)** section general idea - for Large and Small screens devices - **[View](https://github.com/tsokac2/newirishlife/blob/main/static/wireframes/W4_Bag.png)**
* **FOOTER** section general idea - for Small devices - **[View](https://github.com/tsokac2/newirishlife/blob/main/static/wireframes/W3_Footer.png)**

****
