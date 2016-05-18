from flask.ext.restful import Resource
from flask import request, jsonify
from app import app, api, db, auth, users
from sensor import Sensor, SensorSchema

schema = SensorSchema()

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

class Index(Resource):
    decorators = [auth.login_required]
    def get(self):
        return "Hello, %s!" % auth.username()

class TemperatureList(Resource):
    decorators = [auth.login_required]
    def get(self):
        allTemperatures = Sensor.query.all()
        result = schema.dump(allTemperatures, many=True).data
        return result
    def post(self):
        args = request.get_json()
        sensor_read = Sensor(args['temperature'])
        db.session.add(sensor_read)
        return 'Temperature added', 200

class Temperature(Resource):
    decorators = [auth.login_required]
    def get(self, id):
        temperature = Sensor.query.get(id)
        result = schema.dump(temperature).data
        return result


api.add_resource(Index, '/api/v1.0', endpoint='index')
api.add_resource(TemperatureList, '/api/v1.0/temperature', endpoint='temperatures')
api.add_resource(Temperature, '/api/v1.0/temperature/<string:id>', endpoint='temperature')

if __name__ == '__main__':
    app.run()
