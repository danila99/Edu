import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.DataAccess as da
import datetime as dt
import csv
import pandas as pd
import numpy as np


orders_fname = "orders.csv"
price_drop = 6.0

def find_events(ls_symbols, d_data):
    df_close = d_data['actual_close']
    close_index = df_close.index
    timestamps = close_index

    with open(orders_fname, "wb") as file:
        writer = csv.writer(file, delimiter=",")
        for i in range(1, len(timestamps)):
            for symbol in ls_symbols:
                if df_close[symbol].ix[timestamps[i]] < price_drop and df_close[symbol].ix[timestamps[i - 1]] >= price_drop:
                    print "found event for:", symbol, "on:", timestamps[i]
                    buy_date = timestamps[i]
                    sell_date = timestamps[i + 5] if len(timestamps) > i + 4 else timestamps[-1]
                    writer.writerow([buy_date.year, buy_date.month, buy_date.day, symbol, 'Buy', '100'])
                    writer.writerow([sell_date.year, sell_date.month, sell_date.day, symbol, 'Sell', '100'])


dt_start = dt.datetime(year=2008, month=1, day=1)
dt_end = dt.datetime(year=2009, month=12, day=31)
print "from", dt_start, 'to', dt_end

ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt.timedelta(hours=16))
dataobj = da.DataAccess('Yahoo')
ls_symbols = dataobj.get_symbols_from_list("sp5002012")
print 'total symbols:', ls_symbols

print 'getting data...'
ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
ldf_data = dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
d_data = dict(zip(ls_keys, ldf_data))

print 'filling n/a with 1.0...'
for s_key in ls_keys:
    d_data[s_key] = d_data[s_key].fillna(method='ffill')
    d_data[s_key] = d_data[s_key].fillna(method='bfill')
    d_data[s_key] = d_data[s_key].fillna(1.0)

print "finding Events"
find_events(ls_symbols, d_data)

print "orders put to:", orders_fname
print "done."