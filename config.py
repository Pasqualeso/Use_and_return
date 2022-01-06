'''
Note per la configurazione in PRODUZIONE
Valorizzare:
FLASK_APP=app.py
FLASK_CONFIG=production
SECRET_KEY=...tbd...
MAIL_USERNAME=
MAIL_PASSWORD=
MAIL_USE_TLS=true
PBG_ADMIN=
'''
import os
from pathlib import Path

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

import secretsData


class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or "supersupersupersecretkey"
    # Mail
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.mailtrap.io')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '2525'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in \
                   ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('95f990732c6465')
    MAIL_PASSWORD = os.environ.get('7388f0c373c6aa')
    # Costanti usati nelle mail registrazione utenti
    PBG_MAIL_SUBJECT_PREFIX = '[UseAndReturn Napoli Group]'
    PBG_MAIL_SENDER = 'Python Napoli Group Admin <useandreturn1@gmail.com>'
    # Definizione email dell'utente ADMIN iniziale
    PBG_ADMIN = os.environ.get('PBG_ADMIN')

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    pass


class DevConfig(Config):

    DEBUG = True
    # Settings per usare https://mailtrap.io/ - Registrati e cambia con i tuoi dati
    MAIL_SERVER = 'smtp.mailtrap.io'
    MAIL_USERNAME = '95f990732c6465'
    MAIL_PASSWORD = '7388f0c373c6aa'
    MAIL_PORT = 2525
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    PBG_ADMIN = "useandreturn1@gmail.com"


'''

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "testdata.sqlite")
    # To test configuration usage in unit test
    TESTING = True
    # disabling CSRF protection in the testing conguration
    WTF_CSRF_ENABLED = False
    # test admin
    EMAIL_ADMIN = "test1@test.it"
'''

config = {
    'development': DevConfig,
    # 'testing': TestConfig,
    'production': ProdConfig,
    'default': DevConfig
}
