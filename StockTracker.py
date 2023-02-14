#Import libraries and packages and set display settings
import nasdaqdatalink
nasdaqdatalink.ApiConfig.api_key = "DvTefYf51gvtS51sk33E"
import pandas as pd
import datetime
import math
import numpy as np
from openpyxl import load_workbook
pd.options.display.max_columns = 999
pd.options.display.max_rows = 50
pd.set_option('display.float_format', lambda x: '%.3f' % x)

#Grab tracker tickers
tracker= "C:/Users/shelabd/OneDrive - Microsoft/Personal Stuff/Personal Files/Personal Projects/StockTracker.xlsx"

df_tracker = pd.read_excel(tracker, 'Tickers')

#Initialize dates for silcing
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=3)
oneYear = today - datetime.timedelta(days=365)
sixMths = today - datetime.timedelta(days=180)
threeMths = today - datetime.timedelta(days=90)
twoMnth = today - datetime.timedelta(days=60)


today = np.datetime64(today)
yesterday = np.datetime64(yesterday)
oneYear = np.datetime64(oneYear)
sixMths = np.datetime64(sixMths)
threeMths = np.datetime64(threeMths)
twoMnth = np.datetime64(twoMnth)

#Connect with SHARDAR Api and feed tickers from tracker sheet 
data = nasdaqdatalink.get_table('SHARADAR/SF1', calendardate={'gte': '2016-12-31'}, dimension=["ART","ARY"],ticker=df_tracker['Name'], paginate=True)
data2 = nasdaqdatalink.get_table('SHARADAR/SEP', date=yesterday, ticker=df_tracker['Name'], paginate=True)
data3 = nasdaqdatalink.get_table('SHARADAR/SF2', filingdate={'gte': '2019-12-31'},ticker=df_tracker['Name'], paginate=True)
data4 = nasdaqdatalink.get_table('SHARADAR/TICKERS', lastupdated={'gte': '2020-12-31'}, paginate=True)
df = pd.DataFrame(data)
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame(data3)
df4= data4
