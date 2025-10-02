#############################################
# PANDAS
#############################################

# Pandas Series
# Reading Data
# Quick Look at Data
# Selection in Pandas
# Aggregation & Grouping
# Apply and Lambda
# Join Operations

#############################################
# Pandas Series
#############################################
# The most commonly used data structures in Pandas are:
# - Pandas Series: one-dimensional data structure with index information.
# - Pandas DataFrame: multi-dimensional data structure with index information.
#
# Index information is an inherent feature of both structures.
# Pandas Series are one-dimensional and always contain index labels.

import pandas as pd

# Create a Pandas Series
s = pd.Series([10, 77, 12, 4, 5])

type(s)        # -> <class 'pandas.core.series.Series'> (Pandas Series object)
s.index        # -> RangeIndex(start=0, stop=5, step=1) (index labels)
s.dtype        # -> int64 (data type of elements)
s.size         # -> 5 (total number of elements)
s.ndim         # -> 1 (number of dimensions, Series is 1D)
s.values       # -> array([10, 77, 12,  4,  5]) (underlying NumPy array)
type(s.values) # -> <class 'numpy.ndarray'>

s.head(3)      # first 3 elements -> 0    10
               #                        1    77
               #                        2    12
s.tail(3)      # last 3 elements -> 2    12
               #                      3     4
               #                      4     5



#############################################
# Reading Data
#############################################
# Pandas Cheatsheet (most common methods)
# By holding CTRL and clicking on a method,
# you can jump to its definition and explore it.
# You can also browse other available methods by using CTRL+F (search).
import pandas as pd

# Read a CSV file into a DataFrame
df = pd.read_csv("datasets/advertising.csv")

# Show the first 5 rows
df.head()

#############################################
# Quick Look at Data
#############################################
# In Pandas, "object" and "category" dtypes are used for categorical variables.
# - object: usually represents string-based categorical data.
# - category: represents categorical data with better memory efficiency and performance.

import pandas as pd
import seaborn as sns

# Load Titanic dataset from seaborn
df = sns.load_dataset("titanic")

df.head()         # first 5 rows of the dataset
df.tail()         # last 5 rows of the dataset
df.shape          # (rows, columns) -> dataset dimensions
df.info()         # data types and non-null counts
df.columns        # column names
df.index          # index information
df.describe().T   # summary statistics (transposed for readability)

# Checking missing values
df.isnull().values.any()   # check if there is any missing value -> True/False
df.isnull().sum()          # count missing values in each column

# Looking at a specific column
df["sex"].head()           # first 5 values of the "sex" column
df["sex"].value_counts()   # frequency of unique values in "sex" column

#############################################
# Selection in Pandas
#############################################
import pandas as pd
import seaborn as sns
df = sns.load_dataset("titanic")
df.head()

df.index              # index information
df[0:13]              # select rows 0 to 12
df.drop(0, axis=0).head()   # drop row with index 0

# Drop multiple rows by index
delete_indexes = [1, 3, 5, 7]
df.drop(delete_indexes, axis=0).head(10)

# Permanent deletion options:
# df = df.drop(delete_indexes, axis=0)             # reassign
# df.drop(delete_indexes, axis=0, inplace=True)    # inplace


# Converting a variable into index
#######################
df["age"].head()
df.age.head()         # same as df["age"]

df.index = df["age"]  # set "age" column as index

df.drop("age", axis=1).head()           # drop the age column
df.drop("age", axis=1, inplace=True)    # drop permanently
df.head()


# Converting index back into a variable
#######################
df.index              # show current index

df["age"] = df.index  # convert index back into a column

df.head()
df.drop("age", axis=1, inplace=True)    # drop again if needed

df.reset_index().head()   # reset index (age becomes a column again)
df = df.reset_index()     # reassign permanently
df.head()

#######################
# Operations on Variables
#######################
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

"age" in df          # check if "age" column exists

df["age"].head()     # selecting a single column
df.age.head()        # same as df["age"]

df["age"].head()
type(df["age"].head())    # -> pandas.Series

