import conversions
import functions
import os

alphabet = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwyxz{|}~"""

def search(A, v):
	"""
	Returns the first index so that the given value is at that index in the given list.
	"""
	for i in range(0, len(A)):
		if A[i] == v:
			return i

def ascii_to_binary(string):
	"""
	Converts an ascii string into its binary representation.
	"""
	bin_string = ""
	for i in range(0,len(string)):
		bin_string += conversions.decimal_to_binary(search(alphabet, string[i])+32)
	return bin_string

def padding(string):
	"""
	Pads the string in the SHA-256 method.
	NOT YET SUPPORTED FOR STRINGS WITH LENGTH OVER 448 BITS.
	"""
	binary = ascii_to_binary(string)
	l = len(binary)
	if l >= 448:
		return "STRING IS TOO LONG"
	else:
		binary += "1"
			
		for i in range(448-len(binary)):
			binary += "0"

		binary = binary + conversions.decimal_to_binary(l, 64)

		return binary

def blocking(string):
	"""
	Creates a new folder and 64 files, each with a 32 bit binary string used in the hashing algortihm.
	"""
	try:
		os.mkdir("input_string")
	except FileExistsError:
		pass

	os.chdir("input_string")
	for i in range(0, 16):
		f = open("W"+str(i+1), 'w')
		f.write(padding(string)[32*i:32*(i+1)] + '\n')
		f.close()

	for i in range(16, 64):
		W1 = functions.sigma1(open('W'+str(i-1), 'r').read()[-33:-1])
		W2 = open('W'+str(i-6), 'r').read()[-33:-1]
		W3 = functions.sigma0(open('W'+str(i-14), 'r').read()[-33:-1])
		W4 = open('W'+str(i-15), 'r').read()[-33:-1]
		f = open("W"+str(i+1), 'w')
		f.write(functions.binary_adder(functions.binary_adder(functions.binary_adder(W1, W2), W3), W4) + '\n')
		f.close()
	os.chdir('..')

