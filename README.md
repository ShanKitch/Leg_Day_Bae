# Leg_Day_Bae
Leg Day Bae is an application that allows users who workout from home to connect with other users who workout from home as virtual gym buddies.

## Dependencies
```
pip install django==2.2
pip install bcrypt
pip install django-debug-toolbar
pip install Pillow
```
## Features
- User Creation/Authentication 
- Profile Creation with ability to add exercise preferences, location, age , sex and upload a profile picture
- Main page with all users displayed. Search feature to allow users to search based on exercise type, frequency, time of day, location, age and sex.
- User to User messaging system (Validated)
- User Forum (Validated)
- Ability to update user profile.





## Install Instructions

1. Clone the repository
```
git clone https://github.com/ShanKitch/Leg_Day_Bae
```
2. cd into the Leg_Day_Bae folder
```
cd Leg_Day_Bae
```
3.Create a new virtual environment
 ```
python -m venv venv
 ```
4.Run Virtual Evironment
 ```
call venv/scripts/activate 
 ```
5.Make migrations & migrate
```
python manage.py makemigrations
python manage.py migrate
```
6.Runserver
```
python manage.py runserver
```

