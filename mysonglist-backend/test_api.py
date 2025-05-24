import unittest
from pyramid import testing
from mysonglist.views.api import register_view, login_view, get_songs, add_song, update_song, delete_song

class DummyRequest:
    def __init__(self, json_body=None, matchdict=None, authenticated_userid=None):
        self.json_body = json_body or {}
        self.matchdict = matchdict or {}
        self.authenticated_userid = authenticated_userid
        self.dbsession = DummyDBSession()
        self.create_jwt_token = lambda user_id: "dummy_token"

class DummyDBSession:
    def __init__(self):
        self.data = []

    def query(self, model):
        return DummyQuery()

    def add(self, obj):
        self.data.append(obj)

    def delete(self, obj):
        self.data.remove(obj)

class DummyQuery:
    def filter_by(self, **kwargs):
        return self

    def first(self):
        return None

    def all(self):
        return []

class MySongListTests(unittest.TestCase):
    def test_register(self):
        request = DummyRequest(json_body={'username': 'u', 'password': 'p'})
        response = register_view(request)
        self.assertEqual(response['message'], 'User registered successfully')

    def test_login_invalid(self):
        request = DummyRequest(json_body={'username': 'u', 'password': 'wrong'})
        request.dbsession.query = lambda model: DummyQuery()
        from pyramid.response import Response
        response = login_view(request)
        self.assertIsInstance(response, Response)

    def test_get_songs(self):
        request = DummyRequest(authenticated_userid=1)
        response = get_songs(request)
        self.assertEqual(response, [])

    def test_add_song(self):
        request = DummyRequest(json_body={'title': 'Song', 'artist': 'Artist'}, authenticated_userid=1)
        response = add_song(request)
        self.assertEqual(response['message'], 'Song added successfully')

    def test_update_song_not_found(self):
        request = DummyRequest(json_body={'title': 'New'}, matchdict={'id': '1'}, authenticated_userid=1)
        from pyramid.response import Response
        response = update_song(request)
        self.assertIsInstance(response, Response)

    def test_delete_song_not_found(self):
        request = DummyRequest(matchdict={'id': '1'}, authenticated_userid=1)
        from pyramid.response import Response
        response = delete_song(request)
        self.assertIsInstance(response, Response)

if __name__ == '__main__':
    unittest.main()
