# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
testList = [[34587,'Learning Python, Mark Lutz',4,40.95],[98762,'Programming Python, Mark Lutz',5,56.80],[77226,'Head First Python, Paul Barry',3,32.95],[88112,'Einfuhrung in Python3, Bernd Klein',3,24.99]]


# %%
def getPrices(l):
    return list(map(lambda x : (x[0],x[2]*x[3]) if x[2]*x[3] >= 100 else (x[0],x[2]*x[3]+10),l))


# %%
getPrices(testList)


# %%
testList2 = [34587,('Learning Python, Mark Lutz',4,40.95),98762,('Programming Python, Mark Lutz',5,56.80),77226,('Head First Python, Paul Barry',3,32.95),88112,('Einfuhrung in Python3, Bernd Klein',3,24.99)]


# %%
def getPrices2(l):
    l2 = zip(l[::2],l[1::2])
    return(list(map(lambda x : (x[0],x[1][1]*x[1][2]) if x[1][1]*x[1][2] >= 100 else (x[0],x[1][1]*x[1][2]+10), l2)))


# %%
getPrices2(testList2)
