def prime_factorization(num):
    
    def factors(n):
        return [x for x in range(1,n+1) if not n%x]

    def is_prime(n):
        return len(factors(n)) == 2

    def prime_factors(n):
        return list(filter(is_prime, factors(n)))

    print('prime factors: ')

    while True:
        if is_prime(num):
            print(num)
            break
        else:
            print(prime_factors(num)[0])
            num = int(num / prime_factors(num)[0])
            