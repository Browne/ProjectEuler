import time

def euler_1():
	"""Print the sum of divisors of 3/5 between 1-999"""
	start = time.time()
	sum = 0
	for x in range (1, 1000):
		if ((x % 3 == 0) or (x % 5 == 0)):
			sum += int(x)
	elapsed = (time.time() - start)		
	print ("1: %s in %s seconds" %(sum, elapsed))

def euler_2():
	"""Print the sum of even fib numbers between 0 and 4million"""
	start = time.time()
	prev, cur = 0, 1
	total = 0
	while True:
	    prev, cur = cur, prev + cur
	    if cur >= 4000000:
	        break
	    if cur % 2 == 0:
	        total += cur
	elapsed = (time.time() - start)	        
	print ("2: %s in %s seconds" %(total, elapsed))

def euler_3():
	"""Find the highest prime factor of 600851475143"""
	start = time.time()
	c, n = 2, 600851475143
	while c * c < n:
		while n % c == 0:
			n = n/c
		c = c + 1
	elapsed = (time.time() - start)	
	print ("3: %s in %s seconds" %(n, elapsed))

def euler_4():
	"""Find largest palindrome between 0 and 999*999"""
	start = time.time()
	isPali = lambda x: str(x) == str(x)[::-1]
	largest = 0
	y = 999*999
	"""Put all palindromes in a list, largest first"""
	for i in range (999, 100, -1):
		for j in range (999, 100, -1):
			x = i*j
			if (x > largest) and isPali(x):
				largest = x
	elapsed = (time.time() - start)
	print ("4: %s in %s seconds" %(largest, elapsed))


def euler_5():
	"""Smallest +ve number that is divisible by all of 1 to 20"""
	start = time.time()
	divisors = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
	x = 2520
	i = 0
	while True:
		if (x % divisors[i] != 0):
			x = x + 20 #Has to be a multiple of 20!
			i = 0 #Reset i to restart
		elif (i >= 9):
			"""If we've reached the end of divisors we're finished"""
			elapsed = (time.time() - start)
			print ("5: %s in %s seconds" %(x, elapsed))
			return True	
		else:	
			i = i + 1	
		
def euler_6():
	"""Calculate the difference between sum of squares and square of the sum for [1..100]"""
	start = time.time()
	SquareOfSums = 0
	sumOfSquares = 0
	for x in range (1, 101, 1):
		SquareOfSums = SquareOfSums + x
		sumOfSquares = sumOfSquares + (x**2)
	SquareOfSums = SquareOfSums**2
	ans = SquareOfSums - sumOfSquares
	elapsed = (time.time() - start)
	print ("6: %s in %s seconds" %(ans, elapsed))
	
def helper_7():
	"""Generate prime numbers, from http://code.activestate.com/recipes/117119/"""
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
	print (D)	

def euler_7():
	"""Find the 10001 prime number"""
	start = time.time()
	n = 10001	
	solution = (j for i,j in enumerate(helper_7()) if i == n-1).next()
	elapsed = (time.time() - start)	
	print ("7: %s in %s seconds" %(solution, elapsed))


def euler_8():
	"""Find the largest product of five numbers in """
	start = time.time()
	L = ["7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"]
	M = []
	for numbers in L:
			for vars in list(numbers): 
				M.append(vars)
	product = 0
	for x in range(len(M)-4):
		p = int(M[x])*int(M[x+1])*int(M[x+2])*int(M[x+3])*int(M[x+4])
		if p > product:
			product = p
	elapsed = (time.time() - start)		
	print ("8: %s in %s seconds" %(product, elapsed))

def euler_9(): 
	"""a+b+c=1000, a^2 + b^2 = c^2. Find a*b*c"""
	start = time.time()
	sum = 1000
	for a in range(1, sum/3, 1):
		for b in range(a+1, sum/2, 1):
			c = sum - a - b
			if (c > 0) and (a**2 + b**2 == c**2):
				ans = (a*b*c)
				elapsed = (time.time() - start)
				print ("9: %s in %s seconds" %(ans, elapsed))
	return 1		

def helper_10(sieve, x):
    """ Returns  a list of primes < n """
    for i in xrange(x+x, len(sieve), x):
    	sieve[i] = False

def euler_10():
	""" """
	start = time.time()
	sieve = [True] * 2000000
	for x in xrange(2, int(len(sieve) ** 0.5) + 1):
	    if sieve[x]: helper_10(sieve, x)
	ans = sum(i for i in xrange(2, len(sieve)) if sieve[i])
	elapsed = (time.time() - start)
	print ("10: %s in %s seconds" %(ans, elapsed))

def euler_11():
	""" """
	with open ('helpers/data_11', 'r') as f:
		L = [map(int, lines.split(' ')) for lines in f]
	start = time.time()
	max_product = 0

	for i in range(20):
	    for j in range(16):
	        prod = L[i][j]*L[i][j+1]*L[i][j+2]*L[i][j+3]
	        if prod > max_product: max_product = prod
	        prod = L[j][i]*L[j+1][i]*L[j+2][i]*L[j+3][i]
	        if prod > max_product: max_product = prod
	
	for i in range(16):
	    for j in range(16):
	        prod = L[i][j]*L[i+1][j+1]*L[i+2][j+2]*L[i+3][j+3]
	        if prod > max_product: max_product = prod
	for i in range(3,20):
	    for j in range(16):
	        prod = L[i][j]*L[i-1][j+1]*L[i-2][j+2]*L[i-3][j+3]
	        if prod > max_product: max_product = prod
	 
	elapsed = (time.time() - start)
	print '11: {} found in {} seconds'.format(max_product,elapsed)


def euler_12():
	"""What is the value of the first triangle number to have over five hundred divisors?"""
	start = time.time()
	index = helper_12_2(501)
	triangle = (index * (index+1)) / 2
	elapsed = (time.time() - start)
	print '12: {} found in {} seconds'.format(triangle, elapsed)

def helper_12_1(n):
	"""Get the divisors"""
	if n % 2 == 0:
		n /= 2
	divisors = 1
	c = 0
	while n % 2 == 0:
		c += 1
		n /= 2
	divisors *= (c + 1)
	x = 3
	while n != 1:
		c = 0
		while n % x == 0:
			c += 1
			n /= x
		divisors *= (c + 1)
		x += 2
	return divisors


def helper_12_2(floor):
	"""Get index's at location"""
	n = 1
	lnum, rnum = helper_12_1(n), helper_12_1(n+1)
	while lnum * rnum < 500:
		n += 1
		rnum, lnum = helper_12_1(n+1), rnum
	return n
	
def euler_13():
	"""Largest ten digit sum"""
	start = time.time()
	sums = 0 
	with open ('helpers/data_13', 'r') as f:
		for values in f:
			sums += int(values)
		solution = (str(sums)[0:10])
	elapsed = (time.time() - start)
	print '13: {} in {} seconds'.format(solution, elapsed)


if __name__ == '__main__':
	euler_1()
	euler_2()
	euler_3()		
	euler_4()
	euler_5() #too slow to keep running!
	euler_6()
	euler_7()
	euler_8()
	euler_9()
	euler_10()
	euler_11()
	euler_12()
	euler_13()