df[["age"]].head()
type(df[["age"]].head())  # -> pandas.DataFrame
# NOTE:
# - df["age"]  gives a Pandas Series (1D)
# - df[["age"]] gives a Pandas DataFrame (2D, still with one column)

# Select multiple columns
df[["age", "alive"]]

# Select columns with a list of names
col_names = ["age", "adult_male", "alive"]
df[col_names]

# Create new columns by transformations
df["age2"] = df["age"] ** 2            # square of age
df["age3"] = df["age"] / df["age2"]    # ratio of age to age2

# Drop a single column
df.drop("age3", axis=1).head()

# Drop multiple columns
df.drop(col_names, axis=1).head()

# Select all columns except those containing "age"
# Explanation:
# - df.loc[...] → .loc is label-based selection (rows/columns by name)
# - First argument before comma (:) → select all rows
# - Second argument (~df.columns.str.contains("age")) → select all columns
#   where column name does NOT contain "age"
# - "~" means logical NOT in Pandas
df.loc[:, ~df.columns.str.contains("age")].head()

#######################
# iloc & loc
#######################
# .loc and .iloc are special structures used for selection in Pandas.
# - .loc : label-based selection (uses row/column names)
# - .iloc: integer/location-based selection (uses row/column index numbers)
#
# Example:
# df.loc[0:5, "age"]   -> rows 0 to 5 of the "age" column (by label)
# df.iloc[0:5, 2]      -> rows 0 to 5 of the 3rd column (by position)

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

# iloc: integer-based selection (uses row/column positions)
df.iloc[0:3]        # first 3 rows (rows 0,1,2)
df.iloc[0, 0]       # element at row 0, column 0 (by position)

# loc: label-based selection (uses row/column labels)
df.loc[0:3]         # rows with labels 0,1,2,3  (note: 3 is inclusive for loc!)

# iloc with both rows and columns
df.iloc[0:3, 0:3]   # rows 0–2 and columns 0–2 (3x3 subset by position)

# loc with rows and a single column
df.loc[0:3, "age"]  # "age" values for rows 0–3

# loc with multiple columns
col_names = ["age", "embarked", "alive"]
df.loc[0:3, col_names]   # select rows 0–3 and the specified columns

#######################
# Conditional Selection
#######################
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

# Select rows where age > 50
df[df["age"] > 50].head()

# Count how many passengers older than 50
df[df["age"] > 50]["age"].count()

# Select rows where age > 50 and return only age & class columns
df.loc[df["age"] > 50, ["age", "class"]].head()

# Multiple conditions: age > 50 AND sex == male
# NOTE: when using multiple conditions (&, |), each condition must be enclosed in parentheses
df.loc[(df["age"] > 50) & (df["sex"] == "male"), ["age", "class"]].head()

# Frequency of embarkation towns
df["embark_town"].value_counts()

# Complex condition:
# - age > 50
# - sex == male
# - embarked from Cherbourg OR Southampton
# NOTE: multiple conditions → always use parentheses for each condition
df_new = df.loc[(df["age"] > 50) & (df["sex"] == "male")
       & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")),
       ["age", "class", "embark_town"]]

# Count embarkation towns for the filtered group
df_new["embark_town"].value_counts()

#############################################
# Aggregation & Grouping
#############################################
# Aggregation = representing the values inside a data structure collectively.
# Aggregation and grouping operations usually go hand in hand.
#
# Common aggregation methods:
# - count()  : number of elements
# - first()  : first element
# - last()   : last element
# - mean()   : average
# - median() : median value
# - min()    : minimum value
# - max()    : maximum value
# - std()    : standard deviation
# - var()    : variance
# - sum()    : sum of values
# - pivot_table : multi-dimensional aggregation

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

# Simple aggregation
df["age"].mean()    # average age of all passengers

# Group by a single variable
df.groupby("sex")["age"].mean()
# average age grouped by sex (male/female)

# Group by with aggregation dictionary
df.groupby("sex").agg({"age": "mean"})
df.groupby("sex").agg({"age": ["mean", "sum"]})

