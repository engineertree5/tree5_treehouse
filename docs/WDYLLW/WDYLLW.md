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
chart_dir = '/home/pi/Documents/automation/awtybot/' # Directory for saving files
#set current date & 1 year from now
today = dt.datetime.now().date()
end = dt.datetime(today.year, today.month,today.day)
start = dt.datetime(today.year -1, today.month,today.day)
```

If you run the above snippet in a terminal you should not encounter any errors IF you have all the necessary modules installed. However, if you did not change the variable `chart_dir` you will need to do so.

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
I'm looking to chart the exponential moving average for the short(20) mid(50) and long-term(100) for each stock picked. After I've defined the EMA it is on to setting up my candlesticks. Because I pulled a years worth of data I'm looking to present that as a weekly candlestick vs daily (52 vs 365). As you continue to use Pandas you begin to learn that it does a lot of heavy lifting for you. such as converting data into Open High Low Close candlesticks! All you truly need to do is select the column which you want to create your candlesticks after. Then using the `.resample()` method, pick a time frame to re-sample your data (Quarterly, monthly, weekly, daily). Then all you have to do is use the `.ohlc()` method to transform that information into pretty candlesticks

Beca

```python
    df_ohlc = df['Adj Close'].resample('W-Fri').ohlc() #This will give you ohlc data for the week ending on a Friday.
    df_volume = df['Volume'].resample('W-Fri').sum()
```

However, there is more work to do before we can get those pretty candles printed on a graph. Because we are going to be using Matplotlib to graph the columns, we do not need the date to be an index anymore. We can remove that by using the `reset_index()` method.

> Pandas reset_index() is a method to reset index of a Data Frame. reset_index() method sets a list of integer ranging from 0 to length of data as index.
```python
    df_ohlc.reset_index(inplace=True)
```

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
due to the "interesting" nature of using the candlestick library within matplotlib we will need to perform some date conversion. For that we are using `mdates`.  

```python
    df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)
```

The rest of the code is used to setup and design our chart. Our chart requires two axises, so we assign candlesticks and EMA data to one `ax1` axis and trading volume data to `ax2` axis. I wont go into great detail as to what each line does but I will recommend that you do some due diligence and google these methods to get a better understanding of the "how" and "why" 

```python
    ax1 = plt.subplot2grid((6,1), (0,0), rowspan=4, colspan=1, title=f"${stock_pick} STOCK")
    ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1, label='Volume')

    candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')
    ax1.plot(df.index, df[['200d_EMA']], label='200d_EMA')
    ax1.plot(df.index, df[['50d_EMA']], label='50d_EMA')
    ax1.plot(df.index, df[['20d_EMA']], label='20d_EMA')
    ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0) #x and y 
    ax1.xaxis_date() # converts the axis from the raw mdate numbers to dates.
    ax1.legend()

    plt.savefig(f'{chart_dir}{stock_pick}.png', bbox_inches='tight')
