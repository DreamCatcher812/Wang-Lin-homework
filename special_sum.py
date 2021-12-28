def calculate_special_sum(a):
    sumnumber = 0
    while a>= 1:
        sumnumber = sumnumber + ((a - 1) ** 2) * a
        a = a-1
    else:
        return sumnumber

assert calculate_special_sum ( 3 ) == 14