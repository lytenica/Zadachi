def sum_of_min_and_max(arr):
	maxel = 0

	for item in arr:
		if item > maxel:
			maxel = item
	minel = maxel
	for item in arr:
		if item < minel:
			minel = item

	return minel + maxel



def main():
	arr = [1,2,3,4,5,6,8,9]
	print(sum_of_min_and_max(arr))
if __name__ == '__main__':
	main()