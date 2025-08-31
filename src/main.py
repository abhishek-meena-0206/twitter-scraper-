from scraper import scrape_tweets
from parser import load_raw_data, parse_tweets, save_to_parquet
from analyzer import generate_signals
from visualizer import plot_signal_strength

def main():
    print("🚀 Starting Market Intelligence Pipeline...")

    # Step 1: Scrape tweets
    print("🔍 Scraping tweets...")
    scrape_tweets(output_file="data/raw_tweets.json", limit=2000)

    # Step 2: Load and parse raw data
    print("🧹 Parsing and cleaning tweets...")
    raw_df = load_raw_data("data/raw_tweets.json")
    parsed_df = parse_tweets(raw_df)
    save_to_parquet(parsed_df, "data/cleaned_tweets.parquet")

    # Step 3: Analyze signals
    print("📊 Generating trading signals...")
    signals = generate_signals(parsed_df)

    # Step 4: Visualize insights
    print("📈 Plotting signal strength...")
    plot_signal_strength(signals)

    print("✅ Pipeline completed successfully!")

if __name__ == "__main__":
    main()
