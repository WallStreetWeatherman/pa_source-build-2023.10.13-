<<<<<<< HEAD
import pandas as pd
import matplotlib.pyplot as plt

def fetch_data_from_csv(filename):
    historical_data = pd.read_csv(filename, parse_dates=['Date'], index_col='Date')
    return historical_data

def calculate_z_scores(historical_data, window=20):
    historical_data['Moving_Avg'] = historical_data['Close'].rolling(window=window).mean()
    historical_data['Std_Dev'] = historical_data['Close'].rolling(window=window).std()
    z_scores = (historical_data['Close'] - historical_data['Moving_Avg']) / historical_data['Std_Dev']
    return z_scores

def mean_reversion_analysis(daily_data, weekly_data, monthly_data, pe_ratio, z_threshold=2.0, pe_threshold=20.0):
    daily_z = calculate_z_scores(daily_data)
    weekly_z = calculate_z_scores(weekly_data)
    monthly_z = calculate_z_scores(monthly_data)

    # Reindex weekly and monthly data to match daily data index
    weekly_z = weekly_z.reindex(daily_data.index, method='ffill')
    monthly_z = monthly_z.reindex(daily_data.index, method='ffill')

    signals = pd.DataFrame(index=daily_data.index)
    signals['price'] = daily_data['Close']
    signals['signal'] = 0.0

    signals['Daily_Z'] = daily_z
    signals['Weekly_Z'] = weekly_z
    signals['Monthly_Z'] = monthly_z

    if pe_ratio < pe_threshold:
        signals.loc[(signals['Daily_Z'] > z_threshold) & 
                    (signals['Weekly_Z'] > z_threshold) & 
                    (signals['Monthly_Z'] > z_threshold), 'signal'] = 1.0

        signals.loc[(signals['Daily_Z'] < -z_threshold) & 
                    (signals['Weekly_Z'] < -z_threshold) & 
                    (signals['Monthly_Z'] < -z_threshold), 'signal'] = -1.0

    return signals

def plot_signals(signals, ticker):
    plt.figure(figsize=(12, 6))
    plt.plot(signals['price'], label='Price')
    plt.plot(signals.loc[signals['signal'] == 1.0].index, signals.price[signals['signal'] == 1.0], '^', markersize=10, color='g', label='Buy Signal')
    plt.plot(signals.loc[signals['signal'] == -1.0].index, signals.price[signals['signal'] == -1.0], 'v', markersize=10, color='r', label='Sell Signal')
    plt.title(f'Mean Reversion Signals for {ticker}')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend(loc='best')
    plt.show()

if __name__ == "__main__":
    ticker = "HIMS"  # Replace with the ticker of your choice
    daily_filename = "C:\\Users\\Nick\\Desktop\Programming\\python\\historical data CSVs\\stocks\\HIMS_daily.csv"
    weekly_filename = "C:\\Users\\Nick\\Desktop\Programming\\python\\historical data CSVs\\stocks\\HIMS_weekly.csv"  # Replace with the path to your weekly CSV
    monthly_filename = "C:\\Users\\Nick\\Desktop\Programming\\python\\historical data CSVs\\stocks\\HIMS_monthly.csv"  # Replace with the path to your monthly CSV
    pe_ratio = -21.69  # Replace with the P/E ratio

    daily_data = fetch_data_from_csv(daily_filename)
    weekly_data = fetch_data_from_csv(weekly_filename)
    monthly_data = fetch_data_from_csv(monthly_filename)

    signals = mean_reversion_analysis(daily_data, weekly_data, monthly_data, pe_ratio)
    plot_signals(signals, ticker)
=======
import pandas as pd
import matplotlib.pyplot as plt

def fetch_data_from_csv(filename):
    historical_data = pd.read_csv(filename, parse_dates=['Date'], index_col='Date')
    return historical_data

def calculate_z_scores(historical_data, window=20):
    historical_data['Moving_Avg'] = historical_data['Close'].rolling(window=window).mean()
    historical_data['Std_Dev'] = historical_data['Close'].rolling(window=window).std()
    z_scores = (historical_data['Close'] - historical_data['Moving_Avg']) / historical_data['Std_Dev']
    return z_scores

def mean_reversion_analysis(daily_data, weekly_data, monthly_data, pe_ratio, z_threshold=2.0, pe_threshold=20.0):
    daily_z = calculate_z_scores(daily_data)
    weekly_z = calculate_z_scores(weekly_data)
    monthly_z = calculate_z_scores(monthly_data)

    # Reindex weekly and monthly data to match daily data index
    weekly_z = weekly_z.reindex(daily_data.index, method='ffill')
    monthly_z = monthly_z.reindex(daily_data.index, method='ffill')

    signals = pd.DataFrame(index=daily_data.index)
    signals['price'] = daily_data['Close']
    signals['signal'] = 0.0

    signals['Daily_Z'] = daily_z
    signals['Weekly_Z'] = weekly_z
    signals['Monthly_Z'] = monthly_z

    if pe_ratio < pe_threshold:
        signals.loc[(signals['Daily_Z'] > z_threshold) & 
                    (signals['Weekly_Z'] > z_threshold) & 
                    (signals['Monthly_Z'] > z_threshold), 'signal'] = 1.0

        signals.loc[(signals['Daily_Z'] < -z_threshold) & 
                    (signals['Weekly_Z'] < -z_threshold) & 
                    (signals['Monthly_Z'] < -z_threshold), 'signal'] = -1.0

    return signals

def plot_signals(signals, ticker):
    plt.figure(figsize=(12, 6))
    plt.plot(signals['price'], label='Price')
    plt.plot(signals.loc[signals['signal'] == 1.0].index, signals.price[signals['signal'] == 1.0], '^', markersize=10, color='g', label='Buy Signal')
    plt.plot(signals.loc[signals['signal'] == -1.0].index, signals.price[signals['signal'] == -1.0], 'v', markersize=10, color='r', label='Sell Signal')
    plt.title(f'Mean Reversion Signals for {ticker}')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend(loc='best')
    plt.show()

if __name__ == "__main__":
    ticker = "HIMS"  # Replace with the ticker of your choice
    daily_filename = "C:\\Users\\Nick\\Desktop\Programming\\python\\historical data CSVs\\stocks\\HIMS_daily.csv"
    weekly_filename = "C:\\Users\\Nick\\Desktop\Programming\\python\\historical data CSVs\\stocks\\HIMS_weekly.csv"  # Replace with the path to your weekly CSV
    monthly_filename = "C:\\Users\\Nick\\Desktop\Programming\\python\\historical data CSVs\\stocks\\HIMS_monthly.csv"  # Replace with the path to your monthly CSV
    pe_ratio = -21.69  # Replace with the P/E ratio

    daily_data = fetch_data_from_csv(daily_filename)
    weekly_data = fetch_data_from_csv(weekly_filename)
    monthly_data = fetch_data_from_csv(monthly_filename)

    signals = mean_reversion_analysis(daily_data, weekly_data, monthly_data, pe_ratio)
    plot_signals(signals, ticker)
>>>>>>> 84bf0d4324d6448d3b46f82f3c1e806e30f05588
