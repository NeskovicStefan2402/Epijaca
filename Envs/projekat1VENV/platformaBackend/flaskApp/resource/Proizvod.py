from flaskApp.models.Proizvod import ProizvodModel
from flaskApp.models.Korisnik import KorisnikModel
from flaskApp.models.TipProizvoda import TipProizvodaModel
from flaskApp.resource.Upotreba import Upotereba
class Proizvod:

    @classmethod
    def vratiProizvodeZaFirmu(cls,naziv):
        id=KorisnikModel.find_firma(naziv).id
        lista=[]
        for i in ProizvodModel.find_all_with_id(id):
            lista.append(i.json())
        return lista

    @classmethod
    def dodajProizvod(cls,data):
        if ProizvodModel.find_one(data['naziv'],data['korisnikID'],data['kolicina']):
            return {'Poruka':'Uneti proizvod vec postoji!'}
        else:
            if TipProizvodaModel.find_one(data['tipID']):
                if KorisnikModel.find_one_id(data['korisnikID']):
                    proizvod=ProizvodModel(data['cena'],data['naziv'],data['organsko'],data['korisnikID'],data['tipID'],data['kolicina'])
                    proizvod.add()
                    for i in data['sastojci']:
                        Upotereba.poveziSastojkeSaProizvodima(ProizvodModel.find_one(data['naziv'],data['korisnikID'],data['kolicina']).id,i['id'])
                    return {'Poruka':'Uspesno je unet proizvod {0}'.format(data['naziv'])}
                else:
                   return {'Greska':'Uneseni proizvod nije od korektnog korisnika!'} 
            else:
                return {'Greska':'Uneseni proizvod nije korektnog tipa!'}
        
    
    @classmethod
    def uradiFilter(cls,vrednost):
        result=[]
        proizvodi=ProizvodModel.find_all()
        for i in proizvodi:
            if vrednost.lower() in i.naziv.lower():
                result.append(i)
        return result    


