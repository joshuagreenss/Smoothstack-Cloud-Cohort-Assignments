# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
print([1,"word",2.00])


# %%
l = [1,1,[1,2]]
print(l[2][1])


# %%
lst = ['a','b','c']
print(lst[1:])


# %%
wkdy = {}
wkdy["Sunday"] = 0
wkdy["Monday"] = 1
wkdy["Tuesday"] = 2
wkdy["Wednesday"] = 3
wkdy["Thursday"] = 4
wkdy["Friday"] = 5
wkdy["Saturday"] = 6
print(wkdy)


# %%
d = {'k1':[1,2,3]}
print(d['k1'][1])


# %%
t = tuple([1,[2,3]])
print(t)


# %%
m = set('Mississippi')
print("".join(m))


# %%
m.add('x')
print(''.join(m))


# %%
print(set([1,1,2,3]))


# %%
def findFactors(s,e):
    vals = ""
    for i in range(s,e+1):
        if i%7 == 0 and i%5 != 5:
            vals += str(i) + ','
    vals = vals[:-1]
    print(vals)


# %%
findFactors(2000,3200)


# %%
def fact_recur(x):
    if(x == 0):
        return 1
    return x * fact_recur(x-1)


# %%
def fact(x):
    ans = 1
    for i in range(2,x+1):
        ans *= i
    return ans


# %%
fact(9)


# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



