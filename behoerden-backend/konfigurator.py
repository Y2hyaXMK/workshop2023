import math

from common.classes import AlleInfos, Fahrtuechtig


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
    wohnort = vergleiche_wohnort(info1.verkaeufer.meldedaten.wohnort, info2.verkaeufer.meldedaten.wohnort)
    summe = alter**2 +gewicht**2 + groesse**2+versicherung**2  + behinderungs_grad**2 + fahrtuechtig**2+vorstrafen**2+unfalls**2+wohnort**2
    return math.sqrt(summe)


def vergleiche_alter(info1: AlleInfos, info2: AlleInfos) -> int:
    vergleich = abs(info1.verkaeufer.meldedaten.alter - info2.verkaeufer.meldedaten.alter)
    return skaliere_ergebnis(0,150,vergleich)

def k_nearest_neighbor()