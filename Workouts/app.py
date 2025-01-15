# This will is Streamlit app that will be used to display the data and the visualizations

import streamlit as st
import pandas as pd

### Variables
file_path = "data/workout_history_updated.csv"

## Load the data
df = pd.read_csv(file_path)
# Ensure 'time_of_day' is parsed as a string and replace 'NaT' with 'Unknown'
df['time_of_day'] = df['time_of_day'].astype(str).replace('NaT', 'Unknown')

st.title("Workout Report and Visualizations")
st.write("This is a simple Streamlit app that will display the workout data and visualizations")
st.write("From January 2017 to December 2024")

st.dataframe(df)