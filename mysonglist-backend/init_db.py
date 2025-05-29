import os
import sys
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from pyramid.paster import get_appsettings, setup_logging

from mysonglist.models.meta import Base
from mysonglist.models import song_models  # pastikan import ini ada!

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python init_db.py <config_uri>")
    
    config_uri = sys.argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)

    engine = engine_from_config(settings, 'sqlalchemy.')
    Base.metadata.create_all(engine)  # ini yang buat tabel!

    print("✅ Tables created in database.")

if __name__ == "__main__":
    main()
