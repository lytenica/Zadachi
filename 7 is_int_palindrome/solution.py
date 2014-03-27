def is_int_palindrom(n):
	if str(n)==str(n)[::-1]:
		return True
	else:
		return False
def main():
	print(is_int_palindrom(231))
if __name__ == '__main__':
	main()
