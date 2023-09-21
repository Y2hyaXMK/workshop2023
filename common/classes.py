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


class Fahrtuechtig(Enum):
    JA