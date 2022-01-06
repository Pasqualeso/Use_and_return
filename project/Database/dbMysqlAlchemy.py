from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql
import secretsData
from project import create_app,db

conn = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(secretsData.dbUser, secretsData.dbPass, secretsData.dbHost,secretsData.dbPort, secretsData.dbSchema)
db = create_engine(conn)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=db))

app = create_app('development')
app_context = app.app_context()
app_context.push()
metadata = MetaData(bind=db)
Base = declarative_base()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    Base.metadata.create_all(bind=db)
    return db


