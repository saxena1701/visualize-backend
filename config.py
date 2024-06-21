class Config:
    # SQLALCHEMY_DATABASE_URI = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}/{os.getenv('POSTGRES_DB')}"
    SQLALCHEMY_DATABASE_URI = f"{os.getenv('SQLALCHEMY_DATABASE_URI')}"
    # SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5431/animal-movement"
    JWT_SECRET_KEY = 'secret_key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False



