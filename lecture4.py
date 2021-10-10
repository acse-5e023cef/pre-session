#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pybryt
from lecture import ok, pybryt_reference


# # Introduction to programming in Python
# 
# # Lecture 4

# Learning objectives: You will learn how to:
# 
# * Parse strings to extract specific data of interest.
# * Use dictionaries to index data using any type of key.
# * Learn how to create your own **objects** in Python and develop **member functions** for these new data types.

# ## Python dictionaries
# Suppose we need to store the temperatures in Oslo, London, and Paris. The Python list solution might look like:

# In[3]:


temps = [13, 15.4, 17.5]
# temps[0]: Oslo
# temps[1]: London
# temps[2]: Paris


# In this case, we need to remember the mapping between the index and the city name. It would be easier to specify the name of the city to get the temperature. Containers such as lists and arrays use a continuous series of integers to index elements. However, for many applications, such an integer index is not useful.
# 
# **Dictionaries** are containers where any Python object can be used as an index. Let us rewrite the previous example using a Python dictionary:

# In[4]:


temps = {"Oslo": 13, "London": 15.4, "Paris": 17.5}
print("The temperature in London is", temps["London"])


# Add a new item to a dictionary:

# In[5]:


temps["Madrid"] = 26.0
print(temps)


# Loop (iterate) over a dictionary:

# In[6]:


for city in temps:
    print("The temperature in %s is %g" % (city, temps[city]))


# The index in a dictionary is called the **key**. A dictionary is said to hold key–value pairs. So, in general:
# 
# ```python
# for key in dictionary:
#     value = dictionary[key]
#     print(value)
# ```

# Does the dictionary have a particular key (i.e. a particular data entry)?

# In[7]:


if "Berlin" in temps:
    print("We have Berlin and its temperature is ", temps["Berlin"])
else:
    print("I don't know Berlin' temperature.")


# In[8]:


print("Oslo" in temps)  # i.e. standard boolean expression


# The keys and values can be reached as lists:

# In[9]:


print("Keys = ", temps.keys())
print("Values = ", temps.values())


# Note that the sequence of keys is **arbitrary**! Never rely on it, if you need a specific order of the keys then you should explicitly sort:

# In[10]:


for key in sorted(temps):
    value = temps[key]
    print(key, value)


# Remove Oslo key-value pair:

# In[11]:


del temps["Oslo"]  # remove Oslo key w/value
print(temps)
print(len(temps))


# Similarly to what we saw for arrays, two variables can refer to the same dictionary:

# In[12]:


t1 = temps
t1["Stockholm"] = 10.0
print(temps)


# So, we can see that while we modified `t1`, the `temps` dictionary was also changed.

# Let us look at a simple example of reading the same data from a file and putting it into a dictionary. We will be reading the file [data/deg2.dat](./data/deg2.dat).

# In[13]:


infile = open("data/deg2.dat", "r")
# Start with an empty dictionary
temps = {}
for line in infile:
    # If you examine the file you will see a ':' after the city name,
    # so let's use this as the delimiter for splitting the line.
    city, temp = line.split(":")
    temps[city] = float(temp)
infile.close()

print(temps)


# ## Exercise 4.1: Make a dictionary from a table
# 
# The file [data/constants.txt](data/constants.txt) contains a table of the values and the dimensions of some fundamental constants from physics. We want to load this table into a dictionary `constants`, where the keys are the names of the constants. For example, `constants['gravitational constant']` holds the value of the gravitational constant (6.67259 $\times$ 10$^{-11}$) in Newton's law of gravitation. Make a function `read_constants(file_path)` that reads and interprets the text in the file passed as an argument, and after that returns the dictionary.

# In[14]:


# Uncomment and modify the following code. Do not change variable names for testing purposes.

#def read_constants(file_path):
#     ...
infile = open("data/constants.txt")
    
values = {}
a = []    
for line in infile:
    word = line.split(str)
    a.append(word)
print(a)
#print(constant, value, dimension)
    #values[constant] = float(value)
        
        


# In[15]:


with pybryt.check(pybryt_reference(4, 1)):
    read_constants('./data/constants.txt')


