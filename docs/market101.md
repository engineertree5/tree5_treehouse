# VIEW MARKET DATA WITH PYTHON
<figure>
    <img src="media/img/pystock.jpg" alt="pystock" title="pystock">
</figure>
Jumping right in. I'm going to go over how we can look at stock market data by using python. I went on and made a simple twitter bot to tweet stock analytics from my watchlist. We wont go that far in this post. This post is to give you a leg up and get you used to pulling in data on the market

## Environment Setup

There are a number of api's avaiable (free & paid) to pull stock market data. We will be using `yfinance` a free python module that will give us a breadth of information pulled from the stock market. We are also using this because its free and I avoid paying for software at all cost (this website is hosted for 'free'). That's it! 

You probably do not have this module installed so go ahead and run `pip3 install yfinance`. 

> pip3 is for python3. Depending on your environment you may need to run pip instead of pip3

## Pulling Market Data
The easiest way to follow along is to jump into the python REPL (READ, EVAL, PRINT, LOOP) so you are not having to save your .py file and having to run it. Jump over to your terminal and type `python`. Enter the REPL. 



```python
import yfinance as yf
```
If you are seting errors after the import you did not insatll yfinance. we are importing `yfinance as yf` so we can yf instead of typing yfinance each time we need to call the module

lets create an instance of yfinance. This is how we are going to "activate" the yfinance module we just downloaded. We will need a stock to look at so i'm going to load in the Microsoft using the `MSFT` stock symbol.   

```python
stock = yf.Ticker('MSFT')
```
Now that we have created an instance of the yfinance with MSFT loaded in we can look at some of the attributes avaiable to us. to do so we can use `dir()` to examine

```python
dir(stock)

```
You should get back a long list of avaiable methods we can calls. For example, lets look at history. Lets see gander at the performance of the last 5 days of the stock. 

```python
stock_data = stock.history('5d')
stock_data
```

Yup! It's quite easy to get up and running with looking at market data using python. Our next mission is to start analyzing this data so we can make market predictions. For now, get familiar with this module and do some exploaring. 