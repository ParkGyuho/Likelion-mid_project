import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="오늘은뭐4먹지",
    page_icon="🍚",
)

st.write("# 🍚오늘은 뭘4먹지🍣")

st.sidebar.success("Select a page above.")

st.markdown(
    """
    멋쟁이 사자처럼 AI School 6기 Mid-Project **🍚오늘은 뭘4먹지🍣**의 미드 프로젝트 결과 홈페이지입니다.
    ### 주제는 무엇인가요?
    1. 서울시 구별 모범음식점 지정현황 분석
    2. 모범음식점 밀도와 서울시 지역구별 생활인구와의 상관관계
    (서울 생활인구: 서울의 특정지역, 특정시점에 존재하는 모든 인구)
    

    ### 데이터 살펴보기
"""
)
st.write(
    "* [모범음식점 데이터 페이지](https://data.seoul.go.kr/dataList/OA-11295/S/1/datasetView.do)")
st.write(
    "* [서울시 생활인구 데이터 페이지1](https://data.seoul.go.kr/dataVisual/seoul/seoulLivingPopulation.do)")
st.write(
    "* [서울시 생활인구 데이터 페이지2](https://data.seoul.go.kr/dataList/OA-15379/S/1/datasetView.do)")


@st.cache
def load_data():
    data = pd.read_csv("all_seoul_good_rest_final.csv", encoding='utf-8')
    return data


def load_pop_data():
    data = pd.read_csv("rest_with_popul.csv", encoding='utf-8')
    data['지역구'] = data['Unnamed: 0']
    data.index = data['지역구']
    data = data.drop(['Unnamed: 0', '지역구'], axis=1)
    return data


data_load_state = st.text('Loading data...')
df = load_data()
gu_pop = load_pop_data()
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df)
    st.write(gu_pop)
