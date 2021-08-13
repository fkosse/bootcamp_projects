import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import itertools
import math as math

from SMABacktester import SMABacktester
from MeanRevBacktester import MeanRevBacktester
from MLBacktester import MLBacktester

from scipy.optimize import minimize

class MultiBacktester:
    

    def __init__(self, symbol, start, end, tc):
        '''
        Parameters
        ----------
        symbol: str
            ticker symbol (instrument) to be backtested
        start: str
            start date for data import
        end: str
            end date for data import
        tc: float
            proportional transaction/trading costs per trade
        '''
        self.symbol = symbol
        self.start = start
        self.end = end
        self.tc = tc
        self.results = None
        self.strategies = None
        self.method = None
    
    def prepare_data(self):
        comb = eval(strat_list[0]).results.loc[:, ["returns", "position"]].copy()
        comb.rename(columns = {"position": strat_list[0]}, inplace = True)
        comb["position_comb"] = comb[strat_list[0]]

        for i in range(1,len(strat_list)):
            comb[strat_list[i]] = eval(strat_list[i]).results.position.astype("int")

            if option == 'unanimous':
                comb["position_comb"] = np.where(comb.eval(strat_list[i]) == comb.position_comb, comb.eval(strat_list[i]), 0)
            else:
                comb["position_comb"] = np.sign(comb.eval(strat_list[i]) + comb.position_comb)


    def test_strategy(self):
        comb["strategy"] = comb["position_comb"].shift(1) * comb["returns"]
        comb.dropna(inplace=True)
        comb["trades"] = comb.position_comb.diff().fillna(0).abs()
        tc = 0
        comb.strategy = comb.strategy - comb.trades * tc
        comb["creturns"] = comb["returns"].cumsum().apply(np.exp)
        comb["cstrategy"] = comb["strategy"].cumsum().apply(np.exp)

        perf = data["cstrategy"].iloc[-1] # absolute performance of the strategy
        outperf = perf - data["creturns"].iloc[-1] # out-/underperformance of strategy
            
        return round(perf, 6), round(outperf, 6)


    def optimal_strategy(self, parameters):

        #strat_list = ['sma_tester', 'mr_tester', 'ml_tester']
        strat_combs = [['sma_tester'],
                        ['mr_tester'],
                        ['ml_tester'],
                        ['sma_tester', 'mr_tester'],
                        ['sma_tester', 'ml_tester'],
                        ['mr_tester', 'ml_tester'],
                        ['sma_tester', 'mr_tester', 'ml_tester']]

        #for i in range(1, len(strat_list)+1):
        #    combination = [list(x) for x in itertools.combinations(strat_list, i)]
        #    strat_combs.extend(combination)
        
        # SMA
        sma_tester = SMABacktester(self.symbol, int(parameters[0]), int(parameters[1]), self.start, self.end, self.tc)
        sma_tester.test_strategy()
        
        # Bollinger
        mr_tester = MeanRevBacktester(self.symbol,  int(parameters[2]),  int(parameters[3]), self.start, self.end, self.tc)
        mr_tester.test_strategy()

        # Logistic Regression
        ml_tester = MLBacktester(self.symbol, self.start, self.end, self.tc)
        ml_tester.test_strategy()
        
        # Create comb
        s= strat_combs[math.floor(parameters[5])]
            
        if len(s) == 1:
            comb = eval(s[0]).results.loc[:, ["returns", "position"]].copy()
            comb.rename(columns = {"position": s[0]}, inplace = True)
            comb["position_comb"] = comb[s[0]]
        
        if len(s) > 1:
            comb = eval(s[0]).results.loc[:, ["returns", "position"]].copy()
            comb.rename(columns = {"position": s[0]}, inplace = True)
            comb["position_comb"] = comb[s[0]]

        for c in range(1,len(s)):
            comb[s[c]] = eval(s[c]).results.position.astype("int")
            # 2 Methods
            if math.floor(parameters[4]) == 0:
                comb["position_comb"] = np.where(comb.eval(s[c]) == comb.position_comb, comb.eval(s[c]), 0)
            else:
                comb["position_comb"] = np.sign(comb.eval(s[c]) + comb.position_comb)
        
        
        # Busy Hours
        #comb["NYTime"] = comb.index.tz_convert("America/New_York")
        #comb["hour"] = comb.NYTime.dt.hour
        #comb.position_comb = np.where(comb.hour.between(2, 12), comb.position_comb, 0)
        
        # Backtest
        comb["strategy"] = comb["position_comb"].shift(1) * comb["returns"]
        comb.dropna(inplace=True)
        comb["trades"] = comb.position_comb.diff().fillna(0).abs()
        comb.strategy = comb.strategy - comb.trades * self.tc
        comb["creturns"] = comb["returns"].cumsum().apply(np.exp)
        comb["cstrategy"] = comb["strategy"].cumsum().apply(np.exp)
        return -comb["cstrategy"].iloc[-1]


    def optimized_parameters(self, parameters):
        bnds =  ((50, 100), (100, 200), (100, 200), (2, 5), (0,1), (2,3))
        opts = minimize(self.optimal_strategy, parameters, method = "Powell" , bounds = bnds)
        return opts.x



