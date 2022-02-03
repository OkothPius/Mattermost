from . import db

class Game(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    viewer_hour = db.Column(db.Integer)
    hours_streamed = db.Column(db.Integer)
    acv_num = db.Column(db.Integer)
    creators = db.Column(db.Integer)
    streams_num = db.Column(db.Integer)

    def save_game(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Game is {self.name}'
