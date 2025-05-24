from pyramid.view import view_config
from pyramid.response import Response
from passlib.hash import bcrypt
from ..models.song_models import User, Song

@view_config(route_name='home', renderer='json')
def home_view(request):
    return {'message': 'MySongList API is running!'}

@view_config(route_name='register', request_method='POST', renderer='json')
def register_view(request):
    data = request.json_body
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return Response(json_body={'error': 'Username and password required'}, status=400)

    session = request.dbsession
    if session.query(User).filter_by(username=username).first():
        return Response(json_body={'error': 'Username already exists'}, status=400)

    hashed_pw = bcrypt.hash(password)
    user = User(username=username, password=hashed_pw)
    session.add(user)
    session.flush()

    return {'message': 'User registered successfully'}

@view_config(route_name='login', request_method='POST', renderer='json')
def login_view(request):
    data = request.json_body
    username = data.get('username')
    password = data.get('password')

    session = request.dbsession
    user = session.query(User).filter_by(username=username).first()

    if not user or not bcrypt.verify(password, user.password):
        return Response(json_body={'error': 'Invalid credentials'}, status=401)

    token = request.create_jwt_token(user.id)
    return {'token': token}

@view_config(route_name='songs', request_method='GET', renderer='json', permission='view')
def get_songs(request):
    session = request.dbsession
    user_id = request.authenticated_userid
    songs = session.query(Song).filter_by(user_id=user_id).all()
    return [{'id': s.id, 'title': s.title, 'artist': s.artist, 'favorite': s.favorite} for s in songs]

@view_config(route_name='songs', request_method='POST', renderer='json', permission='view')
def add_song(request):
    data = request.json_body
    session = request.dbsession
    user_id = request.authenticated_userid
    song = Song(
        title=data['title'],
        artist=data['artist'],
        favorite=data.get('favorite', False),
        user_id=user_id
    )
    session.add(song)
    session.flush()
    return {'message': 'Song added successfully'}

@view_config(route_name='song_detail', request_method='PUT', renderer='json', permission='view')
def update_song(request):
    data = request.json_body
    song_id = int(request.matchdict['id'])
    session = request.dbsession
    song = session.query(Song).filter_by(id=song_id, user_id=request.authenticated_userid).first()
    if not song:
        return Response(json_body={'error': 'Song not found'}, status=404)
    song.title = data.get('title', song.title)
    song.artist = data.get('artist', song.artist)
    song.favorite = data.get('favorite', song.favorite)
    session.flush()
    return {'message': 'Song updated successfully'}

@view_config(route_name='song_detail', request_method='DELETE', renderer='json', permission='view')
def delete_song(request):
    song_id = int(request.matchdict['id'])
    session = request.dbsession
    song = session.query(Song).filter_by(id=song_id, user_id=request.authenticated_userid).first()
    if not song:
        return Response(json_body={'error': 'Song not found'}, status=404)
    session.delete(song)
    session.flush()
    return {'message': 'Song deleted successfully'}
