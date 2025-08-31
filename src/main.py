from scraper import scrape_tweets
from parser import load_raw_data, parse_tweets, save_to_parquet
from analyzer import generate_signals
from visualizer import plot_graph

def main():
    scrape_tweets()
    print("tweets have been scraped and saved in tweets.parquet file")
    
    plot_graph()
    
    
    

if __name__ == "__main__":
    main()
