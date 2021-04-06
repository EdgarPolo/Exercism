# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 21:31:28 2021

@author: Edgar_Polo
"""
# Dado un año, informe si es un año bisiesto

def is_leap_year(year):

    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
