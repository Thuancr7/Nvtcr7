def is_prime(n):
    dem = 0
    for i in range(1, n+1):
        if n % i == 0:
            dem +=1
    if dem == 2:
        return True
    return False
print(is_prime(5)) 
