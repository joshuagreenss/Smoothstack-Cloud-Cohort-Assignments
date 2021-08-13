# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd


# %%
df = pd.read_csv("D:/Documents/Python Projects/Smoothstack-Cloud-Cohort-Assignments/Salaries.csv")


# %%
df.head(1)


# %%
df.info()


# %%
df.head(10000).sum()["BasePay"]


# %%
df.max()["TotalPayBenefits"]


# %%
df.loc[df['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']


# %%
df.loc[df['TotalPayBenefits'] == df.max()['TotalPayBenefits']]['EmployeeName']


# %%
df.loc[df['TotalPayBenefits'] == df.min()['TotalPayBenefits']]['EmployeeName']
#This employee has a negative salary, which is strange for somebody to be paid


# %%
df.groupby('Year').mean()['TotalPay']


# %%
len(df.groupby("JobTitle").count().index)


# %%
df.groupby("JobTitle").count().sort_values(by="Id",ascending=False).head(7).axes[0]


# %%
count2013 = df.loc[df['Year'] == 2013].groupby("JobTitle").count()
len(count2013.loc[count2013['Id'] == 1].axes[0])


# %%
c = df.copy()
c['JobTitle'] = c['JobTitle'].map(lambda x: x.__contains__('Chief'))
len(c.loc[c['JobTitle'] == True].axes[0])


# %%
c2 = df.copy()
c2['JobTitle'] = c2['JobTitle'].map(lambda x: len(x))
c2.corr(method='pearson')['JobTitle']['BasePay']
#The correlation between Job Title length and Base Pay is almost zero, so there is no correlation


