#!/usr/local/bin/python3
import csv
import datetime as dt
import yfinance as yf # used to pull stock data, thanks yahoo
import matplotlib.pyplot as plt # used for ploting and charting
import pandas as pd # used to handle large datasets from stock market
import pandas_datareader.data as web # used to pull in data from the web
import csv # creating, updating modifying csv files
import matplotlib.dates as mdates
from datetime import date
from IPython.core.pylabtools import figsize
from matplotlib import style
from mpl_finance import candlestick_ohlc
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
    chart_dir = '/Users/MisterFili/Documents/misc_files/'
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

    def get_stocks(self):
        self.get_market_status() # check market status
        time_length = self.time_length
        stock_pick = self.stock_pick
        for stock in stock_pick:
            # try:
            company = yf.Ticker(stock)
                # self.get_fa(company)
            self.get_ta(company,time_length)
            # except Exception as e:
            #     print(f'\nError with {stock}\n{e}')
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
            print(f'{LVGO} has no company info\n ERROR: {err}')
        
    def get_ta(self, company, time_length):
        """
        Method for performing technical analysis on given companies.
        Values needed are the company & time length of market data.
        """
        self.company = company
        self.time_length = time_length
        today = stock_list.today
        end = dt.datetime(today.year, today.month,today.day)
        start = dt.datetime(today.year -1, today.month,today.day)

        short_name = company.get_info()['shortName']
        company_symbol = company.get_info()['symbol']
        # df = web.DataReader(f'{company_symbol}', 'yahoo', start=start, end=end)
        # df.to_csv(f'{company_symbol}.csv')
        df = pd.read_csv(f'{company_symbol}.csv', parse_dates=True, index_col=0)
        
        df['10d_SMA'] = df.Close.rolling(window=10).mean()
        df['200d_EMA'] = df.Close.ewm(span=200,min_periods=0,adjust=False,ignore_na=False).mean()
        df['50d_EMA'] = df.Close.ewm(span=50,min_periods=0,adjust=False,ignore_na=False).mean()     
        df['20d_EMA'] = df.Close.ewm(span=20,min_periods=0,adjust=False,ignore_na=False).mean()
        df['26d_EMA'] = df.Close.ewm(span=26,min_periods=0,adjust=False,ignore_na=False).mean()          
        df['21d_EMA'] = df.Close.ewm(span=21,min_periods=0,adjust=False,ignore_na=False).mean()     
        df['12d_EMA'] = df.Close.ewm(span=12,min_periods=0,adjust=False,ignore_na=False).mean()   

        #calculate the MCAD
        df['mcad'] = df['12d_EMA'] - df['26d_EMA']
        df['macdsignal'] = df['mcad'].ewm(span=9, adjust=False).mean()

        #Pull in volume from dataframe
        df_volume = df['Volume'].resample('10D').sum()

        df_ohlc = df['Adj Close'].resample('W-Fri').ohlc()
        df_ohlc.reset_index(inplace=True)
        # don't want date to be an index anymore, reset_index
        # dates is just a regular column. Next, we convert it
        df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

        ax1 = plt.subplot2grid((6,1), (0,0), rowspan=4, colspan=1, title=f"${company_symbol}")
        # ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1, title="MACD")
        candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g', alpha=0.7)
        
        # ax2.plot(df.index, df[['macdsignal']], label='Signal')
        # ax2.plot(df.index, df[['mcad']], label='MCAD')
        ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1, label='Volume')
        ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)
        ax1.plot(df.index, df[['21d_EMA']], label='21d_EMA')
        ax1.plot(df.index, df[['50d_EMA']], label='50d_EMA')
        ax1.plot(df.index, df[['200d_EMA']], label='200d_EMA')
        ax1.xaxis_date() # converts the axis from the raw mdate numbers to dates.
        ax1.legend()
        ax2.legend()
        plt.savefig(f'{stock_list.chart_dir}{company_symbol}.png', bbox_inches='tight')
        plt.show()
    def create_ta_charts(self):
        pass

def main():
#### TESTING SECTION ####
    my_stocks = ['SHOP'] #Simple watchlist 
    f_analysis = stock_list(my_stocks, 365) #we instantiate the stock_list class, passing in mystocks and a set time frame
    f_analysis.get_stocks()
main()