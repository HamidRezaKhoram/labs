# def duplicate_digit_bonus(n):
#     n_list = (list(map(int, str(n))))
#     sum = 0
#     in_run = False
#     first_index = []
#     last_index = [] 
#     for i in range(len(n_list)-1):
#         if n_list[i] == n_list[i+1] and not in_run:
#             first_index.append(i)
#             in_run = True
#         elif n_list[i] != n_list[i+1] and in_run:
#             last_index.append(i)

#             in_run = False
#         elif i == len(n_list)-2 and in_run:
#             last_index.append(i+1)
#         if i == len(n_list)-2:
#             if n_list[len(n_list)-2] == n_list[len(n_list)-1]:
#                 last_index.append(len(n_list)-1)
#             else:
#                 last_index.append('no')
#                 first_index.append('no')
#     for i in range(len(first_index)):
#         if i < len(first_index)-1:  
#             sum += 10**(int(last_index[i])-int(first_index[i])-1)
#         elif last_index[i] != 'no' and first_index[i] != 'no':
#             sum += (10**(int(last_index[i])-int(first_index[i])-1))*2
#     if len(str(n)) == 3 and str(n)[0] == str(n)[1] and str(n)[1] != str(n)[2]:
#         return 2
#     return sum




def only_odd_digits(n):
    n = str(n)
    for num in n:
        if int(num) % 2 == 0:
            return False
    return True


def frequency_sort(items):
    itemsSet = list(set(items))
    itemStr = [str(items[i]) for i in range(len(items))]
    itemStr = ''.join(itemStr)
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
    tempStr = ''
    firstColor = 'r'
    secondColor = 'b'
    thirdColor = 'r'
    while length > 1:
        for i in range(len(colours)-1):
            if colours[i] == 'r':
                firstColor = 'r'
                secondColor = 'b'
                thirdColor = 'y'
            elif colours[i] == 'b':
                firstColor = 'b'
                secondColor = 'r'
                thirdColor = 'y'
            elif colours[i] == 'y': 
                firstColor = 'y'
                secondColor = 'b'
                thirdColor = 'r'
            if colours[i+1] == firstColor:
                tempStr += firstColor
            elif colours[i+1] == secondColor:
                tempStr += thirdColor
            elif colours[i+1] == thirdColor:
                tempStr += secondColor
        length -= 1
        colours = tempStr
        tempStr = ''

    return colours


def taxi_zum_zum(moves):
    if type(moves) == list:
        moves = ''.join(moves)
    if "F" not in moves:
        return (0, 0)
    lastMove = moves.rfind('F')
    realMoves = moves[:lastMove+1]
    numberOfMoves= realMoves.count('F')
    counter = 0
    firstIndex = 0
    check = 0
    xy = (0, 0)
    
    while numberOfMoves > counter:
        fIndex = realMoves.find('F')
       
        tempString = realMoves[firstIndex:fIndex+1]
        
           
        check += (360-((tempString.count("L"))*90)%360)

        
        check += ((tempString.count("R"))*90)%360
        
        if check >= 360:
                check = check%360
       
        if check == 0:
            xy = (xy[0], xy[1] + 1)
        elif check == 180:
            xy = (xy[0], xy[1] -1)
        elif check == 90:
            xy = (xy[0] + 1, xy[1])
        elif check == 270:
            xy = (xy[0] - 1, xy[1])
            
        # print(check)
        # print(check)
        realMoves = realMoves[fIndex+1:]
        # print(realMoves)
        numberOfMoves -= 1

    return(xy)

def is_cyclops(n):
    n = str(n)
    print(len(n))
    if len(n) % 2 == 0 :
        return False
    eye = int(n[len(n)//2])
    print(eye)
    if eye != 0:
        return False
    otherThanEye = n[:len(n)//2] + n[len(n)//2+1:]
    if '0' in otherThanEye:
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
    # print(listOfCoins)
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

def three_summers(items, goal):
    j = len(items)-1
    i = 0
    ii = i + 1
    while i < j:
        x = items[i] + items[j] + items[ii]
        if x == goal:
            return True  # Okay, that's a solution.
        elif x < goal:
            i += 1  # Smallest element can't be part of solution.
        else:
            j -= 1  # Largest element can't be part of solution.
    return False
    
if __name__ == "__main__":
    # frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]) # works
    # print(only_odd_digits(999999)) # works
    # print(colour_trio('yrbbbbryyrybb')) # works
    # print(taxi_zum_zum('LFFLF'))
    # print(taxi_zum_zum('LLFLFLRLFR')) # works
    # print(taxi_zum_zum('FFLLLFRLFLRFRLRRL'))
    # print(taxi_zum_zum('FR' * 1729))
    # print(is_cyclops(99099))
    # print(domino_cycle([(3, 5), (5, 2), (2, 3)])) # works
    # give_change(64, [50, 25, 10, 5, 1])
    # give_change(123, [100, 25, 10, 5, 1])
    # give_change(100, [42, 17, 11, 6, 1])
#    print(is_ascending([1, 1, 1, 1]))
    print(three_summers([10, 11, 16, 18, 19,99], 127))



    
