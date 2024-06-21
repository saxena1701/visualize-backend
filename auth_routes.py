from flask import request,jsonify,Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token,unset_jwt_cookies,jwt_required
from models import db,User
from marshmallow import Schema, fields, validate, ValidationError
auth_routes = Blueprint('auth',__name__)




class RegisterSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1, error="Name is required"))
    email = fields.Email(required=True, error_messages={"required": "Email is required", "invalid": "Invalid email address"})
    password = fields.Str(required=True, validate=validate.Length(min=6, error="Password must be at least 6 characters long"))

class LoginSchema(Schema):
    email = fields.Email(required=True, error_messages={"required": "Email is required", "invalid": "Invalid email address"})
    password = fields.Str(required=True, validate=validate.Length(min=6, error="Password must be at least 6 characters long"))

@auth_routes.route('/auth/register',methods=['POST'])
def register():

    register_schema = RegisterSchema()

    try:
        data = register_schema.load(request.json)
    except ValidationError as err:
        return jsonify({"success": False, "errors": err.messages}), 400

    data = request.json
    email = data['email']
    
    try:
        user_record = User.query.filter(User.email == email).first()
        if(user_record!=None):
            return jsonify({
                "success":False,
                'message' : "User already exist! Please Login"
            }), 409
        
        name = data['name']
        password = data['password']
        password_hash = generate_password_hash(password)
        
        new_user_record = User(
            name = name,
            email = email,
            password = password_hash
        )

        db.session.add(new_user_record)
        db.session.commit()
        return jsonify({"success":True,"message": "User record added successfully!"}), 201, {'Access-Control-Allow-Credentials': 'true'}

    except Exception as e:
        return jsonify({"success":False,"error" : str(e)}),500
    

@auth_routes.route('/auth/login',methods=['POST'])
def login():
    
    login_schema = LoginSchema()

    try:
        data = login_schema.load(request.json)
    except ValidationError as err:
        return jsonify({"success": False, "errors": err.messages}), 400

    data = request.json
    email = data['email']
    
    try:
        user_record = User.query.filter(User.email == email).first()
        password = data['password']
        if(user_record==None or check_password_hash(user_record.password,password)==False):
            return jsonify({
                "success":False,
                'message' : "Invalid Credentials"
            }), 400
        access_token = create_access_token(identity=user_record.email)
        return jsonify({"success":True,"payload": user_record.to_dict(),"token":access_token }), 201

    except Exception as e:
        return jsonify({"success":False,"error" : str(e)}),500


@auth_routes.route('/auth/logout')
@jwt_required()
def logout():
    try:
        response = jsonify({'message': 'Logged out successfully'})
        unset_jwt_cookies(response)
        return jsonify({'message': 'Logged out successfully'}), 200
    except Exception as e:
        return jsonify({"success":False,"error" : str(e)}),500



