from db import db

class MarketModel(db.Model):
    __tablename__='markets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    location = db.Column(db.String(300))

    farm_id = db.Column(db.Integer, db.ForeignKey('farms.id'))
    farm = db.relationship('FarmModel')


    def __init__(self, name, location, farm_id):
        self.name = name
        self.location = location
        self.farm_id = farm_id

    def json(self):
        return {'name': self.name, 'location': self.location}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() #select * from makrets where name = name limit 1

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
