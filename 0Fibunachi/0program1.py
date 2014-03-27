def nth_fibonacci(n):
    a,b=1,1
    for i in range(n-1):
    	a,b=b,a+b
    return a
def main():
	print(nth_fibonacci(1))
	print(nth_fibonacci(3))
	print(nth_fibonacci(10))
if __name__ == '__main__':
	main()

