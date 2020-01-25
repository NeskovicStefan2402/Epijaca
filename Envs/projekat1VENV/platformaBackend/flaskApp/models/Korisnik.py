from flaskApp import db,app

class KorisnikModel(db.Model):
    __tablename__='korisnici'
    id=db.Column(db.Integer,primary_key=True)
    ime=db.Column(db.String(50))
    prezime=db.Column(db.String(50))
    username=db.Column(db.String(50))
    password=db.Column(db.String(50))
    firma=db.Column(db.String(50))
    email=db.Column(db.String(50))
    telefon=db.Column(db.String(50))
    adresa=db.Column(db.String(50))
    
    def __init__(self,ime,prezime,password,username,email,telefon,adresa,firma):
        self.ime=ime
        self.prezime=prezime
        self.password=password
        self.username=username
        self.email=email
        self.telefon=telefon
        self.adresa=adresa
        self.firma=firma

    def json(self):
        return {
            'id':self.id,
            'ime':self.ime,
            'prezime':self.prezime,
            'username':self.username,
            'password':self.password,
            'telefon':self.telefon,
            'firma':self.firma,
            'email':self.email,
            'adresa':self.adresa
            }

    @classmethod
    def find_one(cls,username,password):
        return cls.query.filter_by(username=username,password=password).first()
        
    @classmethod
    def find_one_id(cls,id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_one_Prijava(cls,username,password):
        return cls.query.filter_by(username=username,password=password).first()


    @classmethod
    def find_firma(cls,naziv):
        return cls.query.filter_by(firma=naziv).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        