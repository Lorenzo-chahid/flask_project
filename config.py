import os

SECRET_KEY = 'H4S6%YI}r,w5#"jya3#<\x0c>gh'

FB_APP_ID = 162644931682205

if os.environ.get('DATABASE_URL') is None:
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
