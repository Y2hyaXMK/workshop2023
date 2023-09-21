import pandas as pd
from urllib.error import URLError
import altair as alt
import flask
from common.classes import VerkaeuferInfos, HoverboardParameter
import requests

myobj = {'id': 0, 'groesse': 0, 'gewicht': 0}

x = requests.post("http://localhost:8222", json = myobj)
print(x)


