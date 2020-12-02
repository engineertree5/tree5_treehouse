#!/usr/local/bin/python3

import datetime as dt
import yfinance as yf # used to pull stock data, thanks yahoo
import matplotlib.pyplot as plt # used for ploting and charting
import pandas as pd # used to handle large datasets from stock market
import pandas_datareader.data as web # used to pull in data from the web
import csv # creating, updating modifying csv files
import matplotlib.dates as mdates
from datetime import date

###### SCRIPT SUMMARY ######
# Purpose of this class(user-defined data structure)
# is to use the yfinance module and pandas_datareader.data
# to pull in company data programmatically.
# Store the company data in memory or .csv file 
# and begin to performn technical and fundamental analysis
###### SCRIPT SUMMARY ######

# GLOBAL VARS
today = date.today()
d_slash = today.strftime("%Y/%m/%d")
d_dash = today.strftime("%Y-%m-%d")


class pyetf(object):
    """
    pytef class is used to pull & chart company financial data.
    Initinatializing requires the following 2 arguments
    pytef("COMPANY_NAME", "DAYS")
    """
    def __init__(self, stock_pick, time_length ):
        """All stocks must have a $STOCK_PICK and time_length (# of Days) var for input
        """
        self.stock_pick = stock_pick #creates an attribute called stock and is assigned to value of stock
        self.time_length = time_length

    def set_time(self):
                #The SELF parameter is a reference to the current instance of the class
        #and is used to access variables that belong to the class.
        # we will be using the stock the stock attribute to get more data
        today = dt.datetime.now().date()
        end = dt.datetime(today.year, today.month,today.day)
        start = dt.datetime(today.year -1, today.month,today.day)
        d_dash = today.strftime("%Y-%m-%d")
        return today, end, start, d_dash

    def get_stocks(self): 

        today, end, start, d_dash = self.set_time()
        stock_pick = self.stock_pick
        for stock in stock_pick:
            company = yf.Ticker(stock)
            print(f'pulling data for {stock}\nSector:{company.info["sector"]}\n')
            df = web.DataReader(f'{stock}', 'yahoo', start=start, end=end)
            return df
    
# get_picks() - get_market_status() - get_ta() - create_ta_charts() - get_fa()
my_list = ['SMLR', 'NET', 'B']
sample = pyetf(my_list, 365)
print(sample.get_stocks())