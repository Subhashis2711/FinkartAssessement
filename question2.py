def add(list1, key):
    hash = set()
    result = None

    for i in list1:
        if (key-i) in hash:
            result = (i, key-i)
        else:
            hash.add(i)
    
    return result

list1 = [1, 2, 3 ,4]
print(add(list1, 5))