# Project Euler Library - Written in Python
# This library contains all the functions needed to solve
# the problems from the website

#!usr/bin/python
import math, time, itertools

# number of digits
def num_digits(n):
	return int(math.log10(n)) + 1

# Check if it's a prime number
def isPrime(n):
	i = 2
	limit = int(math.sqrt(n))

	while i <= limit:
		if n % i == 0:
			return 0
		i = i + 1

	return 1

# Check if it's double squared	
def isDoubleSquare(n):
	x = math.sqrt(n/2)
	if x - int(x) == 0:
		return True
	else:
		return False

# Better version of checking a prime number using the AKS primality check
def checkPrime(n):
	if n == 2 or n == 3:
		return True

	if n % 2 == 0 or n % 3 == 0:
		return False

	i = 5
	w = 2

	# 6n+1 and 6n-1 check
	while i * i <= n:
		if n % i == 0:
			return False

		i += w
		w = 6 - w

	return True

# Check if number is pandigital
def checkPandigital(n):
	pandigital = ""
	
	#sorted the number
	s = ''.join(sorted(str(n)))

	# generate pandigital numbers according the number of digits
	for i in range(1, len(s)+1):
		pandigital += str(i)


	if s == pandigital:
		return True
	else:
		return False

# Check if the number is both prime and pandigital
def isPrime_n_isPandigital(n):
	x = checkPrime(n)
	y = checkPandigital(n)

	if x and y == True:
		return True
	else:
		return False

# Generate all permutations
def genAllPandigitals():
	s = "0123456789"
	arr = [''.join(i) for i in itertools.permutations(s)]
	return arr

# Generate all factors of a number
def factors(n):
	list = []

	# for i in range(1, n + 1):
	for i in range(1, n):
		if n % i == 0:
			list.append(i)
	
	return list

# Generate all prime factors
def primeFactors(n):
	list = []
	factor = 2

	while n > 1:
		while n % factor == 0:
			list.append(factor)
			n = n / factor
		factor = factor + 1

	return list

def primeFactorsTwo(n):
	i = 2
	factors = []
	while i * i <= n:
		if n % i:
			i += 1
		else:
			n /= i
			factors.append(i)
	if n > 1:
		factors.append(n)
	return set(factors)

def num_of_prime_factors(n):
	return len(primeFactorsTwo(n))

# Check if the number is a palindrome
def checkPalindrome(n):
	num_str = str(n)
	rev_str = num_str[::-1]

	if num_str == rev_str:
		return True
	else:
		return False

# Return the largest palindrome product within a given range
def largestPalindromeProduct(start, end):
	max_prod = 0

	for i in range(start, end+1):
		for j in range(start, end+1):
			
			temp_prod = i * j

			# Check if it's a palindrome
			if checkPalindrome(temp_prod) == True:
				if temp_prod > max_prod:
					max_prod = temp_prod

	return max_prod

# Greatest Common Divisor
def gcd(a,b):
	if a == b or b == 0:
		return a
	else:
		return gcd(b, a % b)

# Least Common Divisor
def lcm(a,b):
	return (a*b) / gcd(a,b)

# Smallest Multiple
def smallestMultiple(n):
	lcm_count = 1

	for i in range (1, n+1):
		lcm_count = lcm(i, lcm_count)

	return lcm_count

# Sum of numbers
def sumOfNumbers(n):
	return (n*(n+1))/2

# Sum of Squares Formula
def sumOfSquares(n):
	return ((n*(n+1))*((2*n)+1))/6

# Square of Sum Formula
def squareOfSum(n):
	total = (n*(n+1))/2
	return pow(total, 2)	

# Largest Product in a series
def largestProdInSeries(str, limit):
	maxProd = 0

	for i in range(0, len(str)):
		if i + (limit-1) < len(str):

			count = 0
			prodSeries = ""
			tempProd = 1

			while count != limit:
				prodSeries += str[i]
				i += 1
				count += 1

			for j in range(0, len(prodSeries)):
				tempProd *= int(prodSeries[j])

			if tempProd > maxProd:
				maxProd = tempProd

	return maxProd

