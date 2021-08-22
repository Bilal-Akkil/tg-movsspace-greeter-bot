import os

class Config(object):
    API_KEY = os.environ.get["API_KEY"]
    TMDB_TOKEN = os.environ.get["TMDB_TOKEN", ""]
