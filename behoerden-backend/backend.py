import json

import flask
import requests as requests
from flask import Flask
from waitress import serve

from common.classes import VerkaeuferInfos, BehoerdenInfos, Fahrtuechtig, Versicherung, MeldeDaten

app = Flask(__name__)


def get_fahrtuechtigkeit_from_behoerde(verkaufinfos: VerkaeuferInfos) -> Fahrtuechtig:
    return Fahrtuechtig.JA


def get_vorstrafen_from_Polizei(verkaufinfos: VerkaeuferInfos)-> int:
    return 5


def get_versicherung_from_allianz(verkaufinfos: VerkaeuferInfos)-> Versicherung:
    return Versicherung.JA


def get_behinderungs_grad_from_medizin(verkaufinfos: VerkaeuferInfos) -> float:
    return 50


def get_unfallswahrscheinlichkeit(verkaufinfos: VerkaeuferInfos) -> float:
    return 70


@app.route('/boardinfos',methods=['POST'])
def add_todo():
    requestinfos={key: value for key,value in flask.request.json.items()}
    print('asdf')
    verkaufinfos = VerkaeuferInfos(gewicht= requestinfos['gewicht'], groesse=requestinfos['groesse'], meldedaten= MeldeDaten(**requestinfos['meldedaten']))
    fahrtuechtigkeit = get_fahrtuechtigkeit_from_behoerde(verkaufinfos)
    vorstrafen = get_vorstrafen_from_Polizei(verkaufinfos)
    versicherung = get_versicherung_from_allianz(verkaufinfos)
    behinderungsgrad = get_behinderungs_grad_from_medizin(verkaufinfos)
    unfallswahrscheinlichkeit = get_unfallswahrscheinlichkeit(verkaufinfos)
    ret = BehoerdenInfos(fahrtuechtig= fahrtuechtigkeit, vorstrafen= vorstrafen, versicherung=versicherung, behinderungsgrad=behinderungsgrad, unfallswahrscheinlichkeit=unfallswahrscheinlichkeit)
    return flask.jsonify(ret.model_dump_json())

if __name__ == '__main__':
    print('asdf')
    serve(app,port=8222)
