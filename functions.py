def xor(A, B):
	if A != B:
		return 1
	else:
		return 0

def _sum(A, B, C):
	return xor(xor(A, B), C)

def _carry(A, B, C):
	return (A and B) or (C and xor(A, B))

def binary_adder(A, B):
	"""
	Takes two binary strings of length l and adds them mod 2^l.
	"""
	A = list(reversed(A))
	B = list(reversed(B))
	print(A, B)
	carrylist = [0]
	sumlist = []

	for i in range(0 , len(A)):
		carrylist.insert(len(carrylist), _carry(int(carrylist[i]), int(A[i]), int(B[i])))
		sumlist.insert(len(sumlist), _sum(int(carrylist[i]), int(A[i]), int(B[i])))
		print(list(reversed(carrylist)), list(reversed(sumlist)))

	bin_sum = ""
	for i in reversed(range(0, len(A))):
		bin_sum += str(sumlist[i])
	return bin_sum

def sub_majority(a, b, c):
	"""
	Majority function for 3 given bits: returns the most common bit out of the three inputs.
	"""
	if a == '0':
		if b == '0':
			return '0'
		elif b == '1':
			if c == '0':
				return '0'
			elif c == '1':
				return '1'
	elif a == '1':
		if b == '0':
			if c == '0':
				return '0'
			if c == '1':
				return '1'
		elif b == '1':
			return '1'
def majority(A, B, C):
	"""
	Returns the majority function for each of the 32 bits in the strings A, B, and C.
	"""
	new_string = ""
	for i in range(0, len(A)):
		new_string += str(sub_majority(A[i], B[i], C[i]))
	return new_string

def sub_choice(a, b, c):
	"""
	Choice function: Returns a if c=0 and b if c=1.
	"""
	if c == '0':
		return a
	elif c == '1':th
		return b
def choice(A, B, C):
	"""
	Returns the choice function for each of the 32 bits in the strings A, B, and C. The array C governs the choice.
	"""
	new_string = ""
	for i in range(0, len(A)):
		new_string += sub_choice(A[i], B[i], C[i])
	return new_string

def right_rotation(A, shift):
	"""
	Rotates the array by "shift" bits, and the bits at the end rotate to the beginning.
	"""
	new_string = ""
	for i in range(0, len(A)-shift):
		new_string += A[i+shift]
	for i in range(0, shift):
		new_string += A[i]
	return new_string

def right_shift(A, shift):
	"""
	Shifts the array by "shift" bits, and replaces the bits at the beginning with 0's.
	"""
	new_string = ""
	for i in range(0, len(A)-shift):
		new_string += A[i]
	for i in range(0, len(A)-len(new_string)):
		new_string = "0" + new_string
	return new_string
