from flask import request,jsonify,Blueprint
from models import Population,Movement,db,User
from flask_jwt_extended import JWTManager,jwt_required
import json
routes = Blueprint('routes',__name__)

@routes.route('/api/population_records',methods=['GET','POST'])
@jwt_required()
def get_population_records():
    from main import redis
    
    if request.method == 'GET':

        try:
            cached_response = redis.get('population_records')
            if cached_response:
                return jsonify(json.loads(cached_response))


            population_records = Population.query.all()
            population_records_serialized = json.dumps([population.to_dict() for population in population_records])
            redis.set('population_records', population_records_serialized, ex=300)

            return jsonify(json.loads(population_records_serialized)), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    elif request.method == 'POST':
        try:
            data = request.json
            new_population_record = Population(
                premiseid = data['premiseid'],
                total_animal = data['total_animal']
            )
            
            db.session.add(new_population_record)
            db.session.commit()

            redis.delete('population_records')

            return jsonify({
                'response' : "population record added successfully",
            }), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 500


@routes.route('/api/movement_records',methods=['GET','POST'])
@jwt_required()
def movement_records():
    from main import redis

    if request.method == 'GET':
        try:
            cached_response = redis.get('movement_records')
            if cached_response:
                return jsonify(json.loads(cached_response))
            movement_records = Movement.query.all()
            movement_records_serialized = json.dumps([movement.to_dict() for movement in movement_records])
            redis.set('movement_records', movement_records_serialized,ex=300)
            return jsonify(json.loads((movement_records_serialized))),200
        except:
            return jsonify({"error": str(e)}), 500

        
    
    elif request.method == 'POST':
        try:
            data = request.json
            print(data)

            origin_farm_ID = data['new_originpremid']
            dest_farm_ID=data['new_destinationpremid']

            origin_farm = Population.query.filter(Population.premiseid == origin_farm_ID).first()
            destination_farm = Population.query.filter(Population.premiseid == dest_farm_ID).first()
            animals_moved = int(data['new_numitemsmoved'])
            if(origin_farm.total_animal < animals_moved):
                return jsonify({
                    "message" : "Not enough animals present in the farm!"
                }) , 200
            
            destination_farm.total_animal+=animals_moved
            origin_farm.total_animal-=animals_moved

            new_movement = Movement(
                account_company=data['account_company'],
                new_movementreason=data['new_movementreason'],
                new_species=data['new_species'],
                new_originaddress=data['new_originaddress'],
                new_origincity=data['new_origincity'],
                new_originname=data['new_originname'],
                new_originpostalcode=data['new_originpostalcode'],
                new_originpremid=data['new_originpremid'],
                new_originstate=data['new_originstate'],
                new_destinationaddress=data['new_destinationaddress'],
                new_destinationcity=data['new_destinationcity'],
                new_destinationname=data['new_destinationname'],
                new_destinationpostalcode=data['new_destinationpostalcode'],
                new_destinationpremid=data['new_destinationpremid'],
                new_destinationstate=data['new_destinationstate'],
                origin_Lat=float(data['origin_Lat']),
                origin_Lon=float(data['origin_Lon']),
                destination_Lat=float(data['destination_Lat']),
                destination_Long=float(data['destination_Long']),
                new_numitemsmoved=int(data['new_numitemsmoved']),
                new_shipmentsstartdate=data['new_shipmentsstartdate']
            )
            db.session.add(new_movement)
            db.session.commit()
            redis.delete('movement_records')
            return jsonify({"message": "New movement added successfully!"}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 500


@routes.route('/api/population_record_by_id',methods = ['GET','PUT'])
@jwt_required()
def population_record_by_ID():
    
    if request.method == 'GET':
        try:
            recordID = request.args.get('premiseid')
            population_record = Population.query.filter(Population.premiseid == recordID).first()
            return jsonify(population_record.to_dict()),200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    elif request.method == 'PUT':
        try:
            recordID = request.args.get('premiseid')
            data = request.json

            population_record = Population.query.filter(Population.premiseid == recordID).first()
            for  key,value in data.items():
                setattr(population_record,key,value)

            db.session.commit()
            return jsonify({"message": "Population record updated successfully!"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

@routes.route('/api/movement_record_by_id',methods=['GET','PUT'])
@jwt_required()
def movement_record_by_ID():
    
    if request.method == 'GET':
        try:
            recordID = request.args.get('id')
            movement_record = Movement.query.filter(Movement.id == recordID).first()
            return jsonify(movement_record.to_dict()),200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    elif request.method == 'PUT':
        try:
            recordID = request.args.get('id')
            data = request.json

            movement_record = Movement.query.filter(Movement.id == recordID).first()
            for  key,value in data.items():
                setattr(movement_record,key,value)

            db.session.commit()
            return jsonify({"message": "Movement record updated successfully!"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500
 

