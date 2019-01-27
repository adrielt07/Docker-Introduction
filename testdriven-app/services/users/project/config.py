# services/users/project/config.py

from os import getenv

class BaseConfig:
    '''Base Configuration'''
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATION = False

class DevelopmentConfig(BaseConfig):
    '''Development Configuration'''
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URL', "")

class TestingConfig(BaseConfig):
    '''Testing Configuration'''
    TESTING = True
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_TEST_URL', "")

class ProductionConfig(BaseConfig):
    '''Production Configuration'''
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URL', "")