# Generate a list of primes
def genPrimesOne(n):
	list = []
	i = 2
	count = 0
	
	while count != n:
		if isPrime(i) == 1:
			list.append(i)
			count += 1
		i += 1

	return list

# Generate a list of primes - Sieve of Eratosthenes
def genPrimesTwo(n):
	p = 2

	list = []
	primes = [True for i in range(n)]

	while p * p <= n:
		if primes[p] == True:

			# Update any number that is a multiple of p to False
			for i in range(p * 2, n, p):
				primes[i] = False
		p += 1

	for i in range(2, len(primes)-1):
		if(primes[i] == True):
			list.append(i)

	return list

# Sum of a list of primes
def sumOfPrimesList(list):
	return sum(list)

# Product in a grid - diagonal downright
def prGrid_diagDR(r,c,grid):
	maxProd = 0
	for i in range(0,r-3):
		prod = 0
		for j in range(0,c-3):
			prod = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]				
			# str = grid[i][j], grid[i+1][j+1], grid[i+2][j+2], grid[i+3][j+3], prod
			# print str
			if prod > maxProd:
				maxProd = prod
	return maxProd

# Product in a grid - diagonal downleft
def prGrid_diagDL(r,c,grid):
	maxProd = 0
	for i in range(0,r-3):
		for j in range(3,c):
			prod = grid[i][j] * grid[i+1][j-1] * grid[i+2][j-2] * grid[i+3][j-3]				
			# str = grid[i][j], grid[i+1][j+1], grid[i+2][j+2], grid[i+3][j+3], prod
			# print str
			if prod > maxProd:
				maxProd = prod
	return maxProd			

# Product in a grid - rows
def prGrid_rows(r,c,grid):
	maxProd = 0
	for i in range(0,r):
		for j in range(0,c-3):
			prod = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]				
			# str = grid[i][j], grid[i+1][j+1], grid[i+2][j+2], grid[i+3][j+3], prod
			# print str
			if prod > maxProd:
				maxProd = prod
	return maxProd			

# Product in a grid - columns
def prGrid_cols(r,c,grid):
	maxProd = 0
	for i in range(0,r-3):
		for j in range(0,c):
			prod = grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j]				
			# str = grid[i][j], grid[i+1][j+1], grid[i+2][j+2], grid[i+3][j+3], prod
			# print str
			if prod > maxProd:
				maxProd = prod
	return maxProd

# Generate Triangular Numbers
def triangularSeries(n):
	list = []
	for i in range(1,n+1):
		list.append(sumOfNumbers(i))
	return list

# Trial Division
def trialDivision(n):
	count = 0
	size = int(math.sqrt(n))

	for i in range(2,size+1):
		if n % i == 0:
			count += 2

	if size * size == n:
		count -= 1

	return count

# Factorial
def factorial(n):
	if n <= 1:
		return 1
	else:
		return n * factorial(n-1)

# Collatz Sequence
def collatzSequence(n):
	count = 0
	while n != 1:
		if n > 0:
			if n % 2 == 0:
				n = n/2
			elif n % 2 != 0:
				n = (3*n)+1
			count += 1

	return count+1

# Largest Collatz Sequence
def largestCollatzSequence(n):
	largeTerms = 0
	largeNumber = 0
	for i in range(2,n+1):
		terms = collatzSequence(i)
		if terms > largeTerms:
			largeNumber = i
			largeTerms = terms
	return largeNumber

# Combinations - Refer to the equation from:
# https://en.wikipedia.org/wiki/Combination
# n = number of moves which is going to be 2n
# k = number of elements
def combinations(n):
	k = n
	return (factorial(2*n))/(factorial(k) * factorial((2*n)-k))

