# 1. Importing libraries
import pandas as pd
import matplotlib.pyplot as plt


# 2. Loading datasets
sentiment = pd.read_csv("fear_greed_index.csv")
trades = pd.read_csv("historical_data.csv")


# 3. Data Cleaning and Preprocessing

# Rename columns to simpler names
sentiment.rename(columns={
    "date": "Date",
    "classification": "Classification"
}, inplace=True)

trades.rename(columns={
    "Timestamp": "TradeTime",
    "Closed PnL": "closedPnL",
    "Size USD": "size"
}, inplace=True)


# Convert dates
sentiment["Date"] = pd.to_datetime(sentiment["Date"])
trades["TradeTime"] = pd.to_datetime(trades["TradeTime"])


# Extract only date
sentiment["Date"] = sentiment["Date"].dt.date
trades["Date"] = trades["TradeTime"].dt.date


# 4. Merge datasets
df = pd.merge(
    trades,
    sentiment[["Date", "Classification"]],
    on="Date",
    how="left"
)


# 5. Feature Engineering

# Profit/Loss classification
df["win"] = df["closedPnL"] > 0


# Clean missing sentiment values
df = df.dropna(subset=["Classification"])


# 6. Basic Exploration

print("\nDataset Shape:", df.shape)

print("\nSentiment Distribution:")
print(df["Classification"].value_counts())

print("\nPnL Summary:")
print(df["closedPnL"].describe())


# 7. Analysis by Sentiment

# 7.1 Average PnL
avg_pnl = df.groupby("Classification")["closedPnL"].mean()

print("\nAverage PnL:")
print(avg_pnl)


# 7.2 Total PnL
total_pnl = df.groupby("Classification")["closedPnL"].sum()

print("\nTotal PnL:")
print(total_pnl)


# 7.3 Win Rate
win_rate = df.groupby("Classification")["win"].mean()

print("\nWin Rate:")
print(win_rate)


# 7.4 Average Trade Size
avg_size = df.groupby("Classification")["size"].mean()

print("\nAverage Trade Size:")
print(avg_size)


# 8. Visualisations

# Average PnL
plt.figure()
avg_pnl.plot(kind="bar")
plt.title("Average PnL by Market Sentiment")
plt.xlabel("Sentiment")
plt.ylabel("Average PnL")
plt.tight_layout()
plt.show()


# Win Rate
plt.figure()
win_rate.plot(kind="bar")
plt.title("Win Rate by Market Sentiment")
plt.xlabel("Sentiment")
plt.ylabel("Win Rate")
plt.tight_layout()
plt.show()


# Trade Size
plt.figure()
avg_size.plot(kind="bar")
plt.title("Average Trade Size by Market Sentiment")
plt.xlabel("Sentiment")
plt.ylabel("Trade Size (USD)")
plt.tight_layout()
plt.show()


# 9. Advanced Insights

# Profit distribution
plt.figure()
df.boxplot(column="closedPnL", by="Classification")
plt.title("PnL Distribution by Sentiment")
plt.suptitle("")
plt.xlabel("Sentiment")
plt.ylabel("PnL")
plt.tight_layout()
plt.show()


# 10. Saving Results

summary = pd.DataFrame({
    "Average PnL": avg_pnl,
    "Total PnL": total_pnl,
    "Win Rate": win_rate,
    "Avg Trade Size": avg_size
})

summary.to_csv("trading_insights_summary.csv")

print("\nAnalysis Complete. Results saved!")