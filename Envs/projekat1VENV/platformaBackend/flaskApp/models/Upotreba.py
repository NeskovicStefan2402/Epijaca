from flaskApp import db

class UpotrebaModel(db.Model):
    __tablename__='upotrebe_sastojaka'
    id=db.Column(db.Integer,primary_key=True)
    idProizvoda=db.Column(db.Integer)
    idSastojka=db.Column(db.Integer)
    
    def __init__(self,idProizvoda,idSastojka):
        self.idSastojka=idSastojka
        self.idProizvoda=idProizvoda
    
    def json(self):
        return {
            'id':self.id,
            'idSastojka':self.idSastojka,
            'idProizvoda':self.idProizvoda
        }
    
    @classmethod
    def find_for_one(cls,idProizvoda):
        return cls.query.filter_by(idProizvoda=idProizvoda)

    @classmethod
    def find_one(cls,idProizvoda,idSastojka):
        return cls.query.filter_by(idProizvoda=idProizvoda,idSastojka=idSastojka).first()
    
    @classmethod
    def find_all(cls,idSastojka):
        return cls.query.filter_by(idSastojka=idSastojka)
    
    def add(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    