from math import sqrt
# Find the sum of all the primes below two million.
def euler_10():
	current = 2
	prime_sum = 1

	while current < 2000000:
		if is_prime(current):
			prime_sum += current
		current += 1
	return prime_sum

def euler_10_plus():
	current = 2
	prime_sum = 1

	for next_prime in prime_generator(2):
		if next_prime < 2000000:
			prime_sum += next_prime
		else:
			return prime_sum

def is_prime(n):
	if n < 1:
		return False
	if n == 1 or n == 2:
		return True
	for i in range(3, int(sqrt(n) + 1), 2):
		if n % i == 0:
			return True
	return False

def prime_generator(current):
	while True:
		if is_prime(current):
			yield current
		current += 1



print('Running traditional algorithm...')
print(euler_10())
print('Running generator algorithm...')
print(euler_10_plus())







