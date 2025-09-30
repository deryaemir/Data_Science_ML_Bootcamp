##################################
#CONDITIONS
from statsmodels.sandbox.regression.example_kernridge import upper

##########################
#Expressions that check if something is true or false.
#True-False remember
1 == 1
1 == 2
#if : Used to run a block of code only when a condition is true.
if 1 == 1: #If true, it performs the operation below.
    print("something is true")

number = 11
if number == 10:
     print("number is 10")
number = 10
#We started repeating, so let’s use a function:
def number_check(number):
    if number == 10:
        print("number is 10")
    else:#It is used when the condition is not met.
        print("number is not 10")
number_check(12)
number_check(10)
#elif : Used after if to check another condition if the first one is false.

def number_check(number):
    if number> 10:
        print("greater than 10")
    elif number< 10:
        print("less than 10")
    else:
        print("equal to 10")
number_check(12)
##########################################
#LOOPS : Structures that repeat a block of code as long as a condition is true.
#for loop:

students = ["John", "Michael", "Sarah"]
for student in students:
    print(student)
for student in students:
    print(student.upper())

salaries = [1000, 2000, 3000, 4000]
for salary in salaries:
    print(int(salary*20/100+salary))

def new_salary(salary,rate):
    return int(salary*rate/100+salary)
new_salary(1000,10)
for salary in salaries:
    print(new_salary(salary,10))

salaries2 = [1070, 1080, 1090, 1110]
for salary in salaries2:
    print(new_salary(salary,15))

for salary in salaries:
    if salary >=3000:
        print(new_salary(salary,10))
    else:
        print(new_salary(salary,20))

#######application – interview question alternating
#Goal: Write a function that modifies a string. Characters at even indexes should be uppercase, and characters at odd indexes should be lowercase.
str_text ="hi my name is John"
def alternating(str_text):
    new_string = ""
    for i in range(len(str_text)) :
        if i % 2 == 0:
            new_string += str_text[i].upper()
        else:
           new_string+= str_text[i].lower()
    return new_string
alternating(str_text)
################################################3
##Break and Continue and While

####################################
salaries3 = [1000, 2000, 3000, 4000]
for salary in salaries:
    if salary == 3000:
        break #Used to immediately exit a loop.
    print(salary)

for salary in salaries:
    if salary == 3000:
        continue #Skips the current iteration of a loop and moves to the next one.
    print(salary)

#while: Repeats a block of code as long as the condition is true.
number = 1
while number <= 10:
    print(number)
    number += 1

############################
#ENUMERATE : Automatic Counter/Indexer with for loop
students = ["John", "Michael", "Sarah"]
for student in students:
    print(student)

for index, student in enumerate(students):
    print(index, student)

A = []
B = []
for index, student in enumerate(students):
    if index % 2 == 0:
        A.append(student)
    else:
        B.append(student)

print(A)
print(B)
################################
#######application – interview question : Enumerate
# Write the divide_students function.
# Put the students at even indexes into one list.
# Put the students at odd indexes into another list.
# But return these two lists combined as a single list.
students = ["John", "Michael", "Sarah","Mariam", "Kevin"]

def new_enumerate(strings):
    groups = [[], []]
    for index, string in enumerate(strings):
        if index % 2 == 0:
            groups[0].append(string)
        else:
            groups[1].append(string)
    return groups
new_enumerate(students)

#####################################
#Writing the alternating function with enumerate
strings = "hi my name is John"
def new_alternating(strings):
    new_string = ""
    for index, string in enumerate(strings):
        if index % 2 == 0:
            new_string += string.upper()
        else:
            new_string += string.lower()
    return new_string
new_alternating(strings)

###########################
#ZİP : It allows evaluating different lists together.
students1 = ["John", "Michael", "Sarah"]
departments = ["Computer Science", "Science", "Business"]
ages = [20, 30, 40]
list(zip(students, departments, ages)) #in tuple format

#######################
#LAMBDA, MAP, FİLTER, REDUCE
#lambda : Used to create small, anonymous functions in a single line.
def summer(a, b):#function
    return a+b
new_sum = lambda x, y: x + y #function

#map : Applies a function to each item in an iterable.
salaries = [1000, 2000, 3000, 4000]
def new_salary(salary):
    return int(salary*20/100+salary)
new_salary(1000)
for salary in salaries:
    print(new_salary(salary))
list(map(new_salary, salaries))#We managed it without writing a loop.
list(map(lambda x : x * 20 / 100 + x ,salaries))

#filter : Selects elements from an iterable that meet a given condition.
list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(filter(lambda x : x % 2 == 0, list_store))

