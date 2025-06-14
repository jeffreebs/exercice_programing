def prime_number (num):
    if num <= 1:
        return False
    

    for n in range(2,int(num ** 0.5)+1):
        if num % n == 0:
            return False
    return True

def get_primes (list):
    prime= []
    for number in list:
        if prime_number(number):
            prime.append(number)
    return prime

def main():
    list1 = [1,4,6,7,13,9,67]
    prime = get_primes(list1)
    print(f"Prime numbers:{prime}")


if __name__=="__main__":
    main()