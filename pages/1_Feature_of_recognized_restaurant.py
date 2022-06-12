import streamlit as st
import time
import numpy as np
import pandas as pd
import folium
from streamlit_folium import folium_static
from matplotlib import pyplot as plt
import seaborn as sns
from plotly import express as px
import koreanize_matplotlib

st.set_page_config(page_title="서울시 모범음식점 현황", page_icon="🗺️")


# style 설정은 꼭 폰트설정 위에서 합니다.
# style 에 폰트 설정이 들어있으면 한글폰트가 초기화 되어 한글이 깨집니다.
plt.style.use("seaborn")
# 폰트설정
plt.rc("font", family='Malgun Gothic')

# 마이너스폰트 설정
plt.rc('axes', unicode_minus=False)

st.markdown("# 서울시 모범음식점 현황")


@st.cache
def load_rest_data():
    data = pd.read_csv("all_seoul_good_rest_final.csv", encoding='utf-8')
    return data


df = load_rest_data()

lat = df['위도'].sum()/(len(df)-df[df['위도'] == 0].shape[0])
long = df['경도'].sum()/(len(df)-df[df['경도'] == 0].shape[0])

st.subheader('1) 메뉴별 모범음식점 분류')
st.write('빨강:한식, 파랑:중식, 초록:일식, 노랑:기타')
m = folium.Map(location=[lat, long], zoom_start=11)
for bst in df.index[:]:
    row = df.loc[bst]
    if row['업태명'] == '한식':
        folium.Circle(
            radius=10,
            location=[row['위도'], row['경도']],
            tooltip=row['업소명'] + '-' + row['업태명'] + '\t' + row['소재지도로명'],
            color="red",
            fill=True,
        ).add_to(m)
    elif row['업태명'] == '중국식':
        folium.Circle(
            radius=10,
            location=[row['위도'], row['경도']],
            tooltip=row['업소명'] + '-' + row['업태명'] + '\t' + row['소재지도로명'],
            color="blue",
            fill=True,
        ).add_to(m)
    elif row['업태명'] == '일식':
        folium.Circle(
            radius=10,
            location=[row['위도'], row['경도']],
            tooltip=row['업소명'] + '-' + row['업태명'] + '\t' + row['소재지도로명'],
            color="green",
            fill=True,
        ).add_to(m)
    else:
        folium.Circle(
            radius=10,
            location=[row['위도'], row['경도']],
            tooltip=row['업소명'] + '-' + row['업태명'] + '\t' + row['소재지도로명'],
            color="yellow",
            fill=True,
        ).add_to(m)
folium_static(m)

hist0 = px.histogram(df, x="업태명", text_auto=True, width=800,
                     height=500, title="업태명별 모범업소갯수").update_xaxes(categoryorder="total descending")
hist0


hist1 = px.histogram(df, x="지정년도", color="면적분류",
                     width=800, height=500, title="연도별 면적분류 매장갯수", text_auto=True)
hist1

st.subheader('구별 면적별 업장개수 히스토그램')
hist2 = px.histogram(df, x="구", color="면적분류", width=800,
                     height=500, text_auto=True, title="구별 면적별 업장개수").update_xaxes(categoryorder="total descending")
hist2
