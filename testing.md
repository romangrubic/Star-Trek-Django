## Summary
* [Responsiveness](#responsiveness)
* [Overall](#overall)
    * [Navigation](#navigation)
    * [Carousel](#carousel)
    * [Button "Go to top"](#button-"go-to-top")
    * [Pagination](#pagination)
    * [Footer](#footer)
* [Home](#home-section)
* [News](#news-section)
* [Shop](#shop-section)
* [Games](#games-section)
* [Forum](#forum-section)
* [Cart & Checkout](#cart-and-checkout-section)
* [Account](#account-section)
    * [Registration](#registration)
    * [Sign In](#sign-in)
    * [Profile](#profile)
    * [Messages](#messages)
    * [Orders](#orders)
    * [Log out](#log-out)


#### Back to [Readme.md](https://github.com/romangrubic/Star-Trek-Django)

---

## Responsiveness
This site was was tested on multiple browsers (Google Chrome, Mozzila Firefox and Opera), multiple mobile devices (Samsung Galaxy, Huawei, Sony) and tablet device(Samsung Galaxy Tab) and it shown responsivness and compatibility.
Web-site is responsive for screens from 350px to 2k. Everything is in order and responsive. But, viewing it on a 4k desktop, Background pictures are too small and they cover 2/3 of the width. 

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Viewing on mobile device | Pages rendering properly, no distortion | As Expected | Pass |
| Viewing on tablet device | Pages rendering properly, no distortion | As expected | Pass |
| Viewing on laptop device | All in order, no distortion | As expected | Pass |
| Viewing on desktop device up to 2k | All in order, no distortion | As expected | Pass |
| Viewing on desktop device up to 4k | All in order, no distortion | Background images do not cover all of the background  | Fail |

[Back to top](#summary)

---

## Overall

### Navigation 
| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on Logo button | Opens "Home" page | As Expected | Pass |
| Clicking on `News` link | Opens "News" page | As expected | Pass |
| Hovering on `News` link | Opens dropdown tab with links | As expected | Pass |
| Clicking on `News` dropdown links | Open `News` page with chosen filter | As expected | Pass |
| Clicking on `Shop` link | Opens "Shop" page | As expected | Pass |
| Clicking on `Games` link | Opens "Games" page | As expected | Pass |
| Clicking on `Forum` link | Opens "Forum" page | As expected | Pass |
| Clicking on `Cart` link | Opens "Cart" page | As expected | Pass |
| Hovering on `Account` link | Opens dropdown tab with links | As expected | Pass |
| Clicking on `Account` dropdown links | Opens the chosen page from dropdown | As expected | Pass |

### Carousel 
| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on Previous and Next button | Slides images | As Expected | Pass |
| Clicking on indicators at the bottom | Slides to selected image | As expected | Pass |

### Button "Go to top" 
| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on `Go to top` button | Scrolls up to top of the page | As Expected | Pass |

### Pagination
| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on `<< Previous` button | Open the previous page (if on page 2, opens page 1) | As Expected | Pass |
| Clicking on `Next >>` button | Open the next page (if on page 1, opens page 2) | As Expected | Pass |

### Footer 
| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on `News` link | Opens "News" page | As expected | Pass |
| Clicking on `Shop` link | Opens "Shop" page | As expected | Pass |
| Clicking on `Games` link | Opens "Games" page | As expected | Pass |
| Clicking on `Forum` link | Opens "Forum" page | As expected | Pass |
| Clicking on `Github` icon | Opens "Github" profile in new tab | As expected | Pass |
| Clicking on `LinkedIn` icon | Opens "LinkedIn" profile in new tab | As expected | Pass |
| Clicking on `E-mail` icon | Opens contact modal for user to contact me | As expected | Pass |
| Clicking on `Submit` button without filling e-mail modal form | User is not able to send | As expected | Pass |
| Clicking on `Submit` button after filling e-mail modal form | Changes `Submit` button from red to green and modal closes itself  | As expected | Pass |
| Clicking on My projects `Portfolio` icon | Opens "Portfolio" project in new tab | As Expected | Pass |
| Clicking on My projects `Snoop` icon  | Opens "Snoop" project in new tab | As expected | Pass |
| Clicking on My projects `Weather 360°` icon | Opens "Weather 360°" project in new tab | As Expected | Pass |
| Clicking on My projects `Animals` icon  | Opens "Animals" project in new tab | As expected | Pass |

[Back to top](#summary)

---
## Home section
| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on `Star Trek` landing image | Opens registration page, if user authorized, no action | As Expected | Pass |
| Clicking on `News` card | Opens "News" section | As Expected | Pass |
| Clicking on `Shop` card | Opens "Shop" section | As Expected | Pass |
| Clicking on `Games` card | Opens "Games" section | As Expected | Pass |
| Clicking on `Forum` card | Opens registration page, if user authorized, opens "Forum" section | As Expected | Pass |

[Back to top](#summary)

---
## News section
| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on News image, title and/or button | Opens news in a detailed view | As Expected | Pass |
| Clicking on `Go to Forum` button | Opens Forum post about that news, if user not authorized, opens registration page | As Expected | Pass |
| Clicking on `Back to News` button | Opens "News" page | As Expected | Pass |

[Back to top](#summary)

---
## Shop section
| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on filter button | Show products under that category | As Expected | Pass |
| Hovering over product | Shows white overlay with "Click to view" button | As Expected | Pass |
| Clicking on product | Show product details info on a new page | As Expected | Pass |
| Selecting the number in input and clicking "Add" | Adds the selected quantity of the item to cart and then opens "Shop" page | As Expected | Pass |
| Clicking on `Back to Shop` button | Opens "Shop" page | As Expected | Pass |

[Back to top](#summary)

---
## Games section
| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on image or/and button | Show games details in a new page | As Expected | Pass |
| Clicking on `Link to game` button | Opens games creator page for user to download game | As Expected | Pass |
| Clicking on `Go to Forum` button | Opens Forum post about that game, if user not authorized, opens registration page | As Expected | Pass |
| Clicking on `Back to Games` button | Opens "Games" page | As Expected | Pass |

[Back to top](#summary)

---
## Forum section
| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Typing in search bar and `search` | Search Forum with a post that has the searched input in title and the shows it. If no match, shows 404 Page | As Expected | Pass |
| Clicking on `Start a topic` button | Opens "Create post" modal | As Expected | Pass |
| Clicking on `Share it!` button | Creates a new post with user input and redirect user to that post page. If user input incomplete, shows `Please fill out this field.` | As Expected | Pass |
| Clicking on `Back to Forum` button | Opens "Forum" page | As Expected | Pass |
| Clicking on Forum filters | Opens "Forum" page with selected filters | As Expected | Pass |
| Clicking on post title | Opens post details page | As Expected | Pass |
| Clicking on post creators username and image | Redirects to that user profile info page | As Expected | Pass |
| Clicking on `Edit post` button | Opens "Edit post" page. Only visible to post creator | As Expected | Pass |
| Clicking on `Comment` button  | Adds a comment bellow the post. If comment input is empty, shows `Please fill out this field.` | As Expected | Pass |

[Back to top](#summary)

---
## Cart and checkout section
| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| If no items, clicking on `Shop` button | Shows "Shop" page | As Expected | Pass |
| Changing quantity and clicking on `Amend` button | Changes quantity of product and shows "Cart" page. If quantity changed to zero, removes product from cart | As Expected | Pass |
| Clicking on products image and/or name | Shows that products detail page | As Expected | Pass |
| Clicking on `Checkout` button | Opens "Chekout" page | As Expected | Pass |
| Clicking on `Submit` button without filling the form | Redirects user to required field | As Expected | Pass |
| Clicking on `Submit` button after filling out the form | Checks with Stripe if everything is ok and redirects to "Cart" page | As Expected | Pass |

[Back to top](#summary)

---
## Account section

### Registration
| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on `Register` button | Registers the user and redirects to Index.html. If registration form is incomplete, shows `Please fill out this field.`  | As Expected | Pass |

### Sign in
| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on `Log In` button | Logs the user in and redirects to Index.html. If user info not correct, shows error and asks user to try again | As Expected | Pass |
| Clicking on `Forgot password` | Opens "Forgot password" page | As Expected | Pass |


### Profile
| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on `Edit profile` button | Opens "Edit profile" page | As Expected | Pass |
| Clicking on `Save` button | Saves changes to profile and redirects to "Profile" page | As Expected | Pass |
| Clicking on `Cancel` button | Cancel changes to profile and redirects to "Profile" page | As Expected | Pass |
| Clicking on `Send message` button on "Profile" page | Opens "Message" form modal | As Expected | Pass |
| Clicking on `Send message` button on "Message" form modal | Creates a conversation between request user and the user  | As Expected | Pass |
| Clicking on `Cancel` button on "Message" form modal | Closes "Message" form modal | As Expected | Pass |

### Messages
| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on "Inbox" tab | Shows received messages | As Expected | Pass |
| Clicking on "Outbox" tab | Shows sent messages | As Expected | Pass |
| Clicking on message name | Opens "Profile" page of the selected user | As Expected | Pass |
| Clicking on message title | Opens "Message" page with the conversation history | As Expected | Pass |
| Clicking on senders image and/or name | Opens profile page of the sender | As Expected | Pass |
| Clicking on receivers image and/or name | Opens profile page of the receiver | As Expected | Pass |
| Clicking on `Send reply` button | Adds the reply to the message at the bottom. If reply input is empty, shows `Please fill out this field.` | As Expected | Pass |
| Clicking on `Go to Messages` button | Opens "Messages" page | As Expected | Pass |

### Orders
| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| If no items, clicking on `Shop` button | Shows "Shop" page | As Expected | Pass |
| Clicking on a orders date | Expands accordion with the selected order, items and total price | As Expected | Pass |
| Clicking on products name in order | Shows that products detail page | As Expected | Pass |

### Log out
| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on `Log out` | Log outs the user | As Expected | Pass |

[Back to top](#summary)