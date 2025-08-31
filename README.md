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
<img width="430" height="576" alt="image" src="https://github.com/user-attachments/assets/2c2715e0-6032-4f6a-a36d-f4b9c0438568" />






Installation:

Clone the repository

git clone https://github.com/abhishek-meena-0206/twitter-scraper-.git
cd market




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






Example Output:

Graph of signals over time
<img width="998" height="594" alt="image" src="https://github.com/user-attachments/assets/13d34322-96fc-4024-b964-dbe07e8fd6cc" />




Notes:

Make sure Google Chrome is installed (for Selenium scraping).

The script may take some time when scraping live tweets.
