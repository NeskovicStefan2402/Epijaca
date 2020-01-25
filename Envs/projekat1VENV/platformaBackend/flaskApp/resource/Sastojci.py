from flaskApp.models.Sastojci import SastojciModel

class Sastojci:

    @classmethod
    def dodajSastojak(cls,data):
        if SastojciModel.find_one(data['naziv']):
            return {'Obavestenje':'Uneti Sastojak vec postoji u bazi!'}
        else:
            try:
                sastojak=SastojciModel(data['naziv'],data['posno'])
                sastojak.add()
            except:
                return {'Greska':'Nije moguce uneti podatak u bazu'}
        return {'Poruka':'Uspesno je unet sastojak {0} u bazu!'.format(data['naziv'])}
    
    