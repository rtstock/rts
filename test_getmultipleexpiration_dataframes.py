# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 15:23:29 2015

@author: justin.malinchak
"""

# ##########
# Date setup
import pullprices as pp
import datetime
today_datetime = datetime.datetime.today()
today_date = datetime.date.today()
iter_date = today_date

for i in range(8):
    
    while iter_date.weekday() != 4:
        iter_date += datetime.timedelta(1)    
    iter_date_string = iter_date
    iter_date += datetime.timedelta(1)
    print i,iter_date_string
    
    df_optionpricescurrent = pp.options_to_dataframe('SPY',iter_date_string,0)
    if not df_optionpricescurrent is None:
        print df_optionpricescurrent
    else:
        print 'Ha, caugnt the issue'
    

