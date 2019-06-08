def hanoi(n, s="start", z="ziel", h="hilf"):
    if n == 0:
        return
    else:
        # H1
        hanoi(n - 1, s, h, z)
        # H2
        print("bewege von " + s + " nach " + z)
        # H3
        hanoi(n - 1, h, z, s)


hanoi(4)
