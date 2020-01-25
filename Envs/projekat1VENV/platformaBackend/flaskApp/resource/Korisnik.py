
from flaskApp.models.Korisnik import KorisnikModel

class Korisnik:
    
    @classmethod
    def dodajKorisnika(cls,data):
        if KorisnikModel.find_one(data['username'],data['password']):
            return {'Obavestenje':'Uneti korisnik vec postoji u bazi!'}
        else:
            try:
                korisnik=KorisnikModel(data['ime'],data['prezime'],data['password'],data['username'],data['email'],data['telefon'],data['adresa'],data['firma'])
                korisnik.add()
            except:
                return {'Greska':'Nije moguce uneti korisnika u bazu!'}
            return {'Poruka':'Uspesno je unesen korisnik u bazu'}
    
    @classmethod
    def prijavaKorisnika(cls,data):
        korisnik=KorisnikModel.find_one_Prijava(data['username'],data['password'])
        if korisnik:
            return korisnik.json()
        else:
            return {'Obavestenje':'Uneti podaci ne odgovaraju nijednm korisniku!'}

    @classmethod
    def vratiSveKorisnike(cls):
        lista=[]
        for i in KorisnikModel.find_all():
            lista.append(i.json())
        return lista


    @classmethod
    def vratiFirmu(cls,naziv):
        return KorisnikModel.find_firma(naziv).json()['id']

    @classmethod
    def uradiFilter(cls,vrednost):
        result=[]
        korisnici=Korisnik.vratiSveKorisnike()
        for i in korisnici:
            if vrednost.lower() in (i['ime']+' '+i['prezime']).lower():
                result.append(i)
        return result    

    @classmethod
    def uradiFilterFirma(cls,vrednost):
        result=[]
        korisnici=Korisnik.vratiSveKorisnike()
        for i in korisnici:
            if i['firma'] is not '' and i['firma'] is not None:
                if vrednost.lower() in i['firma'].lower():
                    result.append(i)
        return result    
