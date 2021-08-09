# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
def divFiveAndSeven():
    l = []
    for i in range(1500,2701):
        if i % 7 == 0 and i % 5 == 0:
            l.append(i)
    return l


# %%
l = divFiveAndSeven()


# %%
print(l)


# %%
def cToF(c):
    return c*9/5+32


# %%
def fToC(f):
    return (f-32)*5/9


# %%
cToF(10)


# %%
fToC(10)


# %%
import random


# %%
def guessNumb():
    g = 0
    random.seed()
    r = random.randrange(1,11)
    while g != r:
        g = int(input("Guess a number!"))
        if(g != r):
            print("Wrong, try again!")
    print("Good job!")


# %%
guessNumb()


# %%
def drawPattern():
    for i in range(1,6):
        for j in range(i):
            print('* ',end='')
        print('\n',end='')
    for i in range(4,0,-1):
        for j in range(i):
            print('* ',end='')
        print('\n',end='')


# %%
drawPattern()


# %%
def myReverse(word):
    return word[::-1]


# %%
myReverse('Test')


# %%
def evenOddCount(l):
    eCount = 0
    oCount = 0
    for n in l:
        if n%2 == 0:
            eCount += 1
        else:
            oCount += 1
    print("Number of even numbers :", eCount)
    print("Number of odd numbers:", oCount)


# %%
evenOddCount([1,2,3,4,5,6,7,8,9])


# %%
def listTypes(l):
    for item in l:
        print(item,':',type(item))


# %%
listTypes([1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}])


# %%
def printNums():
    for i in range(7):
        if i == 3 or i == 6:
            continue
        else:
            print(i)


# %%
printNums()
