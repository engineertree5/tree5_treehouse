# What Did You Learn Last Week

# 6/20 - Creating Dictionaries + Adding key,values
<center>
<b>THE PROBLEM</b>
</center>

I was looking to improve my current tweet format. I was able to pull out the stock symbol from the `yfinance` api but to be more explicit as to what company I'm analyzing, lets add the company name. To do this I knew the best way was to create a dict.  

<figure>
    <img src="media/img/lastweek/dic620.png" alt="pystock" title="pystock">
</figure>

The first thing you will ALWAYS need to do when you are looking to store objects in a list or dict is initialize the dict if you do not already have one. 

```python
pick_info = {}
pick_info['symbols'] = {}

##### 
REPL OUTPUT: {'symbols': {}}
```
I took the time to doodle my dict on some paper so I knew it was going to be a nested dict. This way `symbols` is the parent and the stock symbols + names are the children. now to add the children to this dict

```python
watchlist = ['MSFT', 'V', 'DLR', 'CONE']
for stock_pick in stock_list:
    company_symbol = yf.Ticker(f'{stock_pick}')
    data = company_symbol.history(period=f"{days}d")
    try:
        s_name = company_symbol.get_info()['shortName']
    except IndexError as err:
        s_name = '*'
        print(err)
    pick_info['symbols'][stock_pick] = s_name

```
<b>ErrorHandling</b> 

I needed error handling due to the fact that all stock api's are not made equal. the `get_info()['shortName']` method would throw an `IndexError` each time I would make a call against a stock where the attribute `shortName` was not available. So, putting the method call into a try except block would let my program still run if/when a stock shortName is not available.

After the try catch block is where we are updating the dict `pick_info['symbols'][stock_pick] = s_name` This is how you update a dict. We did this after we first initialized by adding `symbols`. Now we are dynamically creating a list each time the for-loop is executed. If our list of stock grows so will our dict without having to make updates.

# 6/28 - Candlesticks w/ Yahoo,Matplotlib,Pandas
Before I jump off into the deep end of what I learned about candlesticks. I'm going to give you a general idea of how candlesticks are used and the different types of candlesticks you will see in a chart. 

What are candlesticks? 
Candlesticks are a representation of a stocks **Open High Low and Close** price for a given period (month, day, hour etc). Depending on the type of day the stock had the candle size will reflect that. Before we go any further, lets get some basic terminology down so we are all speaking the same language. . 

<figure>
    <img src="media/img/WDYLLW/IMG_0010.JPG" alt="c-sticks" title="c-sticks">
</figure>

<center>
<b>Real Body</b>
</center>
The real body is almost self-explanatory. The real body is the wide part of the candlestick body. The body is usually filled in with a shade of green or red. The color (green or red) lets you know if the stock closing price was Higher or Lower than the stock opening. 

<figure>
    <img src="media/img/WDYLLW/IMG_0009.JPG" alt="REALBODY" title="REALBODY">
</figure>

<center>
<b>Wicks</b>
</center>

I'm sure you've noticed the skinny whiskers coming out the top and bottom of the candlesticks. Those are called "shadows" or "wicks". I call them wicks because we are talking about candlesticks, ah duh. But the wicks highlight the fluctuation of price relative to the open and close.

<figure>
    <img src="media/img/WDYLLW/IMG_0011.JPG" alt="wicks" title="Wicks">
</figure>

<center>
<b>Doji</b>
</center>

Lastly, when you have a day when the stock opens up flat - little to no change from the opening and close price. A doji is born. Doji's appear when the stock `open` price is almost identical to the `close` price. This means that traders (buyers and sellers) are indecisive on trading the stock. In Japanese, "doji" means blunder or mistake, referring to the rarity of having the open and close price be exactly the same.

<figure>
    <img src="media/img/WDYLLW/IMG_0013.JPG" alt="doji" title="blunder">
</figure>

<center>
<b>Candlesticks</b>
</center>

Now that we have the basics of a candlestick lets drop into the code and understand how we went from a single line chart to ploting candlesticks. 

Due to the lifecycle of software these modules may be obslete, out-of-date, or the name has changed. So, if you are following along and something is not present give it a google and see if there were updates made since the posting of this 7-01-2020. Anyway, The module we will be working with is the `mpl_finance`. This module will help us transfrom our data and present this in a open, high, low close(OHLC) candlestick chart. 

To get started we can just copy the below lines of code to jump start our progress. What we are doing is importing the basic libraries that are necessary for our program to run. You should be able to deciphyer where and why we are using these libraries. I've added comments in the section below to share more light into why this code is doing what its doing. 


