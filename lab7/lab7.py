# Hamidreza KHoramrokh
# 501146941
# lab7

import random

def random_die():
    inRun = False
    list_dies = []
    list_2 = []
    list_dies.append(random.randrange(1,7))
    
    for i in range(20):
        list_dies.append(random.randrange(1,7))

        if list_dies[i] == list_dies[i+1] and inRun == False:
            # print('(', end=' ')
            list_2.append('o')
            inRun = True
            # print(list_dies[i], end=' ')
            list_2.append(str(list_dies[i]))
        else:
            # print(list_dies[i], end=' ')
            list_2.append(str(list_dies[i]))
        if list_dies[i] != list_dies[i+1] and inRun == True:
            # print(')', end=' ')
            list_2.append('x')
            inRun = False
    return list_2
def seqgen():
    list_seq = (random_die())
    list_seq = ''.join(list_seq)
    tempS = ''
    list2 = []
    check = False
    len2 = len(list_seq)-1
    len3 = 0
    for i in range(len(list_seq)-1):
        if list_seq[i] == 'o':
            for j in range(i+1, len2):
                if list_seq[j] == 'x':
                    len2 = j + 1
                    
                    
                    list2.append(list_seq[i:j])
                tempS = ''
    print(list2)


if __name__ == '__main__':
    # random_die()
    seqgen()