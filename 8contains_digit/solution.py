def contains_digit(number, digit):
	while number>0:
		if number%10==digit:
			return True
		else:
		    return False
def main():
	print(contains_digit(123,4))
if __name__ == '__main__':
	main()
