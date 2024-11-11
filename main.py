from flask import Flask, request, jsonify
from flask_cors import CORS
from config import Config
from models import db,Population,Movement,User
from data_load import load_movement_data,load_population_data
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from redis import Redis
from routes import routes 
from auth_routes  import auth_routes
import os

redis = Redis.from_url(Config.REDIS_URI,ssl_cert_reqs=None)
# redis = Redis(host='localhost',port=6379,db=0)


redis.ping()
app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

app.register_blueprint(routes)
app.register_blueprint(auth_routes)

db.init_app(app)

jwt=JWTManager(app)


def check_db():
    records = Population.query.first()
    if(records==None):
        return True
    
    return False

# @app.route('/')
# def healthcheck():
#     return "Application up and running"


with app.app_context():
    db.create_all() 
    if(check_db()):
        load_population_data('./population.csv')
        load_movement_data('./movement.csv')    


if __name__ == '__main__':
    app.run(debug=True,use_reloader=True,port=int(os.getenv('FLASK_RUN_PORT', 8000)))
    

