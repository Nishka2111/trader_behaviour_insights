This analysis demonstrates that market sentiment plays a critical role in shaping trader behavior and performance. By integrating sentiment data into trading strategies, traders can make more informed decisions, manage risk effectively, and improve long-term outcomes.📊 Trader Behavior Insights: Sentiment vs Performance
- Overview
This project analyzes the relationship between Bitcoin market sentiment (Fear & Greed Index) and trader performance using historical trading data from Hyperliquid.
The objective is to uncover how market psychology influences trading outcomes, risk-taking behavior, and overall profitability.
 
- Objectives
Analyze trader performance across different market sentiments
Identify patterns in profitability, win rates, and losses
Evaluate how risk behavior (leverage & trade size) changes with sentiment
Derive actionable insights for smarter trading strategies

- Datasets Used
1. Bitcoin Market Sentiment Dataset
Columns: Date, Classification

Categories include:
Extreme Fear
Fear
Neutral
Greed
Extreme Greed

2. Historical Trader Data (Hyperliquid)

Columns include:
account
symbol
execution price
size
side
time
leverage
closedPnL

-  Methodology
- Data Preprocessing
Converted timestamps into standard datetime format
Extracted date for merging datasets
Merged trading data with sentiment data
Removed missing or inconsistent values

- Feature Engineering
Created a win/loss indicator:
win = closedPnL > 0

-  Analysis Performed
Average Profit/Loss by sentiment
Total Profit/Loss by sentiment
Win rate comparison
Average leverage usage
Trade size behavior

Key Findings
-  Higher profitability during Greed phases
Traders tend to perform better when market sentiment is optimistic
- Lower win rates during Fear periods
Increased uncertainty leads to more losing trades
- Higher leverage usage in Greed
Indicates overconfidence and increased risk-taking
-Larger losses during Fear
Suggests panic-driven or emotional trading
- Trade sizes increase in Greed markets
Traders become more aggressive in bullish conditions

📉 Visualizations

The project includes:
Bar charts for PnL, win rate, leverage, and trade size
Box plots for profit distribution across sentiments

Insights & Strategy Recommendations

Avoid excessive leverage during Greed phases to reduce risk exposure
Apply stricter risk management during Fear periods
Use sentiment indicators as a decision-making filter before trading
Focus on consistency rather than aggressive position sizing

Tech Stack

Python
Pandas
Matplotlib


Conclusion
This analysis demonstrates that market sentiment plays a critical role in shaping trader behavior and performance. By integrating sentiment data into trading strategies, traders can make more informed decisions, manage risk effectively, and improve long-term outcomes.
