def contains_digits(number, digits):
	exist = False
	numberStr = str(number)
	for item in digits:
		for strItem in numberStr:

			if strItem == str(item):
				exist = True
		if exist == False:
			return False
		exist = False
	return True
def main():
	print(contains_digits(402123,[0, 3, 4]))
if __name__ == '__main__':
	main()
