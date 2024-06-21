
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100),nullable=False)
    password = db.Column(db.String(200),nullable=False)

    def to_dict(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'email' : self.email
        }

class Population(db.Model):
    __tablename__ = 'Population'

    id = db.Column(db.Integer, primary_key=True)
    premiseid = db.Column(db.String(50), unique=True, nullable=False)
    total_animal = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'premiseid': self.premiseid,
            'total_animal': self.total_animal
        }

class Movement(db.Model):
    __tablename__ = 'Movements'

    id = db.Column(db.Integer, primary_key=True)
    account_company = db.Column(db.String(100), nullable=False)
    new_movementreason = db.Column(db.String(100), nullable=False)
    new_species = db.Column(db.String(50), nullable=False)
    new_originaddress = db.Column(db.String(200), nullable=False)
    new_origincity = db.Column(db.String(100), nullable=False)
    new_originname = db.Column(db.String(100), nullable=False)
    new_originpostalcode = db.Column(db.String(20), nullable=False)
    new_originpremid = db.Column(db.String(50), db.ForeignKey('Population.premiseid'), nullable=False)
    new_originstate = db.Column(db.String(2), nullable=False)
    new_destinationaddress = db.Column(db.String(200), nullable=False)
    new_destinationcity = db.Column(db.String(100), nullable=False)
    new_destinationname = db.Column(db.String(100), nullable=False)
    new_destinationpostalcode = db.Column(db.String(20), nullable=False)
    new_destinationpremid = db.Column(db.String(50), db.ForeignKey('Population.premiseid'), nullable=False)
    new_destinationstate = db.Column(db.String(2), nullable=False)
    origin_Lat = db.Column(db.Float, nullable=False)
    origin_Lon = db.Column(db.Float, nullable=False)
    destination_Lat = db.Column(db.Float, nullable=False)
    destination_Long = db.Column(db.Float, nullable=False)
    new_numitemsmoved = db.Column(db.Integer, nullable=False)
    new_shipmentsstartdate = db.Column(db.String(10), nullable=False)

    population_origin = db.relationship('Population', foreign_keys=[new_originpremid], backref='movements_origin')
    population_destination = db.relationship('Population', foreign_keys=[new_destinationpremid], backref='movements_destination')

    def to_dict(self):
        return {
            'id': self.id,
            'account_company': self.account_company,
            'new_movementreason': self.new_movementreason,
            'new_species': self.new_species,
            'new_originaddress': self.new_originaddress,
            'new_origincity': self.new_origincity,
            'new_originname': self.new_originname,
            'new_originpostalcode': self.new_originpostalcode,
            'new_originpremid': self.new_originpremid,
            'new_originstate': self.new_originstate,
            'new_destinationaddress': self.new_destinationaddress,
            'new_destinationcity': self.new_destinationcity,
            'new_destinationname': self.new_destinationname,
            'new_destinationpostalcode': self.new_destinationpostalcode,
            'new_destinationpremid': self.new_destinationpremid,
            'new_destinationstate': self.new_destinationstate,
            'origin_Lat': self.origin_Lat,
            'origin_Lon': self.origin_Lon,
            'destination_Lat': self.destination_Lat,
            'destination_Long': self.destination_Long,
            'new_numitemsmoved': self.new_numitemsmoved,
            'new_shipmentsstartdate': self.new_shipmentsstartdate
        }

