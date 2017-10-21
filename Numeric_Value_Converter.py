#!/usr/bin/python
# -*- coding: utf-8 -*-    
# Previous line is for encoding
# Imported scripts holding classes of numerical values
from Decimal import *
from Binary import *
from Octal import *
from Hexadecimal import *

class NumericValueConverter:    # This class contains the mainmenu and convertion navigator
    
    def showMainMenu(self):
        print """
 1: Decimal     -> Binary  -> Octal  -> Hexadecimal
 2: Binary      -> Decimal -> Octal  -> Hexadecimal
 3: Octal       -> Decimal -> Binary -> Hexadecimal
 4: Hexadecimal -> Decimal -> Binary -> Octal
 5: Exit Program
        """
        option = int(raw_input(" Enter Option >>> "))
        print ""
        if option == 1:
            self.decimalConverter()
        elif option == 2:
            self.binaryConverter()
        elif option == 3:
            self.octalConverter()
        elif option == 4:
            self.hexadecimalConverter()
        elif option == 5:
            exit()
        else:
            print "\n Wrong Option."
        self.showMainMenu()
        
    def decimalConverter(self):
        dec = Decimal()
        decimal = int(raw_input(" Decimal     : "))
        binary = dec.toBinary(decimal) # Convert decimal to binary by calling 'toBinary' method of class object 'converter'
        octal = dec.toOctal(decimal) 
        hexadecimal = dec.toHexadecimal(decimal)
        print " Binary      : %d" % binary
        print " Octal       : %d" % octal
        print " Hexadecimal : %s" % hexadecimal
        
    def binaryConverter(self):
        _bin = Binary()
        binary = int(raw_input(" Binary      : "))
        decimal = _bin.toDecimal(binary)
        octal = _bin.toOctal(binary)
        hexadecimal = _bin.toHexadecimal(binary)
        print " Decimal     : %d" % decimal
        print " Octal       : %d" % octal
        print " Hexadecimal : %s" % hexadecimal
        
    def octalConverter(self):
        _oct = Octal()
        octal = int(raw_input(" Octal       : "))
        decimal = _oct.toDecimal(octal)
        binary = _oct.toBinary(octal)
        hexadecimal = _oct.toHexadecimal(octal)
        print " Decimal     : %d" % decimal
        print " Binary      : %d" % binary
        print " Hexadecimal : %s" % hexadecimal
        
    def hexadecimalConverter(self):
        _hex = Hexadecimal()
        hexadecimal = str(raw_input(" Hexadecimal : "))
        decimal = _hex.toDecimal(hexadecimal)
        binary = _hex.toBinary(hexadecimal)
        octal = _hex.toOctal(hexadecimal)
        print " Decimal     : %d" % decimal
        print " Binary      : %d" % binary
        print " Octal       : %d" % octal

application = NumericValueConverter() # Creates and object of class: NumericValueConverter 
if __name__ == '__main__':
    application.showMainMenu()
