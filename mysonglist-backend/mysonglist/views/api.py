import logging
log = logging.getLogger(__name__)

from pyramid.view import view_config
from pyramid.response import Response
from ..models.song_models import User, Song
import jwt, datetime
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")
SECRET_KEY = 'mysecretkey'

@view_config(route_name='home', renderer='json')
def home_view(request):
    return {'message': 'MySongList API is running!'}


@view_config(route_name='register', request_method='POST', renderer='json')
def register_view(request):
    try:
        data = request.json_body
        username = data.get('username')
        password = data.get('password')
        log.info(f"Register request: username={username}")
    except Exception as e:
        log.exception("Invalid JSON in register")
        return Response(json_body={'error': f'Invalid JSON format: {str(e)}'}, status=400)

    if not username or not password:
        log.warning("Register failed: missing username or password")
        return Response(json_body={'error': 'Username and password required'}, status=400)

    session = request.dbsession
    if session.query(User).filter_by(username=username).first():
        log.warning(f"Register failed: username '{username}' already exists")
        return Response(json_body={'error': 'Username already exists'}, status=400)

    try:
        hashed_pw = pwd_context.hash(password)
        user = User(username=username, password=hashed_pw)
        session.add(user)
        request.tm.commit()  # ✅ WAJIB agar data tersimpan
        log.info(f"User registered: {username}")
        return {'message': 'User registered successfully'}
    except Exception as e:
        log.exception("Unexpected error during registration")
        return Response(json_body={'error': 'Internal server error'}, status=500)


@view_config(route_name='login', request_method='POST', renderer='json')
def login_view(request):
    try:
        data = request.json_body
        username = data.get('username')
        password = data.get('password')
        log.info(f"Login request: username={username}")
    except Exception as e:
        log.exception("Invalid JSON in login")
        return Response(json_body={'error': f'Invalid JSON format: {str(e)}'}, status=400)

    session = request.dbsession
    users = session.query(User).all()
    log.debug(f"[DEBUG] All users in DB: {[u.username for u in users]}")  # 👈 Debug tambahan

    user = session.query(User).filter_by(username=username).first()

    if not user:
        log.warning("Login failed: User not found")
        return Response(json_body={'error': 'Invalid credentials'}, status=401)

    try:
        if not pwd_context.verify(password, user.password):
            log.warning("Login failed: Password incorrect")
            return Response(json_body={'error': 'Invalid credentials'}, status=401)
    except Exception as e:
        log.exception("Password hash error")
        return Response(json_body={'error': 'Internal server error'}, status=500)

    try:
        payload = {
            'sub': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        if isinstance(token, bytes):
            token = token.decode('utf-8')

        log.info(f"User logged in: {username}")
        return {'token': token, 'user_id': user.id}
    except Exception as e:
        log.exception("Unexpected error during token generation")
        return Response(json_body={'error': 'Internal server error'}, status=500)


@view_config(route_name='songs', request_method='GET', renderer='json', permission='view')
def list_songs_view(request):
    user_id = request.authenticated_userid
    session = request.dbsession
    songs = session.query(Song).filter_by(user_id=user_id).all()
    log.info(f"Listing songs for user_id={user_id}")
    return [{'id': s.id, 'title': s.title, 'artist': s.artist} for s in songs]


@view_config(route_name='add_song', request_method='POST', renderer='json', permission='view')
def add_song_view(request):
    try:
        data = request.json_body
        title = data.get('title')
        artist = data.get('artist')
    except Exception as e:
        log.exception("Invalid JSON in add_song")
        return Response(json_body={'error': f'Invalid JSON format: {str(e)}'}, status=400)

    if not title:
        log.warning("Add song failed: Title is missing")
        return Response(json_body={'error': 'Title is required'}, status=400)

    user_id = request.authenticated_userid
    session = request.dbsession
    song = Song(title=title, artist=artist, user_id=user_id)
    session.add(song)
    request.tm.commit()  # ⬅️ Tambahkan commit
    log.info(f"Song added: '{title}' by {artist} (user_id={user_id})")
    return {'message': 'Song added successfully'}


@view_config(route_name='delete_song', request_method='DELETE', renderer='json', permission='view')
def delete_song_view(request):
    song_id = request.matchdict.get('id')
    user_id = request.authenticated_userid
    session = request.dbsession

    song = session.query(Song).filter_by(id=song_id, user_id=user_id).first()
    if not song:
        log.warning(f"Delete failed: song_id={song_id} not found for user_id={user_id}")
        return Response(json_body={'error': 'Song not found'}, status=404)

    session.delete(song)
    request.tm.commit()  # ⬅️ Tambahkan commit
    log.info(f"Song deleted: id={song_id} (user_id={user_id})")
    return {'message': 'Song deleted'}
