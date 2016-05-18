from datetime import datetime
from app import db, ma


class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float())
    date = db.Column(db.DateTime)


    def __init__(self, temperature, date=None):
        self.temperature = temperature
        if date is None:
            date = datetime.utcnow()
        self.date = date


class SensorSchema(ma.ModelSchema):
    class Meta:
        model = Sensor