# In[16]:


ok.grade('exercise-4_1')


# ## Exercise 4.2: Reverse a dictionary
# 
# Consider the following dictionary translating some English words to German:
# 
# ```python
# my_dict = {'dog': 'Hund', 'cat': 'Katze', 'house': 'Haus', 'bicycle': 'Fahrrad'}
# ```
# 
# Write a Python function `reverse_dict(dictionary)` that takes any dictionary as input and reverses it. For instance, if `my_dict` is passed, a German-English dictionary with key-value pairs (items) is returned.

# In[17]:


# Uncomment and modify the following code. Do not change variable names for testing purposes.

def reverse_dict(dictionary):
    r_dict = {}
    for key in dictionary:
        r_dict[dictionary[key]] = key
    return r_dict
print(reverse_dict({'a': 'b', 'c': 'd', 'e': 'f', 'g': 'h'}))
#     ...


# In[18]:


with pybryt.check(pybryt_reference(4, 2)):
    reverse_dict({'a': 'b', 'c': 'd', 'e': 'f', 'g': 'h'})


# In[19]:


ok.grade('exercise-4_2')


# ## Exercise 4.3: Compute the area of a triangle
# 
# An arbitrary triangle can be described by the coordinates of its three vertices: $(x_1, y_1), (x_2, y_2), (x_3, y_3)$, numbered in a counterclockwise direction. The area of the triangle is given by the formula:
# 
# $$A = \frac{1}{2}|x_2y_3 - x_3y_2 - x_1y_3 + x_3y_1 + x_1y_2 - x_2y_1|.$$
# 
# Write a function `triangle_area(vertices)` that returns the area of a triangle whose vertices are specified by the argument `vertices`, which is a dictionary and not a list. The keys in the dictionary correspond to the vertex number (1, 2, or 3) while the values are 2-tuples with the $x$ and $y$ coordinates of the vertex - $(x, y)$. For example, for a triangle with vertices $(0, 0)$, $(1, 0)$, and $(0, 2)$ the `vertices` argument is: `{1: (0, 0), 2: (1, 0), 3: (0, 2)}`.
# 
# **Question**: Can the function `triangle_area(vertices)` accept both a nested list and a dictionary as an argument?

# In[28]:


# Uncomment and modify the following code. Do not change variable names for testing purposes.

def triangle_area(vertices):
    v1 = vertices[1]
    v2 = vertices[2]
    v3 = vertices[3]
    return 1/2*(v2[0]*v3[1] - v3[0]*v2[1] - v1[0]*v3[1] + v3[0]*v1[1] + v1[0]*v2[1] - v2[0]*v1[1])
print(triangle_area({1: (100, 20), 2: (101, 130), 3: (-50, 22)}))


# In[29]:


with pybryt.check(pybryt_reference(4, 3)):
    triangle_area({1: (100, 20), 2: (101, 130), 3: (-50, 22)})


# In[30]:


ok.grade('exercise-4_3')


# ## String manipulation
# 
# Text in Python is represented as **strings**. Programming with strings is therefore the key to interpret text in files and construct new text (i.e. **parsing**). First we show some common string operations and then we apply them to real examples. Our sample string used for illustration is:

# In[31]:


s = "Berlin: 18.4 C at 4 pm"


# Strings behave much like lists/tuples - they are simply a sequence of characters:

# In[32]:


print("s[0] =", s[0])
print("s[1] =", s[1])


# Substrings are just slices of lists and arrays:

# In[33]:


# from index 8 to the end of the string
print(s[8:])


# In[34]:


# indices 8, 9, 10 and 11 (not 12!)
print(s[8:12])


# In[36]:


# from index 8 to 8 from the end of the string
print(s[8:-8])


# You can also find the start index of a substring:

# In[37]:


# where does "Berlin" start?
print(s.find("Berlin"))


# In[38]:


print(s.find("pm"))


# In[40]:


print(s.find("Oslo"))


# In this last example, `Oslo` does not exist in the list so the return value is -1.

# We can also check if a substring is contained in a string:

# In[41]:


