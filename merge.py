def merge(l1,l2):
    x = []
    i = 0
    j = 0
    len1 = len(l1)
    len2 = len(l2)
    while i<len1 or j<len2:
        if j>=len2 or (i<len1 and l1[i]<l2[j]):
            x.append(l1[i])
            i += 1
        else:
            x.append(l2[j])
            j += 1
    if type(l1)==tuple:
        x = tuple(x)
    return x
print(merge([1 , 2 , 7], [3]))
print(merge(( 3 , 15 ) , (7 , 8 ) ))
assert merge([1 , 2 , 7], [3]) == [1 , 2 , 3 , 7]
assert merge(( 3 , 15 ) , (7 , 8 ) ) == (3 , 7 , 8 , 15 )