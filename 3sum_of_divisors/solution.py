def sum_of_divisors(n):
	sum=0
	for x in range(1,n+1):
		if n % x== 0:
			sum=sum+x
	return sum
def main():
		print(sum_of_divisors(8))
if __name__ == '__main__':
	main()
