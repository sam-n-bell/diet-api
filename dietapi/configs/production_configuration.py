import os
from dotenv import load_dotenv
load_dotenv()

class ProductionConfig(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('PRODUCTION_DATABASE_URI')
