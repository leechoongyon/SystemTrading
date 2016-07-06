from __future__ import division

import numpy as np
import statsmodels.tsa.stattools as ts

from common.stock_common import *
from config.services import *


class StockFinder:

    def __init__(self):
        self.dbhandler = services.get('dbhandler')
        self.dbreader = services.get('dbreader')
        self.predictor = services.get('predictor')
        self.config = services.get('configurator')

    def loadDataFrame(self, code):
        sql = 'select * from prices'
        sql += " where code='%s'" % code
        sql += " and price_date between '%s' and '%s' " % (self.config.get('start_date'), self.config.get('end_date'))
        df = pd.read_sql(sql, self.dbhandler.conn)
        return df

    def calcADF(self, df):
        adf_result = ts.adfuller(df)
        ciritical_values = adf_result[4]
        return (adf_result[0],
         ciritical_values['1%'],
         ciritical_values['5%'],
         ciritical_values['10%'])

    def calcHurstExponent(self, df, lags_count = 100):
        lags = range(2, lags_count)
        ts = np.log(df)
        tau = [ np.sqrt(np.std(np.subtract(ts[lag:], ts[:-lag]))) for lag in lags ]
        poly = np.polyfit(np.log(lags), np.log(tau), 1)
        result = poly[0] * 2.0
        return result

    def calcHalfLife(self, df):
        price = pd.Series(df)
        lagged_price = price.shift(1).fillna(method='bfill')
        delta = price - lagged_price
        beta = np.polyfit(lagged_price, delta, 1)[0]
        half_life = -1 * np.log(2) / beta
        return half_life

    def assessADF(self, test_stat, adf_1, adf_5, adf_10):
        if test_stat < adf_10:
            return 3
        if test_stat < adf_5:
            return 2
        if test_stat < adf_1:
            return 1
        return 0

    def assessHurst(self, hurst):
        if hurst > 0.4:
            return 0
        if hurst < 0.1:
            return 3
        if hurst < 0.2:
            return 2
        return 1

    def assessHalflife(self, percentile, halflife):
        for index in range(len(percentile)):
            if halflife <= percentile[index]:
                if index < 2:
                    return 3
                if index < 3:
                    return 2
                if index < 4:
                    return 1

        return 0

    def assessMachineLearning(self, percentile, halflife):
        for index in range(len(percentile)):
            if halflife <= percentile[index]:
                if index < 2:
                    return 3
                if index < 3:
                    return 2
                if index < 4:
                    return 1

        return 0

    def doStationarityTest(self, column, lags_count = 100):
        rows_code = self.dbreader.loadCodes(limit=self.config.get('data_limit'))
        test_result = {'code': [],
         'company': [],
         'adf_statistic': [],
         'adf_1': [],
         'adf_5': [],
         'adf_10': [],
         'hurst': [],
         'halflife': []}
        index = 1
        for a_row_code in rows_code:
            code = a_row_code[0]
            company = a_row_code[1]
            print '... %s of %s : Testing Stationarity on %s %s' % (index,
             len(rows_code),
             code,
             company)
            a_df = self.loadDataFrame(code)
            a_df_column = a_df[column]
            if a_df_column.shape[0] > 0:
                test_result['code'].append(code)
                test_result['company'].append(company)
                test_result['hurst'].append(self.calcHurstExponent(a_df_column, lags_count))
                test_result['halflife'].append(self.calcHalfLife(a_df_column))
                test_stat, adf_1, adf_5, adf_10 = self.calcADF(a_df_column)
                test_result['adf_statistic'].append(test_stat)
                test_result['adf_1'].append(adf_1)
                test_result['adf_5'].append(adf_5)
                test_result['adf_10'].append(adf_10)
            index += 1

        df_result = pd.DataFrame(test_result)
        return df_result

    def rankStationarity(self, df_stationarity):
        df_stationarity['rank_adf'] = 0
        df_stationarity['rank_hurst'] = 0
        df_stationarity['rank_halflife'] = 0
        halflife_percentile = np.percentile(df_stationarity['halflife'], np.arange(0, 100, 10))
        for row_index in range(df_stationarity.shape[0]):
            df_stationarity.loc[row_index, 'rank_adf'] = self.assessADF(df_stationarity.loc[row_index, 'adf_statistic'], df_stationarity.loc[row_index, 'adf_1'], df_stationarity.loc[row_index, 'adf_5'], df_stationarity.loc[row_index, 'adf_10'])
            df_stationarity.loc[row_index, 'rank_hurst'] = self.assessHurst(df_stationarity.loc[row_index, 'hurst'])
            df_stationarity.loc[row_index, 'rank_halflife'] = self.assessHalflife(halflife_percentile, df_stationarity.loc[row_index, 'halflife'])

        df_stationarity['rank'] = df_stationarity['rank_adf'] + df_stationarity['rank_hurst'] + df_stationarity['rank_halflife']
        return df_stationarity

    def buildUniverse(self, df_stationarity, column, ratio):
        percentile_column = np.percentile(df_stationarity[column], np.arange(0, 100, 10))
        ratio_index = np.trunc(ratio * len(percentile_column))
        universe = {}
        for row_index in range(df_stationarity.shape[0]):
            percentile_index = getPercentileIndex(percentile_column, df_stationarity.loc[row_index, column])
            if percentile_index >= ratio_index:
                universe[df_stationarity.loc[row_index, 'code']] = df_stationarity.loc[row_index, 'company']

        return universe

    def doMachineLearningTest(self, split_ratio = 0.75, lags_count = 10):
        return self.predictor.trainAll(split_ratio=split_ratio, time_lags=lags_count)

    def rankMachineLearning(self, df_machine_learning):

        def listed_columns(arr, prefix):
            result = []
            for a_item in arr:
                result.append(prefix % a_item)

            return result

        mr_models = ['logistic', 'rf', 'svm']
        for a_predictor in mr_models:
            df_machine_learning['rank_%s' % a_predictor] = 0

        percentiles = {}
        for a_predictor in mr_models:
            percentiles[a_predictor] = np.percentile(df_machine_learning[a_predictor], np.arange(0, 100, 10))
            for row_index in range(df_machine_learning.shape[0]):
                df_machine_learning.loc[row_index, 'rank_%s' % a_predictor] = self.assessMachineLearning(percentiles[a_predictor], df_machine_learning.loc[row_index, a_predictor])

        df_machine_learning['total_score'] = df_machine_learning[mr_models].sum(axis=1)
        df_machine_learning['rank'] = df_machine_learning[listed_columns(mr_models, 'rank_%s')].sum(axis=1)
        return df_machine_learning