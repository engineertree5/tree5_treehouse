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
import finplot as fplt 
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
        fplt.candlestick_ochl(df[['Open','Close','High','Low']])
        ax = fplt.create_plot(company_symbol, rows=1)

        # plot candle sticks
        candles = df[['Open','Close','High','Low']]
        fplt.candlestick_ochl(candles, ax=ax)

        # # overlay volume on the top plot
        volumes = df[['Open','Close','Volume']]
        fplt.volume_ocv(volumes, ax=ax.overlay())

        #     # put an MA on the close price
        fplt.plot(df['Close'].rolling(25).mean(), legend='ma-25')

        # place some buy markers on low wicks
        lo_wicks = df[['Open','Close']].T.min() - df['Low']
        df.loc[(lo_wicks>lo_wicks.quantile(0.99)), 'marker'] = df['Low']
        fplt.plot(df['marker'], ax=ax, color='#4a5', style='^', width=3, legend='BUY')

        # draw some random crap on our second plot
        # fplt.plot(df['time'], np.random.normal(size=len(df)), ax=ax2, color='#927', legend='stuff')
        # fplt.set_y_range(-1.4, +3.7, ax=ax2) # hard-code y-axis range limitation

        # restore view (X-position and zoom) if we ever run this example again
        # fplt.autoviewrestore()

        # we're done
        fplt.timer_callback(self.save, 0.5, single_shot=True) # wait some until we're rendered
        # fplt.show()
    def save(self):
        # import io
        # f = io.BytesIO()
        # fplt.screenshot(f)
        fplt.screenshot(open('screenshot.png', 'wb'))

def main():
#### TESTING SECTION ####
    my_stocks = ['SHOP'] #Simple watchlist 
    f_analysis = stock_list(my_stocks, 365) #we instantiate the stock_list class, passing in mystocks and a set time frame
    f_analysis.get_stocks()
main()