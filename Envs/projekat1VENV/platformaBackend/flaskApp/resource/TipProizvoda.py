from flaskApp.models.TipProizvoda import TipProizvodaModel
from flaskApp.models.Proizvod import ProizvodModel

class TipProizvoda:

    @classmethod
    def dodajTipProizvoda(cls,data):
        if TipProizvodaModel.find_one_naziv(data['naziv']):
            return {'Obavestenje':'Uneseni tip proizvoda vec postoji!'}
        else:
            tip=TipProizvodaModel(data['naziv'])
            tip.add()
        return {'Poruka':'Uspesno je unet tip proizvoda {0}'.format(data['naziv'])}

    @classmethod
    def vratiProizvodePoTipu(cls,id):
        proizvodi=ProizvodModel.find_all()
        result=[]
        for i in proizvodi:
            if i.tip == id:
                result.append(i)

        return result

    @classmethod
    def uradiFilter(cls,vrednost):
        tipovi=TipProizvodaModel.find_all()
        for i in tipovi:
            if i.naziv == vrednost:
                return TipProizvoda.vratiProizvodePoTipu(i.id).json()
        
        return []
