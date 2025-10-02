############################################
###DATA STRUCTURES

############################################
##-Abstract
x = 5
type(x)  #The type function indicates the data type of a value.
#Lists, tuples, sets, and dictionaries are also referred to as Python collections (arrays).

############################################
##Numbers: int,float,complex
a = 5
b = 10.5
#Mathematical and arithmetic operations can also be used.
a * 3
a / 7
a * b / 10
a ** 2
#Type conversion allows converting one data type to another.
int(b)
float(a)
int(a * b / 10)
c = a * b / 10
int(c)

###########################################
##Strings : A string is a sequence of characters used to store and represent text.
print("Derya")  #print outputs the specified message or value to the console.
print('İlker')
name = "Derya"
#Multi-line string representation:
long_str = """Veri Yapıları: Hızlı Özet,
Sayılar (Numbers): int, float, complex,
Karakter Dizileri (Strings): str,
List, Dictionary, Tuple, Set,
Boolean (TRUE-FALSE): bool"""

#Accessing elements in strings:
name[0]
name[0:2]  #except 2
long_str[0:15]  #slicing

#Checking for elements (or substrings) in a string:
long_str
"Veri" in long_str

#Method : Functions defined within classes.
##String Methods :
dir(str)  # It is used to find methods of the string class

##len() function returns the number of items in an object.
name1 = "Derya"
len(name1)
len("data")
#How do we distinguish between a method and a function? If a function is defined inside a class structure, it is a method; if it is not inside a class structure, it is a function.

##upper() and lower() :
#upper() converts all characters in a string to uppercase.
#lower() converts all characters in a string to lowercase.
"derya".upper()
"DERYA".lower()

#replace() : returns a copy of the string with specified values replaced.
hi = "Hello, Data Science!"
hi.replace("l", "d")

#split() : splits a string into a list using a specified separator.
"Hello, Data Science!".split()

#strip(): removes leading and trailing whitespace (or specified characters) from a string.
" ofof ".strip()
"ofof".strip("o")

#capitalize() : converts the first character of a string to uppercase and the rest to lowercase.
"python programming".capitalize()

########################################################################
##List : A list is a collection that is ordered and changeable. It allows duplicate elements.
# - Mutable
# - Ordered. Indexing operations can be performed.
# - It is a container.
notes = [1, 2, 3, 4]
names = ["a", "b", "c", "d"]
not_nam = [1, 2, 3, "a", True, [1, 2]]
not_nam[0]
not_nam[5][1]
not_nam[0] = 99
not_nam[0:4]

#List Methods :
dir(notes)
len(notes)

#append : Adds an element at the end
notes.append(100)

#pop : Removes element by index (default: last)
notes.pop(0)

#insert : Inserts an element at a specified position
notes.insert(1, 5)

#sort() : Sorts the list in ascending order (default)
#reverse() : Reverses the list
#clear() : Removes all elements

################################################
#Dictonary : A dictionary is a collection of key-value pairs that is unordered, changeable, and does not allow duplicate keys.
# - Mutable
# - Unordered (Ordered as of Python 3.7+)
# - It is a container
#key-value
dictionary = {"REG": "Regression",
              "LOG": "Logistic",
               "CART": "Classification"}
dictionary = {"REG": ["Regression",10],
              "LOG": "Logistic",
               "CART": "Classification"} #Different data types can also be included.
dictionary["REG"]
dictionary["REG"][0]

#Searching for a key in a dictionary:
"REG" in dictionary

#Retrieving values from a dictionary using their keys:
dictionary.get("REG")
#Updating a value
dictionary["REG"] = ["YSA",10]

#Retrieving all keys from a dictionary
dictionary.keys()
dictionary.values()

#Converting all key-value pairs into a list of tuples
dictionary.items()

#Updating the value of a key in a dictionary
dictionary.update({"REG": 11})

#If the key does not exist, it creates a new key-value pair; if it exists, it updates the value.
dictionary.update({"RF": 10})

#################################################
##Tuples :
#Immutable.
#Ordered.(Being ordered means that the elements are accessible.)
#Inclusive (can contain different data types).
t = ("john","mark",1,2)
t[0]
t[0:3]
t[0]=52#immutable
t = list(t)
t[0] = 99
t = tuple(t)

###############################################
##Set :
# - Mutable.
# - Unordered + Unique.
# - Inclusive.
set1 = set([1,2,3]) #Creating a set from a list
set2 = set([1,4,3])

#difference(): method returns the elements that are present in one set but not in another.
set1.difference(set2)
set2.difference(set1)

#symmetric_difference() : The elements that are not in both sets compared to each other.
set1.symmetric_difference(set2)

#intersection() : Intersection of two sets
set1.intersection(set2)

#union() : Union of two sets
set1.union(set2)

#isdisjoint() : Is the intersection of the two sets empty?
#Usually, if it starts with is-, it returns a boolean value.
set3=set([1,7,3,6,21])
set4=set([1,7,3,6,21,3,2])
set3.isdisjoint(set4)

#issubset() : Is one set a subset of the other?
set3.issubset(set4)
set4.issubset(set3)

#issuperset() : Is one set a superset of the other?
set3.issuperset(set4)
set4.issuperset(set3)