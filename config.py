import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI= 'sqlite:///'+os.path.join(basedir, 'logs.sqlite')
clear=False

# SECRET_KEY = '52d3f853c19f8b63c0918c126422aa2d99b1aef33ec63d41dea4fadf19406e54'