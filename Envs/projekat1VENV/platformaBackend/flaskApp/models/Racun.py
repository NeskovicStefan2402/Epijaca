from flaskApp import db
from datetime import datetime
from flaskApp.models.StavkaRacuna import StavkaRacunaModel
class RacunModel(db.Model):
    __tablename__='racuni'
    id=db.Column(db.Integer,primary_key=True)
    datumIzdavanja=db.Column(db.DateTime)
    idKorisnika=db.Column(db.Integer,db.ForeignKey('korisnici.id'))
    idGosta=db.Column(db.Integer,db.ForeignKey('korisnici.id')) #TODO potrebno je kreirati klasu gost i referencirati nju 
    
    def __init__(self,idKorisnika,idGosta):
        self.datumIzdavanja=datetime.now()
        self.idKorisnika=idKorisnika
        self.idGosta=idGosta

    def json(self):
        return {
            'id':self.id,
            'Datum izdavanja ' : self.id,
            'Prodavac ' : self.idKorisnika,
            'Kupac ' : self.idGosta,
            'Stavke ':self.get_stavke()
        }
    
    @classmethod
    def find_all_gost(cls,idGosta):
        return cls.query.filter_by(idGosta=idGosta)
    
    def add(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def get_stavke(self):
        stavke=[]
        for i in StavkaRacunaModel.find_stavke_za_racun(self.id):
            stavke.append(i.json())
        return stavke