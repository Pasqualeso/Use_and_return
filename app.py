'''
Per eseguire:

set FLASK_APP=app.py
set FLASK_DEBUG=true
flask run

oppure

python app.py

Per cambiare configurazione da ambiente:
set FLASK_CONFIG=...

'''

import os

from flask_uploads import UploadSet, IMAGES, configure_uploads

from project import create_app, db, images
from flask import render_template
from flask_migrate import Migrate

from project.ruoli.models import Ruolo
from project.utenti.models import Utente
'''
from project.corsi.models import Corso
from project.serate.models import Serata
from project.tags.models import Tag
'''

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
# Create db and migrations
Migrate(app, db)

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
UPLOAD_FOLDER = 'project/static/uploads'
app.config['UPLOADS_DEFAULT_DEST'] = UPLOAD_FOLDER

configure_uploads(app, images)

'''
Per "navigare" in modalità shell
Use shell_context_processor() to add other automatic imports.
'''


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Ruolo=Ruolo, Utente=Utente)


'''
Per i test di unità automatici, il decorator
app.cli.command permette di creare comandi "custom".
Il nome della funzione "decorata", in questo caso "test" sarà il comando per richiamarla.
In questo caso l'implementazione di test() invoca il test runner del package unittest.

Quindi per lanciare i test automatici:

set FLASK_APP=app.py
flask test

'''


@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    # tests è il modulo
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


''' 
Prova"flask pippo" :-)
'''


@app.cli.command()
def pippo():
    print("Bravo! Hai capito come funziona il decorator cli di flask")


if __name__ == "__main__":
    app.run()
