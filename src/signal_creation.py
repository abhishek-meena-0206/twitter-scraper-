import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def signal_conversion(parquet_file="data/tweets.parquet"):
    # Load the Parquet file
    df = pd.read_parquet(parquet_file, engine="pyarrow", use_nullable_dtypes=False)
    print("Loaded DF shape:", df.shape)

    # Fill NaN or empty tweets with a placeholder
    df["content"] = df["content"].fillna("").astype(str)

    # Initialize TF-IDF Vectorizer
    tfidf = TfidfVectorizer(
        max_features=5000,      # top 5000 words
        ngram_range=(1,2),      # unigrams + bigrams
        stop_words="english"    # remove common stopwords
    )

    # Transform tweet content
    X_tfidf = tfidf.fit_transform(df["content"])
    print("TF-IDF shape:", X_tfidf.shape)  # Should match number of rows in df

    return X_tfidf, df, tfidf
