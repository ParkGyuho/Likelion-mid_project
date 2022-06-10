import streamlit as st
import time
import numpy as np
import pandas as pd
import folium
import plotly.express as px

st.set_page_config(page_title="모범음식점 위치", page_icon="🗺️")

st.markdown("# 서울시 모범음식점 위치")

@st.cache
def load_data():
    data = pd.read_csv("all_seoul_good_rest_final.csv", encoding='utf-8')
    return data

df = load_data()

lat = df['위도'].sum()/(len(df)-df[df['위도'] == 0].shape[0])
long = df['경도'].sum()/(len(df)-df[df['경도'] == 0].shape[0])

m = folium.Map(location=[lat,long], zoom_start=12)
for bst in df.index[:]:
    row = df.loc[bst]
    if row['업태명']=='한식':
        folium.Circle(
            radius = 7,
            location = [row['위도'],row['경도']],
            tooltip = row['업소명'] + '-' + row['업태명'] + '\t' + row['소재지도로명'],
            color = "red",
            fill = True,
        ).add_to(m)
    elif row['업태명']=='중국식':
        folium.Circle(
            radius = 7,
            location = [row['위도'],row['경도']],
            tooltip = row['업소명'] + '-' + row['업태명'] + '\t' + row['소재지도로명'],
            color = "blue",
            fill = True,
        ).add_to(m)
    elif row['업태명']=='일식':
        folium.Circle(
            radius = 7,
            location = [row['위도'],row['경도']],
            tooltip = row['업소명'] + '-' + row['업태명'] + '\t' + row['소재지도로명'],
            color = "green",
            fill = True,
        ).add_to(m)
    else:
        folium.Circle(
            radius = 7,
            location = [row['위도'],row['경도']],
            tooltip = row['업소명'] + '-' + row['업태명'] + '\t' + row['소재지도로명'],
            color = "yellow",
            fill = True,
        ).add_to(m)
m

'''
st.sidebar.header("Plotting Demo")
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")
'''
