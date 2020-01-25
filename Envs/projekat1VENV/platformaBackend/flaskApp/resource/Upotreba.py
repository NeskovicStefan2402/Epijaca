from flaskApp.models.Upotreba import UpotrebaModel
from flaskApp.models.Sastojci import SastojciModel
from flaskApp.models.Proizvod import ProizvodModel

class Upotereba:

    @classmethod
    def poveziSastojkeSaProizvodima(cls,idProizvoda,idSastojka):
        if UpotrebaModel.find_one(idProizvoda,idSastojka):
            return {'Obavestenje':'Upotreba sastojka {0} za proizvod {1} je vec uneta!'}
        else:
            upotreba=UpotrebaModel(idProizvoda,idSastojka)
            try:
                upotreba.add()
            except:
                return {'Greska':'Problem prilikom unosa podataka u bazu!'}
        return {'Poruka':'Unos podataka je uspesno izvrsen!'}
    
    @classmethod
    def uradiFilter(cls,vrednost):
        sastojci=SastojciModel.find_all()
        upotrebe=[]
        for i in sastojci:
            if vrednost.lower() in i.naziv.lower():
                upotrebe.append(UpotrebaModel.find_all(i.id))
        result=[]
        for i in upotrebe:
            result.append(ProizvodModel.find_one_idProizvoda(i.idProizvoda).json())
        
        return result

