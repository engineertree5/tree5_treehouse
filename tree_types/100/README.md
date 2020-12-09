# 100 Days Of Code

 For my 100 days of code the aim is to be a better teacher, investor, and programmer. I'm designing the plan as I draw it, so my agenda will be shared on a day by day basis. 

## Day 1 - Birth of pyetf
For Day 1 of 100 we will be working with the yfinance module which is used to pull stock market information from yahoo. I will be going at MY own pace so if you need more information or get stuck just reach out. Most of this information/code is for myself and anyone willing to read/use it. 

> Go visit this [LINK](https://github.com/ranaroussi/yfinance) to get started with yfinance module.


So we will be putting all of our code into a class so we can easily add new code to what we do within the 100 days. Think of a class as a collection of commands. By just looking at the methods within the class we are only performing verbs - GET SET. 

### Quick Summary
By default, A user will need to pass in the stock(s) they are looking to get information on and the number of trading days. As of day 1 we are only pulling basic fundamental data. As we look to improve the code more functions will be added as we reach 100 days.  

## Day 5 - Fundamental Analysis 
I cleaned up the code to function better in the future. If I want to ONLY call on a certain function, say fundamental analysis, I can do that. As of now we have it pulling fundamental analysis on N number of companies. It is basic, yes, but wait until we start getting funky with the technical analysis.

## Day 6 - Check Market status
The market is not open every day we shouldn't expect it to be. But what days are the market closed? Well, we can figure that out through code. For day 6 of 100 I'm going to be creating the method `get_market_status():`. 

The thought here is to pull in the current date from the `dattime` module. Use the current date and check that against the most recent day of data from the `yfinance` module. IF the current data does not equal the most recent date from `yfinance`, then the market must be closed, or the module api is down.

Let's get started by importing the `datetime` module and creating date variables that match our company data frame

```python
from datetime import date

today = date.today()
d_slash = today.strftime("%Y/%m/%d")
d_dash = today.strftime("%Y-%m-%d")

```

For the next part I'm going to jump to my python (REPEL). You can open up a REPEL window by typing `python3` into the terminal. by using REPEL it makes logic validation easier for me. I also realized that I can do the same with a jupyter notebook but I'm more comfortable at the cmd line. 

```python
from datetime import date
import yfinance as yf

today = date.today()
d_slash = today.strftime("%Y/%m/%d")
d_dash = today.strftime("%Y-%m-%d")
f_dash = '2020-12-08' # THIS IS ONE DAY AHEAD OF CURRENT DAY

roku = yf.Ticker("ROKU") # looking at roku stock
# pulling the last 365 days of roku history
# invert data to sort current date to oldest
invert_data = roku.history("365d").sort_index(axis=0, ascending=False)

market_open_check = invert_data.loc[d_dash]
mkt_check.empty

```

lets look at what I'm doing with the `market_open_check` variable. Within `pandas` there is a method you can use to access a group of rows and columns by label(s) or a boolean array. I'm only looking for the current date and I know that is the first row and column of the dataframe. we can check this by inserting `f_dash` or `d_dash`

```python

>>> invert_data.loc[f_dash]
Empty DataFrame
Columns: [Open, High, Low, Close, Volume, Dividends, Stock Splits]
Index: []

>>> invert_data.loc[d_dash]
              Open    High    Low   Close   Volume  Dividends  Stock Splits
Date                                                                       
2020-12-07  295.65  302.62  289.0  299.98  3679462          0             0
>>>
```

One dataframe is empty while the other matched the current date to the most recent row X column date in the dataframe. 

All we need to do is write some logic to catch for days when the market is closed and exit, else continue processing. 

Below is 90% of my function for getting stock data. You can see how I used logic to exit if the market is closed. This will also exit if the company has no data for the given day. Think about the companies that have merged or been acquired... will need to make a note for the future... maybe day 7 fix

```python
    def get_stocks(self):
        stock_pick = self.stock_pick # value needs to be passed into function
        self.get_market_status()
        for stock in stock_pick:
            company = yf.Ticker(stock)
            OHLC_data = company.history(period=f"{self.time_length}d") # we will be using the data var for TA
        #CHECK TO SEE IF MARKETS ARE OPEN
            invert_dataframe = OHLC_data.sort_index(axis=0, ascending=False)
            market_date_check = invert_dataframe.loc[stock_list.d_dash]
            if market_date_check.empty == True:
                print('\n!!MARKET CLOSED!!')
                print('exiting')
                exit(0)
            else:
                pass
```

# Day 7

Today I moved my code for checking the market status into its own function `get_market_status()`. I also moved it up the stack before any major processing done. This was previously within a `for loop` and that didnt make sense to process the market for each stock. 

```python
    def get_market_status(self):
        """
        Check to see if market is open
        """

        QQQ = yf.Ticker("QQQ")
        QQQ_data = QQQ.history("365d")
        invert_dataframe = QQQ_data.sort_index(axis=0, ascending=False)
        market_date_check = invert_dataframe.loc[stock_list.d_dash]
        if market_date_check.empty == True:
            print('\n!!MARKET CLOSED!!')
            print('exiting')
            exit(0)
            # Need to update code to proably target an index and not an individual stock. 
            # we can do this for day 7 of 100
        else:
            pass
```

Also added in some exception handling for companies that are no longer listed

'''Python
except Exception as e:
    print(f'\nError with {stock}\n{e}')

## EXAMPLE OF ERROR OUTPUT

Error with LVGO
name 'LVGO' is not defined
'''
