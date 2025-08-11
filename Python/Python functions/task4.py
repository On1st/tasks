def count_primes(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    return sum(1 for x in lst if is_prime(x))

print(count_primes([2, 3, 4, 5, 10, 11]))
print(count_primes([12, 15, 17, 19, 20]))
