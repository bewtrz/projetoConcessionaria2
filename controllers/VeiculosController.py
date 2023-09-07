import sys
from flask import render_template, redirect, url_for, request, abort

from models.Veiculos import Veiculo, db
from sqlalchemy import select
from sqlalchemy.orm import Session

def index():
    with Session(db) as session:
    # query for ``User`` objects
        veiculos = db.session.query(Veiculo).all()

    return render_template('index.html', veiculos = veiculos)

    
def indexUsados():
    veiculos = db.session.query(Veiculo).all(Novo = False)

    return render_template('index.html', veiculos = veiculos)

def indexNovos():
    veiculos = db.session.query(Veiculo).all()

    return render_template('novos.html', veiculos = veiculos)

def store():
    if(request.method == 'GET'):
        return render_template('cadastro.html')
    if(request.form.getlist):
        
        try:
            print(request.form.get("veiculo"))
            print(request.form.get("cor"))
            print(request.form.get("marca"))
            print(request.form.get("modelo"))
            print(request.form.get("fabricacao"))
            print(request.form.get("estado"))
            print(request.form.get("kmrodados"))
            print(request.form.get("leilao"))
            print(request.form.get("formapagamento"))



            addVeiculo = Veiculo(
            request.form.get("veiculo"),
            request.form.get("cor"),
            request.form.get("marca"),
            request.form.get("modelo"),
            request.form.get("fabricacao"),
            request.form.get("estado"),
            request.form.get("kmrodados"),
            request.form.get("leilao"),
            request.form.get("formapagamento"))
            print(addVeiculo.serialize)
            db.session.add(addVeiculo)
          
        except:
            print("Exception")
            db.session.rollback()
            raise
        else:
            db.session.commit()
            return index()
    return render_template('cadastro.html')


def show(veiculoId):
    veiculos = db.session.query(Veiculo).first(id = veiculoId)

    return render_template('index.html', veiculos = veiculos)

def update(userId):
    ...

def delete(userId):
    ...