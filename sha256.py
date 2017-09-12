import os
import conversions
import functions
import input_padding
import tkinter as tk

# CREATE FILES CONTAINING INITIAL VALUES #
"""
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,
			67,71,73,79,83,89,97,101,103,107,109,113,127,131,
			137,139,149,151,157,163,167,173,179,181,191,
			193,197,199,211,223,227,229,233,239,241,251,
			257,263,269,271,277,281,283,293,307,311]

# FRACTIONAL PART OF SQUARE ROOTS OF THE FIRST 8 PRIMES #
try:
	os.mkdir('initial_hash_values')
	os.mkdir('constant_words_K')
except FileExistsError:
	pass

os.chdir('initial_hash_values')
for i in range(1, 9):
	f = open("H0_"+str(i), 'w')
	f.write(conversions.fraction_to_hex(primes[i-1]**0.5))
	f.close()
os.chdir('..')

# FRACTIONAL PART OF CUBE ROOTS OF THE FIRST 64 PRIMES #
os.chdir('constant_words_K')
for i in range(1, len(primes)+1):
	f = open("K"+str(i), 'w')
	f.write(conversions.fraction_to_hex(primes[i-1]**(1/3)))
	f.close()
os.chdir('..')
"""
# CREATE A GUI FOR ALGORITHM SETUP #

root = tk.Tk()
root.title("SHA256 Encryptor")
root.geometry('{}x{}'.format(600, 80))
enterframe = tk.Frame(root)
enterframe.pack(side=tk.TOP)
enterlabel = tk.Label(enterframe, text="Enter String (less than 56 characters): ")
enterlabel.pack(side = tk.LEFT)
enterstring = tk.Entry(enterframe, width = 60)
enterstring.pack(side = tk.RIGHT)

def update_label():
	output["text"] = hash(enterstring.get())

button = tk.Button(root, text="Encrypt!", command=update_label)
button.pack(side = tk.BOTTOM)

outputframe = tk.Frame(root)
outputframe.pack(side= tk.LEFT)

outputlabel = tk.Label(outputframe, text="SHA256 KEY:")
outputlabel.pack(side= tk.LEFT)
output = tk.Label()

def hash(string):

	# COLLECT INITIAL HASH VALUES FROM FILE #

	f = open('initial_hash_values/H0_1', 'r')
	A = conversions.hex_to_binary(f.read())
	f.close()
	f = open('initial_hash_values/H0_2', 'r')
	B = conversions.hex_to_binary(f.read())
	f.close()
	f = open('initial_hash_values/H0_3', 'r')
	C = conversions.hex_to_binary(f.read())
	f.close()
	f = open('initial_hash_values/H0_4', 'r')
	D = conversions.hex_to_binary(f.read())
	f.close()
	f = open('initial_hash_values/H0_5', 'r')
	E = conversions.hex_to_binary(f.read())
	f.close()
	f = open('initial_hash_values/H0_6', 'r')
	F = conversions.hex_to_binary(f.read())
	f.close()
	f = open('initial_hash_values/H0_7', 'r')
	G = conversions.hex_to_binary(f.read())
	f.close()
	f = open('initial_hash_values/H0_8', 'r')
	H = conversions.hex_to_binary(f.read())
	f.close()

	input_padding.blocking(string)
	
	# PRETTY FORMATTED PRINTING #

#	print('  ', 'A', '      ', 'B', '      ', 'C', '      ', 'D', '      ', 'E', '      ', 'F', '      ', 'G', '      ', 'H')
#	print('  ', conversions.binary_to_hex(A), conversions.binary_to_hex(B), conversions.binary_to_hex(C), conversions.binary_to_hex(D), conversions.binary_to_hex(E), conversions.binary_to_hex(F), conversions.binary_to_hex(G), conversions.binary_to_hex(H))

	# HASHING ALGORITHM #

	for i in range(64):
		ch = functions.choice(G, F, E)
		maj = functions.majority(A, B, C)
		sum0 = functions.sum0(A)
		sum1 = functions.sum1(E)
		K = conversions.hex_to_binary(open('constant_words_K/K'+str(i+1), 'r').read())
		W = open('input_string/W'+str(i+1), 'r').read()[:-1]
		T1 = functions.binary_adder(functions.binary_adder(functions.binary_adder(functions.binary_adder(H, sum1), ch), K), W)
		T2 = functions.binary_adder(sum0, maj)
		H = G
		G = F
		F = E
		E = functions.binary_adder(D, T1)
		D = C
		C = B
		B = A
		A = functions.binary_adder(T1, T2)

#		print(str(i), conversions.binary_to_hex(A), conversions.binary_to_hex(B), conversions.binary_to_hex(C), conversions.binary_to_hex(D), conversions.binary_to_hex(E), conversions.binary_to_hex(F), conversions.binary_to_hex(G), conversions.binary_to_hex(H))

	# RECOLLECTING THE INITIAL HASH VALUES #

	f = open('initial_hash_values/H0_1', 'r')
	H0_1 = conversions.hex_to_binary(f.read())
	f.close()
	f = open('initial_hash_values/H0_2', 'r')
	H0_2 = conversions.hex_to_binary(f.read())
	f.close()
	f = open('initial_hash_values/H0_3', 'r')
	H0_3 = conversions.hex_to_binary(f.read())
	f.close()
	f = open('initial_hash_values/H0_4', 'r')
	H0_4 = conversions.hex_to_binary(f.read())
	f.close()
	f = open('initial_hash_values/H0_5', 'r')
	H0_5 = conversions.hex_to_binary(f.read())
	f.close()
	f = open('initial_hash_values/H0_6', 'r')
	H0_6 = conversions.hex_to_binary(f.read())
	f.close()
	f = open('initial_hash_values/H0_7', 'r')
	H0_7 = conversions.hex_to_binary(f.read())
	f.close()
	f = open('initial_hash_values/H0_8', 'r')
	H0_8 = conversions.hex_to_binary(f.read())
	f.close()

	# FINAL ADDITION OF LAST HASHING VALUES WITH THE INITIAL ONES #

	H1 = functions.binary_adder(H0_1, A)
	H2 = functions.binary_adder(H0_2, B)
	H3 = functions.binary_adder(H0_3, C)
	H4 = functions.binary_adder(H0_4, D)
	H5 = functions.binary_adder(H0_5, E)
	H6 = functions.binary_adder(H0_6, F)
	H7 = functions.binary_adder(H0_7, G)
	H8 = functions.binary_adder(H0_8, H)

	SHA256FINAL = conversions.binary_to_hex(H1+H2+H3+H4+H5+H6+H7+H8)
	return SHA256FINAL

output.pack()
root.mainloop()
