def distance(target, source, insertcost, deletecost, replacecost):
    n = len(target)+1
    m = len(source)+1
    dist = [[0 for j in range(m)] for i in range(n)]
    for i in range(1,n):
        dist[i][0] = dist[i-1][0] + insertcost
    for j in range(1,m):
        dist[0][j] = dist[0][j-1] + deletecost
    for j in range(1,m):
        for i in range(1,n):
            inscost = insertcost + dist[i-1][j]
            delcost = deletecost + dist[i][j-1]
            if (source[j-1] == target[i-1]):
                add = 0
            else:
                add = replacecost
            substcost = add + dist[i-1][j-1]
            dist[i][j] = min(inscost, delcost, substcost)

    src = ""
    targ = ""
    mid = ""
    srcIdx = len(source) - 1
    targIdx = len(target) - 1
    y = n - 1
    x = m - 1
    add = 0
    step = 0

    while(y > 0 and x > 0):
        diagFlag = 0
        inscost = insertcost + dist[y-1][x]
        delcost = deletecost + dist[y][x-1]
        substcost = replacecost + dist[y-1][x-1]
        short = min(inscost, delcost, substcost)

        if(dist[y-1][x-1] == dist[y][x] and min(dist[y][x], dist[y-1][x], dist[y][x-1]) == dist[y][x]):
            src += source[srcIdx]
            mid += "|"
            targ += target[targIdx]
            targIdx -= 1
            srcIdx -= 1
            y -= 1
            x -= 1
        elif(inscost == short and delcost == short and substcost == short):
            src += source[srcIdx]
            mid += " "
            targ += target[targIdx]
            y -= 1
            x -= 1
            srcIdx -= 1
            targIdx -= 1
        elif(delcost == short):
            targ += "_"
            mid += " "
            src += source[srcIdx]
            srcIdx -= 1
            x -= 1
        else:
            targ += target[targIdx]
            mid += " "
            src += "_"
            targIdx -= 1
            y -= 1
        step += 1
    if (x > 0):
        while (x > 0):
            targ += "_"
            mid += " "
            src += source[srcIdx]
            srcIdx -= 1
            x -= 1
    if (y > 0):
        while (y > 0):
            targ += target[targIdx]
            mid += " "
            src += "_"
            targIdx -= 1
            y -= 1
    targ = targ[::-1]


    src = src[::-1]
    mid = mid[::-1]

    print(targ)
    print(mid)
    print(src)
    return dist[n-1][m-1]

if __name__ == "__main__":
    from sys import argv
    if len(argv) > 2:
        print("levenshtein distance =", distance(argv[1], argv[2], 1, 1, 2))


