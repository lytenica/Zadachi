def prime_number_of_divisors(n):
	sum=0
	for x in range(1,n+1):
		if n%x==0:
			sum=sum+1

	if sum==2 or sum==3:
		return True
	else:
		if sum%2==0 and sum%3==0:
			return True
		else:
			return False
def main():
	print(prime_number_of_divisors(28))
if __name__ == '__main__':
	main()
