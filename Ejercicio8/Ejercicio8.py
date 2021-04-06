# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 21:12:07 2021

@author: Edgar_Polo
"""
# Determinar si es un Pangrama
from string import ascii_lowercase


def is_pangram(sentence):
    return all((ch in sentence.lower()) for ch in ascii_lowercase)
