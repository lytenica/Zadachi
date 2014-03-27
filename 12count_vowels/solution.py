def count_vowels(str):
	vlowes=0
	for item in str.lower():
		if item=='a':
			vlowes+=1
		if item=='o':
			vlowes+=1
		if item=='e':
			vlowes+=1
		if item=='u':
			vlowes+=1
		if item=='y':
			vlowes+=1
		if item=='i':
			vlowes+=1
	return vlowes
def main():
	print(count_vowels("baba ti dobre li e bee"))
if __name__ == '__main__':
	main()
