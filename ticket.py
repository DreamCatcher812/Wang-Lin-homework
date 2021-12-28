
def get_nearest_lucky_ticket(n):
    i = 0
    while i <= n:
        li = list(map(int, str(n + i)))
        a = sum(li[0::2])
        b = sum(li[1::2])
        if a == b:
            return n + i
        li = list(map(int, str(n - i)))
        a = sum(li[0::2])
        b = sum(li[1::2])
        if a == b:
            return n - i
        i += 1


assert get_nearest_lucky_ticket(111111) == 111111
assert get_nearest_lucky_ticket(123321) == 123321
assert get_nearest_lucky_ticket(123320) == 123321
assert get_nearest_lucky_ticket(333999) == 334004
