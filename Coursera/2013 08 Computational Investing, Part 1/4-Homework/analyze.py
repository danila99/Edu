import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.DataAccess as da
import QSTK.qstkutil.tsutil as tsu
import sys
import csv
import numpy as np
import datetime as dt
import pandas as pd


def get_fund_performance(data):
    initial_level = float(data[0])
    last_level = float(data[-1])
    normalized_data = data / initial_level
    tsu.returnize0(normalized_data)

    std = np.std(normalized_data, axis=0)
    avg = np.mean(normalized_data, axis=0)
    sharpie = np.sqrt(252) * avg / std
    total_return = last_level / initial_level
    return sharpie, total_return, std, avg


assert len(sys.argv) > 1

portfolio_values_file = sys.argv[1]
benchmark = sys.argv[2]
print "portfolio values from:", portfolio_values_file
print "benchmark:", benchmark


print "reading portfolio file"
dates = []
with open(portfolio_values_file, 'rU') as f:
    csvdata = csv.reader(f)
    for arr in csvdata:
        dates.append(dt.datetime(year=int(arr[0]), month=int(arr[1]), day=int(arr[2]), hour=16))


print "defining the time frame"
portfolio_start_date = dates[0]
portfolio_end_date = dates[-1]
index = du.getNYSEdays(portfolio_start_date, portfolio_end_date, dt.timedelta(hours=16))
print "from:", portfolio_start_date, "to:", portfolio_end_date

print "reading benchmark close prices to DataFrame from Yahoo"
ldt_timestamps = du.getNYSEdays(portfolio_start_date, portfolio_end_date, dt.timedelta(hours=16))
c_datable = da.DataAccess('Yahoo')
key_list = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
data_list = c_datable.get_data(ldt_timestamps, [benchmark], key_list)
d_data = dict(zip(key_list, data_list))
df_rets = d_data['close'].copy()
df_rets = df_rets.fillna(method='ffill')
df_rets = df_rets.fillna(method='bfill')


print "portfolio mock up"
portfolio = pd.DataFrame(0, index, ["CASH"])
print "reading actual trades to DataFrame"
with open(portfolio_values_file, 'rU') as f:
    csvdata = csv.reader(f)
    for arr in csvdata:
        date = dt.datetime(year=int(arr[0]), month=int(arr[1]), day=int(arr[2]), hour=16)
        portfolio["CASH"][date] = float(arr[3])
portfolio[benchmark] = df_rets[benchmark]
print "portfolio initialized with cash"

sharpie_fund, total_return_fund, std_fund, avg_fund = get_fund_performance(portfolio["CASH"].copy())
sharpie_mark, total_return_mark, std_mark, avg_mark = get_fund_performance(portfolio[benchmark].copy())

print
print "Sharpe Ratio of Fund:     ", sharpie_fund
print "Sharpe Ratio of Benchmark:", sharpie_mark
print
print "Total Return of Fund:     ", total_return_fund
print "Total Return of Benchmark:", total_return_mark
print
print "Standard Deviation of Fund:     ", std_fund
print "Standard Deviation of Benchmark:", std_mark
print
print "Average Daily Return of Fund:     ", avg_fund
print "Average Daily Return of Benchmark:", avg_mark
