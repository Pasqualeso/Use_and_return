import os

from flask_login import LoginManager
from flask_migrate import Migrate

from project import db, create_app
from project.utenti.models import Utente

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
Migrate(app, db)

# login_manager = LoginManager()
# current_app_login = login_manager.init_app(app)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Utente=Utente)


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


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
