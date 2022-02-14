# Use_and_return
Back_end progetto Tecnologie Web svolto da Pasquale Sorrentino, Eduardo Autore e Sara Terlizzi.

Per eseguire il progetto eseguire i passaggi:

Spostarsi nella cartella "use_and_return" e creare un virtual environment per Python :

python3 -m venv venv (Mac)

python -m venv venv (Windows)

Una volta attivato il virtual environment, istallare le librerie richieste:

andare su "Add Configuration" in PyCharm

Selezionare "Add New Configuration" e selezionare Flask Server

Dopodichè impostare Target type su Script patch,

selezionare in Target il file app.py.

Eseguire i comandi:

venv\Scripts\activate (Windows)

source venv/bin/activate (Mac)

Installare le librerie con i seguenti comandi:

// pip install -r requirements.txt (non installa tutto)

~~pip install Flask

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

Spostarsi nella cartella "static" (all'interno della cartella "project"), creare una directory di nome 'uploads' e una di nome 'downloads'  

Spostarsi nella cartella Flask e far partire il web-server

flask run --host 0.0.0.0

Cosi il webserver parte in modo tale da essere raggiugibile su tutta la rete locale, per farlo partire solo sul localhost 
flask run


Istruzioni database:
Nella cartella "Database" sono presenti i file per la creazione delle tabelle del database in linguaggio SQL.
Abbiamo utilizzato Mysql:

https://dev.mysql.com/downloads/workbench/
https://dev.mysql.com/downloads/mysql/

Eseguire lo script CREA_DB_NOLEGGIO_OGGETTI.sql per creare tutte le tabelle e per inizializzare le due tuple con i ruoli User e Administrator.
