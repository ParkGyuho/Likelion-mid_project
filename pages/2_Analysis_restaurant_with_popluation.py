import streamlit as st
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from plotly import express as px
import koreanize_matplotlib

st.set_page_config(page_title="Analysis Page", page_icon="π")
st.set_option('deprecation.showPyplotGlobalUse', False)


@st.cache
def load_rest_data():
    data = pd.read_csv("all_seoul_good_rest_final.csv", encoding='utf-8')
    return data


def load_pop_data():
    data = pd.read_csv("rest_with_popul.csv", encoding='utf-8')
    data['μ§μ­κ΅¬'] = data['Unnamed: 0']
    data.index = data['μ§μ­κ΅¬']
    data = data.drop(['Unnamed: 0', 'μ§μ­κ΅¬'], axis=1)
    return data


df = load_rest_data()
gu_pop = load_pop_data()

st.markdown("# λͺ¨λ²μμμ  λ°λμ μνμΈκ΅¬ μκ΄κ΄κ³")

# λ§μ΄λμ€ν°νΈ μ€μ 
plt.rc('axes', unicode_minus=False)


def jointPlot1():
    # fig = plt.figure(figsize=(12, 5))
    temp_df = df[df['μλ'] != 0]
    sns.jointplot(data=temp_df, x="κ²½λ", y="μλ", kind='hex')
    st.pyplot()


st.subheader('1) μμΈμ λͺ¨λ²μμμ  λ°λ')
jointPlot1()


def heatmap1():
    plt.figure(figsize=(4, 3))
    sns.heatmap(data=gu_pop.corr(), annot=True,
                fmt='.2f', linewidths=.5, cmap='Blues')
    st.pyplot()


st.subheader('2) λͺ¨λ²μμμ  μμ κ΅¬λ³ μνμΈκ΅¬ μκ΄κ΄κ³')
heatmap1()


st.subheader('3) μμΈμ μμΉκ΅¬λ³ λͺ¨λ²μμμ  μ')
barplot1 = px.bar(data_frame=gu_pop, y='λͺ¨λ²μμμ (κ°)', text_auto=True, width=850,
                  height=500, title='μμΈμ μμΉκ΅¬λ³ μνμΈκ΅¬ μ').update_xaxes(
    categoryorder="total descending")
barplot1


st.subheader('4) μμΈμ μμΉκ΅¬λ³ λͺ¨λ²μμμ  μ')
barplot2 = px.bar(data_frame=gu_pop, y='νκ· μνμΈκ΅¬(λͺ)', text_auto=True, width=850,
                  height=500, title='μμΈμ μμΉκ΅¬λ³ μνμΈκ΅¬ μ').update_xaxes(
    categoryorder="total descending")
barplot2
