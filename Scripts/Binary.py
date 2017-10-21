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