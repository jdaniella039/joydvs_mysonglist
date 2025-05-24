from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from .base import Base

Base = declarative_base()
DBSession = sessionmaker()

def includeme(config):
    settings = config.get_settings()
    engine = engine_from_config(settings, prefix='sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config.registry['dbsession_factory'] = DBSession

    def dbsession_request(request):
        dbsession = DBSession()
        request.add_finished_callback(lambda request: dbsession.close())
        return dbsession

    config.add_request_method(dbsession_request, 'dbsession', reify=True)
