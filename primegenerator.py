def prime_generator(n):
    if not isinstance(n, int):
        raise TypeError
    
    elif n < 2:
        return "The number has to be greater than 1"
    
    #added two to my list since two will not get tested in the for loop
    prime_nums = [2]    
    for num in range(2, n+1):
        #optimized with trial division and added two due to
        #truncation effect of int() function
        for divisor in range(2, int(num**(1/2.0) + 2)):
            if num % divisor == 0:
                break
        else:
            prime_nums.append(num)

    return  prime_nums
