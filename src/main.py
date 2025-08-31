from scraper import scrape_tweets

from visualizer import plot_graph

def main():
    scrape_tweets()
    print("tweets have been scraped and saved in tweets.parquet file")
    
    plot_graph()
    print("graph is plotted")
    
    
    

if __name__ == "__main__":
    main()
