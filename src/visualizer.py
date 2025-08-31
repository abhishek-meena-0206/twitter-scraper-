import matplotlib.pyplot as plt
from sig_aggregation import signal_aggregation
import pandas as pd

# Get signals

def plot_graph():
    df = signal_aggregation()
    
    # Convert timestamp to datetime
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    
    # Optional: sort by timestamp
    df = df.sort_values("timestamp")
    
    # Quick check
    print(df.head())
    
    # Plot
    plt.figure(figsize=(12,6))
    plt.plot(df["timestamp"], df["signal"], marker="o", markersize=2, alpha=0.7)
    plt.title("Signal Plot (All points)")
    plt.xlabel("Time")
    plt.ylabel("Signal")
    plt.xticks(rotation=45)  # rotate x labels for readability
    plt.tight_layout()
    plt.show()
