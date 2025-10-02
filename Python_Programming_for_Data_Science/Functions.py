################################################
#FUNCTIONS

################################################
##FUNCTIONS : They are pieces of code written to perform specific tasks.

#Function literacy:
print("a")
#?print : It is used to display the help page of the function.
#A parameter is a variable defined when a function is declared, while an argument is the value passed to these parameters when the function is called.
print("a", "b", sep="__")  #Formatting example


#help(print) : It is used to display the help page of the function.

#Function definition:

def calculate(x):
    print(x * 2)


calculate(5)


#Let's define a function with two arguments/parameters.
def summer(arg1, arg2):
    print(arg1 + arg2)


summer(1, 2)


#Docstring : A docstring is a special string in Python that documents a function, class, or module by describing its purpose and usage.
#information note
def summer(arg1, arg2):
    """
    sum of two numbers
    Parameters
    ----------
    arg1 : int or float
    arg2 : int or float

    Returns
    -----
    result : int or float--

    Examples
    -------
    >>> summer(1, 2)
    """
    print(arg1 + arg2)


summer(1, 2)


# Functions Statement/Body Section:
# def function_name(parameters/arguments):
#     statements (function body)
def say_hi(string):
    print(string)
    print("hi")
    print("hello")


say_hi("hiii")


def multiplication(a, b):
    c = a * b
    print(c)


multiplication(1, 2)

#A function that stores the entered values in a list
list_store = []  #global scope : Variable accessible everywhere in the program.


def add_element(a, b):
    c = a * b
    list_store.append(c)
    print(list_store)
    #local scope : Variable accessible only inside its function/block.


add_element(1, 2)
add_element(1, 7)


##Default Parameters/Arguments
def divide(a, b):
    c = a / b
    print(c)


divide(1, 2)


def divide(a, b=1):
    c = a / b
    print(c)


divide(1)


def say_hi(string="Merhaba"):
    print(string)
    print("hi")


say_hi()  #If a parameter is defined with a default value, the function will run without error even if no argument is provided when it is called.


#DRY (Don’t Repeat Yourself) principle means avoiding code duplication by keeping each piece of knowledge or logic in a single place.
#A function is written to group repetitive tasks, organize code, and ensure reusability.

#RETURN: Using function outputs as inputs
def calculate(warm, moisture, charge):
    return (warm + moisture + charge) * 2
calculate(98,10,5)*10
a = calculate(98,10,5)

def calculate(warm, moisture, charge):
    warm=warm * 10
    moisture=moisture * 10
    charge=charge * 10
    output =( warm + moisture + charge)*2
    return warm, moisture, charge, output
calculate(98,10,5)#type=tuple
warm, moisture, charge, output = calculate(98,10,5)

########################################################
#Function call inside a function

def calculate(warm, moisture, charge):
    return int((warm + moisture ) / charge)
calculate(90,10,5)*10

def standardization(a, p):
    return a * 10 / 100 * p * p
standardization(45, 1)
#If we want to use the arguments of other functions inside a function, we also need to add these arguments to the main function.

def all_calculation(warm, moisture, charge, p):
    a = calculate(warm, moisture, charge)
    b = standardization(a, p)
    print(b*10)
all_calculation(1, 3, 5,12)

##################################################
#Local and Global Variables

list_store = [1, 2]#global
def add_element(a, b):
    c = a * b#local
    list_store.append(c)#Affecting the global scope from the local scope
    print(list_store)
add_element(1, 2)
