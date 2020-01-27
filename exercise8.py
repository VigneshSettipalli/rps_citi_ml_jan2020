# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 15:22:53 2020

@author: Balasubramaniam
"""

from abc import ABC,abstractmethod

class Booking(ABC):
    @abstractmethod
    def book(self,amount):
        pass

class ForeignExchange(Booking):
    def book(self,amount):
        print("Convert %d" %(amount))

foreignExchange=ForeignExchange()
foreignExchange.book(32684586)






