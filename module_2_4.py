numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] # Дан список чисел
primes = [] # составить  список содержащий простые числа
not_primes = [] # составить  список содержащий непростые числа
for i in numbers: # при помощи цикла перебираем список
    if i == 1:
        continue
    is_prime = True  # перменный флаг
    for j in range(2, i): # цикл (вложенный). подбираются делители для числа из 1го цикла
        if i % j == 0:
            is_prime = False # перменный флаг
            break
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)
print('primes:', primes)
print('not_primes:', not_primes)
