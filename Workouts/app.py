# This will is Streamlit app that will be used to display the data and the visualizations

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

### Variables
file_path = "data/workout_history_cleaned.csv"

## Load the data
df = pd.read_csv(file_path)
# Ensure 'time_of_day' is parsed as a string and replace 'NaT' with 'Unknown'
df['time_of_day'] = df['time_of_day'].astype(str).replace('NaT', 'Unknown')
# Convert 'month' and 'year' to strings
df['month'] = df['month'].astype(str)
df['year'] = df['year'].astype(str)


st.title("Workout Report and Visualizations")
st.write("This is a simple Streamlit app that will display the workout data and visualizations")
st.write("From January 2017 to December 2024")

with st.expander("View the data"):
    st.write( """
             The data below is an export from 
             Mindbody.com. It contains the workout history
             & was done using BeautifulSoup. 
             """)
    st.dataframe(df)
    

st.write("## Visualizations")

