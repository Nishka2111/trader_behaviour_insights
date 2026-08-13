import pandas as pd
import matplotlib.pyplot as plt

sentiment = pd.read_csv("fear_greed_index.csv")
trades = pd.read_csv("historical_data.csv")

sentiment.rename(columns={
    "date": "Date",
    "classification": "Classification"
}, inplace=True)

trades.rename(columns={
    "Timestamp IST": "TradeTime",
    "Closed PnL": "closedPnL",
    "Size USD": "size"
}, inplace=True)


sentiment["Date"] = pd.to_datetime(
    sentiment["Date"],
    errors="coerce"
)

trades["TradeTime"] = pd.to_datetime(
    trades["TradeTime"],
    errors="coerce"
)

sentiment = sentiment.dropna(subset=["Date"])
trades = trades.dropna(subset=["TradeTime"])


sentiment["Date"] = sentiment["Date"].dt.normalize()
trades["Date"] = trades["TradeTime"].dt.normalize()


#checking the date ranges of both datasets
print("\nSentiment date range:")
print(sentiment["Date"].min(), "to", sentiment["Date"].max())

print("\nTrade date range:")
print(trades["Date"].min(), "to", trades["Date"].max())


df = pd.merge(
    trades,
    sentiment[["Date", "Classification"]],
    on="Date",
    how="left"
)


df["win"] = df["closedPnL"] > 0
df = df.dropna(subset=["Classification"])


print("\nDataset Shape:", df.shape)

print("\nSentiment Distribution:")
print(df["Classification"].value_counts())

#PnL Summary
print("\nPnL Summary:")
print(df["closedPnL"].describe())

#average PnL by sentiment classification
avg_pnl = df.groupby("Classification")["closedPnL"].mean()
print("\nAverage PnL:")
print(avg_pnl)


#Total PnL
total_pnl = df.groupby("Classification")["closedPnL"].sum()
print("\nTotal PnL:")
print(total_pnl)


#win rate
win_rate = df.groupby("Classification")["win"].mean()
print("\nWin Rate:")
print(win_rate)


#average trade size
avg_size = df.groupby("Classification")["size"].mean()

print("\nAverage Trade Size:")
print(avg_size)


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


#distribution of PnL by sentiment classification
plt.figure()
df.boxplot(column="closedPnL", by="Classification")
plt.title("PnL Distribution by Sentiment")
plt.suptitle("")
plt.xlabel("Sentiment")
plt.ylabel("PnL")
plt.tight_layout()
plt.show()


summary = pd.DataFrame({
    "Average PnL": avg_pnl,
    "Total PnL": total_pnl,
    "Win Rate": win_rate,
    "Avg Trade Size": avg_size
})

summary.to_csv("trading_insights_summary.csv")

print("\nAnalysis Complete. Results saved!")