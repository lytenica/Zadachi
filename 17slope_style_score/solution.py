
def biggest_difference(arr):
	maxel=0
	bdif=0

	for item in arr:
		if item > maxel:
			maxel = item
	minel = maxel
	for item in arr:
		if item < minel:
			minel = item
	bdif =maxel-minel
	return bdif
def main():
	arr = [1,2,3,4,5]
	print(biggest_difference(arr))
if __name__ == '__main__':
	main()
