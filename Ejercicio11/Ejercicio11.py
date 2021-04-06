# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 21:51:49 2021

@author: Edgar_Polo
"""

# Dado un número, encuentre la suma de todos los múltiplos únicos de números

# particulares hasta ese número, pero sin incluirlo.

(ns sum-of-multiples)

(defn sum-of-multiples [factors n]
  (->> factors
       (mapcat #(range % n %))
       (set)
       (apply +)))
  