import streamlit as st
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from plotly import express as px

st.set_page_config(page_title="Mapping Demo", page_icon="🌍")
st.set_option('deprecation.showPyplotGlobalUse', False)


@st.cache
def load_rest_data():
    data = pd.read_csv("all_seoul_good_rest_final.csv", encoding='utf-8')
    return data


def load_pop_data():
    data = pd.read_csv("rest_with_popul.csv", encoding='utf-8')
    data['지역구'] = data['Unnamed: 0']
    data.index = data['지역구']
    data = data.drop(['Unnamed: 0', '지역구'], axis=1)
    return data


df = load_rest_data()
gu_pop = load_pop_data()

st.markdown("# 모범음식점 밀도와 생활인구 상관관계")


# style 설정은 꼭 폰트설정 위에서 합니다.
# style 에 폰트 설정이 들어있으면 한글폰트가 초기화 되어 한글이 깨집니다.
plt.style.use("seaborn")
# 폰트설정
plt.rc("font", family='Malgun Gothic')

# 마이너스폰트 설정
plt.rc('axes', unicode_minus=False)


def jointPlot1():
    # fig = plt.figure(figsize=(12, 5))
    temp_df = df[df['위도'] != 0]
    sns.jointplot(data=temp_df, x="경도", y="위도", kind='hex')
    st.pyplot()


st.subheader('1) 서울시 모범음식점 밀도')
jointPlot1()


def heatmap1():
    plt.figure(figsize=(4, 3))
    sns.heatmap(data=gu_pop.corr(), annot=True,
                fmt='.2f', linewidths=.5, cmap='Blues')
    st.pyplot()


st.subheader('2) 모범음식점 수와 구별 생활인구 상관관계')
heatmap1()


st.subheader('3) 서울시 자치구별 모범음식점 수')
barplot1 = px.bar(data_frame=gu_pop, y='모범음식점(개)', text_auto=True, width=850,
                  height=500, title='서울시 자치구별 생활인구 수').update_xaxes(
    categoryorder="total descending")
barplot1


st.subheader('4) 서울시 자치구별 모범음식점 수')
barplot2 = px.bar(data_frame=gu_pop, y='평균생활인구(명)', text_auto=True, width=850,
                  height=500, title='서울시 자치구별 생활인구 수').update_xaxes(
    categoryorder="total descending")
barplot2
