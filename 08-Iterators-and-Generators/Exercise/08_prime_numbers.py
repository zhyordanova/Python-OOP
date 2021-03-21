def get_primes(nums):
    for num in nums:
        if num < 2:
            continue
        is_prime = True
        for i_num in range(2, num):
            if num % i_num == 0:
                is_prime = False
                break
        if is_prime:
            yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
