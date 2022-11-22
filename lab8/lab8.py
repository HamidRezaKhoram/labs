def add(a, b):
    if b == 1:
        return a+1
    else:
        return add(a+1, b-1)

def log2(x):
    if x <= 1:
        return 0
    else:
        return log2(x/2) + 1
# recursive function for getting a reversed sentence
def reverse(sentence):
    if sentence == "":
        return sentence
    else:
        return reverse(sentence[1:]) + sentence[0]

# declaring global variable
counter_for_q5 = 0
def power(x,n):
    # using global variable
    global counter_for_q5
    counter_for_q5 += 1
    
    if n == 0:
        return 1
    else:
        return x * power(x,n-1)
def powerHalf(x,n):
    # using global variable
    global counter_for_q5
    counter_for_q5 += 1
    if n <= 0:
        return 1
    elif n%2 == 0:
         return (powerHalf(x,(n/2)))**(2)
    else:
        return x*powerHalf(x,n-1)


def findSeq():
    f= open("kdpF.txt")
    seq = ''
    for line in f:
        if '>' not in line:
            seq = seq + line
            seq = seq.replace('\n', '')
            seq.upper()
    return(seq)
def gcContent():
    percent = 0
    # getting the sequence from previous function
    seq = findSeq()
    for gc in seq:
        if gc =='g' or gc =='c':
            percent += 1
    return (percent/len(seq))*100

if __name__ == "__main__":
    print(add(5,9))
    print(log2(5))
    print(reverse('Who let the dogs out?'))
    print(power(2,20))
    print(counter_for_q5)
    counter_for_q5 = 0
    print(powerHalf(2,20))
    print(counter_for_q5)
    print(findSeq())
    print(gcContent())
>>>>>>> 98da711a608ef2e42ff8df206c5a0fd661f0b150
