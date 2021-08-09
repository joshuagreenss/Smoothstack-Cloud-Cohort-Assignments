# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
def func():
    print("Hello World")


# %%
func()


# %%
def func1(name):
    print("Hi, my name is",name)


# %%
func1("Joshua")


# %%
def func3(x,y,z):
    if z:
        return x
    else:
        return y


# %%
func3('hello','goodbye',False)


# %%
def func4(x,y):
    return x*y


# %%
func4(1,2)


# %%
def is_even(x):
    return not x%2


# %%
is_even(2)


# %%
def gThan(x,y):
    return x>y


# %%
gThan(2,1)


# %%
def sum(*args):
    i = 0
    for v in args:
        i += v
    return i


# %%
sum(1,2,3,4)


# %%
def getEvens(*args):
    e = []
    for i in args:
        if not i%2:
            e.append(i)
    return e


# %%
getEvens(1,2,3,4,5,6,7,8,9)


# %%
def hillValleyCase(s):
    hvc = ''
    for i in range(len(s)):
        if(i%2):
            hvc += s[i].upper()
        else:
            hvc += s[i].lower()    
    return hvc


# %%
hillValleyCase("Hello World")


# %%
def toggleGrThan(x,y):
    if not x%2 and not y%2:
        return x < y
    else:
        return x > y


# %%
toggleGrThan(3,2)


# %%
def sameLetter(s1,s2):
    if s1[0].lower() == s2[0].lower():
        return True
    return False


# %%
sameLetter("test","words")


# %%
sameLetter('test','two')


# %%
def fromSeven(x):
    return 7 - (x-7)*2


# %%
fromSeven(8)


# %%
def capFirstFourth(s1):
    s2 = ''
    for i in range(len(s1)):
        if i == 0 or i == 3:
            s2 += s1[i].upper()
        else:
            s2 += s1[i]
    return s2


# %%
capFirstFourth("test")