print("Berlin" in s)


# In[42]:


print("Oslo" in s)


# In[43]:


if "C" in s:
    print("C found")
else:
    print("C not found")


# ### Search and replace
# Strings also support substituting a substring by another string. In general this looks like `s.replace(s1, s2)`, which replaces string `s1` in `s` by string `s2`, e.g.:

# In[44]:


s = s.replace(" ", "_")
print(s)


# In[45]:


s = s.replace("Berlin", "Bonn")
print(s)


# In[46]:


# Replace the text before the first colon by 'London'
s = s.replace(s[:s.find(":")], "London")
print(s)


# Notice that in all these examples, we assign the new result back to `s`. One of the reasons we are doing this is that strings are actually constant (i.e immutable) and therefore cannot be modified *inplace*. We **cannot** write for example:
# 
# ```python
# s[18] = '5'
# TypeError: "str" object does not support item assignment
# ```

# We also encountered examples above where we used the `split` function to break up a line into separate substrings for a given separator (where a space is the default delimiter). Sometimes we want to split a string into lines - i.e. the delimiter is the [carriage return](http://en.wikipedia.org/wiki/Carriage_return). This can be surprisingly tricky because different computing platforms (e.g. Windows, Linux, MacOS) use different characters to represent a carriage return. For example, Unix uses `\n`. Luckly Python provides a *cross platform* way of doing this so regardless of what platform created the data file, or what platform you are running Python on, it will do the *right thing*: 

# In[48]:


t = "1st line\n2nd line\n3rd line"

print(f"original t =\n{t}")


# In[49]:


# This works here but will give you problems if you are switching
# files between Windows and either Mac or Linux.
print(t.split("\n"))


# In[ ]:


# Cross platform (i.e. better) solution
print(t.splitlines())


# ### Stripping off leading/trailing whitespace
# When processing text from a file and composing new strings, we frequently need to trim leading and trailing whitespaces:

# In[50]:


s = "        text with leading and trailing spaces          \n"
print("-->%s<--" % s.strip())


# In[51]:


# left strip
print("-->%s<--" % s.lstrip())


# In[52]:


# right strip
print("-->%s<--" % s.rstrip())


# Please note that carriage return is considered as a whitespace character as well.

# ### `join()` - the opposite of `split()`
# We can join a list of substrings to form a new string. Similar to `split()`, we put strings together with a delimiter inbetween:

# In[54]:


strings = ["Newton", "Secant", "Bisection"]
print(", ".join(strings))


# You can prove to yourself that these are inverse operations:
# ```python
# t = delimiter.join(stringlist)
# stringlist = t.split(delimiter)
# ```

# As an example, let's split off the first two words on a line:

# In[55]:


line = "This is a line of words separated by space"
words = line.split()
print("words = ", words)
line2 = " ".join(words[2:])
print("line2 = ", line2)


# ## Exercise 4.4: Improve a program
# 
# The file [data/densities.dat](./data/densities.dat) contains a table of densities of various substances measured in $\text{gcm}^{-3}$. The following program reads the data in this file and produces a dictionary whose keys are the names of substances, and the values are the corresponding densities.

# In[56]:


def read_densities(filename):
    infile = open(filename, 'r')
    densities = {}
    for line in infile:
        words = line.split()
        density = float(words[-1])

        if len(words[:-1]) == 2:
            substance = words[0] + ' ' + words[1]
        else:
            substance = words[0]

        densities[substance] = density

    infile.close()
    return densities


densities = read_densities('data/densities.dat')
print(densities)


# One problem we face when implementing the program above is that the name of the substance can contain one or two words, and maybe more words in a more comprehensive table. The purpose of this exercise is to use string operations to shorten the code and make it more general. Implement the following two methods in separate functions `read_densities_join` and `read_densities_substrings`, and control that they give the same result.
# 
# 1. In `read_densities_join`, let *substance* consist of all the words but the last and use the `join()` method to combine the words. Replace any spaces between words in substances with underscore.
# 2. In `read_densities_substrings`, observe that all the densities (numerical values) start in the same column, and use substrings to divide line into two parts. Replace any spaces between words in substances with underscore. (**Hint**: Remember to strip the first part such that, e.g. the density of ice is obtained as `densities['ice']` and not `densities['ice     ']`.)

