from app import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(80), nullable=False)
    min_result = db.Column(db.Integer, nullable=False)
    max_result = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<ID:{} {}'.format(self.id, self.event_name)


db.create_all()