# Number to Words
def num_to_words():
	# a dictionary of number words
	number_words = {
		1 : 'one',	2 : 'two',	3 : 'three',
		4 : 'four',	5 : 'five',	6 : 'six',	
		7 : 'seven', 8 : 'eight', 9 : 'nine',	
		10 : 'ten',	11 : 'eleven',	12 : 'twelve',	
		13 : 'thirteen', 14 : 'fourteen', 15 : 'fifteen',
		16 : 'sixteen',	17 : 'seventeen', 18 : 'eighteen',	
		19 : 'nineteen', 20 : 'twenty',	30 : 'thirty',	
		40 : 'forty', 50 : 'fifty',	60 : 'sixty',	
		70 : 'seventy',	80 : 'eighty',	90 : 'ninety',	
		100 : 'hundred', 1000 : 'thousand'
	}

	num_str = ""

	for i in range(1, 1001):

		x = str(i)

		# numbers from 1 to 20
		if i >= 1 and i <= 20:
			num_str += number_words[i]

		# numbers from 21 to 99
		elif i >= 21 and i <= 99:
			# if the second digit is not a zero
			if x[1] != '0':
				num_str += number_words[int(x[0]) * 10] + number_words[int(x[1])]
			else:
				num_str += number_words[int(x[0]) * 10]

		# numbers from 100 to 999
		elif i >= 100 and i <= 999:
			# if the second digit is zero and third digit is zero
			if x[1] == '0' and x[2] == '0':
				num_str += number_words[int(x[0])] + number_words[100]

			# if the second digit is zero and third digit is not zero
			elif x[1] == '0' and x[2] != '0':
				num_str += number_words[int(x[0])] + number_words[100] + 'and' + number_words[int(x[2])]

			# if the second digit is not zero and third digit is zero
			elif x[1] != '0' and x[2] == '0':
				num_str += number_words[int(x[0])] + number_words[100] + 'and' + number_words[int(x[1]) * 10]

			# if the second digit is not zero and third digit is not zero
			elif x[1] != '0' and x[2] != '0':
				# if the second digit is one and third digit is less than or equal to 9
				if int(x[1]) == 1 and int(x[2]) <= 9:
					num_str += number_words[int(x[0])] + number_words[100] + 'and' + number_words[int(x[1]+x[2])]
				else:
					num_str += number_words[int(x[0])] + number_words[100] + 'and' + number_words[int(x[1]) * 10] + number_words[int(x[2])]

		# if the number is 1000
		elif i == 1000:
			num_str += number_words[1] + number_words[1000]

	return num_str

# Return the maximum path sum in a triangle
# Bottom Up Approach
def maxPathSum(list):
	# the last number of the list
	last = len(list)

	# number of rows in the triangle
	nrow = 1

	# count the number of rows in the triangle
	# use the sum of numbers method to count the number of rows
	while sumOfNumbers(nrow) < last:
		# print (sumOfNumbers(nrow))
		nrow += 1

	last -= 1

	for i in range(nrow, 0, -1):
		# print list[last - i]

		# iterate through each number in each row
		for j in range(2, i+1):
			# pick a number from the row above the current row
			# and pick the 2 numbers from the current row
			# Find the max between the two numbers and add it
			list[last - i] = list[last - i] + max(list[last - 1], list[last])
			
			# shift to the next number in the row above
			last -= 1

		# shift to the next number in the row above
		last -= 1

	# return the max sum
	return list[0]

# Check if it's a leap year
def isLeapYear(n):
	if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
		return True
	return False

