import streamlit as st

import pandas as pd
import numpy as np
import tpqoa
from datetime import datetime, timedelta
import time
import datetime

from SMABacktester import SMABacktester
from MeanRevBacktester import MeanRevBacktester
from MLBacktester import MLBacktester
from MultiBacktester import MultiBacktester
api = tpqoa.tpqoa("oanda.cfg")

#instr = api.get_instruments()
#for i in instr:
#    print (i[1])

#st.sidebar.image("conv_curry_logo.png", use_column_width=True)

u_ticker = st.sidebar.selectbox('Select one symbol', ('EUR_USD', 'EUR_AUD','BTC_USD','SPX500_USD', 'USD_HKD'))
today = datetime.date.today()
before = today - datetime.timedelta(days=700)
u_start = st.sidebar.date_input('Start date', before)
u_end = st.sidebar.date_input('End date', today)
if u_start < u_end:
    st.sidebar.success('Start date: `%s`\n\nEnd date:`%s`' % (u_start, u_end))
else:
    st.sidebar.error('Error: End date must fall after start date.')

st.sidebar.subheader('Strategies')
st.sidebar.write('Simple Moving Averages')
u_sma_s = st.sidebar.slider('Short SMA', value= 50)
u_sma_l = st.sidebar.slider('Long SMA', 50, 300, value= 100)
#u_sma_s = st.sidebar.slider('Short SMA', value= 50 if optimus_3 == None else optimus_3[0])
#u_sma_l = st.sidebar.slider('Long SMA', 50, 300, value= 100 if optimus_3 == None else optimus_3[1])

sma_tester = SMABacktester(u_ticker, u_sma_s, u_sma_l, u_start.isoformat(), u_end.isoformat(),0)

if st.sidebar.button('optimize'):
    optimus = sma_tester.optimize_parameters((50, 80, 1), (100, 120, 1))
    u_sma_s, u_sma_l = optimus[0]

# Main Page Plots

'''
# Analyzing our Strategy

We are using the plots and calculations of indicators to generate the best trading strategy 
or just gain good intuition for our data and our strategy.
'''
st.subheader('Strategy 1: Simple Moving Averages')
st.write('Value gain/loss over time:', round((sma_tester.test_strategy()[0]*100)-100,2),'%')
st.write("Performance compared to 'buy and hold':", round(sma_tester.test_strategy()[1]*100,2),'%')
st.write('SMA_S:', u_sma_s)
st.write('SMA_L:', u_sma_l)

st.write('Strategy Performance over Time')
st.line_chart(sma_tester.results[["creturns", "cstrategy"]])
progress_bar = st.progress(0)

st.sidebar.write('Mean Reversion Strategy')
u_sma = st.sidebar.slider('SMA', 1, 200, value= 50)
u_dev = st.sidebar.slider('Deviations', 1, 5, value= 2)
#u_sma = st.sidebar.slider('SMA', value= 50 if optimus_3 is None else optimus_3[2])
#u_dev = st.sidebar.slider('Deviations', 1, 5, value= 2 if optimus_3 is None else optimus_3[3])

mr_tester = MeanRevBacktester(u_ticker, u_sma, u_dev, u_start.isoformat(), u_end.isoformat(),0)

if st.sidebar.button('optimize '):
    optimus_2 = mr_tester.optimize_parameters((100,150), (2,5))
    u_sma, u_dev = optimus_2[0]

st.subheader('Strategy 2: Mean Reversion')
st.write('Value gain/loss over time:', round((mr_tester.test_strategy()[0]*100)-100,2),'%')
st.write("Performance compared to 'buy and hold':", round(mr_tester.test_strategy()[1]*100,2),'%')
st.write('SMA:', u_sma)
st.write('Deviations:', u_dev)

st.write('Strategy Performance over Time')
st.line_chart(mr_tester.results[["creturns", "cstrategy"]])
progress_bar = st.progress(0)

st.sidebar.write('Strategy 3: Logistic Regression')
st.sidebar.write('No paramters necessary') #possible paramters are lags

ml_tester = MLBacktester(u_ticker, u_start.isoformat(), u_end.isoformat(),0)

st.subheader('Strategy 3: Logistic Regression')
st.write('Value gain/loss over time:', round((ml_tester.test_strategy()[0]*100)-100,2),'%')
st.write("Performance compared to 'buy and hold':", round(ml_tester.test_strategy()[1]*100,2),'%')

st.write('Strategy Performance over Time')
st.line_chart(ml_tester.results[["creturns", "cstrategy"]])
progress_bar = st.progress(0)

