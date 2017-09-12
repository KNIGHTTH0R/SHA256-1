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

print(binary_adder('1001', '1001'))

