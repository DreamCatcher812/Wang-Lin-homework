def get_primes(x):
    li = []
    i = 2
    for i in range(2, x+1):
        j = 2
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            li.append(i)

    return li
# print(get_primes(11))
assert [2 , 3 , 5 , 7 , 11] == sorted ( get_primes ( 11 ) )

