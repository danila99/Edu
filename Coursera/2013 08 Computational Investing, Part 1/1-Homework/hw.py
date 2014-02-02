import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da

import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from copy import deepcopy


def optimize(dt_start, dt_end, ls_symbols):
    allocations = [(x, y, z, t)
                   for x in range(11)
                   for y in range(11)
                   for z in range(11)
                   for t in range(11)
                   if x + y + z + t == 10]
    print 'allocations:', len(allocations)
    allocations = np.multiply(allocations, 0.1)

    results = []
    for a in allocations:
        vol, daily_ret, sharpe, cum_ret = simulate(dt_start, dt_end, ls_symbols, a)
        results.append((sharpe, a))

    s = sorted(results, key=lambda r: r[0])
    return s[-1]


def simulate(dt_start, dt_end, ls_symbols, allocations):
    absolute = abs(sum(allocations) - 1)
    if absolute**2 > 1e-14:
        print allocations, sum(allocations)
        assert absolute**2 > 1e-14

    dt_timeofday = dt.timedelta(hours=16)
    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)

    c_datable = da.DataAccess('Yahoo')
    key_list = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
    data_list = c_datable.get_data(ldt_timestamps, ls_symbols, key_list)
    d_data = dict(zip(key_list, data_list))
    df_rets = d_data['close'].copy()
    df_rets = df_rets.fillna(method='ffill')
    df_rets = df_rets.fillna(method='bfill')

    na_price = df_rets.values
    na_normalized_price = na_price / na_price[0, :]
    na_rets = na_normalized_price.copy()

    na_rets = np.multiply(allocations, na_rets)
    na_port = sum(na_rets[:,axis] for axis in range(len(allocations)))

    cum_ret = na_port[-1]
    tsu.returnize0(na_port)

    std = np.std(na_port, axis=0)
    avg = np.mean(na_port, axis=0)
    sharpie = np.sqrt(252) * avg / std

    # print 'Sharpe Ratio:', sharpie
    # print 'Volatility (stdev of daily returns):', std
    # print 'Average Daily Return:', avg
    # print 'Cumulative Return:', cum_ret

    return std, avg, sharpie, cum_ret

    # Start Date: January 1, 2011
    # End Date: December 31, 2011
    # Symbols: ['AAPL', 'GLD', 'GOOG', 'XOM']
    # Optimal Allocations: [0.4, 0.4, 0.0, 0.2]

    # Sharpe Ratio: 1.02828403099
    # Volatility (stdev of daily returns):  0.0101467067654
    # Average Daily Return:  0.000657261102001
    # Cumulative Return:  1.16487261965