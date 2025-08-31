Project Title:  Stock Market Twitter Sentiment Analysis

Overview:

This project collects tweets related to the Indian stock market (hashtags like #nifty50, #sensex, #banknifty), processes them, and generates sentiment signals (positive/negative/neutral).
The signals are then aggregated and visualized for analysis.

Features:

Scrapes tweets using Selenium and BeautifulSoup

Stores tweets in Parquet format

Processes tweets with TF-IDF for text features

Generates sentiment signals

Aggregates and plots signals with Matplotlib

Project Structure:
project/
│-- data/               # Parquet files (tweets)
│-- signal_creation.py  # Converts tweet text to signals
│-- sig_aggregation.py  # Aggregates signals
│-- main.py             # Runs the pipeline & plots graph
│-- requirements.txt    # Python dependencies
│-- README.md           # Documentation


Installation:

Clone the repository

git clone <repo-link>
cd project


Install dependencies:

pip install -r requirements.txt

Usage:

Run the main script to process and visualize:

python main.py


This will:

Load tweets from tweets.parquet

Generate sentiment signals

Aggregate signals

Plot the sentiment graph

Example Output

Graph of signals over time
<img width="998" height="594" alt="image" src="https://github.com/user-attachments/assets/13d34322-96fc-4024-b964-dbe07e8fd6cc" />




Notes:

Make sure Google Chrome is installed (for Selenium scraping).

The script may take some time when scraping live tweets.
