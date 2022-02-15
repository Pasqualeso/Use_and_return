# Use_and_return
Back_end Web Technologies project carried out by Pasquale Sorrentino, Eduardo Autore and Sara Terlizzi.

 To run the project follow the steps:

 Navigate to the "use_and_return" folder and create a virtual environment for Python:

 python3 -m venv venv (Mac)

 python -m venv venv (Windows)

 Once the virtual environment has been created, perform the following steps:

 Go to "Add Configuration" in PyCharm

 Select "Add New Configuration" and select Flask Server

 Then set Target type to Script patch,

 Select the "app.py" file in Target.

 Run the commands to activate the virtual environment:

 venv \ Scripts \ activate (Windows)

 source venv / bin / activate (Mac)

 Install the libraries with the following commands:

 // pip install -r requirements.txt (don't install everything)

 pip install Flask

 pip install Flask-Bootstrap

 pip install Flask-Login

 pip install Flask-Mail

 pip install Flask-Migrate

 pip install Flask-Reuploaded

 pip install Flask-SQLAlchemy

 pip install Flask-WTF

 pip install Jinja2

 pip install Js2p

 pip install Mako

 pip install Markdown

 pip install MarkupSafe

 pip install Pillow

 pip install PyMySQL

 pip install SQLAlchemy

 pip install WTForms

 pip install Werkzeug

 pip install alembic

 pip install app

 pip install blinker

 pip install cffi

 pip install click

 pip install colorama

 pip install config

 pip install cryptography

 pip install decorator

 pip install dnspython

 pip install dominate

 pip install email-validator

 pip install greenlet

 pip install idna

 pip install integer

 pip install itsdangerous

 pip install legacy

 pip install numpy

 pip install prettytable

 pip install pycparser

 pip install pyjsparser

 pip install pytz

 pip install pytz-deprecation-shim

 pip install self

 pip install setuptools

 pip install six

 pip install today

 pip install tz

 pip install tzdata

 pip install tzlocal

 pip install visitor

 pip install wcwidth

 pip install wheel

 Move to the "static" folder (inside the "project" folder), create a directory called 'uploads' and one called 'downloads'.  Create a subfolder "images" in "dowloads" and "uploads"

 Move to the Flask folder and start the web server

 flask run --host 0.0.0.0

 Thus the webserver starts in such a way as to be reachable on the whole local network, to start it only on the localhost flask run

 Database instructions: In the "Database" folder there are the files for creating the database tables in SQL language.  We used Mysql:

 https://dev.mysql.com/downloads/workbench/

 https://dev.mysql.com/downloads/mysql/

 Run the CREA_DB_ROLEGGIO_OBGETTI.sql script to create all the tables and to initialize the two tuples with the User and Administrator roles.