import yfinance as yf
import matplotlib.pyplot as plt
from random import choice
import csv
from datetime import date
import os.path

today = date.today()
d1 = today.strftime("%Y/%m/%d")
watchlist = ['MSFT', 'V', 'DLR', 'CONE', 'PING', 'AMD', 'O', 'BAM', 'DDOG', 'ADBE', 'NKE', 'CHWY', 'NOK']


def watchlist_moving_avearge(days, today):
    for symbol in watchlist:
        company = yf.Ticker(symbol)
        hist = company.history(period=f"{days}d")
        count = 0
        for day in range(0, days):
            count += hist.iloc[day]['Close']
        temp = count / days
    # a 5-day simple moving average is the five-day sum of closing prices divided by five.
        companyMA = f'%.2f' % (temp) #converting to 2 decimal points
        stock_symbol = company.ticker
        csv_location = f'/Users/MisterFili/Documents/{stock_symbol}.csv'
        file_exists = os.path.isfile(csv_location)
        print(f'Here is the {days} day Moving average for {stock_symbol}: {companyMA}')

        with open (f'/Users/MisterFili/Documents/{stock_symbol}.csv', 'a+', newline="") as csvfile:
            fieldnames = ['DATE', 'Ticker', 'MA']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if not file_exists:
                writer.writeheader()
            
            writer.writerow({'DATE': today,  'Ticker': company.ticker, 'MA': companyMA})
    print('\nForLoop Over\ncheck csv')


# SMA = Sum of data points in the moving average period / Total number of periods

# Exponential Weighted Moving Average using Pandas

def main():
    # is this the best way to call everything? 
    watchlist_moving_avearge(5,d1)
if __name__ == "__main__":
    main()



# # Download stock data then export as CSV
# data_df = yf.download("AAPL", start="2020-02-01", end="2020-03-20")
# data_df.to_csv('aapl.csv')

# Plot everything by leveraging the very powerful matplotlib package

# hist = bep.history(period="5d")
# plt.show(hist['Close'].plot(figsize=(16, 9)))

#Pick a random stock from watchlist

# pull information and show chart on said info

#create a data/calender class