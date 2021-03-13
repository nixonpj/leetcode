def symmetric_check(nodes):
    n = len(nodes)
    for i in range((n//2)):
        print(i)
        if nodes[i]!=nodes[n-1-i]:
            return False
    return True


print(symmetric_check([1,2,1,2,1]))
