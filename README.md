# Address Book

System containing CRUD operations to create and list contact information for Organizations and Users that can also be in an organization.

NOTE: You need to be connected to the internet for the Bootstrap CDN to work (beautify the front-end)

NOTE: Gunicorn (see Procfile) does NOT work in Windows (only Unix) BUT works in Heroku with the help of heroku.settings in settings.py

### Installation:
Requires [Python 3](https://www.python.org/downloads/)

Clone directory to your computer and open your terminal in this directory: `cd "directory_name"/addressbook`

Run `pip install -r requirements.txt` to install requirements

## Configuration:
- Dev:
In addressBook.settings.py: Comment last line (heroku.settings) + Debug=true (to see errors)

- Deploy (Heroku): 
In addressBook.settings.py: Uncomment last line (heroku.settings) + Debug=false (for security)



## Usage:
In the project direcotry run the following in order:

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py runserver 8000`

Then open your browser on localhost:8000
