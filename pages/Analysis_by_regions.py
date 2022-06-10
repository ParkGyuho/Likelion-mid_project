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

# def get_font_family():
#     """
#     시스템 환경에 따른 기본 폰트명을 반환하는 함수
#     """
#     import platform
#     system_name = platform.system()

#     if system_name == "Darwin" :
#         font_family = "AppleGothic"
#     elif system_name == "Windows":
#         font_family = "Malgun Gothic"
#     else:
#         # Linux(colab)
# #         !apt-get install fonts-nanum -qq  > /dev/null
# #         !fc-cache -fv

#         import matplotlib as mpl
#         mpl.font_manager._rebuild()
#         findfont = mpl.font_manager.fontManager.findfont
#         mpl.font_manager.findfont = findfont
#         mpl.backends.backend_agg.findfont = findfont
        
#         font_family = "NanumBarunGothic"
#     return font_family


# style 설정은 꼭 폰트설정 위에서 합니다.
# style 에 폰트 설정이 들어있으면 한글폰트가 초기화 되어 한글이 깨집니다.
#plt.style.use("seaborn")
# 폰트설정
#plt.rc("font", family=get_font_family())

# 마이너스폰트 설정
#plt.rc("axes", unicode_minus=False)

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
