class Config:
    # SQLALCHEMY_DATABASE_URI = "postgresql://postgres_user:sFasFjnh6RIU0mErCT5BJgT06FxgZJfr@dpg-cqgmc7pu0jms73dpdhu0-a.oregon-postgres.render.com/animal_movement_4vxh"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5431/animal-movement"
    JWT_SECRET_KEY = 'secret_key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_URI = "rediss://red-cqprcr2j1k6c73dvhieg:khtIt9WG23UkRWcZvSHlMIAYklJF25Wu@oregon-redis.render.com:6379"
  



