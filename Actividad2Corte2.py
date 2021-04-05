# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 17:45:45 2021

@author: Edgar_Polo
"""
# Ejercicio # 1
def abbreviate(words, acronimo=""):

    if "'" in words:
        words = words.replace("'", "")
    words = words.title()
    for letras in words:
        if letras.isalpha and letras.isupper():
            acronimo = acronimo + letras[0].upper()
    return acronimo
