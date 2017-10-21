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