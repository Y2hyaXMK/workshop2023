from common.classes import AlleInfos, Fahrtuechtig


def vergleiche_gewicht(gewicht, gewicht1) -> int:
    return skaliere_ergebnis(0,200,abs(gewicht-gewicht1))

def skaliere_ergebnis(min_value,max_value,echter_value)-> int: 
    return round(echter_value/(max_value-min_value)*100)


def vergleiche_groesse(groesse, groesse1):
    wert = abs(groesse-groesse1)
    return skaliere_ergebnis(1,210,wert)


def vergleiche_fahrtuechtig(fahrtuechtig, fahrtuechtig1):




def entfernung(info1: AlleInfos, info2: AlleInfos) -> float:
    alter = vergleiche_alter(info1, info2)
    gewicht = vergleiche_gewicht(info1.verkaeufer.gewicht, info2.verkaeufer.gewicht)
    groesse = vergleiche_groesse(info1.verkaeufer.groesse, info2.verkaeufer.groesse)
    vergleiche_fahrtuechtig(info1.behoerde.fahrtuechtig,info2.behoerde.fahrtuechtig)
    vergleiche_versicherung
    vergleich_behinderungsgrad
    vergleiche_unfalswahrscheinlichkeit
    vergleiche_wohnort


def vergleiche_alter(info1: AlleInfos, info2: AlleInfos) -> int:
    vergleich = abs(info1.verkaeufer.meldedaten.alter - info2.verkaeufer.meldedaten.alter)
    return skaliere_ergebnis(0,150,vergleich)