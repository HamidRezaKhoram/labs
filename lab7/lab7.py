# Hamidreza Khoramrokh
# 501146941
# lab7
# importing libraries for random number generation and ceiling
import random
import math

# turning the given sudo code into python syntax
def random_die():
    inRun = False
    # list comprehension 
    list_dies = [random.randrange(1,7) for _ in range(20)]

    # for loop iteration
    for i in range(20):
        # if we are in range of list index:
        if i <= 18:
            if list_dies[i] == list_dies[i+1] and inRun == False:
                print('(', end=' ')
                inRun = True
            print(list_dies[i], end=' ')
            if inRun:
                if list_dies[i] != list_dies[i+1]:
                    print(')', end=' ')
                    inRun = False
        # if not in the range of correct index:
        else:
            # checking only for the last two indexes
            if list_dies[18] == list_dies[19] and inRun == False:
                print('(', end=' ')
                inRun = True
            
            print(list_dies[19], end=' ')
            if inRun:
                if list_dies[18] != list_dies[19]:
                    print(')', end=' ')
                    inRun = False
        
        
    if inRun:
        print(')', end='')
             
    print('')
    
# finding the longest running segment
def seqgen():
    # list comprehension
    list_dies = [str(random.randrange(1,7)) for i in range(20)]
    # using join to turn list into string
    list_dies = ''.join(list_dies)
    # our temp holder
    die_holder = []
    # giving a our temp list its first value
    die_holder.append(list_dies[0])
    # counter for our temp holder
    counte_die = 0
    # saving the longest one
    longest = ''
    # 
    for i in range(19):
        if list_dies[i] == list_dies[i+1]:
            die_holder[counte_die] = die_holder[counte_die] + list_dies[i+1]
            
        elif list_dies[i] != list_dies[i+1]:
            counte_die += 1
            die_holder.append(list_dies[i+1])
            
    for i in die_holder:
        if len(i) > len(longest):
            longest = i
    if len(longest) == 1:
        print(list_dies)
    else:
        print(list_dies.replace(longest, '('+longest+')',1)) 
        
    

def longestFalse(L):
    
    holder = tuple()
    
    for i in range(len(L)):
        list_tuple = [()]
        counter = 0
        check = False
        for i in range(len(L)):
            if L[i] == False and check == False:
                check = True
                list_tuple[counter] += (i,)
            if L[i] == True and check == True:
                list_tuple[counter] += (i-1,)
                list_tuple.append(())
                counter += 1
                check = False
        if L[-1] == False:
            list_tuple[counter] += (len(L)-1, )
    # print(list_tuple)
    longestFalse = -1
    for i in list_tuple:
        if len(i) > 1:
            if abs(i[0]-i[1]) >= longestFalse and abs(i[0]-i[1]) != longestFalse:
                longestFalse = abs(i[0]-i[1])
                holder = i
    
    return holder
    
import math
def birdNest(n):
    listNest = ['-' for _ in range(n)]
    def get_false(dash):
        temp_false = []
        for i in dash:
            if i == '-':
                temp_false.append(False)
            else:
                temp_false.append(True)
        return temp_false
    # print(get_false(listNest))

    print(' '.join(listNest))
    for i in range(len(listNest)):
        biggest = longestFalse(get_false(listNest))
        # print(type(biggest))
        pointA, pointB = biggest[0], biggest[1]
        birdSpot = (pointA + pointB)/2
        listNest[math.ceil(birdSpot)] = 'x'
        print(' '.join(listNest))
    

def isPal(L):
    listL = L[:]
    listL.reverse()
    return listL == L
    
if __name__ == '__main__':
    random_die()
    seqgen()
    print(longestFalse([True,True,True,True,False]))
    birdNest(4)
    print(isPal([5, 1, 9, 9, 1, 5]))
    
    