```

# 7/5 - SMA & EMA
Now we jump over to indicators. Since we have our stock market data generated and we know how to pull whichever stock we want + the time frame of trading days, the only thing left is to apply some indicators. First up, **Simple Moving Average**

The SMA is one of many indicators that can help determine if an asset will either continue on its current trend or reverse into a bull or bear trend. We are starting with the SMA because it is **A.)** the formula for SMA is straight forward and **B.)** The SMA will be a building block for our indicator investing strategy.

<figure>
    <img src="media/img/WDYLLW/IMG_0033.jpg" alt="sma" title="sma">
</figure>

As you can see from the figure above. The SMA formula is only using addition and division to calculate the SMA for N periods. N being the number of days you want to chart the SMA. for example. If you wanted to get the 50 day SMA for $ADBE you would need to add the closing price (A1 + A2 + ...) for the first 50 days then divide by 50 days (N).   

<figure>
    <img src="media/img/WDYLLW/smaexample.jpg" alt="smaexample" title="smaexample">
</figure>

The SMA is a good indicator to understand and have in your toolkit. If you are interested in going further into the space of market indicators its a good idea to start with the basics. everything else going forward will not be as simple as the SMA. Also, keep in mind that the SMA is an intro level indicator and would not provide much value for the near future stock performance. You can also enhance the SMA to put more weight on the recent stock price action by using the EMA - Exponential Moving Average. 

The EMA can be used in a few different ways. Similar to the SMA you can use the EMA to create another indicator. By combining the 12 and 26-day EMA you get the moving average convergence divergence (MACD) and the percentage price oscillator (PPO). But these indicators will come later. First EMA. 

The EMA is primarily used to analyze short-term averages. You would use this indicator to confirm the market move or indicate its strength. Why? because just like the SMA the EMA is a lagging indicator. As we build up or knowledge of indicators we will be able to pull in more advanced techniques that will help us predict future price action (short & long). But lets not get ahead of ourselves let's take a look at how we calculate the EMA.  

<figure>
    <img src="media/img/WDYLLW/emaformula.png" alt="emaformula" title="emaformula">
</figure>

The EMA looks a bit complicated but if you break it down you can start to see how the formula makes sense. The EMA can be broken up into 3 parts

1. Calculate the SMA for the initial EMA values. The SMA is used as the previous periods EMA. 

2. Calculate the weighted multiplier 

3. calculate the EMA for each day between the initial EMA value and today use the price, the multiplier, and the previous periods EMA value. 

<figure>
    <img src="media/img/WDYLLW/emaformula2.png" alt="emaformula2" title="emaformula2">
</figure>

# 10/5 - Bases, Cups, & Double-Downs

Within the last 7 days a lot of new and interesting knowledge was ingested! Thanks to a *How to Make Money in Stocks*, written by William J. O'Neil. This was a book a twitter user recommended every serious investor read. After reading the first few chapters I can say that is is certainly a book that should be in everyone's study. So, what did I learn? The basics of understanding the technical analysis of stock charts. 

?> I HIGHLY recommend you have a general understanding of candle sticks before moving forward

#### History Rhymes
The way the stock market acts is like a machine with a bunch of individual companies that make up the internal parts. Every year the machine grows and new parts are swapped out with old ones, parts break, parts get upgraded etc. The thing to keep in mind is that the parts all work the same. This is how/why technical analysis work! When technical analysis is applied to any winning stock the outcome is usually the same. This is because there are know successful price patterns like `cup with handle` that have proven to work time and time again. Price patterns of the past can serve as models for future stocks.

#### Bases

Bases are like stepping stones or hiking bases for a winning stocks next move. Think of them as resting areas where the stock takes a breather before starting the next climb in its journey.  Each base is different so its important to not generalize past performance for future results.

Drawing out "what is a base" really help me drill into my brain what exactly a base is, how its formed, how long do they last, and what signals does it provide. 

<figure>
    <img src="media/img/WDYLLW/bases.png" alt="emaformula2" title="emaformula2">
</figure>

Understanding the basic lingo of a new subject is important if you want to be successful on your learning journey. **[segue]** Knowing what a base is when learning about technical analysis will help you understand what you are reading and more importantly, help you make better investment decisions. 

<center> <h2> Left Side of Base: The Sell-Off</h2> </center>
<figure>
    <img src="media/img/WDYLLW/baseleftsidesellof.png" alt="emaformula2" title="emaformula2">
</figure>

<center> <h2> Bottom of Base: A "Floor" of Support Forms as Selling Subsides</h2> </center>
<figure>
    <img src="media/img/WDYLLW/basebottom.png" alt="emaformula2" title="emaformula2">
</figure>

<center> <h2> Right Side of Base: Institutional Buying Returns</h2> </center>
<figure>
    <img src="media/img/WDYLLW/baserightside.png" alt="emaformula2" title="emaformula2">
</figure>

<center> <h2> Buy Point: Breaks Through Former "Ceiling" of Resistance</h2> </center>
<figure>
    <img src="media/img/WDYLLW/basebuypoint.png" alt="emaformula2" title="emaformula2">
</figure>

<center> <b> Key Takeaways</b> </center>

* Think of a base as an actual mountain climb. Take breaks as you make your way to the top... sometimes you have to go down the mountain to go up. 

* The base floor cannot be validated until the prior area of resistance is broken. It may be too early to tell if the bottom of the base has truly formed. Double Bottom anyone? 

* Pay close attention to the BUY volume during the breakout period. As the stock punches through the prior area of resistance the volume needs to up to help with the thesis of buying.

*Good link for reference [HERE](https://www.investors.com/ibd-university/how-to-buy/bases-overview-1/)*

#### Cup With Handle
The `cup with handle` is one of the most common price patterns to recognize. After discovering and understanding this price pattern I began to recognize it within most charts instantly! The `cup with handle` is one of the most important price patterns. The reason this pattern is so successful is because history rhymes. The quick takeaway from a technical point of view is the decline (left side of the cup) is usually 12%-35% from the high. The handle should slant lower as the remaining sellers exit the stock. 

<center> <h2> Cup With Handle</h2> </center>
<figure>
    <img src="media/img/WDYLLW/cupwithhandle.png" alt="emaformula2" title="emaformula2">
</figure>

<figure>
    <img src="media/img/WDYLLW/cupwithhan.png" alt="emaformula2" title="emaformula2">
</figure>

Again, when we are talking technicals here. Visuals will always be your best friend. And repetition is the father of learning. So transcribing my notes here further cements my learning.  


<center> <h2> Cup With Handle: $SLP Simulation Plus 2020</h2> </center>
<figure>
    <img src="media/img/WDYLLW/slpcup.png" alt="emaformula2" title="emaformula2">
</figure>

There could possibly be too much noise within the $SLP chart but lets break it down so we can turn down the noise. Lets work our way up from the bottom: 

`Volume` - Notice how the volume begins to dry up right before we see a LARGE buy signal in June. Also take note of the HUGE uptick in volume. This is usually represented by larger investors - fund managers & institutions. 

`Cup with Handle` - we start to see the cup form towards the beginning of May. The base is built out through May to the beginning of June. Then the handle is created towards mid june-ish. After that we see a huge spike in the price and $SLP is out of here!

`Buy Point` - The point appears once all your indicators are validated. Cup with handle, volume support, Relative Price Strength line trending up, Handle abve the 10-week MA, and punching through previous area of resistance. You don't want to get greedy and assume the indicator is around the corner.    
<center> <b> Key Takeaways ... There is A Lot!</b> </center>

* Cup with handle usually last for 3-6 months. Some long as 65 weeks!
* Formation of handle takes more than one or two weeks & has a downward price drift for shakeout. 
* Stocks can advanced without forming a handle. 
* Look for volume dry-ups near the lows of a price pattern
* Handle should be above the 10-week moving average line
* Big volume clues are valuable
* Find pivot points and watch "volume percent change"
* View your stock from a weekly chart 
* Volatile leaders can plunge 40%-50% in a bull market. Corrections happening more than this have a higher rate of failure. 
* When handles do occur, they almost always form in the upper half of the overall base structure. 
* Constructive patterns have tight prices
* Weak cups / Prone to failure = handles that form in the lower half of the overall base structure and/or completely below the stocks 10-week MA line. 

#### Double-Bottom
A double bottom price pattern is just that. The price will bottom out twice creating the "W" shape within the price pattern. This pattern will not occur as often as the `cup with handle` but will occur frequent enough. 

> Its important that the second bottom of the `W` match the price level of the first bottom or as in almost all cases, clearly under cut by one or two points, creating a checkout of weaker investors. 

<center> <h2> Double-Bottom</h2> </center>
<figure>
    <img src="media/img/WDYLLW/doublebottom.png" alt="emaformula2" title="emaformula2">
</figure>

<center> <b> Key Takeaways</b> </center>
* Double bottoms may also have handles, although this is not essential.
* The pivot buy point in a double-bottom is located on the top right side of the W, where the stock is coming up after the second leg down.
* If the double bottom has a handle, then the peak price of the handle determines the pivot buy point.

#### Flat-Base
Just like the `cup with handle` price pattern, the flat base must form within an existing uptrend. look for this formation after a breakout from a deep correction. 
<center> <h2>Flat Base</h2> </center>
<figure>
    <img src="media/img/WDYLLW/flatbase.png" alt="emaformula2" title="emaformula2">
</figure>

<center> <b> Key Takeaways</b> </center>

* Flat base moves straight side-ways in a fairly tight price range for at least 5 or 7 weeks. 
* No correction more than 10-15%

#### Base on Base


* The two bases can be of any type: `cup with handle`, `cup without handle`, `flat base`, and `double bottom`. the second pattern is offten the `flat base`.

* The second base should not encroach much into the price level of the first base. Any base that sinks much into the first base is not a proper base-on-base formation. 

* The proper buy point is determined by the second base. 


# 10/16 - Selection & Timing


#### Overhead Supply

Overhead supply is the additional stock that pushes the stock back down. This is represented by a stock that was once doing well, sold off X percentage and is now dropping. Because the stock has dropped so much it leaves the shareholders wanting to sell, BUT not as a loss. They'd like to break even on their investment so they wait for the stock to regain its value, then sell. This pushes the stock back down further as the stock climbs up after a dip. 

* An area of resistance where there is more supply than you think. 
* After a dip/fall in price the stock will eventually start to trend up and break its previous area of resistance. As it is trending up it will hit the `overhead supply` area. When the stock hits this area it is punched back down even further. 

#### Chapter Review - How To Make Money In Stocks

!> You absolutely do not buy breakouts during a bear market. most of them will fail!

* You can improve your stock selection and overall portfolio performance by learning to read and use charts

* You need **BOTH** Technical analysis (chart reading) and Fundamental analysis, not just one or the other.
* `Most` price patterns will not work during a bear market. Most will be defective.

# 10/18 - Look For Big Growth
#### Accelerating Quarterly Earnings

?> When looking at quarterly earnings the `percentage change in the EPS` is one of the `top elements` for selecting top tier stocks. 

When looking at quarterly earnings you want to see consistent growth for the same quarter YOY from the previous year. One of the main reasons for comparing last years quarterly results with the current results is to account for seasonal shopping, cycles, and the likes of.

<center> <h2>Accelerating Quarterly Earnings</h2> </center>
<figure>
    <img src="media/img/WDYLLW/oct20/eps.png" alt="emaformula2" title="emaformula2">
</figure>

Stocks that you select should have an accelerating percentage increase in current quarterly earnings per share when compared to the prior year's same quarter. You should also be looking at the annual growth of the company. That too should be growing at a rate of `25% and above`!

Even the best orgs can have a slow quarter every once in a while. So before selling at the first sign of a bad quarter it is good practice to wait 2 quarters to identify if there is truly a material slowdown. Usually a decline of two-thirds from the previous rate - 50% to 15%.

#### PE Ratio Is Shite

<center> <h2>You Can't Buy Oceanfront Property For the Same Price You'd Pay For Land A couple of Miles Inland</h2> </center>


?> Earnings, Sales, Return on Equity are 3 things you should look to when searching for your next 100 bagger. The market cap will more than likely need to be under 20bln as well.

# 12/08 No More Positions
Going into the month of December I did a portfolio review and came to the conclusion that I have too many positions. At the time I had around 45 postions within my portfolio. To me that was too much and I really wanted to consolidate those holdings into a more concentrated bunch. 

less is more, right? If I'm to only own stocks with super high conviction and max upside, I should be on the moon sooner than later. So I started trimming existing positions and adding to existing ones. I believe I got down to 37 which put me 2 away from my goal of 35 total positions (still my goal). 

As I started to "research" and hear and read investors discuss their stocks and new opportunities on the horizon. I got a little anxious and wanted to dip my toe in their suggested stock picks... next thing you know I'm back at 43 positions. 

As of right now, 12/08, I've made a mental mark that I can no longer add a position without having to take away an existing position. I also need to review my positions and put some companies on the chopping block... `$RDFN` `$IIPR` `FTCH` `MELI` `GRWG` If I'm being honest,  I would not sell these company's, only if i had to. I dont see any reason why I should sell these companies so I'm going to keep rocking with these until otherwise. 