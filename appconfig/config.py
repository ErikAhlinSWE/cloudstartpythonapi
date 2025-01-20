import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    DEBUG = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:hejsan123@mysqlserver1/gamedatabase'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:hejsan123@mysqlserver1/pythoncrud'
    #gamedatabase/games
    #SQLALCHEMY_DATABASE_URI = os.getenv('CONNECTIONSTRING')

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.sqlite')
    DEBUG = True