import json

import flask
import requests as requests
from flask import Flask
from waitress import serve

from common.classes import VerkaeuferInfos, BehoerdenInfos, Fahrtuechtig, Versicherung, MeldeDaten, AlleInfos, \
    class_to_parameter
from konfigurator import read_in_data, k_nearest_neighbor

app = Flask(__name__)


def get_fahrtuechtigkeit_from_behoerde(verkaufinfos: VerkaeuferInfos) -> Fahrtuechtig:
    if verkaufinfos.meldedaten.id=="Ned":
        return Fahrtuechtig.NEIN
    elif verkaufinfos.meldedaten.id=='Christian':
        return Fahrtuechtig.EINGESCHRÄNKT
    else:
        return Fahrtuechtig.JA


def get_vorstrafen_from_Polizei(verkaufinfos: VerkaeuferInfos)-> int:
    if verkaufinfos.meldedaten.id == 'Kohlhase':
        return 99
    if verkaufinfos.meldedaten.id == 'Boehmann':
        return 66
    else:
        return 0


def get_versicherung_from_allianz(verkaufinfos: VerkaeuferInfos)-> bool:
    if verkaufinfos.meldedaten.id=='Bremen':
        return False
    else:
        return True

def get_behinderungs_grad_from_medizin(verkaufinfos: VerkaeuferInfos) -> float:
    if verkaufinfos.gewicht > 300 or verkaufinfos.groesse < 120:
        return 80
    else:
        return 20


def get_unfallswahrscheinlichkeit(verkaufinfos: VerkaeuferInfos) -> float:
    return len(verkaufinfos.meldedaten.id)


@app.route('/boardinfos',methods=['POST'])
def main_request():
    requestinfos={key: value for key,value in flask.request.json.items()}
    print('asdf')
    verkaufinfos = VerkaeuferInfos(gewicht= requestinfos['gewicht'], groesse=requestinfos['groesse'], meldedaten= MeldeDaten(**requestinfos['meldedaten']))
    fahrtuechtigkeit = get_fahrtuechtigkeit_from_behoerde(verkaufinfos)
    vorstrafen = get_vorstrafen_from_Polizei(verkaufinfos)
    versicherung = get_versicherung_from_allianz(verkaufinfos)
    behinderungsgrad = get_behinderungs_grad_from_medizin(verkaufinfos)
    unfallswahrscheinlichkeit = get_unfallswahrscheinlichkeit(verkaufinfos)
    ret = BehoerdenInfos(fahrtuechtig= fahrtuechtigkeit, vorstrafen= vorstrafen, ist_versichert=versicherung, behinderungsgrad=behinderungsgrad, unfallswahrscheinlichkeit=unfallswahrscheinlichkeit)
    kombinierte_infos = AlleInfos(verkaeufer=verkaufinfos, behoerde = ret, klasse=None)
    klasse = k_nearest_neighbor(kombinierte_infos, data= data)
    return class_to_parameter[klasse].json()

data = read_in_data()
if __name__ == '__main__':
    print('asdf')
    print('qwer')
    serve(app,port=8100)
