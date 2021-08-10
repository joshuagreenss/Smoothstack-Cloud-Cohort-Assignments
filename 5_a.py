# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
def calcBMI(h,w):
    return w/(h**2)


# %%
def getBMI(h,w):
    bmi = calcBMI(h,w)
    if bmi < 18.5:
        print("underweight")
    elif bmi < 25:
        print("normal")
    elif bmi < 30:
        print("overweight")
    else:
        print("obese")


# %%
getBMI(1.73,80)


