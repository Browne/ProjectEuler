def euler_1():
	'''Print the sum of divisors of 3/5 between 1-999'''
	sum = 0
	for x in range (1, 1000):
		if ((x % 3 == 0) or (x % 5 == 0)):
			sum = sum + int(x)
	print (sum)

def euler_2():
	'''Print the sum of even fib numbers between 0 and 4million'''
	prev, cur = 0, 1
	total = 0
	while True:
	    prev, cur = cur, prev + cur
	    if cur >= 4000000:
	        break
	    if cur % 2 == 0:
	        total += cur
	print(total)

def euler_3():
	'''Find the highest prime factor of 600851475143'''
	c, n = 2, 600851475143
	while c * c < n:
		while n % c == 0:
			n = n/c
		c = c + 1
	print(n)

def euler_4():
	'''Find largest palindrome between 0 and 999*999'''
	isPali = lambda x: str(x) == str(x)[::-1]
	# palis = []
	largest = 0
	y = 999*999
	# for x in range (y, 1000, -1):
	'''Put all palindromes in a list, largest first'''
	for i in range (999, 100, -1):
		for j in range (999, 100, -1):
			x = i*j
			if (x > largest) and isPali(x):
				largest = x
			# return 1;
	print largest
	# 		palis.append(x)
	# print palis[:7]
	# for pali in palis[:7]:
	# 	print helper_4(pali)
		
# def helper_4(pali):
# 	'''Get the factors of a passed value)'''
# 	result = set()
# 	for i in range(1, int(pali ** 0.5) + 1):
# 		div, mod = divmod(pali, i)
# 		if mod == 0:
# 			result |= {i, div}
# 	return result

def euler_5():
	'''Smallest +ve number that is divisible by all of 1 to 20'''
	divisors = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
	x = 2520
	i = 0
	while True:
		if (x % divisors[i] != 0):
			x = x + 20 #Has to be a multiple of 20!
			i = 0 #Reset i to restart
		elif (i >= 9):
			'''If we've reached the end of divisors we're finished'''
			print x
			return True	
		else:	
			i = i + 1	
		
def euler_6():
	'''Calculate the difference between sum of squares and square of the sum for [1..100]'''
	SquareOfSums = 0
	sumOfSquares = 0
	for x in range (1, 101, 1):
		SquareOfSums = SquareOfSums + x
		sumOfSquares = sumOfSquares + (x**2)
	SquareOfSums = SquareOfSums**2
	print (SquareOfSums - sumOfSquares)	

def helper_7():
	'''Generate prime numbers, from http://code.activestate.com/recipes/117119/'''
	D = {}
	q = 2  
	while True:
		if q not in D: 
			yield q        
			D[q * q] = [q]
		else:
			for p in D[q]:
				D.setdefault(p + q, []).append(p)
			del D[q]
		q += 1
	n = 10001

def euler_7():
	'''Find the 10001 prime number'''
	n = 10001	
	return (j for i,j in enumerate(helper_7()) if i == n-1).next()


def euler_8():
	pass


euler_1()
euler_2()
euler_3()		
euler_4()
euler_5()
euler_6()
print euler_7()