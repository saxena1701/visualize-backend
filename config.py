class Config:
    # SQLALCHEMY_DATABASE_URI = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}/{os.getenv('POSTGRES_DB')}"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres_user:puzog6jgkvY8LW3LpK9TX1GfX6Fyf14r@dpg-cpqov7o8fa8c739kfbkg-a.oregon-postgres.render.com/animal_movement_wv6q"
    # SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5431/animal-movement"
    JWT_SECRET_KEY = 'secret_key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False