# In[92]:


# Uncomment and modify the following code. Do not change variable names for testing purposes.

def read_densities_join(filename):
    infile = open(filename, 'r')
    densities = {}
    for line in infile:
        words = line.split()
        substance = "_".join(words[: -1])
        density = float(words[-1])
        
        densities[substance] = density
        
    infile.close()
    return densities
#read_densities_join('./data/densities.dat')

def read_densities_substrings(filename):
    infile = open(filename, 'r')
    densities = {}
    for line in infile:
        words = line
        substance = words[:12]
        density = float(words[12:])
        substance = substance.rstrip()
        substance = substance.replace(" ", "_")
        densities[substance] = density
    print(densities)
        
    return
read_densities_substrings('./data/densities.dat')


# In[66]:


with pybryt.check(pybryt_reference(4, '4_1')):
    read_densities_join('./data/densities.dat')


# In[94]:


with pybryt.check(pybryt_reference(4, '4_2')):
    read_densities_substrings('./data/densities.dat')


# In[95]:


ok.grade('exercise-4_4')


# ## Class: encapsulating variables/data and functions
# 
# A class encapsulates variables/data and functions into one single unit. As a programmer, you can create a new class and thereby a new **object type** (similar to those you have already encountered - `int`, `float`, `string`, `list`, `file`, etc.). Once you have created a class you can create many instances of that type as you wish, just as you can have many `int` or `float` objects.
# 
# Modern programming makes heavy use of classes and object orientated programming to manage software complexity, making these important concepts to understand. However, for non-trivial applications the design of good abstractions and classes requires careful consideration, otherwise one can unintentionally increase complexity and hurt the performance of your code. Therefore, you should consider this lecture merely as a gentle introduction illustrated with some simple examples.

# ## Representing a function by a class
# 
# Consider a function of $t$ with a parameter $v_0$:
# 
# $$ y(t: v_0, g)=v_0t - {1\over2}gt^2 $$
# 
# We need both $v_0$, $g$ and $t$ to evaluate $y$. How might we implement this?

# One option is to assume we will always pass in all variables as arguments:
# ```python
# def y(t, v0, g=9.81):
#     return v0*t - 0.5*g*t**2
# ```
# This looks like a reasonable solution when there are only a couple of parameters. But the software complexity quickly gets out of hand as the number of variables increases (I have worked on legacy codes that had function argument lists that were hundreds of lines long because there was no notion of encapsulation!)
# 
# Alternatively we might define `v0` and `g` as global variables:
# ```python
# g = 9.81
# v0 = ...
# 
# ...
# 
# def y(t):
#     return v0*t - 0.5*g*t**2
# ```
# However, the use of global variables is strongly discouraged for many reasons, e.g. very error prone, increased risk of namespace pollution (variables being clobbered when you import a Python module), makes it difficult to manage instances where there might be multiple values for the global variable within the same context, etc.

# Let us look at how we might instead implement this as a class.
# 
# While we will not cover it in detail here, it is worth noting that professional developers often use [UML (Unified Modeling Language)](http://en.wikipedia.org/wiki/Unified_Modeling_Language) to illustrate the design of a class. Here is a UML diagram for this example:
# 
# ![Simple UML example](https://github.com/ggorman/Introduction-to-programming-for-geoscientists/raw/master/notebook/images/class_Y_UML.png)
# 
# For this example `class Y` for $y(t: v_0, g)$ has variables `v0` and `g` and a function `value` for computing $y(t: v_0, g)$. Often classes also have the special function `__init__` for initialising class variables.
# 
# Here is an implementation of this class:

# In[96]:


class Y:
    def __init__(self, v0, g=9.81):
        self.v0 = v0
        self.g = g

    def value(self, t):
        return self.v0*t - 0.5*self.g*t**2


# An example of its usage: 

# In[98]:


y = Y(v0=3)       # Create instance
v = y.value(0.1)  # Compute function value

