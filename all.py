import time

def euler_1():
	'''Print the sum of divisors of 3/5 between 1-999'''
	start = time.time()
	sum = 0
	for x in range (1, 1000):
		if ((x % 3 == 0) or (x % 5 == 0)):
			sum = sum + int(x)
	elapsed = (time.time() - start)		
	print ("1: %s in %s seconds" %(sum, elapsed))

def euler_2():
	'''Print the sum of even fib numbers between 0 and 4million'''
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
	'''Find the highest prime factor of 600851475143'''
	start = time.time()
	c, n = 2, 600851475143
	while c * c < n:
		while n % c == 0:
			n = n/c
		c = c + 1
	elapsed = (time.time() - start)	
	print ("3: %s in %s seconds" %(n, elapsed))

def euler_4():
	'''Find largest palindrome between 0 and 999*999'''
	start = time.time()
	isPali = lambda x: str(x) == str(x)[::-1]
	largest = 0
	y = 999*999
	'''Put all palindromes in a list, largest first'''
	for i in range (999, 100, -1):
		for j in range (999, 100, -1):
			x = i*j
			if (x > largest) and isPali(x):
				largest = x
	elapsed = (time.time() - start)
	print ("4: %s in %s seconds" %(largest, elapsed))


def euler_5():
	'''Smallest +ve number that is divisible by all of 1 to 20'''
	start = time.time()
	divisors = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
	x = 2520
	i = 0
	while True:
		if (x % divisors[i] != 0):
			x = x + 20 #Has to be a multiple of 20!
			i = 0 #Reset i to restart
		elif (i >= 9):
			'''If we've reached the end of divisors we're finished'''
			elapsed = (time.time() - start)
			print ("5: %s in %s seconds" %(x, elapsed))
			return True	
		else:	
			i = i + 1	
		
def euler_6():
	'''Calculate the difference between sum of squares and square of the sum for [1..100]'''
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

def euler_7():
	'''Find the 10001 prime number'''
	start = time.time()
	n = 10001	
	solution = (j for i,j in enumerate(helper_7()) if i == n-1).next()
	elapsed = (time.time() - start)	
	print ("7: %s in %s seconds" %(solution, elapsed))


def euler_8():
	'''Find the largest product of five numbers in '''
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
	'''a+b+c=1000, a^2 + b^2 = c^2. Find a*b*c'''
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

euler_1()
euler_2()
euler_3()		
euler_4()
#euler_5() #too slow to keep running!
euler_6()
euler_7()
euler_8()
euler_9()