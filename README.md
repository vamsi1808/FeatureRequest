# Feature Request App

A web application that allows the user to create "feature requests".A "feature request" is a request for a new feature that will be added onto an existing piece of software.

Table of Contents

- [Technology Stack](#technology-stack)
- [Getting Started](#getting-started)
- [Deployment URL](#deployment-url)
- [API Usage](#api-usage)
- [Project Structure](#project-structure)

# Technology Stack
```
Development OS - Windows

Deployment OS - Ubuntu 16

Server Side Scripting - Python 3.6.4

Framework - Django 2.0

ORM - Django's inbuilt ORM

Database - SQLite

Web technologies - HTML5, CSS3, JS, Jquery, KnockoutJS
```
# Getting Started
To get up and running, simply do the following:
   ```
  $ git clone https://python-test-project.visualstudio.com/_git/testpythong331
  $ cd testpythong331
  
  # Install the requirements
  $ pip install -r requirements.txt
  
  # Perform database mirations
  $ python manage.py makemigrations
  $ python manage.py migrate
  
  $ Create super user
  # python manage.py createsuperuser
  
  $ Running application locally
  # python manage.py runserver
  ```

You can open your browser and type **http://localhost:8000** to see your app running.
Login with the Super User created above.


# Deployment URL

### Alternatively you can use **http://testpythong331.azurewebsites.net/** to check the working application.

# API Usage

#### Login API: **api-token-auth**
```
http POST http://localhost:9001/api-token-auth username=admin password=password1234
HTTP/1.1 200 OK
Allow: POST, OPTIONS
Content-Length: 196
Content-Type: application/json
Date: Mon, 22 Jan 2018 09:56:30 GMT
Server: WSGIServer/0.2 CPython/3.6.4
Vary: Accept
X-Frame-Options: SAMEORIGIN

{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTE2NjE2MTkwLCJlbWFpbCI6ImFkbWluQGV4YW1wbGUuY29tIn0.47PmhWAhv6V5G4z3U2kJ1lyxKZbEwSg7R8ZZbeqd-v8"
}
```
#### Features List: **features/**
```
http GET http://localhost:9001/features/ "Authorization:JWT <Token>"
HTTP/1.1 200 OK
Allow: GET, HEAD, OPTIONS
Content-Length: 1608
Content-Type: application/json
Date: Mon, 22 Jan 2018 10:00:50 GMT
Server: WSGIServer/0.2 CPython/3.6.4
Vary: Accept
X-Frame-Options: SAMEORIGIN

[
    {
        "client_name": "Client",
        "client_priority": 4,
        "create_date": "2018-01-16T22:16:36.105460Z",
        "feature_desc": "feature desc",
        "feature_title": "feature",
        "id": 1,
        "product_area": "Product",
        "target_date": "2018-10-10"
    },
    {
        "client_name": "Client",
        "client_priority": 4,
        "create_date": "2018-01-17T12:55:25.085064Z",
        "feature_desc": "feature desc",
        "feature_title": "feature",
        "id": 2,
        "product_area": "Product",
        "target_date": "2018-10-10"
    }
 ]
```

#### Features Detail: **features/<feature id>/**
```
  GET http://localhost:9001/features/2/ "Authorization:JWT <Token>
HTTP/1.1 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Length: 190
Content-Type: application/json
Date: Mon, 22 Jan 2018 10:03:50 GMT
Server: WSGIServer/0.2 CPython/3.6.4
Vary: Accept
X-Frame-Options: SAMEORIGIN

{
    "client_name": "Client",
    "client_priority": 4,
    "create_date": "2018-01-17T12:55:25.085064Z",
    "feature_desc": "feature desc",
    "feature_title": "feature",
    "id": 2,
    "product_area": "Product",
    "target_date": "2018-10-10"
}

```

#### Add New feature: **features/add**
```
http POST http://localhost:9001/features/add feature_title="New Feature" feature_desc="New feature description" target_date="2018-10-10" client_id=1 product_id=1 priority=1 "Authorization:JWT <Token>"
HTTP/1.1 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Length: 222
Content-Type: application/json
Date: Mon, 22 Jan 2018 10:06:23 GMT
Server: WSGIServer/0.2 CPython/3.6.4
Vary: Accept
X-Frame-Options: SAMEORIGIN

{
    "client_name": "Client A",
    "client_priority": 1,
    "create_date": "2018-01-22T15:02:03.944092Z",
    "feature_desc": "New feature description",
    "feature_title": "New Feature",
    "id": 9,
    "product_area": "Product A",
    "target_date": "2018-10-10"
}
```  

# Project Structure

| Name                               | Description                                                 |
| ---------------------------------- |:-----------------------------------------------------------:|
| **FeatureRequest**/settings.py    | Django settings module containing all the configuration|
| **FeatureRequest**/logger_settings.py    | Logger Settings configuration|
| **FeatureRequest**/urls.py        | Application URL configuration|
| **FeatureRequest/static**/css     | Contains CSS files which are used throughout the application|
| **FeatureRequest/static**/images  | Contains images which are used throughout the application|
| **FeatureRequest/static**/js      | Contains JS files which are used throughout the application|
| **FeatureRequest**/templates      | Contains template (HTML) files for Login screen|
| **FeatureRequest**/requirements.txt      | Contains list of required libraries for installation|
| **FeatureRequest/features**/views.py     | Contains backend logic for feature related APIs|
| **FeatureRequest/features**/models.py    | Contains database models for feature app|
| **FeatureRequest/features**/urls.py      | Contains URl mapping for feature related APIs|
| **FeatureRequest/features**/serializer.py| Contains Serializer class to serialize db data before sending to the user| 
| **FeatureRequest/features/test**/tests.py| Contains unit tests for all the APIs|
| **FeatureRequest/features/static**/css   | Contains CSS files for all feature module related pages|
| **FeatureRequest/features/static**/js    | Contains JS files for all feature module related pages|
| **FeatureRequest/features**/templates   | Contains HTML files for all feature module related pages|