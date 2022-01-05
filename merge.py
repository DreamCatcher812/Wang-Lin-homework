def merge(li1,li2):
    x = []
    i = 0
    j = 0
    len1 = len(li1)
    len2 = len(li2)
    while i<len1 or j<len2:
        if j>=len2 or (i<len1 and li1[i]<li2[j]):
            x.append(li1[i])
            i += 1
        else:
            x.append(li2[j])
            j += 1
    if type(li1)==tuple:
        x = tuple(x)
    return x
print(merge([1 , 2 , 7], [3]))
print(merge(( 3 , 15 ) , (7 , 8 ) ))
assert merge([1 , 2 , 7], [3]) == [1 , 2 , 3 , 7]
assert merge(( 3 , 15 ) , (7 , 8 ) ) == (3 , 7 , 8 , 15 )
