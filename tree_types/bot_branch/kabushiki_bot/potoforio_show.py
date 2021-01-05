#! /usr/local/Cellar/python/3.7.4/bin/python3
import pandas as pd
import csv
import os
import yfinance as yf
import numpy as np
import subprocess
import math
import gspread
from os import system

# This script will be used to follow, update, and show my investing progress throughout the year(s) to come. 
### HOW DOES IT WORK ###
# Pull in .csv file which has stock picks

etrade_portfolio = 'etradeport'
etrade_csv = 'etrade.csv'
robin_csv = 'robinreport.csv'
robinhood_portfolio = 'robinport'

gc = gspread.service_account()
sh = gc.open(etrade_portfolio)
df = pd.DataFrame(sh.sheet1.get_all_records())
# df = pd.read_csv("/Users/MisterFili/Desktop/STOINKS/robin_folio.csv")
symbol_set = df['Symbol'] #assigning Symbol column to var
# df['sector'] = np.nan #creating column called 'sector' and storing 'NaN' as place holder value. 
# df['PS_TTM'] = np.nan
# df = df['gains'] = df['Quantity'] - df['total_gain%']

def get_mkt_cap(n):
    millnames = ['',' Thousand','M','B','T']
    n = float(n)
    millidx = max(0,min(len(millnames)-1,
                        int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))
    return '{:.2f}{}'.format(n / 10**(3 * millidx), millnames[millidx])

def get_close(stock):
    try:
        df = stock.history(period=f"5d")
        close_price = df['Close'].iloc[-1]    
    except IndexError as err:
        s_name = '*'
        print(err)
    return close_price

def get_all_stocks():
    pass

def get_portfolio():
    pass

for symbol in symbol_set:
    try:
        company = yf.Ticker(f'{symbol}')
        sector = company.info['sector']
        symbol = company.info['symbol']
        priceToSalesTrailing12Months = company.info["priceToSalesTrailing12Months"]
        shortName = company.get_info()['shortName']
        fiftyTwoWeekLow = company.info["fiftyTwoWeekLow"]
        fiftyTwoWeekHigh = company.info["fiftyTwoWeekHigh"]
        fiftyDayAverage = company.info["fiftyDayAverage"]
        twoHundredDayAverage = company.info["twoHundredDayAverage"]
        
        marketCap = float(company.info['marketCap'])
        market_cap = get_mkt_cap(marketCap)

        PS_TTM = round(priceToSalesTrailing12Months, 2)
        _50d_ma = round(fiftyDayAverage, 2)
        _200d_ma = round(twoHundredDayAverage, 2)
        # previousClose = company.info['previousClose']
        market_close = get_close(company)
        #### Assignments take place
        # df.loc[df['Symbol'] == f'{symbol}', 'sector'] = f'{sector}' # not necessary right now
        df.loc[df['Symbol'] == f'{symbol}', 'PS_TTM'] = f'{PS_TTM}'
        # df.loc[df['Symbol'] == f'{symbol}', '200d_ma'] = f'{_200d_ma}' # not necessary right now
        df.loc[df['Symbol'] == f'{symbol}', '50d_ma'] = f'{_50d_ma}'
        df.loc[df['Symbol'] == f'{symbol}', 'market_close'] = f'{market_close}'
        df.loc[df['Symbol'] == f'{symbol}', 'market_cap'] = f'{market_cap}'

    except KeyError as err:
        sector = 'N/A'
        symbol = company.info['symbol']
        print(f'{symbol} sector not found {sector}')
    except TypeError as err:
        print(f'{symbol} showing {err}')
    except IndexError as err:
        print(f'{symbol} showing {err}')
try:
    df['market_close'] = pd.to_numeric(df['market_close']) #convert to numeric value
    df['purchase_price'] = pd.to_numeric(df['purchase_price']) #convert to numeric value
    df['50d_ma'] = pd.to_numeric(df['50d_ma']) #convert to numeric value
    df['total_gain%'] = pd.to_numeric(df['total_gain%']) #convert to numeric value
    df['total_gain%'] = ((df['market_close'] - df['purchase_price']) / df['purchase_price'] * 100 ).round(2)
    df['above_50dma'] = np.where((df['market_close'] > df['50d_ma']), True, False)
except KeyError as err:
    print(f'error {KeyError}')
print(df)
#save results to file
etrade_csv
df.to_csv(etrade_csv, index=False)
# df.to_csv(robin_csv, index=False)

def push_csv():
    while True:
        try:  
            gistfile = "robinhoodtracker"
            ## command to run - storing fo##
            list_cmd = f"gist list | grep \"{gistfile}\""
            cmd_results = subprocess.check_output(list_cmd, shell=True, stderr=subprocess.PIPE)
            #subprocess is/was storing the results of the cmd as a byte object
            #needed to decode the byte object to a string 
            glist = cmd_results.decode('utf-8')
            print(f"\nStoring:\n{glist} as var for later use\n")
            print(f"\nDELETING... {glist}")
            del_glist = ("gist delete %s" % glist)
            subprocess.run(del_glist, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, close_fds=True)
            break
        except subprocess.CalledProcessError as e:
            print(f"\n...cmd {list_cmd} is invalid. \nReview word(s) after grep command \n")
            print("you may also need to check the connection to github")
            e.args
            break

    print(f"creating gist with name \"{gistfile}\"")
    ######## RENAME DESKTOP FILE TO REUSEABLE VAR
    create_cmd = f"gist create --public \"{gistfile}\" /Users/MisterFili/Desktop/robinreport.csv"
    subprocess.check_output(create_cmd, shell=True, stderr=subprocess.PIPE)
    new_gist = subprocess.check_output(list_cmd, shell=True, stderr=subprocess.PIPE)
    new_gist_decoded = new_gist.decode('utf-8')
    print(f"\nNew Gist Name and ID:\n{new_gist_decoded}")
    print(f"\nView the gist here: https://gist.github.com/engineertree5")

# push_csv()
#push file to github / back to google_sheets