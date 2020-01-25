from flaskApp import db
from flaskApp.models.Upotreba import UpotrebaModel
from flaskApp.models.Sastojci import SastojciModel

class ProizvodModel(db.Model):
    __tablename__='proizvodi'
    id=db.Column(db.Integer,primary_key=True)
    cena=db.Column(db.Float)
    naziv=db.Column(db.String(50))
    kolicina=db.Column(db.String(50))
    organsko=db.Column(db.Boolean)
    korisnikID=db.Column(db.Integer,db.ForeignKey('korisnici.id'))
    tipProizvodaID=db.Column(db.Integer,db.ForeignKey('tipovi.id'))

    
    def __init__(self,cena,naziv,organsko,kid,tpid,kolicina):
        self.cena=cena
        self.naziv=naziv
        self.organsko=organsko
        self.korisnikID=kid
        self.tipProizvodaID=tpid
        self.kolicina=kolicina
        

    def json(self):
        return {
            'id':self.id,
            'cena':self.cena,
            'naziv':self.naziv,
            'organsko':self.organsko,
            'korisnik' : self.korisnikID,
            'Tip proizoda' : self.tipProizvodaID,
            'kolicina':self.kolicina,
            'sastojci':self.getSastojci()
            }
    
    @classmethod
    def find_one(cls,naziv,korisnikID,kolicina):
        return cls.query.filter_by(naziv=naziv,korisnikID=korisnikID,kolicina=kolicina).first()
        
    @classmethod
    def find_all_with_id(cls,id):
        return cls.query.filter_by(korisnikID=id)
    
    @classmethod    
    def find_one_idProizvoda(cls,id):
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
    
    def update(self):
        db.session.update(self)
        db.session.commit()

    def getSastojci(self):
        sastojci=[]
        lista=UpotrebaModel.find_for_one(self.id)
        for i in lista:
            sastojci.append(SastojciModel.find_one_id(i.idSastojka).naziv)
        return sastojci