# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 00:17:18 2014

@author: jmalinchak
"""

import nameddictionary

#nameddictionaryfiltered.nameddictionary.read('C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\Active\\downloads\\20141130b')
nd = nameddictionary.read('C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\Active\\downloads\\20141130b')

ndoi = nd.optioninstances('KMI','2014-12-12','C','42.5')
for KeyOfOptionInstances,ValueOfOptionInstances in ndoi.items():
    ValueOfOptionInstances.printdelim('|')
    
ndoi = nd.optioninstances('KMI','2014-12-20','C','42.5')
for KeyOfOptionInstances,ValueOfOptionInstances in ndoi.items():
    ValueOfOptionInstances.printdelim('|')