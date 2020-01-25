from flaskApp import db
from flaskApp.models.Proizvod import ProizvodModel

class StavkaRacunaModel(db.Model):
    __tablename__='stavke_racuna'
    id=db.Column(db.Integer,primary_key=True)
    cena=db.Column(db.Float)
    kolicina=db.Column(db.Integer)
    idProizvoda=db.Column(db.Integer,db.ForeignKey('proizvodi.id'))
    idRacuna=db.Column(db.Integer,db.ForeignKey('racuni.id'))

    def __init__(self,kolicina,idProizvoda,idRacuna):
        self.kolicina=kolicina
        self.idProizvoda=idProizvoda
        self.cena=self.get_proizvod().cena
        self.idRacuna=idRacuna


    def json(self):
        return {
        'id':self.id,
        'idRacuna':self.idRacuna,
        'naziv':self.get_proizvod().naziv,
        'cena' : self.get_proizvod().cena,
        'kolicina' : self.kolicina
        }

    @classmethod
    def find_stavke_za_racun(cls,idRacuna):
        return cls.query.filter_by(idRacuna=idRacuna)

    def get_proizvod(self):
        return ProizvodModel.find_one_idProizvoda(self.idProizvoda)

    def add(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

