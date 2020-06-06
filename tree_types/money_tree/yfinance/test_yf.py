import yfinance as yf
import matplotlib.pyplot as plt
import random

def random_pick():
    watchlist = ['MSFT', 'V', 'DLR', 'CONE', 'PING', 'AMD', 'O', 'BAM', 'DDOG', 'ADBE', 'NKE', 'CHWY', 'NOK']
    item_count = len(watchlist) - 1
    print(item_count)
    randppick = random.randint(0, item_count)
    stock_pick = watchlist[randppick]
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


def company_5D_MA(company):
    hist = company.history(period="5d")
    count = 0
    for i in range(0,5):
        count += hist.iloc[i]['Close']
    fiveDMA = count / 5
    print(f'Here is the 5 day Moving average for {company.ticker}: {fiveDMA}')
    
    hist90d = company.history(period="90d")
    count = 0
    for i in range(0,90):
        count += hist90d.iloc[i]['Close']
    nintyDMA = count / 90
    print(f'Here is the 90 day Moving average for {company.ticker}: {nintyDMA}')
    #Pull 5D moving average... what does that look like from alg to code?
    # a 5-day simple moving average is the five-day sum of closing prices divided by five.

def main():
    # is this the best way to call everything? 
    ticker = random_pick()
    company = pick_info(ticker)
    company_5D_MA(company)
    
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