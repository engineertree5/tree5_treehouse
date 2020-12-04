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
        """All stocks must have a $STOCK_PICK and time_length (# of Days)
        """
        self.stock_pick = stock_pick #creates an attribute called stock and is assigned to value of stock
        self.time_length = time_length #creates an attribute called time_length and is assigned to value of time_length

    def set_time(self):
        #The SELF parameter is a reference to the current instance of the class
        #and is used to access variables that belong to the class.
        # we will be using the stock the stock attribute to get more data
        pass

    def get_stocks(self):
        """
        Method for pulling in standard company data. 
        Method can process N number of stocks for analysis
        """
        stock_pick = self.stock_pick
        for stock in stock_pick:
            company = yf.Ticker(stock)
            data = company.history(period=f"{self.time_length}d")
            PS_TTM = company.info["priceToSalesTrailing12Months"]
            FF2_wkL = company.info["fiftyTwoWeekLow"]
            FF2_wkH = company.info["fiftyTwoWeekHigh"]
            FFd_ma = company.info["fiftyDayAverage"]
            THd_ma = company.info["twoHundredDayAverage"]
            try:
                s_name = company.get_info()['shortName']
                print(f'\nPulling data for {s_name}\n***********\n')
                print(f'{s_name}')
                print(f'Sector: {company.info["sector"]}')
                print(f'Industry: {company.info["industry"]}')
                print('PS/TTM:', ('${:,.2f}'.format(PS_TTM)))
                print('52 week low:', ('${:,.2f}'.format(FF2_wkL)))
                print('52 wk high:', ('${:,.2f}'.format(FF2_wkH)))
                print('50d MA:', ('${:,.2f}'.format(FFd_ma)))
                print('200d MA:', ('${:,.2f}'.format(THd_ma)))
            except IndexError as err:
                s_name = '*'
                print(err)
        return FFd_ma

    def get_market_status():

        pass
    def get_fa():
        pass
    def get_ta():
        pass
    def create_ta_charts():
        pass


#### TESTING SECTION ####
my_stocks = ['SHOP', 'NET', 'TDOC']
sample = pyetf(my_stocks, 365)
print(sample.get_stocks())