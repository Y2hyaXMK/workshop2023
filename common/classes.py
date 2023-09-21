from enum import Enum

from pydantic import BaseModel


class VerkaeuferInfos(BaseModel):
    gewicht: int
    groesse: int
    meldedaten: 'MeldeDaten'

class MeldeDaten(BaseModel):
    name: str
    vorname: str
    Wohnort: str

class BehoerdenInfos(BaseModel):
    fahrtuechtig: 'Fahrtuechtig'

class Fahrtuechtig(Enum):
    JA =1
    EINGESCHRAENKT= 2
    NEIN=3