import pandas as pd
from models import Population, Movement
from models import db


def load_population_data(file_path):
    data = pd.read_csv(file_path)
    for index, row in data.iterrows():
        new_farm = Population(premiseid=row['premiseid'],total_animal=int(row['total_animal']))
        db.session.add(new_farm)
    db.session.commit()



def load_movement_data(file_path):
    data = pd.read_csv(file_path)
    for index, row in data.iterrows():

        origin_farm_ID = row['new_originpremid']
        dest_farm_ID=row['new_destinationpremid']

        origin_farm = Population.query.filter(Population.premiseid == origin_farm_ID).first()
        destination_farm = Population.query.filter(Population.premiseid == dest_farm_ID).first()

        origin_farm.total_animal -= row['new_numitemsmoved']
        destination_farm.total_animal += row['new_numitemsmoved']



        new_movement = Movement(
            account_company=row['account/company'],
            new_movementreason=row['new_movementreason'],
            new_species=row['new_species'],
            new_originaddress=row['new_originaddress'],
            new_origincity=row['new_origincity'],
            new_originname=row['new_originname'],
            new_originpostalcode=row['new_originpostalcode'],
            new_originpremid=row['new_originpremid'],
            new_originstate=row['new_originstate'],
            new_destinationaddress=row['new_destinationaddress'],
            new_destinationcity=row['new_destinationcity'],
            new_destinationname=row['new_destinationname'],
            new_destinationpostalcode=row['new_destinationpostalcode'],
            new_destinationpremid=row['new_destinationpremid'],
            new_destinationstate=row['new_destinationstate'],
            origin_Lat=row['origin_Lat'],
            origin_Lon=row['origin_Lon'],
            destination_Lat=row['destination_Lat'],
            destination_Long=row['destination_Long'],
            new_numitemsmoved=row['new_numitemsmoved'],
            new_shipmentsstartdate=row['new_shipmentsstartdate']
        )
        db.session.add(new_movement)
    db.session.commit()