print(v)


# When we write `y = Y(v0=3)` we create a new *instance* of *type `Y`*.
# 
# `Y(3)` is a call to the constructor:
# 
# ```python
# def __init__(self, v0, g=9.81):
#     self.v0 = v0
#     self.g = g
# ```

# Think of `self` as `y`, i.e. the new variable to be created. `self.v0` means that we attach a variable `v0` to self (`y`).
# 
# ```python
# Y.__init__(y, 3)   # is the logic behind Y(3)
# ```
# 
# `self` is always the first argument/parameter in a function, but **never** inserted in the call! After `y = Y(3)`, `y` has two variables `v0` and `g`, and we can take a look at these:

# In[99]:


print(y.v0)
print(y.g)


# Functions in classes are called **methods**. Variables in classes are called **attributes**. Therefore, in the above example the `value` *method* was
# 
# ```python
# def value(self, t):
#   return self.v0*t - 0.5*self.g*t**2
# ```

# Example on a call:

# In[100]:


v = y.value(t=0.1)


# `self` is left out in the call (as discussed above), but Python automatically inserts `y` as the `self` argument inside the `value` method. Inside the `value` *method* things *appear* as
# 
# ```python
# return y.v0*t - 0.5*y.g*t**2
# ```

# The method `value` has, through `self`, access to the attributes. Attributes are like *global variables* in the class, and any method gets a `self` parameter as its first argument. The method can then access the attributes of the class through `self`.

# In summary, `class Y` collects the attributes `v0` and `g` and the method `value` together as a single unit. `value(t)` is function of `t` only, but has access to the class attributes `v0` and `g`.
# 
# The great feature of Python is that we can send `y.value` as an ordinary function of `t` to any other function that expects a function `f(t)`:

# In[101]:


import numpy as np


def table(f, tstop, n):
    """Make a table of t, f(t) values."""
    for t in np.linspace(0, tstop, n):
        print(t, f(t))


# In[103]:


def g(t):
    return np.sin(t)*np.exp(-t)


table(g, 2*np.pi, 5)  # pass in ordinary function as first argument


# In[104]:


y = Y(6.5)
table(y.value, 2*np.pi, 5)  # pass in class method as first argument


# ## Exercise 4.5: Make a class for function evaluation.
# Make a class called `F` that implements the function
# 
# $$f(x: a, w) = e^{−ax}\sin(wx).$$
# 
# A `value(x)` method computes values of $f$ for a given $x$, while $a$ and $w$ are class attributes as specified as arguments in the class's `__init__` method.

# In[105]:


# Uncomment and complete this code - keep the names the same for testing purposes.

class F:
    def __init__(self, a, w):
        self.a = a
        self.w = w

    def value(self, x):
        return np.exp(-self.a*x)*np.sin(self.w*x)
#         ...


# In[106]:


with pybryt.check(pybryt_reference(4, 5)):
    f = F(0.73, 1.14185)
    f.a, f.w, f.value(3)


# In[107]:


ok.grade('exercise-4_5')


# ## Exercise 4.6: Make a simple class
# 
# Make a class called `Simple` with:
# * one attribute, `i`,
# * one method `double` that replaces the value of `i` by `2*i`, and
# * an `__init__` method that initializes the attribute `i`. 
# 
# Use the following code snippet to convince yourself that your class is behaving as expected.
# 
# ```python
# s1 = Simple(4)
# for i in range(4):
#     s1.double()
# print(s1.i)
# 
# s2 = Simple('Hello')
# s2.double(); s2.double()
# print(s2.i)
# s2.i = 100
# print(s2.i)
# ```

# In[116]:


# Uncomment and complete this code - keep the names the same for testing purposes.

class Simple:
    def __init__(self, i):
        self.i = i
        
        ...

    def double(self):
        self.i = 2*self.i
        ...


# In[117]:


with pybryt.check(pybryt_reference(4, 6)):
    simple = Simple(200.51)
    simple.i
    for k in range(10):
        simple.double()
        simple.i


# In[118]:


ok.grade('exercise-4_6')


