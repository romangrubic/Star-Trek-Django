## Databases are sorted by App where they are located.
---
## Summary
* [User](#user)
* [Accounts App](#accounts-app)
    * [Profile](#profile)
    * [Message](#message)
    * [Reply](#reply)
* [Checkout App](#checkout-app)
    * [Order](#order)
    * [OrderLineItem](#orderlineitem)
* [Games App](#games-app)
    * [Games](#games)
* [News App](#news-app)
    * [News](#news)
    * [NewsComment](#newscomment)
* [Posts App](#posts-app)
    * [Post](#post)
    * [Comment](#comment)
* [Products App](#products-app)
    * [Product](#product)
    * [Review](#review)


#### Back to [Readme.md](https://github.com/romangrubic/Star-Trek-Django)

---
## User
The User model utilized for this project is the standard one provided by `django.contrib.auth.models`

[Back to top](#summary)

---
## Accounts App
### Profile
| Name | Key | Validation | Field Type |
--- | --- | --- | ---
Profile id| id | primary_key=True | AutoField
User | user | User, on_delete=models.CASCADE | ForeignKey(User)
Image | image | default='default.jpg' | ImageField
Name | name | default='New user', max_length=40 | CharField
Bio | bio | max_length=500 | TextField
Favourite series| favourite_series | max_length=40 | TextField
Favourite character | favourite_character | max_length=40 | DecimalField
Favourite quote | favourite_quote | max_length=500 | ImageField
Cosplay description | cosplay_input | default='New user', max_length=40 | CharField
Cosplay image 1 | cosplay_image1 | default='no-cosplay-img.jpg' | ImageField
Cosplay image 2 | cosplay_image2 | blank=True | ImageField
Cosplay image 3 | cosplay_image3 | blank=True | ImageField

### Message
| Name | Key | Validation | Field Type |
--- | --- | --- | ---
Message id| id | primary_key=True | AutoField
Sender | sender | User, related_name="sender" | ForeignKey(User)
Receiver | receiver | User, related_name="receiver" | ForeignKey(User)
Title | title | max_length=40 | CharField
Message | message | max_length=200 | TextField
Date | created_date | default=timezone.now | DateTimeField

### Reply 
| Name | Key | Validation | Field Type |
--- | --- | --- | ---
Reply id| id | primary_key=True | AutoField
Message | message | Message, related_name="reply" | ForeignKey(Accounts.Message)
Profile | profile | Profile | ForeignKey(Accounts.Profile)
User | user | User | ForeignKey(User)
Reply | reply | max_length=200 | TextField
Date | created_date | default=timezone.now | DateTimeField

[Back to top](#summary)

---
## Checkout App
### Order
| Name | Key | Validation | Field Type |
--- | --- | --- | ---
Order id| id | primary_key=True | AutoField
User | user | User, on_delete=models.CASCADE, related_name="orders" | ForeignKey(User)
Full name | full_name | max_length=50 | CharField
Phone number | phone_number | max_length=20, blank=False | CharField
Country | country | max_length=40, blank=False | CharField
Postcode | postcode | max_length=40, blank=True | CharField
Town or City | town_or_city | max_length=40, blank=False | CharField
Street address 1 | street_address1 | max_length=40, blank=False | CharField
Street address 2 | street_address2 | max_length=40, blank=False | CharField
County | county | max_length=40, blank=False | CharField
Date | date | default=timezone.now | DateField
Total price | total_price | max_digits=100, decimal_places=2, default=0.00 | DecimalField

### OrderLineItem
| Name | Key | Validation | Field Type |
--- | --- | --- | ---
Order Line Item id| id | primary_key=True | AutoField
Order | order | Order, related_name="orderline", null=False | ForeignKey(Checkout.Order)
Product | product | Product, null=False | ForeignKey(Products.Product)
Quantity | quantity | blank=False | IntegerField

[Back to top](#summary)

---
## Games App
### Games
| Name | Key | Validation | Field Type |
--- | --- | --- | ---
Games id| id | primary_key=True | AutoField
Name | name | max_length=254 | CharField
Description | description | / | TextField
Image1 | image1 | blank=False | ImageField
Image2 | image2 | blank=False | ImageField
Image3 | image3 | blank=False | ImageField
Image4 | image4 | blank=False | ImageField
Image5 | image5 | blank=False | ImageField
Game link | game_link | max_length=254 | CharField
Forum post | forum_thread | max_length=254, blank=True | CharField

[Back to top](#summary)

---
## News App
### News
| Name | Key | Validation | Field Type |
--- | --- | --- | ---
News id| id | primary_key=True | AutoField
Author | author | max_length=40 | CharField
Title | title | max_length=200 | CharField
Content | content | blank=False | TextField
Created Date | created_date | auto_now_add=True | DateTimeField
Published Date | published_date | default=timezone.now | DateTimeField
Views | views | default=0 | IntegerField
Tag | tag | max_length=1, choices=NEWS_CHOICES | CharField
Image | image | blank=False | ImageField
Image2 | image2 | blank=True | ImageField
Image3 | image3 | blank=True | ImageField
Forum post | forum_thread | max_length=254, blank=True | CharField

### NewsComment
| Name | Key | Validation | Field Type |
--- | --- | --- | ---
NewsComment id| id | primary_key=True | AutoField
News | news | News, related_name="newscomments" | ForeignKey(News.News)
Profile | profile | Profile | ForeignKey(Accounts.Profile)
User | user | User | ForeignKey(User)
Content | content | max_length=200 | TextField
Date | created_date | default=timezone.now | DateTimeField

[Back to top](#summary)

---
## Posts App
### Post
| Name | Key | Validation | Field Type |
--- | --- | --- | ---
Post id| id | primary_key=True | AutoField
User | user | User | ForeignKey(User)
Profile | profile | Profile | ForeignKey(Accounts.Profile)
Title | title | max_length=200 | CharField
Content | content | blank=False | TextField
Created Date | created_date | auto_now_add=True | DateTimeField
Published Date | published_date | default=timezone.now | DateTimeField
Views | views | default=0 | IntegerField
Tag | tag | max_length=30, blank=True, null=True | CharField

### Comment
| Name | Key | Validation | Field Type |
--- | --- | --- | ---
Comment id| id | primary_key=True | AutoField
Post | post | Post, related_name="comments" | ForeignKey(Posts.Post)
Profile | profile | Profile | ForeignKey(Accounts.Profile)
User | user | User | ForeignKey(User)
Content | content | blank=False | TextField
Date | created_date | default=timezone.now | DateTimeField


[Back to top](#summary)

---
## Products App
### Product
| Name | Key | Validation | Field Type |
--- | --- | --- | ---
Product id| id | primary_key=True | AutoField
Name | name | default='', max_length=254 | CharField
Description | content | blank=False | TextField
Price | price | max_digits=6, decimal_places=2 | DecimalField
Image | image | blank=False | ImageField
Image2 | image2 | blank=True | ImageField
Image3 | image3 | blank=True | ImageField
Views | views | default=0 | IntegerField
Tag | tag | max_length=1, choices=PRODUCT_FILTERS | CharField

### Review
| Name | Key | Validation | Field Type |
--- | --- | --- | ---
Review id| id | primary_key=True | AutoField
Product | product | Product, related_name="productreview" | ForeignKey(Products.Product)
Profile | profile | Profile | ForeignKey(Accounts.Profile)
User | user | User | ForeignKey(User)
Content | content | blank=False | TextField
Date | created_date | default=timezone.now | DateTimeField

[Back to top](#summary)