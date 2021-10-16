# Правильное решение, но неэффективное еще и долгое для компуктера
def prime_divisors(number):
    for i in range(number - 1, 1, -1):
        counter = 0
        if number % i == 0:
            for j in range(i - 1, 1, -1):
                if i % j == 0:
                    counter += 1
            if counter == 0:
                return i


print(prime_divisors(600851475143))

"""
Правильное решение:
def prime_divisors(number):
    counter = 0
    while number != 1:
        counter += 1
        if number % counter == 0:
            number /= counter
    return counter
    
    
print(prime_divisors(600851475143))
"""
