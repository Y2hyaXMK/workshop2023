import streamlit as st
import pandas as pd
from urllib.error import URLError
import altair as alt
import json
from common.classes import VerkaeuferInfos, HoverboardParameter, MeldeDaten
import requests


@st.cache_data
# def get_UN_data():
#     AWS_BUCKET_URL = "https://streamlit-demo-data.s3-us-west-2.amazonaws.com"
#     df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
#     return df.set_index("Region")

def get_hoverboard_config(_verkaufer_infos):
    return ''

try:
    id = st.text_input('ID')
    st.text(id)
    weight = st.number_input('Gewicht', step=1)
    st.text(weight)
    height = st.number_input('Größe', step=1)
    st.text(weight)
    age = st.number_input('age', step=1)
    st.text(age)
    hoverbaord_config = get_hoverboard_config(VerkaeuferInfos(meldedaten=MeldeDaten(id=id, alter=age), gewicht=weight, groesse=height))

    myobj = {'groesse': 0, 'gewicht': 0, 'meldedaten': {'alter': 0, 'id': 'XXX'}}

    res_text = requests.post("http://localhost:8100/boardinfos", json = myobj).text
    print(res_text)
    res = json.loads(res_text)
    st.text('Fahrstil sportlich: ' + str(res['ist_fahrstil_sportlich']))
    st.text('Boden flüssig: ' + str(res['ist_boden_fluessig']))
    st.text('Funktionserweiterung: ' + str(res['funktionserweiterung']))
    st.text('Max Flughöhe: ' + str(res['max_flughoehe']))
    st.text('Min Flughöhe: ' + str(res['min_flughoehe']))
    st.text('Max Speed: ' + str(res['max_speed']))
    st.text('verbotszone: ' + str(res['verbotszone']))
    st.text('max_breite: ' + str(res['max_breite']))
    st.text('min_breite: ' + str(res['min_breite']))
    st.text('max_laenge: ' + str(res['max_laenge']))
    st.text('min_laenge: ' + str(res['min_laenge']))
    st.text('geographische_lage: ' + str(res['geographische_lage']))
    st.text('beschleunigung: ' + str(res['beschleunigung']))
    st.text('steigung: ' + str(res['steigung']))




    # df = get_UN_data()
    # countries = st.multiselect(
    #     "Choose countrieasdfasdfsadfes", list(df.index), ["China", "United States of America"]
    # )
    # if not countries:
    #     st.error("Please select at least one country.")
    # else:
    #     data = df.loc[countries]
    #     data /= 1000000.0
    #     st.write("### Gross Agricultural Production ($B)", data.sort_index())

    #     data = data.T.reset_index()
    #     data = pd.melt(data, id_vars=["index"]).rename(
    #         columns={"index": "year", "value": "Gross Agricultural Product ($B)"}
    #     )
    #     chart = (
    #         alt.Chart(data)
    #         .mark_area(opacity=0.3)
    #         .encode(
    #             x="year:T",
    #             y=alt.Y("Gross Agricultural Product ($B):Q", stack=None),
    #             color="Region:N",
    #         )
    #     )
    #     st.altair_chart(chart, use_container_width=True)
except URLError as e:
    st.error(
        """
        **This demo requires internet access.**
        Connection error: %s
    """
        % e.reason
    )