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