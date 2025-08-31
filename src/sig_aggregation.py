import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from signal_creation import signal_conversion






def signal_aggregation():
    X_tfidf,df,tfidf=signal_conversion()
    
    feature_names = tfidf.get_feature_names_out()

    # =========================
    # Step 3: Define Word Groups
    # =========================
    bullish_words = ["buy", "bullish", "uptrend", "long", "rally", "gain", "breakout"]
    bearish_words = ["sell", "bearish", "downtrend", "short", "crash", "loss", "fall"]
    neutral_words = ["hold", "wait", "sideways", "flat"]

    # =========================
    # Step 4: Aggregate Scores
    # =========================
    X_dense = X_tfidf.toarray()
    word_to_index = {word: idx for idx, word in enumerate(feature_names)}
    def aggregate_signal(row_vector):
        bullish_score = sum(row_vector[word_to_index[w]] for w in bullish_words if w in word_to_index)
        bearish_score = sum(row_vector[word_to_index[w]] for w in bearish_words if w in word_to_index)
        neutral_score = sum(row_vector[word_to_index[w]] for w in neutral_words if w in word_to_index)
        return bullish_score, bearish_score, neutral_score

    

    signals = np.array([aggregate_signal(row) for row in X_dense])

    # =========================
    # Step 5: Composite Signal
    # =========================
    df_signals = pd.DataFrame(signals, columns=["bullish", "bearish", "neutral"])
    df["bullish"] = df_signals["bullish"]
    df["bearish"] = df_signals["bearish"]
    df["neutral"] = df_signals["neutral"]
    df["signal"] = df["bullish"] - df["bearish"]

    # =========================
    # Step 6: Confidence Interval
    # =========================
    mean_signal = df["signal"].mean()
    std_signal = df["signal"].std()
    ci_lower = mean_signal - 1.96 * std_signal / np.sqrt(len(df))
    ci_upper = mean_signal + 1.96 * std_signal / np.sqrt(len(df))

    # =========================
    # Step 7: Output Results
    # =========================
    print("Composite Signal (mean):", mean_signal)
    print("95% Confidence Interval:", (ci_lower, ci_upper))

    print("\nSample Signals:")
    print(df[["content", "bullish", "bearish", "neutral", "signal"]].head())
    return df
