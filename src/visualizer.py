import matplotlib.pyplot as plt
from sig_aggregation import signal_aggregation

df=signal_aggregation()

plt.plot(df["timestamp"], df["signal"], marker="o", markersize=2, alpha=0.7)
plt.title("Signal Plot (2000 points)")
plt.xlabel("Time")
plt.ylabel("Signal")
plt.show()
