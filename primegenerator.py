def prime_generator(n):
    if not isinstance(n, int):
        raise TypeError
    
    elif n < 2:
        return "The number has to be greater than 1"
    
    elif n == 2:
        return [2]
    
    elif n == 3:
        return [2, 3]
    
    prime_nums = [2]
    for num in range(3, n+1):
        for divisor in range(2, int(num**(1/2.0) + 2)):
            if num % divisor == 0:
                break
        else:
            prime_nums.append(num)
            
    return  prime_nums

print prime_generator(21)