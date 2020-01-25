from flaskApp import db

class TipProizvodaModel(db.Model):
    __tablename__='tipovi'
    id=db.Column(db.Integer,primary_key=True)
    naziv=db.Column(db.String(50))

    def __init__(self,naziv):
        self.naziv=naziv

    def json(self):
        return {'id' : self.id,
                'naziv' : self.naziv}
    
    @classmethod
    def find_one(cls, id):
        return cls.query.filter_by(id=id).first()
        
    @classmethod
    def find_one_naziv(cls,naziv):
        return cls.query.filter_by(naziv=naziv).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def add(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    