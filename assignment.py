#1. Importing libraries
import pandas as pd
import matplotlib.pyplot as plt


# 2.Loading datasets
# Replace file names with your actual downloaded files
sentiment = pd.read_csv("fear_greed.csv")
trades = pd.read_csv("historical_data.csv")

# 3.Data Cleaning and Preprocessing
# Convert date columns
sentiment['Date'] = pd.to_datetime(sentiment['Date'])
trades['time'] = pd.to_datetime(trades['time'])

# Extract only date
sentiment['Date'] = sentiment['Date'].dt.date
trades['Date'] = trades['time'].dt.date


# 4.merging datasets
df = pd.merge(trades, sentiment, on='Date', how='left')


# 5.Feature Engineering 
# Profit/Loss classification
df['win'] = df['closedPnL'] > 0

# Clean missing values
df = df.dropna(subset=['Classification'])


# 6.Basic Exploration
print("\nDataset Shape:", df.shape)
print("\nSentiment Distribution:\n", df['Classification'].value_counts())
print("\nPnL Summary:\n", df['closedPnL'].describe())


# 7. Analysis by Sentiment
# 7.1 Average PnL by Sentiment
avg_pnl = df.groupby('Classification')['closedPnL'].mean()
print("\nAverage PnL:\n", avg_pnl)

# 7.2 Total PnL
total_pnl = df.groupby('Classification')['closedPnL'].sum()
print("\nTotal PnL:\n", total_pnl)

# 7.3 Win Rate
win_rate = df.groupby('Classification')['win'].mean()
print("\nWin Rate:\n", win_rate)

# 7.4 Average Leverage
avg_leverage = df.groupby('Classification')['leverage'].mean()
print("\nAverage Leverage:\n", avg_leverage)

# 7.5 Average Trade Size
avg_size = df.groupby('Classification')['size'].mean()
print("\nAverage Trade Size:\n", avg_size)

# 8. Visualisations 
# Average PnL
plt.figure()
avg_pnl.plot(kind='bar')
plt.title("Average PnL by Market Sentiment")
plt.xlabel("Sentiment")
plt.ylabel("Average PnL")
plt.show()

# Win Rate
plt.figure()
win_rate.plot(kind='bar')
plt.title("Win Rate by Market Sentiment")
plt.xlabel("Sentiment")
plt.ylabel("Win Rate")
plt.show()

# Leverage
plt.figure()
avg_leverage.plot(kind='bar')
plt.title("Average Leverage by Sentiment")
plt.xlabel("Sentiment")
plt.ylabel("Leverage")
plt.show()

# Trade Size
plt.figure()
avg_size.plot(kind='bar')
plt.title("Average Trade Size by Sentiment")
plt.xlabel("Sentiment")
plt.ylabel("Trade Size")
plt.show()

# 9. advanced insights
# Profit distribution
plt.figure()
df.boxplot(column='closedPnL', by='Classification')
plt.title("PnL Distribution by Sentiment")
plt.suptitle("")
plt.xlabel("Sentiment")
plt.ylabel("PnL")
plt.show()

# 10. saving the results 
summary = pd.DataFrame({
    "Average PnL": avg_pnl,
    "Total PnL": total_pnl,
    "Win Rate": win_rate,
    "Avg Leverage": avg_leverage,
    "Avg Trade Size": avg_size
})

summary.to_csv("trading_insights_summary.csv")

print("\n Analysis Complete. Results saved!")