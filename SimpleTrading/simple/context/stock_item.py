'''
Created on 2016. 6. 27.

@author: lee
'''


class StockItem:
    def __init__(self, stock_cd, 
                 stock_nm, 
                 pt_eps, 
                 pt_bps, 
                 pt_per, 
                 pt_pbr, 
                 stock_group_cd, 
                 market_cd):
        
        self.stock_cd = stock_cd
        self.stock_nm = stock_nm
        self.pt_eps = pt_eps
        self.pt_bps = pt_bps
        self.pt_per = pt_per
        self.pt_pbr = pt_pbr
        self.stock_group_cd = stock_group_cd
        self.market_cd = market_cd
        
        
        
