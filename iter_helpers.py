import itertools
def transpose(li):
    return itertools.zip_longest(li[0],li[1],fillvalue='anything')

expected = [[1, 2], [-1, 3]]
actual = transpose([[1, -1], [2, 3]])
assert expected == list(map(list, actual))
print(list(transpose([[1, -1], [2, 3]])))


def scalar_product(li1 , li2):
        try:
                 return sum(list(map(lambda i, j: int(str(i),0) * int(str(j),0), li1, li2)))

        except ValueError:
                return None

expected = 1
actual = scalar_product([1, '2'], [-1, 1])
assert expected == actual
actual = scalar_product([1, 'xyz'], [-1, 1])
assert actual is None