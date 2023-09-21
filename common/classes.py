from enum import Enum

from pydantic import BaseModel


class VerkaeuferInfos(BaseModel):
    gewicht: int
    groesse: int
    meldedaten: 'MeldeDaten'

class MeldeDaten(BaseModel):
    name: str
    vorname: str
    wohnort: str

class BehoerdenInfos(BaseModel):
    fahrtuechtig: 'Fahrtuechtig'
    vorstrafen: int
    versicherung: 'Versicherung'
    behinderungsgrad: int
    unfallswahrscheinlichkeit: int


class Versicherung(Enum):
    JA = 1
    NEIN =2


class Fahrtuechtig(Enum):
    JA =1
    EINGESCHRAENKT= 2
    NEIN=3