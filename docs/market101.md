# VIEW MARKET DATA WITH PYTHON
<figure>
    <img src="media/img/pystock.jpg" alt="pystock" title="pystock">
</figure>
Jumping right in. I'll be going to go over how we can programatically pull stock market data by using python. There are a number of things you can do with this data such as dig into the financials of your favorite company, create a mock portfolio or show staticts from a specific industry. You can do anything you anything your mind can imagine.

?> Assuming you've already know the basics of using python

## System Setup

There are a number of api's avaiable (free & paid) to pull stock market data. I'm not looking to build an app (not yet at least) so my default is to go with all things free when possible. The free api (python module) we will be using is `yfinance`. This python module will give us a breadth of information pulled directly from the stock market, which comes directly from yahoo hence the module name. 

You probably do not have this module installed so go ahead and run `pip3 install yfinance`. 

> pip3 is for python3. Depending on your environment you may need to run pip instead of pip3

## Pulling Market Data 101

```python
import yfinance as yf

#Pick a familiar stock ticker
stock = yf.Ticker('MSFT')
stock_data = stock.history('5d')
print(stock_data)
```

We will need create an instance of yfinance [`stock = yf.Ticker('MSFT')`]and pass in a string. That string will need to be a stock ticker that is a publicly traded company.

Because we already created our instance of yfinance and assigned it to the stock varialbe. We can now use that instance to look at stock history. Lets check the stock performance of the last 5 trading days. 

```

                  Open        High         Low       Close    Volume  Dividends  Stock Splits
Date                                                                                         
2021-12-17  320.880005  324.920013  317.250000  323.799988  47750300          0             0
2021-12-20  320.049988  322.799988  317.570007  319.910004  28326500          0             0
2021-12-21  323.290009  327.730011  319.799988  327.290009  24740600          0             0
2021-12-22  328.299988  333.609985  325.750000  333.200012  24831500          0             0
2021-12-23  332.750000  336.390015  332.730011  334.690002  19611200          0             0

```

Yup! There you have it. It's that easy to get up and running with looking at market data using python. I'll be sharing other ways to use yfinance to create small projects that can help us better understand python and finance. Take some time and familiarize yourself with the above code and module. Think about what else can be done with this data and play around, get lost and explore. 


[UNFINISHED]