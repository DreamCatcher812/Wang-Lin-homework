def compress(li):
    n = len(li)
    dict = {}
    while n>0:
        if str(li[n-1]) in dict.keys() :
            dict[str(li[n - 1])] = dict[str(li[n-1])] + 1
        else:
            dict[str(li[n-1])] = 1
        n = n-1
    for key, value in dict.items():

          return [(int(key), value) for key, value in dict.items()]

expected_sorted = [(1, 2), (2, 1), (3, 1)]
actual_sorted = sorted(compress([1, 2, 1, 3]))
assert expected_sorted == actual_sorted

