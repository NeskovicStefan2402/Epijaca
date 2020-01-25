from flaskApp import db

class SastojciModel(db.Model):
    __tablemodel__='sastojci'
    id=db.Column(db.Integer,primary_key=True)
    naziv=db.Column(db.String(50))
    posno=db.Column(db.Boolean)

    def __init__(self,naziv,posno):
        self.naziv=naziv
        self.posno=posno
    
    def json(self):
        return {
            'id':self.id,
            'naziv':self.naziv,
            'posno':self.posno
        }
    
    @classmethod
    def find_one(cls,naziv):
        return cls.query.filter_by(naziv=naziv).first()
    
    @classmethod
    def find_one_id(cls,id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    