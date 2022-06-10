import streamlit as st

st.set_page_config(
    page_title="오늘은뭐4먹지",
    page_icon="🍚",
)

st.write("# 🍚오늘은 뭘4먹지🍣의 미드 프로젝트 홈페이지입니다.")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    멋쟁이 사자처럼 AI School 6기 Mid-Project **🍚오늘은 뭘4먹지🍣**의 미드 프로젝트 결과 홈페이지입니다.
    ### 주제는 무엇인가요?
    - 서울시 구별 모범음식점 지정현황 분석입니다. [데이터 페이지](https://data.seoul.go.kr/dataList/OA-11295/S/1/datasetView.do)
    
    ### 데이터 살펴보기
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)
