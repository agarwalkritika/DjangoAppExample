# Django: OTP Based Login and Search

## Overview
Django based application that allows OTP based login functionality.

* OTP is valid for 80 secs by default (configurable)
* OTP can be re-generated after 40 seconds (configurable)
* Logging in once logs you in for 1 hour by default (configurable)

## Installation
#### Requirements
* Python 3.6 (or higher)
* Additional packages : **pyotp** (available through pip)
* Django framework (Tested on Django 2.2)

#### How to install
1. Install the otp dependency : `sudo pip install pyotp`
2. Clone or download the repository to any folder
3. Make Migrations `python manage.py makemigrations`
4. Migrate Database `python manage.py migrate`
5. Put some default data in the database `python manage.py loaddata initial_data.json`

#### Summary of Steps
```
$ sudo pip install pyotp
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py loaddata initial_data.json
```

## Functionality and Navigation
#### Signup
Before doing anything you must create a user for yourself
* Go to the url `<server_root>/auth/signup/` `(Or just <server_root>)`
* Fill in the Signup Form and Click Submit

#### Login
* On the Login page you will see two fields: email and OTP
* If you don't have a OTP yet, just fill the email and click submit. An OTP shall be generated.
* Now enter the OTP along with the email, and you will log in successfully.

#### Dashboard
* The dashboard shall consist of a search filed and a search button, that you can use to search anything in the existing database
* The results can consist fields which are click-able.
* Clicking those links shall take you to a separate details page

#### Logout
* At any page on the website, you can click on Logout and you shall be safely logged out.
