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
    list_dies = [random.randrange(1, 7) for _ in range(20)]
    # for loop iteration
    for i in range(20):
        # if we are in range of list index:
        if i <= 18:
            if list_dies[i] == list_dies[i + 1] and inRun == False:
                print("(", end=" ")
                inRun = True
            print(list_dies[i], end=" ")
            if inRun:
                if list_dies[i] != list_dies[i + 1]:
                    print(")", end=" ")
                    inRun = False
        # if not in the range of correct index:
        else:
            # checking only for the last two indexes
            if list_dies[18] == list_dies[19] and inRun == False:
                print("(", end=" ")
                inRun = True

            print(list_dies[19], end=" ")
            if inRun:
                if list_dies[18] != list_dies[19]:
                    print(")", end=" ")
                    inRun = False

    if inRun:
        print(")", end="")

    print("")


# finding the longest running segment
def biggest_seg():
    # list comprehension
    list_dies = [str(random.randrange(1, 7)) for i in range(20)]
    # using join to turn list into string
    list_dies = "".join(list_dies)
    # our temp holder
    die_holder = []
    # giving a our temp list its first value to have something to compare against
    die_holder.append(list_dies[0])
    # counter for our temp holder
    counte_die = 0
    # saving the longest one
    longest = ""
    # for loop for going through the list
    for i in range(19):
        # checking an element against the next
        if list_dies[i] == list_dies[i + 1]:
            # adding element to the string place holder in our list
            die_holder[counte_die] = die_holder[counte_die] + list_dies[i + 1]
        # if its not the same element go to the next index of our list and also append
        elif list_dies[i] != list_dies[i + 1]:
            counte_die += 1
            die_holder.append(list_dies[i + 1])
    # going through our list and finding our longest element
    for i in die_holder:
        if len(i) > len(longest):
            longest = i
    # if there is no long sequence just print the whole sequence
    if len(longest) == 1:
        print(list_dies)
    # printing the sequence with the longest being in between () with replace method
    else:
        print(list_dies.replace(longest, "(" + longest + ")", 1))


# longest sequence of Falses
def longestFalse(L):
    # tuple for holding our starting index and ending index
    holder = tuple()
    # for each element in L:
    for i in range(len(L)):
        # list of tuples
        list_tuple = [()]
        # counter for list_tuple indexes
        counter = 0
        # checking if we are in a run
        check = False
        # going through all elements agin for creating tuples within list
        for i in range(len(L)):
            # our logic for finding the longest False
            if L[i] == False and check == False:
                # we are in a run so check True
                check = True
                # adding our starting index
                list_tuple[counter] += (i,)
            # if now the False sequence:
            if L[i] == True and check == True:
                # getting our ending index
                list_tuple[counter] += (i - 1,)
                # making another empty tuple for our next sequence
                list_tuple.append(())
                counter += 1
                # we are no longer in a run
                check = False
        # checking for edge cases
        if L[-1] == False:
            list_tuple[counter] += (len(L) - 1,)

    # checking our longest element against longestFalse variable and updating it to the new value if its lower than the our element in list_tuple
    longestFalse = -1
    for i in list_tuple:
        if len(i) > 1:
            if abs(i[0] - i[1]) >= longestFalse and abs(i[0] - i[1]) != longestFalse:
                longestFalse = abs(i[0] - i[1])
                # updating holder too
                holder = i
    # return our holder
    return holder


# our occupy function which uses our last function as a helper
def occupy(n):
    # getting our list of '-' with list comprehension
    listNest = ["-" for _ in range(n)]

    # another helper function for turing '-' into False and 'x' into True and appending it to our temp list for our longestFalse function to work
    def get_false(dash):
        temp_false = []
        for i in dash:
            if i == "-":
                temp_false.append(False)
            else:
                temp_false.append(True)
        return temp_false

    # printing our first row
    print(" ".join(listNest))
    # going trough our list and printing rows
    for i in range(len(listNest)):
        # finding the longest False with longestFalse function
        biggest = longestFalse(get_false(listNest))
        # unpacking our tuple
        pointA, pointB = biggest[0], biggest[1]
        # getting the half way point and ceiling ig
        birdSpot = (pointA + pointB) / 2
        listNest[math.ceil(birdSpot)] = "x"
        # printing our row with join function
        print(" ".join(listNest))


# finding if a sequence of numbers is palindrome
def isPal(L):
    # making a new copy of our original list
    listL = L[:]
    # reversing our second list
    listL.reverse()
    # compare and return boolean
    return listL == L


# calling our functions
if __name__ == "__main__":
    random_die()
    biggest_seg()
    print(
        longestFalse(
            [False, False, True, False, False, False,
                False, True, True, False, False]
        )
    )
    occupy(10)
    print(isPal([5, 1, 9, 9, 1, 5]))
