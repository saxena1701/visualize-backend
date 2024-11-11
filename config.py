from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    #config-uration loaded from .env
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_URI = os.getenv('REDIS_URI')




