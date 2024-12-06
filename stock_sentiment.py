"""
CONVERTED FROM JUPYTER NOTEBOOK TO PYTHON SCRIPT
Sentiment Analysis using a LLM for a Publically Traded Stock
The goal of this project is to use a LLM for sentiment analysis for a publically traded stock.
"""

# Import Libraries

# Financial Data
import yfinance as yf
from finvizfinance.quote import finvizfinance

# Data Manipulation
import pandas as pd
import numpy as np

# Machine Learning Library
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Charts
# import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Connect to OpenAI API
from openai import OpenAI
from config import my_sk

# setup api client
client = OpenAI(api_key=my_sk)


# ### OpenAI Function using the LLM to classify text as positive, negative, or neutral
def classify_sentiment(title):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a sentiment classifier."},
            {
                "role": "user",
                "content": f"Classify the sentiment as 'POSITIVE' or 'NEGATIVE' or 'NEUTRAL' with just that one word only, no additional words or reasoning: {title}",
            },
        ],
        max_tokens=1,
        n=1,
        temperature=0.5,
    )
    return response.choices[0].message.content  # Directly access the .content attribute


# Check to see if the sentiment analysis (classify_sentiment)is working
classify_sentiment("IBM had an amazing run but tanked at the end of the day")


# Function to check the if the ticker symbol the user is entering is valid.
# The function will check the user input against the us_tickers_df symbols column.
def validate_ticker(ticker, df):
    """
    Checks if a ticker symbol exists in a DataFrame.

    Args:
      ticker: The ticker symbol to validate.
      df: The Pandas DataFrame containing the list of valid ticker symbols.

    Returns:
      True if the ticker is valid, False otherwise.
    """
    return ticker in df["symbol"].values


# Load all US publically traded companies into a dataframe
us_tickers_df = pd.read_csv("data/us_tickers.csv")

# Display the first few rows of the dataframe
us_tickers_df.head()

# Prompt the user for input and validate the user input against the us_tickers_df symbols column.
while True:
    ticker = input(
        "Enter a publicly traded company name or stock ticker (or type 'exit'): "
    ).upper()
    if ticker == "EXIT":
        print(f"Thank you for trying, goodbye!")
        break  # Exit the loop if the user types 'exit'

    if validate_ticker(ticker, us_tickers_df):
        print(f"{ticker} is a valid ticker symbol.")
        break  # Exit the loop and continue with the rest of the code
    else:
        print(
            f"{ticker} is not a valid ticker symbol. Please check your input or type EXIT."
        )

# Pull in the latest news for the ticker symbol
# Import Data using the APIs
print(f"Pulling latest news for {ticker}...")
try:
    stock = finvizfinance(ticker)
    news_df = stock.ticker_news()
    print(f"Successfully pulled {len(news_df)} news articles for {ticker}.")
    print(news_df.head())
except Exception as e:
    print(f"An error occurred while fetching news for {ticker}: {e}")


# EDA before and after passing data to the LLM
# Preprocess before putting into LLM
news_df["Title"] = news_df["Title"].str.lower()

# Classify Sentiment function applied to each row of news_df
news_df["sentiment"] = news_df["Title"].apply(classify_sentiment)

# Postprocess after putting into LLM
news_df["sentiment"] = news_df["sentiment"].str.upper()
news_df = news_df[news_df["sentiment"] != "NEUTRAL"]
news_df["Date"] = pd.to_datetime(news_df["Date"])
news_df["DateOnly"] = news_df["Date"].dt.date

# Validation checks of the data to ensure there is sentiment analysis included
print(news_df.head())
news_df["sentiment"].value_counts()

# Visulizations for the Sentiment Analysis

# Simple Bar Chart
plt.figure(figsize=(8, 5))
sns.countplot(x="sentiment", data=news_df)
plt.title(f"Sentiment Distribution for {ticker}")
plt.xlabel("Sentiment")
plt.ylabel("Number of Articles")
plt.show()

# Word Cloud for the Sentiment Analysis
# Combine all the titles into a single string
text = " ".join(news_df["Title"].tolist())

# Create the word cloud
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()


# Function to convert labels to numeric values
# Convert sentiment labels to numeric values, handling potential variations
def convert_sentiment_to_numeric(sentiment):
    if sentiment.startswith("POS"):  # Check if sentiment starts with 'POS'
        return 1
    elif sentiment.startswith("NEG"):  # Check if sentiment starts with 'NEG'
        return -1
    else:
        return 0  # If NE or "NEUTRAL", return 0


# Apply the function to the 'sentiment' column
news_df["sentiment_numeric"] = news_df["sentiment"].apply(convert_sentiment_to_numeric)

# Group by 'Source' and calculate the average sentiment
source_sentiment = news_df.groupby("Source")["sentiment_numeric"].mean()

# Create a bar chart
plt.figure(figsize=(18, 9))
source_sentiment.plot(kind="bar")
plt.title(f"Average Sentiment by Source for {ticker}")
plt.xlabel("News Source")
plt.ylabel("Sentiment Score")
plt.xticks(rotation=45)
plt.show()
