# Hamidreza KHoramrokh
# 501146941
# lab7

import random

def random_die():
    inRun = False
    list_dies = []
    
    list_dies.append(random.randrange(1,7))
    
    for i in range(20):
        list_dies.append(random.randrange(1,7))
        if list_dies[i] == list_dies[i+1] and inRun == False:
            print('(', end=' ')
            inRun = True
            print(list_dies[i], end=' ')
        else:
            print(list_dies[i], end=' ')
        if list_dies[i] != list_dies[i+1] and inRun == True:
            print(' )', end='')
            inRun = False
            
    print('')
def seqgen():
    list_dies = [str(random.randrange(1,7)) for i in range(20)]
    list_dies = ''.join(list_dies)
    print(list_dies)
    die_holder = []
    die_holder.append(list_dies[0])
    counte_die = 0
    longest = ''
    for i in range(19):
        if list_dies[i] == list_dies[i+1]:
            die_holder[counte_die] = die_holder[counte_die] + list_dies[i+1]
            
        elif list_dies[i] != list_dies[i+1]:
            counte_die += 1
            die_holder.append(list_dies[i+1])
            
    for i in die_holder:
        if len(i) >= len(longest):
            longest = i
    print(longest) 
        
    print(die_holder)

def longestFalse(L):
    
    holder = ()
    
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
    print(list_tuple)
    longestFalse = -1
    holder2 = list_tuple[0]
    for i in list_tuple:
        if len(i) > 1:
            if abs(i[0]-i[1]) >= longestFalse and abs(i[0]-i[1]) != longestFalse:
                longestFalse = abs(i[0]-i[1])
                holder = i
    print(holder)
        
                 

if __name__ == '__main__':
    # random_die()
    # seqgen()
    longestFalse([True, True, False, False, True, False, True, True, False, False, True, True])
    
    