#reduce : Applies a function cumulatively to the items of an iterable, reducing it to a single value.
from functools import reduce
list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reduce(lambda x, y : x + y, list_store)

########################################
#LIST COMPREHENSIONS :It provides the ability to easily perform operations that could take multiple lines of code, producing the desired output based on the chosen code or data structure.

salaries = [1000, 2000, 3000, 4000]
null_list = []
for salary in salaries:
    null_list.append(new_salary(salary))
null_list2 = []
for salary in salaries:
    if salary>3000:
        null_list2.append(new_salary(salary))
    else:
        null_list2.append(new_salary(salary*2))

[new_salary(salary*2)if salary>3000 else new_salary(salary*2) for salary in salaries]

[salary * 2 for salary in salaries]
[salary * 2 for salary in salaries if salary < 3000]
[salary * 2 if salary < 3000 else salary * 0 for salary in salaries]#If we use only an if statement, it stays on the right; if we use it with an else, it is placed on the left side of the for part.
[new_salary(salary * 2) if salary < 3000 else new_salary(salary * 0.2) for salary in salaries]

students = ["John", "Mark", "Venessa", "Mariam"]
students_no = ["John", "Venessa"]
[student.lower() if student in students_no else student.upper() for student in students]
[student.upper() if student not in students_no else student.lower() for student in students]

################################
# Dict Comprehension : It allows us to express in a single line the operations that would otherwise need to be written in multiple lines.

dictionary = {'a': 1,
              'b': 2,
              'c': 3,
              'd': 4}
dictionary.keys()
dictionary.values()
dictionary.items()
{k: v ** 2 for (k, v) in dictionary.items()}
{k.upper(): v for (k, v) in dictionary.items()}
{k.upper(): v*2 for (k, v) in dictionary.items()}

#######application – interview question
#Goal: The aim is to calculate the squares of even numbers and add them to a dictionary.
#The keys will be the original values, while the values will be the modified ones.
numbers = range(10)
new_dict = {}
for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2

{n: n ** 2 for n in numbers if n % 2 == 0}

#################################
##LIST AND DICT COMPREHENSION APPLICATIONS

#1-Changing the variable names in a dataset.
# before:
# ['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous', 'ins_premium', 'ins_losses', 'abbrev']
# after:
# ['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS', 'INS_PREMIUM', 'INS_LOSSES', 'ABBREV']

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns
for col in df.columns:
    print(col.upper())
A = []
for col in df.columns:
    A.append(col.upper())
df.columns = A

df = sns.load_dataset("car_crashes")
df.columns = [col.upper() for col in df.columns]
df.columns = [col.upper() for col in df.columns]
df.columns

#2-We want to add "FLAG" to the beginning of variable names that contain "INS", and "NO_FLAG" to the others.

# before:
# ['TOTAL',
# 'SPEEDING',
# 'ALCOHOL',
# 'NOT_DISTRACTED',
# 'NO_PREVIOUS',
# 'INS_PREMIUM',
# 'INS_LOSSES',
# 'ABBREV']

# after:
# ['NO_FLAG_TOTAL',
#  'NO_FLAG_SPEEDING',
#  'NO_FLAG_ALCOHOL',
#  'NO_FLAG_NOT_DISTRACTED',
#  'NO_FLAG_NO_PREVIOUS',
#  'FLAG_INS_PREMIUM',
#  'FLAG_INS_LOSSES',
#  'NO_FLAG_ABBREV']

[col for col in df.columns if "INS" in col]
["FLAG_" + col for col in df.columns if "INS" in col]
df.columns = ["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]
df.columns

#3-The goal is to create a dictionary where the key is a string and the value is a list as shown below.
#We want to do this only for numerical variables.
# Output:
# {'total': ['mean', 'min', 'max', 'var'],
#  'speeding': ['mean', 'min', 'max', 'var'],
#  'alcohol': ['mean', 'min', 'max', 'var'],
#  'not_distracted': ['mean', 'min', 'max', 'var'],
#  'no_previous': ['mean', 'min', 'max', 'var'],
#  'ins_premium': ['mean', 'min', 'max', 'var'],
#  'ins_losses': ['mean', 'min', 'max', 'var']}
import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns
num_cols = [col for col in df.columns if df[col].dtype != "O"]# Create a list of column names that are numeric (exclude object/string columns)
soz = {}
agg_list = ["mean", "min", "max", "sum"]
for col in num_cols:
    soz[col] = agg_list
# kısa yol
new_dict = {col: agg_list for col in num_cols}

# Display the first rows of numeric columns
df[num_cols].head()

# Apply the aggregation functions defined in new_dict to numeric columns
df[num_cols].agg(new_dict)

