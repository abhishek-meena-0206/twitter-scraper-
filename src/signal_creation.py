import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# Load parquet file

def signal_conversion():
    df = pd.read_parquet("tweets.parquet", engine="pyarrow", use_nullable_dtypes=False)
    
    # Initialize TF-IDF Vectorizer
    tfidf = TfidfVectorizer(
        max_features=5000,      # top 5000 words
        ngram_range=(1,2),      # unigrams + bigrams
        stop_words="english"    # remove common stopwords
    )
    
    # Transform tweet content
    X_tfidf = tfidf.fit_transform(df["content"].astype(str))
    
    print("Shape:", X_tfidf.shape)  # (num_tweets, num_features)
    return X_tfidf,df,tfidf