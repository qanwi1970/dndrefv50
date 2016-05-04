from app import db


class CharacterClass(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), index=True, unique=True)
    hit_die = db.Column(db.String(64))
    levels = db.relationship('ClassLevel', backref='character_class', lazy='dynamic')

    def __repr__(self):
        return '<CharacterClass %r>' % self.nickname


class ClassLevel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.Integer)
    prof_bonus = db.Column(db.String(10))
    character_class_id = db.Column(db.Integer, db.ForeignKey('character_class.id'))

    def __repr__(self):
        return '<ClassLevel %r>' % self.level
