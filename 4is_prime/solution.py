def is_prime(n):
    if n<0:
        return False
    if n%2==0 and n%3==0:
        return False
    else:
        return True

def main():
    print(is_prime(5))
if __name__ == '__main__':
        main()
