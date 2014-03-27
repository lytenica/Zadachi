def count_consonants(str):
	vlowels = len(str)
	for item in str.lower():
		if item == 'a':
			vlowels -= 1
		if item == 'e':
			vlowels -= 1
		if item == 'i':
			vlowels -= 1
		if item == 'o':
			vlowels -= 1
		if item == 'u':
			vlowels -= 1
		if item == 'y':
			vlowels -= 1
		if item == ' ':
			vlowels -=1
		if item =='!':
			vlowels -=1
	return vlowels
def main():
	print(count_consonants("Python"))
if __name__ == '__main__':
	main()
