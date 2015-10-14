# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 07:20:16 2014

@author: jmalinchak
"""
# C:\Documents and Settings\jmalinchak\My Documents\My Python\Active\py\downloads\2015-01-14
dDownloadDirectories = {}
dDownloadDirectories[len(dDownloadDirectories)] = 'downloads\\2015-01-14\\test\\AMGN'
#dDownloadDirectories[len(dDownloadDirectories)] = 'downloads\\2014-12-27\\15\\45\\TWTR'
criteria_for_showresults = 1
criteria_for_minspreadpercent=1.7
criteria_for_maxvalueatrisk = 3.4
criteria_for_sortbymeasure = 'spreadpercentageopening' # # spreadpercentageopening | valueatrisk

import buildpairsdictionarywithcriteriafromdirectoryofpulledfiles
import convertpairsdictionaryfromqualifiedtosortable
import concatonatesortablepairdictionaries
import sortasortabledictionary

dSortableDictionaries = {}

# loop dictionary of paths --------------------------------------------------------------------
for k0,v0 in dDownloadDirectories.items():

    print('===',k0,v0)
    
    c = buildpairsdictionarywithcriteriafromdirectoryofpulledfiles.build(rootlocalforfilespulled=v0, 
                                                                         maxvalueatrisk=criteria_for_maxvalueatrisk,
                                                                         showresults=criteria_for_showresults) 
                                                                         
    o = convertpairsdictionaryfromqualifiedtosortable.convert(c.DictionaryOfFilteredCalendarPairs,criteria_for_sortbymeasure)
    r = concatonatesortablepairdictionaries.concatonate(dSortableDictionaries,o.DictionaryOfSortablePairsOutput)
    dSortableDictionaries = r.ResultingDictionaryOfSortablePairsOutput
    s = sortasortabledictionary.sort(dSortableDictionaries,criteria_for_showresults) #  <-- 1 means to show results.  it will print it out

    dSortedPairsOutput = s.DictionaryOfSortedPairsOutput
        
    import serializesortedpairdictionarytoxml
    oSerialize = serializesortedpairdictionarytoxml.serialize(dSortedPairsOutput)
    
#    # ################################################
#    # Prints to screen    
#    # ################################################
#    for k3,v3 in dSortedPairsOutput.items():
#        sortbymeasurevalue = round(v3['sortbymeasurevalue'],3)
#        earlier = v3['earlier']
#        later = v3['later']
#        print(k3,
#                sortbymeasurevalue,
#                earlier.bid,later.ask,
#                earlier.optionsymbol,
#                later.optionsymbol)
#    # ################################################