# ## Another class example: a bank account
# 
# * **Attributes**:
#     * `name`: name of the owner
#     * `number`: account number
#     * `balance`: balance
# * **Methods**:
#     * `deposit`: adds amount to `balance`
#     * `withdraw`: subtracts amount from `balance`
#     * `dump`: pretty pring

# In[119]:


class Account:
    def __init__(self, name, account_number, initial_amount=0):
        self.name = name
        self.number = account_number
        self.balance = initial_amount

    def deposit(self, amount):
        self.balance += amount  # self.balance += amount is equivalent to self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance -= amount  # self.balance -= amount is equivalent to self.balance = self.balance - amount

    def dump(self):
        print(f'name: {self.name}, account number: {self.number}, balance: {self.balance}')


# In[120]:


a1 = Account('John Olsson', '19371554951')
a2 = Account('Liz Olsson', '19371564761', 20000)
a1.deposit(1000)
a1.withdraw(4000)
a2.withdraw(10500)
a1.withdraw(3500)


# In[121]:


a1.dump()


# In[122]:


a2.dump()


# ## Exercise 4.7: Extend a class
# 
# Add an attribute called `transactions` to the `Account` class given above. The new attribute counts the number of transactions done in the `deposit` and `withdraw` methods. The total number of transactions should be printed in the `dump` method. Write a simple test program to convince yourself transaction gets the right value after some calls to `deposit` and `withdraw`. When an object of class `Account` is created, attribute `transactions` is initialised to 0.

# In[135]:


# Uncomment and complete this code - keep the names the same for testing purposes.

class Account:
    def __init__(self, name, account_number, initial_amount=0, initial_transactions=0):
        self.name = name
        self.number = account_number
        self.balance = initial_amount
        self.transactions = initial_transactions

    def deposit(self, amount):
        self.balance += amount
        self.transactions += 1

    def withdraw(self, amount):
        self.balance -= amount
        self.transactions += 1

    def dump(self):
        print(f'name: {self.name}, account number: {self.number}, balance: {self.balance}, transations: {self.transactions}')


# In[136]:


with pybryt.check(pybryt_reference(4, 7)):
    account = Account('Marijan', '321321321', initial_amount=2351)
    account.name, account.number, account.balance, account.transactions

    for i in range(5):
        account.deposit(1001)
        account.balance, account.transactions
        account.withdraw(432.3)
        account.balance, account.transactions


# In[137]:


ok.grade('exercise-4_7')


# ## Protecting attributes
# 
# It is not possible in Python to explicitly protect attributes from being overwritten by the calling function, i.e. the following is possible but not intended:

# In[138]:


a1.name = 'Some other name'
a1.balance = 100000
a1.no = '19371564768'


# **Assumptions** on correct usage include:
# 
# * The attributes should not be modified directly.
# * The `balance` attribute can be viewed.
# * Changing `balance` is done through with the methods `draw` and `deposit`.
# 
# The remedy is to adopt the convention that attributes and methods not intended for use outside the class should be marked as protected by prefixing the name with an underscore (e.g. `_name`). This is just a convention to warn you to stay away from messing with the attribute directly. There is no technical way of stopping attributes and methods from being accessed directly from outside the class.
# 
# We rewrite the account class using this convention:

# In[139]:


class AccountP:
    def __init__(self, name, account_number, initial_amount):
        self._name = name
        self._no = account_number
        self._balance = initial_amount

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def get_balance(self):    # NEW - read balance value
        return self._balance

    def dump(self):
        s = '%s, %s, balance: %s' % (self._name, self._no, self._balance)
        print(s)


# In[140]:


a1 = AccountP('John Olsson', '19371554951', 20000)
a1.withdraw(4000)


# In[141]:


print(a1._balance)      # it works, but a convention is broken


# In[142]:


print(a1.get_balance())  # correct way of viewing the balance


# In[144]:


a1._no = '19371554955'  # if you did this you'd probably lose your job! Don't mess with the convention.


