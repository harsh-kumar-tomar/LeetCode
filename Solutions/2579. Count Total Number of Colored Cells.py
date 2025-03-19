def coloredCells(n: int) -> int:
    if n == 1:
        return 1

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    totalPoints = {(0,0)}
    s = {(0, 0)}
    n -= 1

    while n != 0:
        tempSet = set()
        for coordinates in s:
            x,y = coordinates
            for dir in directions:
                X,Y = dir
                tempSet.add((x+X,y+Y))

        n -= 1
        s = tempSet
        totalPoints.update(tempSet)

    print(totalPoints)

    return len(totalPoints)

a = coloredCells(3)
print(a)
