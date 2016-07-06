from crawler.data_crawler import DataCrawler
from das.data_handler import *
from das.data_writer import *
from portfolio.portfolio_builder import *
from das.data_reader import *

from config.charter import *
from trader.mess_trader import *
from model.predictor import *
from tester.backtester import *


'''
Created on 2016. 5. 26.

@author: lee
'''


def init():
    services.register('dbhandler', DataHandler())
    services.register('dbwriter', DataWriter())
    services.register('dbreader', DataReader())
    services.register('charter', Charter())
    services.register('configurator', Configurator())

    services.register('predictor', Predictors())
    services.register('trader', MessTrader())
    services.register('mean_reversion_model', MeanReversionModel())
    services.register('machine_learning_model', MachineLearningModel())

if __name__ == '__main__':

    # 0. init
    init()

    #########################################################################################
    # 1. Data Collection
    #########################################################################################
    # crawler = DataCrawler()
    # crawler.updateAllCodes()

    #   1.1 Get stock code by crawling

    #   1.2 Store codes to db

    
    #   1.3 After getting stock price by stockCode in db,
    #       stored stock price to db

    # crawler.updateAllStockData(1,2010,1,1,2015,12,1)

    #########################################################################################
    # 2. Alpha model
    #########################################################################################


    universe = Portfolio()
    portfolio = PortfolioBuilder()

    services.get('configurator').register('start_date', '20160101')
    services.get('configurator').register('end_date', '20160526')
    services.get('configurator').register('input_column', 'Price_close')
    services.get('configurator').register('output_column', 'indicator')
    services.get('configurator').register('data_limit', 100)

    # 2.1 Mean Reversion
#     df_stationarity = portfolio.doStationarityTest('Price_close')
#     df_rank = portfolio.rankStationarity(df_stationarity)
#     stationarity_codes = portfolio.buildUniverse(df_rank, 'rank', 0.8)
#     print("Mean Reversion : %s " % stationarity_codes)

    # 2.2  Machine learning
    df_machine_result = portfolio.doMachineLearningTest(split_ratio=0.75, lags_count = 5 )
    df_machine_rank = portfolio.rankMachineLearning(df_machine_result)
    machine_codes = portfolio.buildUniverse(df_machine_rank, 'rank', 0.8)
    print("machine_codes : %s " % machine_codes)

    # 2.3 Dump
    # universe.clear()
    # universe.makeUniverse('price_close', 'stationarity', stationarity_codes)
    # universe.makeUniverse('price_close', 'machine_learning', machine_codes)
    # universe.dump()


    #########################################################################################
    # 3. Trader
    #########################################################################################