# Multiple aggregations on multiple columns
df.groupby("sex").agg({"age": ["mean", "sum"],
                       "survived": "mean"})
# average and total age, survival rate by sex

# Group by multiple variables
df.groupby(["sex", "embark_town"]).agg({"age": ["mean"],
                                        "survived": "mean"})
# mean age and survival rate grouped by sex and embarkation town

df.groupby(["sex", "embark_town", "class"]).agg({"age": ["mean"],
                                                 "survived": "mean"})
# grouped by sex, embarkation town and class

# Adding counts to the aggregation
df.groupby(["sex", "embark_town", "class"]).agg({
    "age": ["mean"],        # mean age
    "survived": "mean",     # survival rate
    "sex": "count"          # count of passengers in group
})

#######################
# Pivot table
#######################
# pivot_table: summarize data by groups (like Excel Pivot Table)
# cut: convert numerical variable into categorical by defined bins
# qcut: convert numerical variable into categorical by quantiles (equal-sized groups)

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

# Survival rate by sex (rows) and embarkation town (columns)
df.pivot_table("survived", index="sex", columns="embarked")

# Survival rate by sex (rows) and a combination of embark_town & class (columns)
df.pivot_table("survived", index="sex", columns=["embarked", "class"])

df.head()

# Create categorical age groups using cut()
df["new_age"] = pd.cut(df["age"], [0, 10, 18, 25, 40, 90])

# Survival rate by sex (rows), broken down by age group and class (columns)
df.pivot_table("survived", index="sex", columns=["new_age", "class"])

# Adjust display width for better readability
pd.set_option('display.width', 500)

#############################################
# Apply & Lambda
#############################################
# apply  : lets you apply a function automatically on rows or columns
# lambda : a way to define "use-and-throw" functions (temporary functions)
#          unlike def, they are created and used inline during code execution
#############################################

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

df["age2"] = df["age"]*2
df["age3"] = df["age"]*5

(df["age"]/10).head()
(df["age2"]/10).head()
(df["age3"]/10).head()

for col in df.columns:
    if "age" in col:
        print(col)

for col in df.columns:
    if "age" in col:
        print((df[col]/10).head())

for col in df.columns:
    if "age" in col:
        df[col] = df[col]/10

df.head()

# apply + lambda to divide all "age" columns by 10
df[["age", "age2", "age3"]].apply(lambda x: x/10).head()

# select columns containing "age" and apply function
df.loc[:, df.columns.str.contains("age")].apply(lambda x: x/10).head()

# standardization with lambda: (x - mean) / std
df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()).head()

# define a reusable function instead of lambda
def standart_scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std()

df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()

# assign standardized values back to dataframe
df.loc[:, df.columns.str.contains("age")] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler)

df.head()

#############################################
# Join Operations
#############################################
import numpy as np
import pandas as pd

# Create two DataFrames
m = np.random.randint(1, 30, size=(5, 3))
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])
df2 = df1 + 99   # add 99 to each element in df1

# Concatenate vertically (default axis=0)
pd.concat([df1, df2])

# Concatenate and reset the index
pd.concat([df1, df2], ignore_index=True)

#######################
# Merge Operations
#######################

# Example DataFrames
df1 = pd.DataFrame({
    'employees': ['john', 'dennis', 'mark', 'maria'],
    'group': ['accounting', 'engineering', 'engineering', 'hr']
})

df2 = pd.DataFrame({
    'employees': ['mark', 'john', 'dennis', 'maria'],
    'start_date': [2010, 2009, 2014, 2019]
})

# Merge on common column "employees" (automatically detected)
pd.merge(df1, df2)

# Explicit merge on "employees"
pd.merge(df1, df2, on="employees")

# Purpose: access each employee's manager info
df3 = pd.merge(df1, df2)

df4 = pd.DataFrame({
    'group': ['accounting', 'engineering', 'hr'],
    'manager': ['Caner', 'Mustafa', 'Berkcan']
})

# Merge employee info with manager info
pd.merge(df3, df4)

