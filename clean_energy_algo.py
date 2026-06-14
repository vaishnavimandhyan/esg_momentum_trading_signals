def run_clean_energy_algorithm():
 print("\n==================================================================")
 print("GREEN CAP_QUANT: ALGORITHMIC TRADING SIGNAL GENERATOR")
 print("Target Asset: iShares Global Clean Energy ETF (Ticker: ICLN)")
 print("==================================================================\n")

 # Historical Closing Prices simulated over a timeline for calculation
 # representing consecutive trading cycles
 historical_prices = [
 45.2, 45.8, 46.1, 45.9, 46.5, 47.2, 47.8, 48.1, 47.9, 48.5,
 49.2, 49.8, 50.1, 49.5, 48.9, 48.2, 47.5, 46.8, 46.2, 45.5,
 44.8, 44.1, 43.5, 43.9, 44.2, 45.1, 46.3, 47.8, 49.5, 51.2,
 52.8, 54.1, 55.5, 56.2, 55.8, 55.1, 54.3, 53.2, 52.1, 51.5
 ]

 print(f"Processing {len(historical_prices)} periods of historical price data...")
 print("Computing Technical Indicators: 3-Period SMA vs 8-Period SMA...")
 print("-" * 66)

 # To keep it lightweight without downloading giant tracking libraries,
 # we use a proportional 3-period (short-term) vs 8-period (long-term) window scale.
 short_window = 3
 long_window = 8

 previous_signal = "HOLD"

 # Loop through the data to look for trend crossovers
 for i in range(long_window, len(historical_prices)):
  current_price = historical_prices[i]

  # Calculate moving averages
  short_ma = sum(historical_prices[i - short_window + 1 : i + 1]) / short_window
  long_ma = sum(historical_prices[i - long_window + 1 : i + 1]) / long_window

# Check for Crossover Logic
  if short_ma > long_ma and previous_signal != "BUY":
   print(f"[SIGNAL] Period {i+1}: GOLDEN CROSS detected!")
   print(f"  Action: BUY ICLN at ${current_price:.2f} | Short MA ({short_ma:.2f}) crossed above Long MA ({long_ma:.2f})")
   print("-" * 66)
   previous_signal = "BUY"

  elif short_ma < long_ma and previous_signal != "SELL" and previous_signal != "HOLD":
   print(f" [SIGNAL] Period {i+1}: DEATH CROSS detected!")
   print(f"  Action: SELL ICLN at ${current_price:.2f} | Short MA ({short_ma:.2f}) dropped below Long MA ({long_ma:.2f})")
   print("-" * 66)
   previous_signal = "SELL"

 print("\n🏁 Backtest complete. Algorithm engine standing by for next market feed.\n")

run_clean_energy_algorithm()
