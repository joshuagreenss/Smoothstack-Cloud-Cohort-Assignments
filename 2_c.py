# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
def crowd_test(l):
    if(len(l) > 3):
        print("Boy, it's crowded in here!")


# %%
l = ["Alexis", "Bill","Cat", "Dennis"]
crowd_test(l)
l.pop(len(l)-1)
crowd_test(l)


# %%
def crowd_test_mod(l):
    if(len(l) > 3):
        print("Boy, it's crowded in here!")
    else:
        print("It's pretty empty in here!")


# %%
l = ["Alexis", "Bill","Cat", "Dennis"]
crowd_test_mod(l)
l.pop(len(l)-1)
crowd_test_mod(l)


# %%
def mob_test(l):
    if len(l) > 5:
        print("There's a mob in here, run!")
    elif len(l) > 2:
        print("Boy, it's crowded in here!")
    elif len(l) > 0:
        print("It's pretty empty in here!")
    else:
        print("It's totally empty in here!")


# %%
l = ["Alexis", "Bill","Cat", "Dennis", "Eliza", "Felix"]
mob_test(l)
for i in range(6):
    l.pop(0)
    mob_test(l)


