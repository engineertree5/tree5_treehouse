import yfinance as yf
import matplotlib.pyplot as plt
import random

def random_pick():
    watchlist = ['MSFT', 'V', 'DLR', 'CONE', 'PING', 'AMD', 'O', 'BAM', 'DDOG', 'ADBE', 'NKE', 'CHWY', 'NOK']
    stock_pick = random.choice(watchlist)
    print(f'random stock pick from watchlist ${stock_pick}')
    return stock_pick

def pick_info(ticker):
    company = yf.Ticker(ticker)
    try:
        rmp = company.info['regularMarketPrice']
        print(f'${company.ticker}\nRegular market price: {rmp}')
    except IndexError as e:
        print(e)
    
    return company


def company_moving_average(company, days):
    hist = company.history(period=f"{days}d")
    count = 0
    for i in range(0, days):
        count += hist.iloc[i]['Close']
    fiveDMA = count / days
    print(f'Here is the {days} day Moving average for {company.ticker}: {fiveDMA}')
    # a 5-day simple moving average is the five-day sum of closing prices divided by five.

def main():
    # is this the best way to call everything? 
    ticker = random_pick()
    company = pick_info(ticker)
    company_moving_average(company, 5)
    
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