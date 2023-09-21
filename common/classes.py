from enum import Enum
from typing import List

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
    energiesparverhalten: int
    ist_boden_fluessig: bool
    funktionserweiterung: List[str]
    max_flughoehe: float
    min_flughoehe: float
    max_speed: int
    verbotszone: List[str]
    breite: int
    laenge: int
    geographische_lage: List[str]
    beschleunigung: int
    steigung: int


class Fahrtuechtig(Enum):
    JA = 0
    EINGESCHRÄNKT = 50
    NEIN = 100
