def prime_factors(n):
    """Returns the prime factors of n."""
    factors = []
    divisor = 2
    
    while n > 1:
        if n % divisor == 0:
            factors.append(divisor)
            n /= divisor
        else:
            divisor += 1
            
    return factors
    print(factors)

n=int(input())
prime_factors(n)
