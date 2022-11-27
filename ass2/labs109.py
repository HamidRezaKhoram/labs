def only_odd_digits(n):
    n = str(n)
    for num in n:
        if int(num) % 2 == 0:
            return False
    return True


def frequency_sort(items):
    itemsSet = list(set(items))
    itemStr = [str(items[i]) for i in range(len(items))]
    itemStr = "".join(itemStr)
    listIndex = []
    for index in itemsSet:
        listIndex.append((index, -items.count(index)))
    sortedTuple = sorted(listIndex, key=lambda x: (x[1], x[0]))
    finalList = []
    for tuple in sortedTuple:
        tempList = [tuple[0] for i in range(-tuple[1])]
        finalList += tempList
    return finalList


def colour_trio(colours):
    length = len(colours)
    tempStr = ""
    firstColor = "r"
    secondColor = "b"
    thirdColor = "r"
    while length > 1:
        for i in range(len(colours) - 1):
            if colours[i] == "r":
                firstColor = "r"
                secondColor = "b"
                thirdColor = "y"
            elif colours[i] == "b":
                firstColor = "b"
                secondColor = "r"
                thirdColor = "y"
            elif colours[i] == "y":
                firstColor = "y"
                secondColor = "b"
                thirdColor = "r"
            if colours[i + 1] == firstColor:
                tempStr += firstColor
            elif colours[i + 1] == secondColor:
                tempStr += thirdColor
            elif colours[i + 1] == thirdColor:
                tempStr += secondColor
        length -= 1
        colours = tempStr
        tempStr = ""

    return colours


def taxi_zum_zum(moves):
    if type(moves) == list:
        moves = "".join(moves)
    if "F" not in moves:
        return (0, 0)
    lastMove = moves.rfind("F")
    realMoves = moves[: lastMove + 1]
    numberOfMoves = realMoves.count("F")
    counter = 0
    firstIndex = 0
    check = 0
    xy = (0, 0)

    while numberOfMoves > counter:
        fIndex = realMoves.find("F")

        tempString = realMoves[firstIndex: fIndex + 1]

        check += 360 - ((tempString.count("L")) * 90) % 360

        check += ((tempString.count("R")) * 90) % 360

        if check >= 360:
            check = check % 360

        if check == 0:
            xy = (xy[0], xy[1] + 1)
        elif check == 180:
            xy = (xy[0], xy[1] - 1)
        elif check == 90:
            xy = (xy[0] + 1, xy[1])
        elif check == 270:
            xy = (xy[0] - 1, xy[1])

        realMoves = realMoves[fIndex + 1:]

        numberOfMoves -= 1

    return xy


def is_cyclops(n):
    n = str(n)
    if len(n) % 2 == 0:
        return False
    eye = int(n[len(n) // 2])

    if eye != 0:
        return False
    otherThanEye = n[: len(n) // 2] + n[len(n) // 2 + 1:]
    if "0" in otherThanEye:
        return False
    return True


def domino_cycle(tiles):
    if len(tiles) == 0:
        return True
    if len(tiles) == 0:
        if tiles[0][0] == tiles[0][1]:
            return True
    list1 = [tiles[i][0] for i in range(len(tiles))]
    list2 = [tiles[i][1] for i in range(len(tiles))]

    list3 = list2[:-1]
    list3.insert(0, list2[-1])
    for i in range(len(list3)):
        if list3[i] != list1[i]:
            return False
    return True


def give_change(amount, coins):
    listOfCoins = []

    for i in coins:
        while amount >= i:
            listOfCoins.append(i)
            amount -= i

    return listOfCoins


def is_ascending(items):

    setList = set(items)

    if len(setList) != len(items):
        return False
    sortList = sorted(items)
    for i in range(len(sortList)):
        if sortList[i] != items[i]:
            return False
    return True



def riffle(items, out=True):
    if len(items) == 0:
        return items
    newList = []
    if out == True:
        newList = items[1:-1]
    else:
        newList = items
    length = int((len(newList)/2))
    newList1 = newList[:length]
    newList2 = newList[length:]

    newList3 = []
    for i in range(length):
        newList3.append(newList2[i])
        newList3.append(newList1[i])
    if out == True :
        newList3.insert(0, items[0])
        newList3.append(items[-1])
    return newList3
        



def three_summers(items, goal):
    for i in range(0, len(items)-2):
        left = i+1; right = len(items)-1
        while(left<right):
            if(items[i]+items[left]+items[right]==goal):
                return True
            elif(items[i]+items[left]+items[right]<goal):
                left+=1
            else:
                right-=1
    return False
    
    

