def sum_of_digits(n):
	sumA=0
	while n!=0:
		sumA= sumA + n%10
		n=n//10	
	return sumA
def main():
	print(sum_of_digits(1325132435356))
	print(sum_of_digits(123))
	print(sum_of_digits(6))
if __name__ == '__main__':
	main()