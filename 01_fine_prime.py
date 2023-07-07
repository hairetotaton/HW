def find_prime_list_under_number(number):
    primes = []
    for num in range(2, number+1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


input = 20
result = find_prime_list_under_number(input)
print(result)
print("-----------------End----------------------")

