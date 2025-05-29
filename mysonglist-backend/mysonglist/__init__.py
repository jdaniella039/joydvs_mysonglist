from pyramid.config import Configurator
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.security import Allow, Authenticated
from sqlalchemy import engine_from_config
from .models.meta import DBSession, Base
from pyramid_jwt import JWTAuthenticationPolicy

class RootFactory:
    __acl__ = [
        (Allow, Authenticated, 'view'),
    ]
    def __init__(self, request):
        pass

def get_user_id(request):
    return request.authenticated_userid

def main(global_config, **settings):
    config = Configurator(settings=settings, root_factory=RootFactory)

    config.set_authorization_policy(ACLAuthorizationPolicy())
    authn_policy = JWTAuthenticationPolicy('mysecretkey', auth_type='Bearer')
    config.set_authentication_policy(authn_policy)
    config.add_request_method(get_user_id, name='user_id', reify=True)

    engine = engine_from_config(settings, prefix='sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    config.include('mysonglist.models')
    config.include('mysonglist.routes')
    config.include('mysonglist.views')

    config.scan()
    return config.make_wsgi_app()
