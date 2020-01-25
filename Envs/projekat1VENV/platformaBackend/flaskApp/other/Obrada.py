from flaskApp.resource.Korisnik import Korisnik
from flaskApp.resource.Proizvod import Proizvod
from flaskApp.resource.Sastojci import Sastojci
from flaskApp.resource.Upotreba import Upotereba
from flaskApp.resource.TipProizvoda import TipProizvoda

class Obrada:
    @classmethod
    def obradiFilter(cls,data):
        try:
            filteri=data['filteri']
            vrednost=data['vrednost']
        except:
            return {'Greska':'Nije prosledjen korektan parametar!'}
        result=[]
        if len(filteri)==0:
            result.append(Korisnik.uradiFilter(vrednost))
            result.append(Korisnik.uradiFilterFirma(vrednost))
            result.append(Proizvod.uradiFilter(vrednost))
            result.append(TipProizvoda.uradiFilter(vrednost))
            result.append(Upotereba.uradiFilter(vrednost))
        else:      
            for i in filteri:
                if i == 'Korisnik':
                    Obrada.provera(Korisnik.uradiFilter(vrednost),result)
                    # result.append(Korisnik.uradiFilter(vrednost))
                elif i == 'Firma':
                    Obrada.provera(Korisnik.uradiFilterFirma(vrednost),result)
                    # result.append(Korisnik.uradiFilterFirma(vrednost))
                elif i == 'Proizvod':
                    Obrada.provera(Proizvod.uradiFilter(vrednost),result)
                    # result.append(Proizvod.uradiFilter(vrednost))
                elif i == 'Tip proizvoda':
                    Obrada.provera(TipProizvoda.uradiFilter(vrednost),result)
                    # result.append(TipProizvoda.uradiFilter(vrednost))
                elif i == 'Sastojci':
                    Obrada.provera(Upotereba.uradiFilter(vrednost),result)
                    # result.append(Upotreba.uradiFilter(vrednost))
                else:
                    return "Nije dobro unet tip za pretragu"
                    
        return result
            
        
    @classmethod
    def provera(cls,podlista,lista):
        for i in podlista:
            if i not in lista:
                lista.append(i)
                