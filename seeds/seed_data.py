from config.config import db
from database.models.models import Members_Info
import json

def insert_static_data():
    filename = 'seeds/static_data.json'  # Hardcoded file name
    with open(filename, 'r') as file:
        json_data = json.load(file)
    data = []
    for item in json_data:
        member = Members_Info(
            firstname=item['firstname'],
            lastname=item['lastname'],
            email=item['email'],
            contact=item['contact'],
            dob=item['dob'],
            gender=item['gender'],
            height=item['height'],
            weight=item['weight'],
            country=item['country'],
            state=item['state'],
            city=item['city'],
            profile=item['profile'],
            pincode=item['pincode'],
            group=item['group'],
            password_hash=item['password_hash']
        )
        data.append(member)

    db.session.bulk_save_objects(data)
    db.session.commit()


# def insert_static_data():
#     data = [Members_Info(
#     firstname='seed',
#     lastname='seeds',
#     email='seed@gmail.com',
#     contact='7788994455',
#     dob='1899-01-01',
#     gender='male',
#     height=170,
#     weight=99,
#     country='india',
#     state='mp',
#     city='indore',
#     profile='pic.png',
#     pincode='452000',
#     group='classB',
#     password_hash='Vinit@12',
#     ),
#     ]
#     db.session.bulk_save_objects(data)
#     db.session.commit()
