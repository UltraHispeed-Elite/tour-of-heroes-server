from .in_memory_db import IMDB

db: IMDB = IMDB()

def init_extensions():
    global db
    print("Hello World")