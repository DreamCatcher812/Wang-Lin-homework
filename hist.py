def distribute(li,k):
    maxn = max(li)
    minn = min(li)
    len = (maxn - minn)/k
    dic = {str(i+1):0 for i in range(0,k)}
    for i in li:
        if i == maxn:
            dic[str(k)] = dic[str(k)] + 1
        elif i == minn:
            dic["1"] = dic["1"] + 1
        else:
            key = int((i-minn)/len)+1
            dic[str(key)] = dic[str(key)]+1
    return list(dic.values())

assert distribute([1.25 , 1 , 2 , 1.75], 2 ) == [2 , 2]

