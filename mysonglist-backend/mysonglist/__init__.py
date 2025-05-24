from pyramid.config import Configurator
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.security import Allow, Authenticated

class RootFactory:
    __acl__ = [
        (Allow, Authenticated, 'view'),
    ]
    def __init__(self, request):
        pass

def main(global_config, **settings):
    config = Configurator(settings=settings, root_factory=RootFactory)

    config.set_authorization_policy(ACLAuthorizationPolicy())
    config.include('pyramid_jwt')
    config.set_jwt_authentication_policy('mysecretkey', auth_type='Bearer')

    config.include('mysonglist.models')   # ⬅️ penting untuk request.dbsession
    config.include('mysonglist.routes')
    config.include('mysonglist.views')

    config.scan()
    return config.make_wsgi_app()
