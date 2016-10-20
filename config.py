import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  UPLOAD_FOLDER = '/tmp/web_file'
  ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']
  SECRET_KEY='35455450a60b0ed766efb716b1aea023'
  USERNAME='admin'
  PASSWORD='default'
  HOST='0.0.0.0'
  PORT=8010

class DevConfig(Config):
  ENV='Development'
  db_uri = 'sqlite:///' + os.path.join(basedir, 'cutaway.db')
  SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
