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

</center>
<b>Wicks</b>
</center>

I'm sure you've noticed the skinny whiskers coming out the top and bottom of the candlesticks. Those are called "shadows" or "wicks". I call them wicks because we are talking about candlesticks, ah duh. But the wicks highlight the fluctuation of price relative to the open and close.

<figure>
    <img src="media/img/WDYLLW/IMG_0011.JPG" alt="wicks" title="Wicks">
</figure>

</center>
<b>Doji</b>
</center>

Lastly, when you have a day when the stock opens up flat - little to no change from the opening and close price. A doji is born. Doji's appear when the stock `open` price is almost identical to the `close` price. This means that traders (buyers and sellers) are indecisive on trading the stock. In Japanese, "doji" means blunder or mistake, referring to the rarity of having the open and close price be exactly the same.

<figure>
    <img src="media/img/WDYLLW/IMG_0013.JPG" alt="doji" title="blunder">
</figure>
