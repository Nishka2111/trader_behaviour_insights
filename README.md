Trader Behaviour Insights
Checks whether crypto market sentiment (Fear & Greed Index) relates to trading performance.
Data
historical_data.csv — trade-level execution data (PnL, size, direction, fees, etc.)
fear_greed_index.csv — daily Bitcoin Fear & Greed sentiment score, 2018–2025
What the script does
Cleans and date-aligns both datasets
Merges each trade with that day's sentiment label
Groups trades by sentiment (Extreme Fear → Extreme Greed)
Compares win rate, avg PnL, total PnL, and avg trade size across groups
Saves results to trading_insights_summary.csv and generates bar/box plots
Key finding
Extreme Fear trades performed worst — 29% win rate, ~$0 average PnL. Extreme Greed trades performed best — 55% win rate, highest average PnL. Performance doesn't scale symmetrically with sentiment intensity: panic hurts more than euphoria helps.
Run it
bash
pip install pandas matplotlib
python3 assignment.py
Output: trading_insights_summary.csv + 4 charts (avg PnL, win rate, avg trade size, PnL distribution — all by sentiment)
