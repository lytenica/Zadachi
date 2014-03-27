def count_substrings(haystack, needle):
    start = haystack.find(needle)
    count = -1
    if start != -1:
        count = count + 1
        while start != -1:
            count += 1
            start += len(needle)
            start =haystack.find(needle, start)
        return count
def main():
    print(count_substrings("dasda", "baba"))
if __name__ == '__main__':
    main()
