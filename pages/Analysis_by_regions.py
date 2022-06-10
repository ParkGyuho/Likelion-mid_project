import streamlit as st
import time
import numpy as np
import pandas as pd
import folium
from streamlit_folium import folium_static
from matplotlib import pyplot as plt
import seaborn as sns
from plotly import express as px

st.set_page_config(page_title="모범음식점 위치", page_icon="🗺️")

plt.rcParams['font.family'] = 'NanumGothic'

st.markdown("# 서울시 모범음식점 위치")

@st.cache
def load_data():
    data = pd.read_csv("all_seoul_good_rest_final.csv", encoding='utf-8')
    return data

df = load_data()

lat = df['위도'].sum()/(len(df)-df[df['위도'] == 0].shape[0])
long = df['경도'].sum()/(len(df)-df[df['경도'] == 0].shape[0])

st.subheader('Folium을 이용한 모범음식점 시각화')
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
folium_static(m)

st.subheader(' 경도와 위도 자치구별 시각화 ')
drop_zero=df[df["위도"]==0].index
drop_zero = df.drop(drop_zero)
plt.figure(figsize=(12, 10))
sns.scatterplot(data=drop_zero, x="경도", y="위도", hue="구")
plt.legend(bbox_to_anchor=(1,1))

st.subheader(' 경도와 위도 자치구별 시각화 ver2(jointplot의 hex 사용) ')
plt.figure(figsize=(12, 10))
sns.jointplot(data=df[df['위도'] != 0], x="경도", y="위도", kind="hex")

st.subheader(' 구별 면적별 업장개수 ')
px.histogram(df, x="구", color="면적분류", width=1300, height=500, title="구별 면적별 업장개수")
