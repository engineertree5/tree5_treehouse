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

class stock_list(object):
    """
    stock_list class is used to pull & chart company financial data.
    Initinatializing requires the following 2 arguments
    stock_list("COMPANY_NAME", "DAYS")
    """
    # GLOBAL VARS
    today = date.today()
    d_slash = today.strftime("%Y/%m/%d")
    d_dash = today.strftime("%Y-%m-%d")
    def __init__(self, stock_pick, time_length ):
        #        #^ The first variable is the class instance in methods.  
        #        #  This is called "self" by convention, but could be any name you want.
        #^ double underscore (dunder) methods are usually special.  This one 
        #  gets called immediately after a new instance is created.
        """All stocks must have a $STOCK_PICK and time_length (# of Days)
        """
        self.stock_pick = stock_pick #creates an attribute called stock and is assigned to value of stock
        self.time_length = time_length #creates an attribute called time_length and is assigned to value of time_length

    def get_market_status(self):
        pass
        #The SELF parameter is a reference to the current instance of the class
        #and is used to access variables that belong to the class.
        # we will be using the stock the stock attribute to get more data
                
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
                # Need to update code to proably target an index and not an individual stock. 
                # we can do this for day 7 of 100
            else:
                pass
            # shortname = company.get_info()['shortName']
            self.get_fa(company)
            # self.get_ta(company)
        pass
    def get_fa(self, company):
        """
        Method for processing company data and extracting 
        fundamental analysis on it. Assuming company = yf.Ticker(company) 
        """
        self.company = company
        try:
            symbol = company.info["symbol"]
            sector = company.info["sector"]
            industry = company.info["industry"]
            PS_TTM = company.info["priceToSalesTrailing12Months"]
            s_name = company.get_info()['shortName']
            _52_wkL = company.info["fiftyTwoWeekLow"]
            _52_wkH = company.info["fiftyTwoWeekHigh"]
            _50d_ma = company.info["fiftyDayAverage"]
            _200d_ma = company.info["twoHundredDayAverage"]
            print(f'\nPulling data for {s_name}\n***********')
            print(f'{s_name.upper()}')
            print(f'Sector: {sector}')
            print('PS/TTM:', ('${:,.2f}'.format(PS_TTM)))
            print('52 week low:', ('${:,.2f}'.format(_52_wkL)))
            print('52 wk high:', ('${:,.2f}'.format(_52_wkH)))
            print('50d MA:', ('${:,.2f}'.format(_50d_ma)))
            print('200d MA:', ('${:,.2f}'.format(_200d_ma)))
        except IndexError as err:
            s_name = '*'
            print(err)
        
    def get_ta(self, OHLC_data):
        self.OHLC_data = daOHLC_datata
        pass
    def create_ta_charts(self):
        pass

def main():
#### TESTING SECTION ####
    my_stocks = ['SHOP', 'NET', 'AMD'] #Simple watchlist 
    f_analysis = stock_list(my_stocks, 365) #we instantiate the stock_list class, passing in mystocks and a set time frame
    f_analysis.get_stocks()
main()