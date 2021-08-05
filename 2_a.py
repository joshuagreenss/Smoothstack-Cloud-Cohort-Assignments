# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
print("Hello World"[9])


# %%
print("thinker"[2:5])


# %%
print("e")


# %%
print("mmy")


# %%
print(''.join(set("Mississippi")))


# %%
def palindromeCheck(w):
    s = ''
    for i in range(len(w)):
        if (w[i] >= 'a' and w[i] <= 'z') or (w[i] >= 'A' and w[i] <= 'Z'):
            s += w[i]
    s = s.lower()
    return 'Y' if s == s[::-1] else 'N'


# %%
palindromeCheck("No 'x' in Nixon")


