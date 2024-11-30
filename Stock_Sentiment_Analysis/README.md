# Stock News Sentiment Analysis

This project analyzes the sentiment of stock news headlines using Finviz and OpenAI's GPT-3.5 Turbo.

## Features

*   Fetches the latest stock news from Finviz.
*   Performs sentiment analysis on news headlines using OpenAI's GPT-3.5 Turbo.
*   Calculates the average sentiment score for each news source.
*   Generates a word cloud to visualize the prominent words in the news.
*   Provides interactive visualizations to explore sentiment trends and distributions.

## Requirements

*   Python 3.10 or higher
*   Pandas
*   finvizfinance
*   openai
*   matplotlib
*   seaborn
*   wordcloud

## Installation

1.  Clone the repository: `git clone https://github.com/your-username/stock-news-sentiment.git`
2.  Install the required packages: `pip install -r requirements.txt`
3.  Set up your OpenAI API key:
    *   Obtain an API key from [OpenAI](https://platform.openai.com/account/api-keys).
    *   Set the `openai.api_key` variable in the code to your API key.

## Usage

1.  Run the `stock_news_sentiment.py` script.
2.  Enter a valid stock ticker symbol when prompted.
3.  The script will fetch news, perform sentiment analysis, and generate visualizations.

## Examples

*   Word cloud of news headlines
*   Time series of daily average sentiment
*   Bar chart of sentiment by news source

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.