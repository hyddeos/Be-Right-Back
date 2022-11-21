# Be-Right-Back
## A simple and fast way to put up an Away-messages on any site.

## Features
* Add estimated return-time and message on your site.
* Update the time if you get delayed.
* Remove the status whenever you get back.
* Get auto-removed if you should forget to remove it yourself(1h after est-time is default).
* Create User-accounts for the concerned without giving them access to your page.
* Sample file included with description and settings for quick setup on the client-side.

<img src="https://user-images.githubusercontent.com/39992041/203168932-0d5d6481-6cd7-4168-95d1-a55b5f517aa4.png" width="400"/>

## How it works, in a nutshell.
With the help of Django and Rest-framework the user will be able to log-in and put up a Message and Return time.
Your regular page can then request the API at yourURL/api to get the info, a sample file, `getBrbData.js` is included with more information about the implementation.

## Background and idea
When you are alone at a smaller office/company/factory you sometimes have to leave and close for a while even if it's in the regular open hours. 
With this app you can easily display a message with the estimated return time to the customers.
Since you get the data from the API you can display it however you like on your page. 

## Installation
- Python, Django and Rest-framework
- Remove the included `db.sqlite3` file from root (it´s demo db)
- Make migrations
- Create superuser
- Create an Away-status. This is **Important**, the page won´t work unless you have an object in your database.
- Set up your local environments.
- Create your users from django admin panel `yourURL/admin`
- If you want, Open for user registration(read further below)

## Open for user registration
If you want to open up so anyone can register and put up Away-statuses you can remove the comment in `brb/urls.py` and around the **register()** function in `brb/views.py` 

Upcoming improvements and features
Create companies-model to be able to host more pages
Better UI experience in when setting the time, with the mobile in mind
Set opening hours and let the timer take that into account when putting up a Away-status



