from flask import jsonify,request,Flask
from flaskApp.resource.Korisnik import Korisnik
from flaskApp.models.Korisnik import KorisnikModel
from flaskApp.resource.Proizvod import Proizvod
from flaskApp.resource.Sastojci import Sastojci
from flaskApp.resource.TipProizvoda import TipProizvoda
from flaskApp.resource.Racun import Racun
from flaskApp import app,db
from flaskApp.other.Obrada import Obrada

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/dodajKorisnika',methods=['POST'])
def funkcija1():
    data=request.json
    return Korisnik.dodajKorisnika(data)

@app.route('/dodajProizvod',methods=['POST'])
def funkcija2():
    data=request.json
    return Proizvod.dodajProizvod(data)

@app.route('/dodajTipProizvoda',methods=['POST'])
def funkcija3():
    data=request.json
    return TipProizvoda.dodajTipProizvoda(data)

@app.route('/dodajSastojak',methods=['POST'])
def funkcija8():
    data=request.json
    return Sastojci.dodajSastojak(data)

@app.route('/dodajPorudzbinu',methods=['POST'])
def funkcija9():
    data=request.json
    return Racun.dodajRacun(data)

@app.route('/vratiSveKorisnike',methods=['GET'])
def funkcij4():
    return jsonify({'Korisnici':Korisnik.vratiSveKorisnike()})

@app.route('/vratiKorisnikaPoFirmi',methods=['GET'])
def funkcija5():
    data=request.json
    return jsonify({'id':Korisnik.vratiFirmu(data['firma'])})

@app.route('/vratiProizvodeZaFirmu',methods=['GET'])
def funkcija6():
    data=request.json
    return jsonify({'Proizvodi':Proizvod.vratiProizvodeZaFirmu(data['firma'])})

@app.route('/prijava',methods=['GET'])
def funkcija7():
    data=request.json
    return Korisnik.prijavaKorisnika(data)

@app.route('/dodajDocx',methods=['POST'])
def funkcija111():
    data=request.json
    korisnik=KorisnikModel.find_one_id(data['idKorisnika'])
    gost=KorisnikModel.find_one_id(data['idGosta'])
    Racun.kreirajPrijemnicu(korisnik,gost,0,data['stavke'])
    return jsonify({'Odgovor':'Radi'})

@app.route('/filter',methods=['GET'])
def funkcija10():
    data=request.json
    return jsonify({'Rezultati pretrage: ': Obrada.obradiFilter(data)})
