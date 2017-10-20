#!/usr/bin/python
# -*- coding: utf-8 -*-    
# Previous line is for encoding

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

class Decimal: # Decimal class | used for converting decimal to other 3 formats
    
    def toBinary(self, decimal): #Converts decimal to binary
        base = 1; remainder = 0; binary = 0
        while decimal > 0:
            remainder = decimal % 2
            decimal /= 2
            binary += (remainder * base)
            base *= 10
        return binary
    
    def toOctal(self, decimal): # Converts decimal to octal
        base = 1; remainder = 0; octal = 0
        while decimal > 0:
            remainder = decimal % 8
            decimal /= 8
            octal += (remainder * base)
            base *= 10
        return octal

    def toHexadecimal(self, decimal): # Converts decimal to hexadecimal
        remainder = 0; hexadecimal = ""
	while (decimal > 0):
            remainder = decimal % 16
	    decimal /= 16
	    hexadecimal = str(remainder) + hexadecimal if (remainder < 10) else str(chr(55 + remainder)) + hexadecimal
	return hexadecimal

class Binary: # Binary Class | used for converting binary to other 3 formats
    
    def toDecimal(self, binary): # Converts binary to decimal
        remainder = 0; maxlength = len(str(binary)); length = 0; decimal = 0
        while length <= maxlength:
            remainder = binary % 10
            decimal += (remainder * (2 ** length))
            binary /= 10
            length += 1
        return decimal

    def toOctal(self, binary): # Converts binary to octal
        decimal = self.toDecimal(binary); base = 1; remainder = 0; octal = 0
        while decimal > 0:
            remainder = decimal % 8
            decimal /= 8
            octal += (remainder * base)
            base *= 10
        return octal

    def toHexadecimal(self, binary): # Converts binary to hexadecimal
        decimal = self.toDecimal(binary); remainder = 0; hexadecimal = ""
	while (decimal > 0):
            remainder = decimal % 16
	    decimal /= 16
	    hexadecimal = str(remainder) + hexadecimal if (remainder < 10) else str(chr(55 + remainder)) + hexadecimal
	return hexadecimal

class Octal: # Octal class | used for converting Octal to other 3 formats
    
    def toDecimal(self, octal): # Converts octal to decimal
        remainder = 0; maxlength = len(str(octal)); length = 0; decimal = 0
        while length <= maxlength:
            remainder = octal % 10
            decimal += (remainder * (8 ** length))
            octal /= 10
            length += 1
        return decimal

    def toBinary(self, octal): # Converts octal to binary
        decimal = self.toDecimal(octal); remainder = 0; base = 1; binary = 0
        while decimal > 0:
            remainder = decimal % 2
            decimal /= 2
            binary += (remainder * base)
            base *= 10
        return binary

    def toHexadecimal(self, octal): # Converts octal to hexadecimal
        decimal = self.toDecimal(octal); remainder = 0; hexadecimal = ""
        while (decimal > 0):
            remainder = decimal % 16
	    decimal /= 16
	    hexadecimal = str(remainder) + hexadecimal if (remainder < 10) else str(chr(55 + remainder)) + hexadecimal
	return hexadecimal

class Hexadecimal: # Hexadecimal class | used for converting hexadecimal to other 3 formats
    
    def toDecimal(self, hexadecimal): # Converts hexadecimal to decimal
        hexadecimal = str(hexadecimal); decimal = 0; maxlength = len(hexadecimal) - 1; length = 0; temp = ""
	for i in range(0, maxlength + 1):
	    if (ord(hexadecimal[i]) >= 97 and ord(hexadecimal[i]) <= 122):
		temp += chr(ord(hexadecimal[i]) - 32)
		continue
	    temp += hexadecimal[i]
        hexadecimal = temp
	while length <= maxlength:
	    if ord(hexadecimal[length]) < 65:
		decimal += (ord(hexadecimal[length]) - 48) * (16 ** (maxlength - length))
	    else:
		decimal += (ord(hexadecimal[length]) - 55) * (16 ** (maxlength - length))
	    length += 1
	return decimal

    def toBinary(self, hexadecimal): # Converts hexadecimal to binary
        decimal = self.toDecimal(hexadecimal); remainder = 0; base = 1; binary = 0
        while decimal > 0:
            remainder = decimal % 2
            decimal /= 2
            binary += (remainder * base)
            base *= 10
        return binary

    def toOctal(self,hexadecimal): # Converts hexadecimal to octal
        decimal = self.toDecimal(hexadecimal); base = 1; remainder = 0; octal = 0
        while decimal > 0:
            remainder = decimal % 8
            decimal /= 8
            octal += (remainder * base)
            base *= 10
        return octal

application = NumericValueConverter() # Creates and object of class: NumericValueConverter 
if __name__ == '__main__':
    application.showMainMenu()
