def number_to_list(n):
	arrNumb
	iterator = len(str(n))
	while iterator == 0 :
		arrNumb[iterator]=n%10:
		    n/=10
		    iterator -=1
	return arrNumb
def main():
	print(number_to_list(123))
if __name__ == '__main__':
	main()
