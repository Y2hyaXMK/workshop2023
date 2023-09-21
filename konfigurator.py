import math
from pathlib import Path

import pandas as pd
from typing import List

from common.classes import AlleInfos, Fahrtuechtig, BehoerdenInfos, MeldeDaten, VerkaeuferInfos


def vergleiche_gewicht(gewicht, gewicht1) -> int:
    return skaliere_ergebnis(0,200,abs(gewicht-gewicht1))

def skaliere_ergebnis(min_value,max_value,echter_value,wichtigkeit=1)-> int:
    return round(echter_value/(max_value-min_value)*100)*wichtigkeit


def vergleiche_groesse(groesse, groesse1):
    wert = abs(groesse-groesse1)
    return skaliere_ergebnis(1,210,wert)


def vergleiche_fahrtuechtig(fahrtuechtig, fahrtuechtig1):
    wert = abs(fahrtuechtig.value - fahrtuechtig1.value)
    return skaliere_ergebnis(0,100,wert)


def vergleiche_versicherung(ist_versichert, ist_versichert1):
    if ist_versichert == ist_versichert1:
        return 0
    else:
        return 100


def vergleich_behinderungsgrad(behinderungsgrad, behinderungsgrad1):
    wert = abs(behinderungsgrad-behinderungsgrad1)
    return skaliere_ergebnis(0,100,wert)


def vergleiche_vorstrafen(vorstrafen, vorstrafen1):
    wert = abs(vorstrafen-vorstrafen1)
    return skaliere_ergebnis(0,10,wert)


def vergleiche_unfallswahrscheinlichkeit(unfallswahrscheinlichkeit, unfallswahrscheinlichkeit1):
    wert = abs(unfallswahrscheinlichkeit- unfallswahrscheinlichkeit1)
    return skaliere_ergebnis(0,10,wert)


def vergleiche_wohnort(wohnort, wohnort1):
    #TODO: benutze geopy
    if wohnort == wohnort1:
        return 0
    else:
        return 100


def entfernung(info1: AlleInfos, info2: AlleInfos) -> float:
    alter = vergleiche_alter(info1, info2)
    gewicht = vergleiche_gewicht(info1.verkaeufer.gewicht, info2.verkaeufer.gewicht)
    groesse = vergleiche_groesse(info1.verkaeufer.groesse, info2.verkaeufer.groesse)
    versicherung = vergleiche_versicherung(info1.behoerde.ist_versichert, info2.behoerde.ist_versichert)
    behinderungs_grad = vergleich_behinderungsgrad(info1.behoerde.behinderungsgrad, info2.behoerde.behinderungsgrad)
    fahrtuechtig = vergleiche_fahrtuechtig(info1.behoerde.fahrtuechtig,info2.behoerde.fahrtuechtig)
    vorstrafen = vergleiche_vorstrafen(info1.behoerde.vorstrafen, info2.behoerde.vorstrafen)
    unfalls = vergleiche_unfallswahrscheinlichkeit(info1.behoerde.unfallswahrscheinlichkeit, info2.behoerde.unfallswahrscheinlichkeit)
    summe = alter**2 +gewicht**2 + groesse**2+versicherung**2  + behinderungs_grad**2 + fahrtuechtig**2+vorstrafen**2+unfalls**2
    return math.sqrt(summe)


def vergleiche_alter(info1: AlleInfos, info2: AlleInfos) -> int:
    vergleich = abs(info1.verkaeufer.meldedaten.alter - info2.verkaeufer.meldedaten.alter)
    return skaliere_ergebnis(0,150,vergleich)

def k_nearest_neighbor(info: AlleInfos, data: List[AlleInfos], k =3):
    assert len(data)>  k
    entfernungen = [{"class": x.parameter_klasse, "entfernung": entfernung(info, x)} for x in data]
    entfernungen.sort(key= lambda x: x['entfernung'])
    sortiert = entfernungen[:k]
    asdf = {}
    for ding in sortiert:
        asdf[ding['class']] = asdf.get(ding['class'],0 ) +1
    most_common_class = max(asdf.keys(), key=lambda x: asdf[x])
    return most_common_class


def read_in_data() -> List[AlleInfos]:
    current_path = Path(__file__).parent / 'Werteliste_Hoverboard.xlsx'
    df = pd.read_excel(current_path)
    print(df.columns)
    ret = []
    for index, row in df.iterrows():
        fahrtuechtig = Fahrtuechtig[(row['Fahrtüchtig']).upper().strip()]
        alter = row['Alter']
        gewicht = row['Gewicht']
        groesse = row['Größe']
        vorstrafen = row['Vorstrafen']
        versicherung = row['Versicherung'] == 'ja'
        behinderung = row['Behinderungsgrad']
        unfalls = row['Unfallwahrscheinlichkeit']
        klasse = row['Klasse']
        behoerde = BehoerdenInfos(fahrtuechtig=fahrtuechtig, vorstrafen=vorstrafen, ist_versichert=versicherung,
                                  behinderungsgrad=behinderung, unfallswahrscheinlichkeit=unfalls)
        meldedaten = MeldeDaten(id=str(row['ID']), alter=int(alter))
        verkaeuferinfos = VerkaeuferInfos(gewicht=gewicht, groesse=groesse, meldedaten=meldedaten)
        if klasse in ['A', 'B', 'C', 'D', 'E', 'F']: #Nicht ausgefüllt = 'nan'
            all_infos = AlleInfos(behoerde=behoerde, verkaeufer=verkaeuferinfos, parameter_klasse=klasse)
            ret.append(all_infos)
    return ret

if __name__ == '__main__':
    read_in_data()


