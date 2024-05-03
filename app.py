import streamlit as st
import pandas as pd
import preprocessor , helper
df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

df = preprocessor.preprocess(df, region_df)
st.sidebar.title("Olympics Analysis")
user_menu = st.sidebar.radio(
    'select an option',('Medal Tally','Overall Analysis','Country-wise','Athlete wise Analysis')
)
st.dataframe(df)

if user_menu == 'Medal Tally':
    st.sidebar.header("Medal Tally")
    year , country = helper.country_year_list(df)
    selected_year = st.sidebar.selectbox("Select Year" , year)
    selected_country = st.sidebar.selectbox("Select Country" , country)
    medal_tally = helper.medal_tally(df)
    st.dataframe(medal_tally)
