def includeme(config):
    config.add_route('home', '/')
    config.add_route('register', '/register')
    config.add_route('login', '/login')  # ⬅️ HARUS ADA
    config.add_route('songs', '/songs')
    config.add_route('song_detail', '/songs/{id}')
