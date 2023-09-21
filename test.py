import pandas as pd
from urllib.error import URLError
import altair as alt
import json
from common.classes import VerkaeuferInfos, HoverboardParameter
import requests

myobj = {'groesse': 0, 'gewicht': 0, 'meldedaten': {'alter': 0, 'id': 'XXX'}}

res_text = requests.post("http://localhost:8100/boardinfos", json = myobj).text
print(res_text)
res = json.loads(res_text)
print(res['ist_fahrstil_sportlich'])