# ### Example - a phone book
# 
# A phone book is a list of data about persons. Typical data includes: name, mobile phone, office phone, private phone, email. This data about a person can be  collected in a class as **attributes**. Think about what kinds of **methods** make sense for this class, e.g.:
# 
# * Constructor for initializing name, plus one or more other data
# * Add new mobile number
# * Add new office number
# * Add new private number
# * Add new email
# * Write out person data

# In[145]:


class Person:
    def __init__(self, name, mobile_phone=None, office_phone=None, private_phone=None, email=None):
        self.name = name
        self.mobile = mobile_phone
        self.office = office_phone
        self.private = private_phone
        self.email = email

    def add_mobile_phone(self, number):
        self.mobile = number

    def add_office_phone(self, number):
        self.office = number

    def add_private_phone(self, number):
        self.private = number

    def add_email(self, address):
        self.email = address

    def dump(self):
        s = self.name + '\n'
        if self.mobile is not None:
            s += 'mobile phone:   %s\n' % self.mobile
        if self.office is not None:
            s += 'office phone:   %s\n' % self.office
        if self.private is not None:
            s += 'private phone:  %s\n' % self.private
        if self.email is not None:
            s += 'email address:  %s\n' % self.email
        print(s)


# In[146]:


p1 = Person('Gerard Gorman', email='g.gorman@imperial.ac.uk')
p1.add_office_phone('49985')

p2 = Person('ICT Service Desk', office_phone='49000')
p2.add_email('service.desk@imperial.ac.uk')

phone_book = {'Gorman': p1, 'ICT': p2}
for p in phone_book:
    phone_book[p].dump()


# ### Example - a circle
# A circle is defined by its center point $x_0$, $y_0$ and its radius $R$. These data can be attributes in a class. Possible methods in the class are `area` and `circumference`. The constructor initializes $x_0$, $y_0$ and $R$.

# In[147]:


class Circle:
    def __init__(self, R, x0, y0,):
        self.x0, self.y0, self.R = x0, y0, R

    def area(self):
        return np.pi * self.R**2

    def circumference(self):
        return 2*np.pi*self.R


# In[148]:


c = Circle(2, -1, 5)
print('A circle with radius %g at (%g, %g) has area %g' % (c.R, c.x0, c.y0, c.area()))


# ## Exercise 4.8: Make a class for straight lines
# 
# Make a class called `Line` whose constructor takes two points `p0` and `p1` (2-tuples or 2-lists) as input. The line goes through these two points (see function `line` defined below for the relevant formula of the line). A `value(x)` method computes the `y` value on the line at the point `x` or returns `None` if the line is vertical (i.e. if `(x1-x0) == 0`).
# 
# ```python
# def line(x0, y0, x1, y1):
#     """
#     Compute the coefficients a and b in the mathematical
#     expression for a straight line y = a*x + b that goes
#     through two points (x0, y0) and (x1, y1).
#     x0, y0: a point on the line (floats).
#     x1, y1: another point on the line (floats).
#     return: coefficients a, b (floats) for the line (y=a*x+b).
#     """
#     try:
#         a = (y1 - y0)/(x1 - x0)
#         b = y0 - a*x0
#     except ZeroDivisionError:
#         a, b = None, None
#     
#     return a, b
# ```

# In[174]:


# Uncomment and complete this code - keep the names the same for testing purposes.

class Line:
    def __init__(self, p0, p1):
        self.p0 = p0
        self.p1 = p1
        self.x0 = p0[0]
        self.x1 = p1[0]
        self.y0 = p0[1]
        self.y1 = p1[1]
        
        
        ...

    def value(self, x):
        try:
            if (self.x1 - self.x0) != 0:
                a = (self.y1 - self.y0)/(self.x1 - self.x0)
                b = self.y0 - a*self.x0
            else:
                raise ZeroDivisionError
        except ZeroDivisionError:
            a, b = None
            return b
        
        return a*x+b
line = Line(p0=(123.1, 251.6), p1=(44.3, 12.9))
line.p0, line.p1, line.value(3.141)


# In[175]:


with pybryt.check(pybryt_reference(4, 8)):
    line = Line(p0=(123.1, 251.6), p1=(44.3, 12.9))
    line.p0, line.p1, line.value(3.141)


