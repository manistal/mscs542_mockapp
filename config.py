import os
import re
import sys
import logging

_this_directory = os.path.dirname(os.path.abspath(__file__))

class Config(object):
    LOG_LEVEL = logging.DEBUG
    LOG_FORMAT = "[%(asctime)s][%(levelname)s][%(filename)s:%(lineno)s - %(funcName)s] %(message)s"
    ROOT_DIR = _this_directory

class DefaultConfig(Config):
    DEBUG = True
    LOG_FILENAME = os.path.join(_this_directory, 'logs/mockapp.log')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mscs542:finalproject@localhost/mscs542_project'

