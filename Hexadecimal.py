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