st.sidebar.subheader('Combining Strategies')
st.sidebar.write('Select your strategies') #buttons for SMA, Bollinger, Logistic Regresison
multi_sma = st.sidebar.checkbox('SMA', value = True)
multi_mr = st.sidebar.checkbox('Mean Reversion', value = True)
multi_ml = st.sidebar.checkbox('Logistic Regression')

option = st.sidebar.radio('Select method:', ['unanimous', 'tendency'])

strat_dict = {'sma_tester': multi_sma, 'mr_tester': multi_mr, 'ml_tester': multi_ml}
strat_list = list(filter(strat_dict.get, strat_dict))

multi_tester = MultiBacktester(u_ticker, u_start.isoformat(), u_end.isoformat(),0)

if st.sidebar.button(' optimize'):
    optimus_3 = multi_tester.optimized_parameters((u_sma_s, u_sma_l, u_sma, u_dev, 1, 3))
    #optimus_3 = multi_tester.optimal_strategy((optimal_params))
    optimus_3 = list(map(round, optimus_3))
    u_sma_s, u_sma_l, u_sma, u_dev, option, strategy = optimus_3
    if option == 0:
        option = 'unanimous'
    else:
        option = 'tendency'
    strat_combs = [['sma_tester'],
                        ['mr_tester'],
                        ['ml_tester'],
                        ['sma_tester', 'mr_tester'],
                        ['sma_tester', 'ml_tester'],
                        ['mr_tester', 'ml_tester'],
                        ['sma_tester', 'mr_tester', 'ml_tester']]
    strat_list = strat_combs[strategy]
    sma_tester = SMABacktester(u_ticker, u_sma_s, u_sma_l, u_start.isoformat(), u_end.isoformat(),0)
    mr_tester = MeanRevBacktester(u_ticker, u_sma, u_dev, u_start.isoformat(), u_end.isoformat(),0)
    ml_tester = MLBacktester(u_ticker, u_start.isoformat(), u_end.isoformat(),0)
    sma_tester.test_strategy()
    mr_tester.test_strategy()
    ml_tester.test_strategy()

    #st.sidebar.checkbox('SMA', value = True)
    #st.sidebar.checkbox('Mean Reversion', value = True)
    #st.sidebar.radio('Select method:', ['unanimous', 'tendency'], value= option)


comb = eval(strat_list[0]).results.loc[:, ["returns", "position"]].copy()
comb.rename(columns = {"position": strat_list[0]}, inplace = True)
comb["position_comb"] = comb[strat_list[0]]

if len(strat_list) > 1:
    for i in range(1,len(strat_list)):
        comb[strat_list[i]] = eval(strat_list[i]).results.position.astype("int")

        if option == 'unanimous':
            comb["position_comb"] = np.where(comb.eval(strat_list[i]) == comb.position_comb, comb.eval(strat_list[i]), 0)
        else:
            comb["position_comb"] = np.sign(comb.eval(strat_list[i]) + comb.position_comb)

comb["strategy"] = comb["position_comb"].shift(1) * comb["returns"]
comb.dropna(inplace=True)
comb["trades"] = comb.position_comb.diff().fillna(0).abs()
tc = 0
comb.strategy = comb.strategy - comb.trades * tc
comb["creturns"] = comb["returns"].cumsum().apply(np.exp)
comb["cstrategy"] = comb["strategy"].cumsum().apply(np.exp)

perf = comb["cstrategy"].iloc[-1] # absolute performance of the strategy
outperf = perf - comb["creturns"].iloc[-1] # out-/underperformance of strategy

trans_strat_dict = {'sma_tester': 'SMA', 'mr_tester': 'Mean Reversion', 'ml_tester': 'Logistic Rgression'} 
trans_strat = map(trans_strat_dict.get, strat_list)
out_strat = str(list(trans_strat)).strip('[]').replace('\'', '')

st.subheader('Combination of Strategies')
st.write('Value gain/loss over time:', round((perf*100)-100,2),'%')
st.write("Performance compared to 'buy and hold':", round(outperf*100,2),'%')
st.write('SMA_S:', u_sma_s)
st.write('SMA_L:', u_sma_l)
st.write('SMA:', u_sma)
st.write('Deviations:', u_dev)
st.write('Method:', option)
st.write('Strategy:', out_strat)

st.write('Strategy Performance over Time')
st.line_chart(comb[["creturns", "cstrategy"]])
progress_bar = st.progress(0)






