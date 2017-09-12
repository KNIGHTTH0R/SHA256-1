hexadecimal = "0123456789ABCDEF"

def binary_to_decimal(num):
	"""
	Converts a binary string into decimal representation.
	"""
	decimal = 0
	num = str(num)

	for i in range(0, len(num)):
		if num[i] == '0' or num[i] == '1':
			decimal += 2**(len(num)-(i+1))*int(num[i])
		else:
			return "INVALID BINARY STRING"

	return decimal

def binary_to_hex(num):
	"""
	Converts a binary string into hexadecimal representation.
	"""
	hexa = ""
	num = str(num)

	while int(len(num) % 4) != 0:
		num = "0" + num

	for i in range(0, len(num)//4):
		try:
			hexa += hexadecimal[binary_to_decimal(int(num[4*i:4*i+4]))]
		except TypeError:
			return "INVALID BINARY STRING"
	return hexa
	
def decimal_to_binary(num, length=4):
	"""
	Converts a decimal string into binary representation
	(in a multiple of "length" bits).
	"""
	bin_num = ""

	while num >= 1:
		if int(num % 2) == 0:
			bin_num = "0" + bin_num
			num = int(num/2)
		elif int(num % 2) == 1:
			bin_num = "1" + bin_num
			num = int((num/2))
	
	while int(len(bin_num) % length) != 0:
		bin_num = "0" + bin_num

	return bin_num

def decimal_to_hex(num):
	"""
	Converts a decimal string into hexadecimal representation.
	"""
	hexa = ""
	
	while num >= 1:
		if str(num % 16) in d_to_h:
			hexa = d_to_h[str(num % 16)] + hexa
			num = num // 16
		elif num % 16 < 10:
			hexa = str(num % 16) + hexa
			num = num // 16
	return hexa

def hex_to_binary(num, length=4):
	"""
	Converts a hexadecimal string into binary representation.
	"""
	bin_num = ""
	num = str(num)

	for i in range(0, len(num)):
		if num[i] not in list(hexadecimal):
			return "INVALID HEXADECIMAL STRING"
		else:
			bin_num += decimal_to_binary(hexadecimal.index(num[i]))

	while int(len(bin_num) % length) != 0:
		bin_num = "0" + bin_num

	return bin_num

def hex_to_decimal(num):
	"""
	Converts a hexadecimal string into decimal representation.
	"""
	decimal = 0
	num = str(num)
	
	for i in range(0, len(num)):
		if num[i] in list(hexadecimal):
			decimal += 16 **(len(num)-(i+1)) * int(hexadecimal.index(num[i]))
		else:
			print("INVALID NUMBER")
			break
	
	return decimal

def fraction_to_hex(frac, length=8):
	"""
	Converts a number between 0 and 1 in decimal into hexadecimal representation.	
	"""
	hexa = ""

	while len(hexa) < length:
		frac %= 1
		frac *= 16
		hexa += str(hexadecimal[int(frac//1)])
	return hexa
