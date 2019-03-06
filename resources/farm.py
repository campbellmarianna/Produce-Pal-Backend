from flask_restful import Resource
from flask_jwt import JWT, jwt_required

from models.farm import FarmModel

class Farm(Resource):

    # @jwt_required
    def get(self, name):
        farm = FarmModel.find_by_name(name)
        if farm:
            return farm.json()
        return {'message': 'Farm not found'}, 404

    # @jwt_required
    def post(self, name):
        if FarmModel.find_by_name(name):
            return {'message': "A farm with name '{}' already exists.".format(name)},400

        farm = FarmModel(name)
        try:
            farm.save_to_db()
        except:
            return {'message': 'An error occured while creating the farm.'}, 500

        return farm.json(), 201

    # @jwt_required
    def delete(self, name):
        farm = FarmModel.find_by_name(name)
        if farm:
            farm.delete_from_db()

        return {'message': 'Farm deleted'}


class FarmList(Resource):
    # @jwt_required
    def get(self):
        return {'farms': list(map(lambda farm: farm.json(), FarmModel.query.all()))}