```python
import matplotlib.pyplot as plt
import csv
from random import sample
from matplotlib import style
import datetime as dt
from mpl_finance import candlestick_ohlc
import pandas as pd
import pandas_datareader.data as web
import matplotlib.dates as mdates
from IPython.core.pylabtools import figsize

watchlist = ['MSFT', 'V', 'DLR', 'CONE', 'PING', 'AMD', 'O', 'BAM', 'DDOG', 'ADBE', 'NKE', 'CHWY', 'NOK', 'BIP', 'O', 'DOCU', 'QCOM', 'BABA', 'DIS', 'ZS', 'NVDA', 'CCI', 'AMT', 'RTX']

figsize(14, 7) # creates an inch-by-inch image
style.use('ggplot') # ggplot is a data visualization pkg
stock_list = sample(watchlist, 4) # pick a random 4 stocks from watchlist
print(f'random stock pick from watchlist ${stock_list}')
chart_dir = '/home/pi/Documents/automation/awtybot/' # Directory for saving failes
#set current date & 1 year from now
today = dt.datetime.now().date()
end = dt.datetime(today.year, today.month,today.day)
start = dt.datetime(today.year -1, today.month,today.day)
```

If you run the above snippet in a terminal you should not encount any errors IF you have all the necessary modules installed. However, if you did not change the variable `chart_dir` you will need to do so.

Next up, chart creation! For this we will be stepping into our for-loop to complete ALL actions per stock symbol from our watchlist. Make note of the indentation. The first action is to download historical data for the stock(s) that are picked. We use your `pandas_datareader` module to vist yahoo to download stock data from current date = `start`, to one year ago = `end`. we then read the csv file into a [DataFrame](https://pandas.pydata.org/pandas-docs/stable/getting_started/dsintro.html#dataframe). 

Now that we have our stock data stored into a dataframe we can use `pandas` built-in functions to apply some analysis to our graphs. 
```python

for stock_pick in stock_list:
    df = web.DataReader(f'{stock_pick}', 'yahoo', start=start, end=end)
    df.to_csv(f'{stock_pick}.csv')
    df = pd.read_csv(f'{stock_pick}.csv', parse_dates=True, index_col=0)
    #  If True -> try parsing the index. dates are stored @ column 0
    
    df['200d_EMA'] = df.Close.ewm(span=200,min_periods=0,adjust=False,ignore_na=False).mean()
    df['50d_EMA'] = df.Close.ewm(span=50,min_periods=0,adjust=False,ignore_na=False).mean()     
    df['20d_EMA'] = df.Close.ewm(span=20,min_periods=0,adjust=False,ignore_na=False).mean()  

```
I'm looking to chart the expoential moving average for the short(20) mid(50) and longterm(100) for each stock picked. After I've defined the EMA it is on to setting up my candlesticks. Because I pulled a years worth of data I'm looking to present that as a weekly candlestick vs daily (52 vs 365). As you continue to use Pandas you begin to learn that it does a lot of heavy lifting for you. such as converting data into Open High Low Close candlesticks! All you trule need to do is select the coloum which you want to create your candlesicks after. Then using the `.resample()` method, pick a timeframe to resample your data (Quarterly, montly, weekly, daily). Then all you have to do is use the `.ohlc()` method to transform that information into pretty candlesticks

Beca

```python
    df_ohlc = df['Adj Close'].resample('W-Fri').ohlc() #This will give you ohlc data for the week ending on a Friday.
    df_volume = df['Volume'].resample('W-Fri').sum()
```

However, there is more work to do before we can get those pretty candles printed on a graph. Because we are going to be using Matplotlib to graph the columns, we do not need the date to be an index anymore. We can remove that by using the `reset_index()` method.

> Pandas reset_index() is a method to reset index of a Data Frame. reset_index() method sets a list of integer ranging from 0 to length of data as index.

**Before**

```
                open      high       low     close
Date                                              
2019-07-05  9.586670  9.586670  9.309369  9.309369
2019-07-12  9.319273  9.527248  9.319273  9.527248
2019-07-19  9.527248  9.527248  8.457662  8.764673
2019-07-26  8.705251  8.913226  8.586408  8.913226
2019-08-02  8.903322  8.903322  8.556698  8.556698
```

**After** 

```
        Date      open      high       low     close
0 2019-07-05  9.586670  9.586670  9.309369  9.309369
1 2019-07-12  9.319273  9.527248  9.319273  9.527248
2 2019-07-19  9.527248  9.527248  8.457662  8.764673
3 2019-07-26  8.705251  8.913226  8.586408  8.913226
4 2019-08-02  8.903322  8.903322  8.556698  8.556698
```
due to the "interesting" nature of candlesticks with matplotlib we will need to perfom some date conversion. For that we are using `mdates`. As for everything else, its setting up the chart.  

```python
    df_ohlc.reset_index(inplace=True)
    df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

    ax1 = plt.subplot2grid((6,1), (0,0), rowspan=4, colspan=1, title=f"${stock_pick} STOCK")
    ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1, label='Volume')

    candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')
    ax1.plot(df.index, df[['200d_EMA']], label='200d_EMA')
    ax1.plot(df.index, df[['50d_EMA']], label='50d_EMA')
    ax1.plot(df.index, df[['20d_EMA']], label='20d_EMA')
    ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0) #x and y 
    ax1.xaxis_date()
    ax1.legend()

    plt.savefig(f'{chart_dir}{stock_pick}.png', bbox_inches='tight')
    print(chart_dir)
```