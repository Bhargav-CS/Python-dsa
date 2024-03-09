def covertFive(n):
    for i in n:
        if i == "0":
            n = n.replace(i, "5")

    return n

n = 10000
