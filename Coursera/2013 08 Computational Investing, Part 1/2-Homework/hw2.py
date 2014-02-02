import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da

import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import copy
import QSTK.qstkstudy.Events as ev
import QSTK.qstkstudy.EventProfiler as ep


def find_events(ls_symbols, d_data):
    ''' Finding the event dataframe '''
    df_close = d_data['actual_close']
    ts_market = df_close['SPY']

    # Creating an empty dataframe
    df_events = copy.deepcopy(df_close)
    df_events = df_events * np.NAN

    # Time stamps for the event range
    ldt_timestamps = df_close.index

    for s_sym in ls_symbols:
        for i in range(1, len(ldt_timestamps)):
            # Calculating the returns for this timestamp
            f_symprice_today     = df_close[s_sym].ix[ldt_timestamps[i]]
            f_symprice_yest      = df_close[s_sym].ix[ldt_timestamps[i - 1]]
            f_marketprice_today  = ts_market.ix[ldt_timestamps[i]]
            f_marketprice_yest   = ts_market.ix[ldt_timestamps[i - 1]]
            f_symreturn_today    = (f_symprice_today / f_symprice_yest) - 1
            f_marketreturn_today = (f_marketprice_today / f_marketprice_yest) - 1

            if f_symprice_today < 10.0 and f_symprice_yest >= 10.0:
                df_events[s_sym].ix[ldt_timestamps[i]] = 1

    return df_events


if __name__ == '__main__':
    dt_start = dt.datetime(year=2008, month=1, day=1)
    dt_end = dt.datetime(year=2009, month=12, day=31)
    print "from", dt_start, 'to', dt_end

    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt.timedelta(hours=16))
    dataobj = da.DataAccess('Yahoo')
    ls_symbols = dataobj.get_symbols_from_list("sp5002012")
    ls_symbols.append('SPY')

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

    print "Finding Events"
    df_events = find_events(ls_symbols, d_data)

    print "Creating Study"
    ep.eventprofiler(df_events, d_data,
                     i_lookback=20,
                     i_lookforward=20,
                     s_filename='MyEventStudy_SP500_10.0_2008_2009.pdf',
                     b_market_neutral=True,
                     b_errorbars=True,
                     s_market_sym='SPY')

    print "Done!"