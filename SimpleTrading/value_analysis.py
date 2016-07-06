# -*- coding: utf-8 -*-

'''
Created on 2016. 6. 27.

@author: lee
'''
import MySQLdb

import pandas as pd
from simple.context.das.jdbc.sql_template import ManagedJdbcTemplate
from simple.core.container.services import services
from simple.db.mysql.data_handler import DataHandler


class ValueAnalysis():
    
    select_stock_item_sql = "SELECT * FROM STOCK_ITEM"
    select_stock_group_cd_sql = "SELECT STOCK_GROUP_CD FROM STOCK_ITEM GROUP BY STOCK_GROUP_CD"
    select_stock_item_with_param_sql = "SELECT * FROM STOCK_ITEM WHERE STOCK_GROUP_CD = %(stock_group_cd)s"
    
    def __init__(self):
        pass

if __name__ == '__main__':
    
    # 0. common init
    host = "112.150.214.10"
    user = "InsanelySimple"
    passwd = "1234"
    db = "stock"
    charset = "utf8"
    use_unicode = True

    data_handler = DataHandler(host, user, passwd, db, charset, use_unicode)
    value_analysis = ValueAnalysis(data_handler)
    value_analysis
    '''
        ** 내용정리 **
        1. 그룹 코드를 가져와 PBR,PER ... 정보를 그룹별로 랭킹을 매겨 가져온다.
        2. 랭킹 정보를 바탕으로 각 종목에 대한 Score를 만든다.
        3. Score 최종 순위를 그룹별로 보여준다. 
    '''
    
    # 1. load stock_item
    
    
    '''
    db = MySQLdb.connect(host=host, 
                             user=user, 
                             passwd=passwd, 
                             db=db, 
                             charset=charset, 
                             use_unicode=use_unicode)
    cursor = db.cursor()
    cursor.execute(select_stock_item_sql)
    results = cursor.fetchall()    # 2. 그룹 코드를 가져와 재무재표에 나오는 특성 값들로(PBR, PER...) Score를 매긴다.
    
    df = pd.DataFrame(list(results), columns=['stock_cd', 'stock_nm', 'pt_eps', 'pt_bps', 'pt_per', 'pt_pbr','stock_group_cd', 'market_cd'])
    df['score'] = 0
#     df.drop('market_cd', axis=1, inplace=True)
    group_codes = df.stock_group_cd.unique()
    
    '''
    #  2.1 PBR로 Score 합산
    
    '''
    for i in range(0, len(group_codes)):
        item = df[df['stock_group_cd'] == group_codes[i]]
        sortedDf = item.sort(['pt_per'], ascending=[False])
        sortedDf = sortedDf.reset_index(drop=True)

        for j in range(0, len(sortedDf)):
            stock_cd = sortedDf.at[j, 'stock_cd']
            df.loc[df.stock_cd == stock_cd, 'score'] += j


    # 2.2 PER로 Score 합산
    for i in range(0, len(group_codes)):
        item = df[df['stock_group_cd'] == group_codes[i]]
        sortedDf = item.sort(['pt_pbr'], ascending=[False])
        sortedDf = sortedDf.reset_index(drop=True)

        for j in range(0, len(sortedDf)):
            stock_cd = sortedDf.at[j, 'stock_cd']
            df.loc[df.stock_cd == stock_cd, 'score'] += j

    # Finalize    
    db.close()

    '''
        