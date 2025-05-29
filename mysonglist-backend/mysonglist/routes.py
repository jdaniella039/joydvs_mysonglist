def includeme(config): 
    config.add_route('home', '/')
    config.add_route('register', '/register')
    config.add_route('login', '/login')
    config.add_route('songs', '/songs')
    config.add_route('add_song', '/songs/add')
    config.add_route('delete_song', '/songs/delete/{id}')
