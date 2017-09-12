import os
import conversions

##### CREATES FILES CONTAINING INITIAL VALUES #####

# LIST OF FIRST 64 PRIME NUMBERS #
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
	f.write(conversions.fraction_to_hex(primes[i-1]**(1/2)))
	f.close()
os.chdir('..')

# FRACTIONAL PART OF CUBE ROOTS OF THE FIRST 64 PRIMES #
os.chdir('constant_words_K')
for i in range(1, len(primes)+1):
	f = open("K"+str(i), 'w')
	f.write(conversions.fraction_to_hex(primes[i-1]**(1/3)))
	f.close()
os.chdir('..')
