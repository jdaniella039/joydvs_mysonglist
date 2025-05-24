from sqlalchemy import create_engine
from mysonglist.models.song_models import Base

engine = create_engine('sqlite:///mysonglist.db')
Base.metadata.create_all(engine)

print("✅ Database tables created.")
