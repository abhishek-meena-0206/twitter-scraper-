from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time, re
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import csv
import json
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

chrome_options = Options()
#chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
#chrome_options.add_argument("user-data-dir=C:/Users/Asus/AppData/Local/Google/Chrome/User Data")

#chrome_options.add_argument("profile-directory=Profile 3")

# Set up the WebDriver
service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=chrome_options)

# Hashtags to search
def scrape_tweets():
    hashtags = ["nifty50","banknifty","intraday","sensex"]
    all_tweets=[]
    flag=0
    for tag in hashtags:
        url = f"https://twitter.com/search?q=%23{tag}&src=typed_query&f=live"
        driver.get(url)
        if flag==0:
            time.sleep(25)  # wait for page load
            flag=1
        
        
        for _ in range(75):  # adjust for more data
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
    
        
        
            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")
            count=0
            
            print(f"\n🔹 Tweets for #{tag}:")
            for tweet in soup.select('[data-testid="tweet"]'):  # limit to 5 tweets per hashtag
            
                if count>=500:
                    break
                username_tag = tweet.select_one('[data-testid="User-Name"] span')
                username = username_tag.get_text(strip=True) if username_tag else "N/A"
        
                # Timestamp
                time_tag = tweet.select_one("time")
                timestamp = time_tag["datetime"] if time_tag else "N/A"
        
                # Tweet Content
                content_tag = tweet.select_one('div[data-testid="tweetText"]')
                content = content_tag.get_text(" ", strip=True) if content_tag else "No text"
        
                # Mentions + Hashtags
                mentions = re.findall(r"@\w+", content)
                hashtags_found = re.findall(r"#\w+", content)
        
                # Engagement Metrics
                replies_tag = tweet.select_one('[data-testid="reply"] span')
                retweets_tag = tweet.select_one('[data-testid="retweet"] span')
                likes_tag = tweet.select_one('[data-testid="like"] span')
                bookmark_tag = tweet.select_one('[data-testid="bookmark"] span')
        
                replies = replies_tag.get_text(strip=True) if replies_tag else "0"
                retweets = retweets_tag.get_text(strip=True) if retweets_tag else "0"
                likes = likes_tag.get_text(strip=True) if likes_tag else "0"
                bookmarks = bookmark_tag.get_text(strip=True) if bookmark_tag else "0"
        
                # Store as dict
                
                tweet_data = {
                    "username": username,
                    "timestamp": timestamp,
                    "content": content,
                    "mentions": mentions,
                    "hashtags": hashtags_found,
                    "replies": replies,
                    "retweets": retweets,
                    "likes": likes,
                    "bookmarks": bookmarks,
                    "search_tag": tag
                }
        
                all_tweets.append(tweet_data)
                print(len(all_tweets),"----------------------------------------")
                count+=1
    
    driver.quit()
    
    
    
    # Save to CSV
    print(len(all_tweets))
    df = pd.DataFrame(all_tweets)
    print(tweet_data)
    
    # Save as Parquet (using pyarrow engine)
    parquet_file = "data/tweets.parquet"
    df.to_parquet(parquet_file, engine="pyarrow", index=False)
    
    driver.quit()
