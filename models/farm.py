
from db import db

class FarmModel(db.Model):
    __tablename__='farms'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    # location = db.Column(db.String(300))

    markets = db.relationship('MarketModel', lazy='dynamic')


    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'markets': [market.json() for market in self.markets.all()]}

    @classmethod
    def find_by_name(cls, name):
        print("testtttttttt")
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