# Counting Sundays
def countingSundays(start_year, end_year):
	counter = 0
	x = 1

	years = [
		[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31], # leap year
		[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	]

	for i in range(start_year, end_year):
		y = 0

		# check if it's a leap year
		if not isLeapYear(i):
			y = 1

		# iterate each month
		for j in range(0, 12):
			x += years[y][j]

			# check if it's a sunday
			if x % 7 == 0:
				counter += 1

	return counter

# Factorial digit sum
def factorialDigitSum(n):
	return sum(map(int, str(factorial(n))))

# Amicable numbers
def amicableNumbers(n):
	total = 0
	for i in range(1, n+1):
		saveA = i
		a = 0
		b = sum(factors(saveA))

		saveB = b
		a = sum(factors(saveB))

		# if it's an amicable pair, add them
		if a == saveA and b == saveB and a != b:
			total += a

	return total

# Get Sum of Proper Divisors
def getSumOfDivisors(n):
	total = 0
	limit = int(math.sqrt(n))
	i = 1

	while i <= limit:
		if n % i == 0:
			# if the divisors are equal, take one of them
			if (n/i) == i:
				total = total + i
			# take both
			else:
				total = total + i
				total = total + (n/i)
		i += 1

	# Sum of proper divisors: sum - the actual number
	return total - n

# Check if number is abundant, perfect or deficient
def isPerfectNumber(n):
	if getSumOfDivisors(n) > n:
		return 1
	elif getSumOfDivisors(n) < n:
		return -1
	else:
		return 0

# Swap numbers in a list
def swap(list, i, j):
	list[i], list[j] = list[j], list[i]

# Get the next permutation
def nextPermutation(list):
	
	i = len(list) - 1

	# As long as the f(x-1) >= f(x), decrement the first index
	while list[i-1] >= list[i]:
		i = i-1

	j = len(list)

	# As long as the f(y-1) <= f(x-1), decrement the second index
	while list[j-1] <= list[i-1]:
		j = j-1

	# make a swap
	swap(list, i-1, j-1)

	i = i+1
	j = len(list)

	# keep swapping until you get the next permutation
	while i < j:
		swap(list, i-1, j-1)
		i = i+1
		j = j-1

	return list

# Repeating decimals
def repeatingDecimals(n):
	return int(((pow(10, n) - 1)/n)/10);

# Coin Sum
def coinSum(coins, total):
	combinations = [0] * (total+1)
	combinations[0] = 1

	for i in range(0, len(coins)):
		for j in range(coins[i], total+1):
			combinations[j] += combinations[j - coins[i]]

	return combinations[len(combinations)-1]

# Convert Base 10(Decimal) to Base 2(Binary)
def base10tobase2(n):
	s = ""

	while n > 0:
		rem = n % 2
		s += str(rem)
		n /= 2

	return s[::-1]

# right to left
def rtl_truncate(n):
	arr = []
	
	while n > 0:
		arr.append(n)
		n = n / 10
		
	return arr

# left to right
def ltr_truncate(n):
	arr = []
	digits = len(str(n))
	
	for i in range(digits, 0, -1):
		mod = pow(10,i)
		arr.append(n%mod)

	return arr

# Generate hexagonal number
def hexagonalNumber(n):
	return (n * ((2 * n) - 1))

# Check if it's a hexagonal number
def isHexagonalNumber(n):
	x = ((math.sqrt((8 * n) + 1) + 1) / 4)

	if x == int(x):
		return True
	else:
		return False

# Generate pentagonal number
def pentagonalNumber(n):
	return ((n * ((3 * n) - 1)) / 2)

# Check if it's a pentagonal Number
# https://www.en.wikipedia.org/wiki/Pentagonal_Number
def isPentagonalNumber(n):
	x = ((math.sqrt((24 * n) + 1) + 1) / 6)

	if x == int(x):
		return True
	else:
		return False

# Generate a triangle number
def triangleNumber(n):
	return (n * (n+1))/2;

# Check if it's a triangular number
def isTriangularNumber(n):
	x = math.sqrt((8*n)+1)
	if x - int(x) == 0.0:
		return True
	else:
		return False

# Generate List of Triangle numbers
def genTriangularNumbers(n):
	arr = []

	for i in range(1, n+1):
		num = triangleNumber(i)
		print(isTriangularNumber(num))
		arr.append(num)

	return arr

# Calculate words to numbers
def words_to_numbers(s):
	count = 0
	reference = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for i in range(0, len(s)):
		count += (reference.find(s[i]) + 1)
	return count

# Split pandigitals by 3 characters
# Made for Problem 43
def split_pandigital(s):
	arr = [s[i:i+3] for i in range(0, len(s) - 2)]
	return arr

# Split string by any number of characters
def split_str_by_n_chars(s, n):
	arr = [s[i:i+n] for i in range(0, len(s), n)]
	return arr

# Largest Consecutive Primes -- Problem 50
def consec_primes(limit):
	primes = genPrimesTwo(limit/2)
	maxTotal = 0
	maxCount = 1

	for i in range(0, len(primes)):
		total = 0
		count = 1
		for j in range(i, len(primes)):
			total += primes[j]

			# if it reached it's limit, break
			if total >= limit:
				break

			# if it's a prime
			if checkPrime(total):
				# save the max total
				if count > maxCount:
					maxTotal = total
					maxCount = count

			count += 1

	return "Total: %d ++++ Terms: %d" % (maxTotal, maxCount)

# Character frequency
def character_frequency(s):
	freq = {}
	for i in s:
		if i in freq:
			freq[i] += 1
		else:
			freq[i] = 1
	return freq

# Prime Digits Replacement
def prime_digit_replacement(num):
	temp = []
	s = list("123456789")
	x = list(str(num))

	digits = num_digits(num)

	if digits == 2:
		x[0] = '*'
		x = "".join(x)
	else:
		x = "".join(x)
		ch = str(character_frequency(x).keys()[0])
		x = x.replace(ch, '*')

	for i in range(0, len(s)):
		t = x.replace('*', s[i])
		if checkPrime(int(t)):
			temp.append(t)

	return temp

# Problem 51
def problem51(digit_limit, series_limit):
	# Generate a list of primes
	primes = genPrimesTwo(200000)

	small_prime = 0

	for i in range(0, len(primes)):
		digits = num_digits(primes[i])

		if(digits == digit_limit):

			# generate a series of numbers
			replaced_series = prime_digit_replacement(primes[i])
			if len(replaced_series) == series_limit:
				small_prime = replaced_series[0]
				break

	return small_prime

# Is permutation
def is_permutation(num1, num2):
	x = ''.join(sorted(num1))
	y = ''.join(sorted(num2))
	if x == y:
		return True
	return False

# Problem 52
def problem52(start, end):
	saveNum = 0

	for i in range(start, end):
		count = 1
		for j in range(2, 7):
			if is_permutation(str(i), str(i*j)):
				count += 1

		if count == 6:
			saveNum = i
			break

	return saveNum

def combinatoric_selection(n, r):
	return (factorial(n)/((factorial(r)) * factorial(n-r)))

def problem_53(combinations):
	count = 0
	for i in range(1, combinations):
		for j in range(1, i):
			if combinatoric_selection(i,j) > 1000000:
				count += 1
	return count

# Count the number of lychrel numbers below ten-thousand
def lychrel_numbers():
	lychrel_list = []
	for i in range(1, 10001):
		x = i
		y = int(str(x)[::-1])
		z = x + y
		counter = 0
		while not checkPalindrome(z):
			z = z + int(str(z)[::-1])
			if counter < 50:
				counter += 1
			else:
				# print "%d is a lychrel number" % (x)
				lychrel_list.append(x)
				break
	print(len(lychrel_list))

# Powerful Digit Sum. Find max digit sum in which a,b < 100
def pow_digit_sum():
	max_sum = 0
	for a in range(1, 100):
		for b in range(1, 100):
			x = a**b
			total = sum(map(int, str(x)))
			if total > max_sum:
				max_sum = total
	print(max_sum)

# Square root convergents
def square_root_conv():
	numerator = 3
	denominator = 2
	expansions = 1000
	count = 0
	for i in range(0, expansions):
		numerator += 2 * denominator
		denominator = numerator - denominator
		if num_digits(numerator) > num_digits(denominator):
			count += 1
	print(count)