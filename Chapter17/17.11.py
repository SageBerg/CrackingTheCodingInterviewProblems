from random import randint

def rand5():
    return randint(0, 4)

def rand4():
    x = rand5()
    while x == 4:
        x = rand5()
    return x

def rand2():
    x = rand5()
    while x > 1:
        x = rand5()
    return x

def rand7():
    flag = True
    while flag:
        x = rand2()
        if x == 0:
            y = rand4() * 2 #gets 0, 2, 4, 6
        if x == 1:
            y = 1 + rand4() * 2 #gets 1, 3, 5, 7
        if y != 7:
            flag = False
    return y
    

def main():
    number_freq = dict()
    for _ in range(100000):
        roll = rand7()
        if roll not in number_freq:
            number_freq[roll] = 1
        else:
            number_freq[roll] += 1
    for i in range(7):
        print i, number_freq[i]

main()
