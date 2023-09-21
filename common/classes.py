from enum import Enum
from typing import List, Dict

from pydantic import BaseModel


class VerkaeuferInfos(BaseModel):
    gewicht: int
    groesse: int
    meldedaten: 'MeldeDaten'


class MeldeDaten(BaseModel):
    id: str
    alter: int


class BehoerdenInfos(BaseModel):
    fahrtuechtig: 'Fahrtuechtig'
    vorstrafen: int
    ist_versichert: bool
    behinderungsgrad: int
    unfallswahrscheinlichkeit: int


class AlleInfos(BaseModel):
    verkaeufer: VerkaeuferInfos
    behoerde: BehoerdenInfos
    parameter_klasse: str = None


class Versicherung(Enum):
    JA = 1
    NEIN = 2


class HoverboardParameter(BaseModel):
    ist_fahrstil_sportlich: bool
    ist_boden_fluessig: bool
    funktionserweiterung: List[str]
    max_flughoehe: float
    min_flughoehe: float
    max_speed: int
    verbotszone: List[str]
    max_breite: float
    min_breite: float
    max_laenge: float
    min_laenge: float
    geographische_lage: List[str]
    beschleunigung: int
    steigung: int

class_to_parameter: Dict['str', HoverboardParameter] ={}

class_to_parameter['A'] = HoverboardParameter(
ist_fahrstil_sportlich= False,
    ist_boden_fluessig = False,
    funktionserweiterung = ['a','b'],
    max_flughoehe=0.1,
    min_flughoehe= 0.1,
    max_speed= 5,
    verbotszone = ['Innenstadt, Wald, 50er Zone, 70er Zone, Autobahn'],
    max_breite = 0.4,
    min_breite = 0.2,
    max_laenge = 0.9,
    min_laenge = 0.7,
    geographische_lage= [],
    beschleunigung =1 ,
    steigung = 15
)
class_to_parameter['B'] = HoverboardParameter(
ist_fahrstil_sportlich= False,
    ist_boden_fluessig = False,
    funktionserweiterung = ['a','b','c'],
    max_flughoehe=0.2,
    min_flughoehe= 0.1,
    max_speed= 15,
    verbotszone = ['Wald, 50er Zone, 70er Zone, Autobahn'],
    max_breite = 0.4,
    min_breite = 0.2,
    max_laenge = 0.9,
    min_laenge = 0.7,
    geographische_lage= [],
    beschleunigung =3 ,
    steigung = 20
)
class_to_parameter['C'] = HoverboardParameter(
ist_fahrstil_sportlich= False,
    ist_boden_fluessig = False,
    funktionserweiterung = ['a','b','c','d'],
    max_flughoehe=0.7,
    min_flughoehe= 0.1,
    max_speed= 40,
    verbotszone = ['Wald, 70er Zone, Autobahn, Fußgängerpassage'],
    max_breite = 0.6,
    min_breite = 0.2,
    max_laenge = 1.2,
    min_laenge = 0.7,
    geographische_lage= [],
    beschleunigung =5 ,
    steigung = 20
)
class_to_parameter['D'] = HoverboardParameter(
ist_fahrstil_sportlich= True,
    ist_boden_fluessig = True,
    funktionserweiterung = ['a','b','c','d','e'],
    max_flughoehe=0.7,
    min_flughoehe= 0.1,
    max_speed= 100,
    verbotszone = ['Autobahn, Fußgängerpassage'],
    max_breite = 0.6,
    min_breite = 0.2,
    max_laenge = 1.2,
    min_laenge = 0.7,
    geographische_lage= [],
    beschleunigung =7 ,
    steigung = 25
)
class_to_parameter['E'] = HoverboardParameter(
ist_fahrstil_sportlich= True,
    ist_boden_fluessig = True,
    funktionserweiterung = ['a','b','c','d','e'],
    max_flughoehe=5,
    min_flughoehe= 0.1,
    max_speed= 190,
    verbotszone = ['Fußgängerpassage'],
    max_breite = 0.8,
    min_breite = 0.2,
    max_laenge = 2,
    min_laenge = 0.6,
    geographische_lage= [],
    beschleunigung =9 ,
    steigung = 30
)
class_to_parameter['F'] = HoverboardParameter(
ist_fahrstil_sportlich= True,
    ist_boden_fluessig = True,
    funktionserweiterung = ['a','b','c','d','e','f'],
    max_flughoehe=5,
    min_flughoehe= 0.1,
    max_speed= 250,
    verbotszone = ['Fußgängerpassage'],
    max_breite = 0.8,
    min_breite = 0.2,
    max_laenge = 2,
    min_laenge = 0.6,
    geographische_lage= [],
    beschleunigung =10 ,
    steigung = 45
)

class Fahrtuechtig(Enum):
    JA = 0
    EINGESCHRÄNKT = 50
    NEIN = 100