# In[176]:


ok.grade('exercise-4_8')


# ## Exercise 4.9: Make a class for quadratic functions
# 
# Consider a quadratic function $f(x; a, b, c) = ax^2 + bx + c$. Make a class called `Quadratic` for representing $f$, where $a$, $b$, and $c$ are attributes, and the methods are:
# 
# 1. `value(self, x)` for computing a value of $f$ at a point $x$,
# 2. `table(self, L, R, n)` for writing out a table of $x$ and $f$ values for $n$ values of $x$ in the interval $[L, R]$,
# 3. `roots(self)` for computing the two roots and returning them both in a tuple `(x1, x2)`.

# In[182]:


# Uncomment and complete this code - keep the names the same for testing purposes.
from math import sqrt
class Quadratic:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
        ...

    def value(self, x):
        return self.a*x**2 + self.b*x + self.c
        ...

    def table(self, L, R, n):
        a = []
        for x in np.linspace(L, R, n):
            a.append([x, self.value(x)])
        return a    
        
            #print(x, self.value(x))
#         ...

    def roots(self):
        
        q = sqrt(self.b**2 - 4*self.a*self.c)
        x1 = (-self.b + q)/(2*self.a)
        x2 = (-self.b - q)/(2*self.a)
        root = [x1, x2]
        return root
#         ...


# In[183]:


with pybryt.check(pybryt_reference(4, 9)):
    f = Quadratic(a=10.2, b=5.6, c=-30.11)
    f.a, f.b, f.c, f.value(500), f.roots()


# In[184]:


ok.grade('exercise-4_9')


# ## Special methods
# 
# Some class methods have leading and trailing double underscores. You have already met one of these, `__init__` used to initialise an object upon creation. Other examples include `__call__(self, ...)` and `__add__(self, other)`. These *special methods* enable more elegant abstractions and interfaces. Consider for example the difference between the equivalent statements:
# 
# ```python
# y = Y(4)
# ```
# rather than
# ```python
# y = Y
# Y.__init__(Y, 4)
# ```

# ### Special member function, `__call__`: make the class instance behave and look as a function
# 
# Let us replace the `value` method in `class Y` by a `__call__` special method:

# In[185]:


class Y:
    def __init__(self, v0, g=9.81):
        self.v0 = v0
        self.g = g

    def __call__(self, t):
        return self.v0*t - 0.5*self.g*t**2


# Now we can write:

# In[186]:


y = Y(3)
v = y(0.1)  # same as v = y.__call__(0.1)


# The instance $y$ behaves/looks as a function! The `value(t)` method in the first example does the same, but the special method `__call__` provides a more elegant and concise syntax for computing function values.

# ### Special member function, `__str__`: represent object as a string for printing
# 
# In Python, we can usually print an object `a` by `print(a)`. This works for built-in types (strings, lists, floats, ...). However, if we have made a new type through a class, Python does not know how to print objects of this type. However, if the class has defined a method `__str__` , Python will use this method to convert the object to a string.

# In[187]:


class Y:
    def __init__(self, v0, g=9.81):
        self.v0 = v0
        self.g = g

    def __call__(self, t):
        return self.v0*t - 0.5*self.g*t**2

    def __str__(self):
        return '%g*t - 0.5*%g*t**2' % (self.v0, self.g)


# In[188]:


y = Y(1.5)
print(y)


# ### Special methods for overloading arithmetic operations
# 
# ```python
# c=a+b               # c = a.__add__(b)  
# c=a-b               # c = a.__sub__(b)  
# c = a*b             # c = a.__mul__(b)  
# c = a/b             # c = a.__div__(b)  
# c = a**e            # c = a.__pow__(e)
# ```

# ### Special methods for overloading conditional operations
# 
# ```python
# a == b               #  a.__eq__(b)  
# a != b               #  a.__ne__(b)  
# a < b                #  a.__lt__(b)  
# a <= b               #  a.__le__(b)  
# a > b                #  a.__gt__(b)  
# a >= b               #  a.__ge__(b)
# ```

# In[189]:


ok.score()


# In[ ]:





# In[ ]:




