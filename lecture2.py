#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pybryt
from lecture import ok, pybryt_reference


# # Introduction to programming in Python
# 
# # Lecture 2

# Learning objectives:
# 
# * Learn how to modify elements in a list.
# * Learn how to iterate through different combinations of lists.
# * Know how to use a *tuple* to store data elements and understand how it differs from a *list*.
# * Know the difference between locally-scoped and globally-scoped variables.
# * Be able to use an *if* statement to execute some code blocks conditionally.
# * Learn how to compute using [Numerical Python (*NumPy*)](http://www.numpy.org/).
# * Know how to handle multidimensional arrays.

# # Changing elements in a list
# Let's say we want to add 2 to all the numbers in a list:

# In[7]:


v = [-1, 1, 10]
for e in v:
    e += 2  # note that e += 2 is equivalent to e = e + 2
print(v)


# We can see that the list `v` is unaltered! This is because inside the loop, `e` is an ordinary (`int`) variable. At the start of the iteration, `e` is assigned a *copy* of the next element in the list. Inside the loop, we can change `e`, but `v` remains unaltered. If we want to change `v`, we have to use an index to access and modify its elements:

# In[8]:


v[1] = 4  # assign 4 to the 2nd element (index 1) in v
print(v)


# To add 2 to all values we need a `for` loop over indices:

# In[9]:


for i in range(len(v)):
    v[i] = v[i] + 2
print(v)


# Note that this time we iterate over the indices of the list elements
# 
# ```python
# for i in range(len(v)):
#     ...
# ```
# 
# instead of iterating over the values of elements in the list
# 
# ```python
# for e in v:
#     ...
# ```

# ## Exercise 2.1: Create a list and modify it.
# 
# Write a Python function `mult(vector, n)` which takes list `vector` and number `n` as an input arguments. The function should multiply each element in the list by `n` using a `for` loop and return the resulting list.

# In[10]:


# Uncomment and modify the following lines. Do not change any variable names for testing purposes.

def mult(vector, n):
    for i in range(len(vector)):
        vector[i] = vector[i]*n
    return vector
#print(mult([2.1, 99.9, -10, 2], 3))


# In[11]:


with pybryt.check(pybryt_reference(2, 1)):
    mult([2.1, 99.9, -10, 2], 3)


# In[12]:


ok.grade('exercise-2_1')


# ## Traversing multiple lists simultaneously: `zip(list1, list2, ...)`
# Let us consider how we can loop over elements in both `Cdegrees` and `Fdegrees` at the same time. One approach would be to use list indices:

# In[13]:


# First, we have to recreate the data from the previous lecture
Cdegrees = [deg for deg in range(-20, 41, 5)]
Fdegrees = [(9/5)*deg + 32 for deg in Cdegrees]

for i in range(len(Cdegrees)):
    print(Cdegrees[i], Fdegrees[i])


# An alternative construct, regarded as more ”Pythonic”, uses the `zip` function:

# In[14]:


for C, F in zip(Cdegrees, Fdegrees):
    print(C, F)


# Using `zip`, we can also traverse three lists simultaneously:

# In[15]:


l1 = [3, 6, 1]; l2 = [1.5, 1, 0]; l3 = [9.1, 3, 2]

for e1, e2, e3 in zip(l1, l2, l3):
    print(f'e1: {e1}, e2: {e2}, e3: {e3}')


# If the lists are of unequal length, then the loop stops when we reach the end of the shortest list. Experiment with this:

# In[16]:


l1 = [3, 6, 1, 4, 6]  # len(l1) == 5
l2 = [1.5, 1, 0, 7]  # len(l1) == 4
l3 = [9.1, 3, 2, 0, 9]  # len(l1) == 5

for e1, e2, e3 in zip(l1, l2, l3):
    print(f'e1: {e1}, e2: {e2}, e3: {e3}')


# ## Nested lists: list of lists
# A `list` can contain **any** object, including another `list`. To illustrate this, consider storing the conversion table as a single Python list rather than two separate lists.

# In[17]:


Cdegrees = [C for C in range(-20, 41, 5)]
Fdegrees = [(9/5)*C + 32 for C in Cdegrees]
table1 = [Cdegrees, Fdegrees]  # List of two lists

print("table1 = ", table1)
print("table1[0] = ", table1[0])  # access the first element of list table1 - Cdegrees list
print("table1[1] = ", table1[1])  # access the second element of list table1 - Fdegrees list
print("table1[1][3] = ", table1[1][3])  # access 4th element in the 2nd list


# This gives us a table with two rows. How do we create a table of columns instead:

# In[18]:


table2 = []
for C, F in zip(Cdegrees, Fdegrees):
    row = [C, F]
    table2.append(row)

print(table2)


# We can also use list comprehension to do this more elegantly:

# In[19]:


table2 = [[C, F] for C, F in zip(Cdegrees, Fdegrees)]
print(table2)


# And we can loop through this list as before:

# In[20]:


for C, F in table2:
    print(C, F)


# Since elements of `table2` are length-2 lists, in each iteration, we *unpack* each of the length-2 elements to `C` and `F`.

# ## Tuples: lists that cannot be changed
# 
# Tuples are **constant** lists, i.e. we can use them in much the same way as lists except we cannot modify them. They are an example of an [**immutable**](http://en.wikipedia.org/wiki/Immutable_object) type.

# In[21]:


t = (2, 4, 6, 'temp.pdf')  # Define a tuple.
t = 2, 4, 6, 'temp.pdf'  # Can skip parenthesis as it is assumed in this context.


# Let us see what happens when we try to modify the tuple like we did with a list:

# ```python
# t[1] = -1
# 
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-3-593c03edf054> in <module>()
# ----> 1 t[1] = -1
# 
# TypeError: 'tuple' object does not support item assignment
# ```

# ```python
# t.append(0)
# 
# ---------------------------------------------------------------------------
# AttributeError                            Traceback (most recent call last)
# <ipython-input-19-78592bf72d62> in <module>()
# ----> 1 t.append(0)
# 
# AttributeError: 'tuple' object has no attribute 'append'
# ```

# ```python
# del t[1]
# 
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-20-0193a527a912> in <module>()
# ----> 1 del t[1]
# 
# TypeError: 'tuple' object doesn't support item deletion
# ```

# However, we can use the tuple to compose a new tuple:

# In[22]:


t = t + (-1.0, -2.0)
print(t)


# So, why would we use tuples when lists have more functionality?
# 
# * Tuples are constant and thus *protected against accidental changes*.
# * Tuples are *faster* than lists.
# * Tuples are *widely used* in Python software (so you need to know about tuples to understand other people's code!)
# * Tuples (but not lists) can be used as *keys in dictionaries* (more about dictionaries later).

# ## Exercise 2.2: Make a table (a list of lists) of function values
# 
# * Write a loop that evaluates the expression $y(t) = v_0 t − {1\over2}gt^2$ for 11 evenly spaced $t$ values ranging from $0$, to $2v_0/g$ (remember that dividing a range into $n$ intervals results in $n+1$ values). You can assume that $v_0 = 1\,$ms$^{-1}$ and $g = 9.81\,$ms$^{-2}$.
# * Store the time values and displacement ($y$) values as a nested list, i.e.
# ```python
# tlist = [t0, t1, t2, ...]
# ylist = [y0, y1, y2, ...]
# displacement = [tlist, ylist]
# ```
# * Use the variable names `tlist`, `ylist` and `displacement` as illustrated in the above example for testing purposes.

# In[23]:


# Uncomment and modify the following lines. Do not change variable names for testing purposes.

v0 = 1
g = 9.81
t = 0

# why is this not working?
# tlist = [t for t in range(0, 2*v0/g + 2*v0/g/10, 2*v0/g/10)]

tlist = []
while t <= 2*v0/g*1.01:
    tlist.append(t)
    t = t + 2*v0/g/10
    
ylist = [v0*t - 1/2*g*t**2 for t in tlist]
displacement = [tlist, ylist]
#print(displacement)


# In[24]:


with pybryt.check(pybryt_reference(2, 2)):
    tlist, ylist, displacement


# In[25]:


ok.grade('exercise-2_2')


# ## The `if` construct
# Let us consider we need to program the following function:
# $$
# f(x)= 
# \begin{cases}
#     \sin(x),& \text{if } 0 \leq x \leq \pi\\
#     0,              & \text{otherwise}
# \end{cases}
# $$
# To do this, we need the `if` construct:

# In[26]:


from math import sin, pi


def f(x):
    if 0 <= x <= pi:
        return sin(x)
    else:
        return 0


print('f(-pi/2) =', f(-pi/2))
print('f(pi/2) =', f(pi/2))
print('f(3*pi/2) =', f(3*pi/2))


# Please note the indentations we used to define which statements belong to which condition. Sometimes, it is clearer to write this as an *inline* statement:

# In[27]:


def f(x):
    return (sin(x) if 0 <= x <= pi else 0)


print('f(-pi/2) =', f(-pi/2))
print('f(pi/2) =', f(pi/2))
print('f(3*pi/2) =', f(3*pi/2))


# The *else* block can be skipped if there are no statements to be executed when `False`. In general, we can put together multiple conditions. Only the first condition that is `True` is executed.
# 
# ```python
# if condition1:
#     <block of statements, executed if condition1 is True>
# elif condition2:
#     <block of statements, executed if condition1 is False and condition2 is True>
# elif condition3:
#     <block of statements, executed if conditions 1 and 2 are False and condition3 is True>
# else:
#     <block of statements, executed if conditions 1, 2, and 3 are False>
#     
# <next statement of the program>
# ```

# ## Exercise 2.3: Express a step (Heaviside) function as a Python function
# The following "step" function is known as the Heaviside function and it is widely used in mathematics:
# $$
# H(x)=
# \begin{cases}
#     0, & \text{if}\; x < 0\\
#     1, & \text{if}\; x \ge 0.
# \end{cases}
# $$
# Write a Python function `heaviside(x)` that computes $H(x)$.

# In[28]:


# Uncomment and modify the following lines. Do not change variable names for testing purposes.

def heaviside(x):
    return(0 if x < 0 else 1)


# In[29]:


with pybryt.check(pybryt_reference(2, 3)):
    heaviside(-1000), heaviside(1000), heaviside(0)


# In[30]:


ok.grade('exercise-2_3')


# ## Exercise 2.4: Implement the factorial function
# 
# The factorial of $n$, written as $n!$, is defined as
# 
# $$n! = n(n − 1)(n − 2) \cdot \ldots \cdot 2 \cdot 1,$$
# 
# with the special cases
# 
# $$1! = 1,$$ $$0! = 1.$$
# 
# For example, $4! = 4 \cdot 3 \cdot 2 \cdot 1 = 24$, and $2! = 2 \cdot 1 = 2$.
# 
# Implement your own factorial function to calculate $n!$. Return $1$ immediately if $n$ is $1$ or $0$; otherwise use a loop to compute $n!$. You can use Python's own [math.factorial(x)](https://docs.python.org/3/library/math.html) to check your code.

# In[31]:


# Uncomment and complete this code - keep the names the same for testing purposes.
import math
def my_factorial(n):
    sum = 1
    if n == 1 or n == 0:
        return 1
    else:
        for i in range(1,n+1):
            sum = sum * i
        return sum


# In[32]:


with pybryt.check(pybryt_reference(2, 4)):
    my_factorial(10)


# In[33]:


ok.grade('exercise-2_4')


# ## Exercise 2.5: Compute the length of a path
# 
# Some object is moving along a path in the plane. At $n$ points of time, we have recorded the corresponding $(x, y)$ positions of the object:
# $(x_0, y_0), (x_1, y_1), \ldots, (x_{n-1}, y_{n-1})$. The total length $L$ of the path from $(x_0, y_0)$ to $(x_{n-1}, y_{n-1})$ is the sum of all the individual line segments $(x_{i-1}, y_{i-1})$ to $(x_i, y_i)$, $i = 1, \ldots, n-1$:
# 
# $$L = \sum_{i=1}^{n-1}{\sqrt{(x_i - x_{i-1})^2 + (y_i - y_{i-1})^2}}.$$
# 
# Create a function `path_length(x, y)` for computing $L$ according to the formula. The arguments `x` and `y` are two lists that hold all the $x_0, \ldots, x_{n-1}$ and $y_0, \ldots, y_{n-1}$ coordinates, respectively. Test the function on a triangular path with the four points (1, 1), (2, 1), (1, 2), and (1, 1).

# In[34]:


# Uncomment and complete this code - keep the names the same for testing purposes.
from math import sqrt
def path_length(x, y):
    L = 0
    for i in range(1,len(x)):
        L = L + sqrt((x[i]-x[i-1])**2 + (y[i]-y[i-1])**2)
    return L


# In[35]:


with pybryt.check(pybryt_reference(2, 5)):
    path_length([-100, 200, -561, 231], [11, 1.1, 2.9, 165.4])


# In[36]:


ok.grade('exercise-2_5')


# ## Exercise 2.6: Approximate $\pi$
# 
# As you know, the circumference of a circle is $2 \pi r$ where $r$ is the circle's radius.  $\pi$ is therefore the circumference of a circle with $r= \frac{1}{2}$. We can approximate this circumference by a many-sided polygon through points on the circle. The sum of the lengths of the sides of the polygon will approximate the circumference.
# 
# Firstly compute $n+1$ points around a circle according to the formulae:
# 
# $ x_i = \frac{1}{2} \cos(\frac{2 \pi i}{n}),   y_i = \frac{1}{2} \sin(\frac{2 \pi i}{n}),   i = 0 \cdots n$
# 
# Then use your `path_length` function from the previous question to approximate $\pi$.  Name your function for estimating $\pi$ `approx_pi` for testing purposes.

# In[37]:


# Uncomment and complete this code - keep the names the same for testing purposes.
from math import sin, cos
def approx_pi(n):
    x=[]
    y=[]
    for i in range(n+1):
        x.append(1/2*cos(2*pi*i/n))
        y.append(1/2*sin(2*pi*i/n))
    return path_length(x,y)


# In[38]:


with pybryt.check(pybryt_reference(2, 6)):
    approx_pi(100)


# In[39]:


ok.grade('exercise-2_6')


# ## Exercise 2.7: Make a list of prime numbers
# 
# Define a function called `prime_list` that lists all the prime numbers up to a given $n$. 
# 
# **Hint**: Google the Sieve of Eratosthenes.

# In[40]:


# Uncomment and complete this code - keep the names the same for testing purposes.

def prime_list(n):
#    IsPrime = [True] * (n + 1)
#    for i in range(2, int(n ** 0.5) + 1):
#        if IsPrime[i]:
#            for j in range(i * i, n + 1, i):
#                IsPrime[j] = False
#    return [x for x in range(2, n + 1) if IsPrime[x]]


# In[41]:


with pybryt.check(pybryt_reference(2, 7)):
    prime_list(100)


# In[42]:


ok.grade('exercise-2_7')


# ## Vectors and arrays
# 
# You have known **vectors** since high school mathematics, e.g. point $(x, y)$ in the plane, point $(x, y, z)$ in space. In general, we can describe a vector $v$ as an $n$-tuple of numbers: $v=(v_0, \ldots, v_{n-1})$. One way to store vectors in Python is by using *lists*: $v_i$ is stored as `v[i]`.

# **Arrays** are a generalisation of vectors where we can have multiple indices: $A_{i, j}$, $A_{i, j, k}$. In Python, this is represented as a nested list, accessed as `A[i][j]`, `A[i][j][k]`.
# 
# **Example**: Matrix, a table of numbers with one index for the row and one for the column
# $$
# \left\lbrack\begin{array}{cccc}
# 0 & 12 & -1 & 5q\cr
# 11 & 5 & 5 & -2
# \end{array}\right\rbrack
# \hspace{1cm}
# A =
# \left\lbrack\begin{array}{ccc}
# A_{0,0} & \cdots &  A_{0,n-1}\cr
# \vdots & \ddots &  \vdots\cr
# A_{m-1,0} & \cdots & A_{m-1,n-1}
# \end{array}\right\rbrack
# $$
# The number of indices in an array is the *number of dimensions*. Using these terms, a vector can be described as a one-dimensional array or dimension-1 array.

# In practice, we use [Numerical Python (*NumPy*)](http://www.numpy.org/) arrays instead of lists to represent mathematical arrays because it is **much** faster for large arrays.
# 
# Let us consider an example where we store $(x,y)$ points along a curve in Python lists and numpy arrays:

# In[43]:


# Sample function
def f(x):
    return x**3


# Generate n points in [0, 1]
n = 5
dx = 1/(n-1)  # x spacing

X = [i*dx for i in range(n)]  # Python list
Y = [f(x) for x in X]

# Turn these Python lists into Numerical Python (NumPy) arrays:
import numpy as np

x2 = np.array(X)
y2 = np.array(Y)


# Instead of first making lists with $x$ and $y = f (x)$ data, and then turning lists into arrays, we can make NumPy arrays
# directly:

# In[46]:


n = 5                        # number of points
x2 = np.linspace(0, 1, n)    # generates n points between 0 and 1
y2 = np.zeros(n)             # n zeros (float data type by default)
for i in range(n):
    y2[i] = f(x2[i])


# List comprehensions create lists, not arrays, but we can do:

# In[47]:


y2 = np.array([f(xi) for xi in x2])  # list -> array


# ### When and where to use NumPy arrays
# 
# * Python lists can hold any sequence of any Python objects. However, NumPy arrays can only hold objects of the same type.
# * Arrays are most efficient when the elements are basic number types (*float*, *int*, *complex*).
# * In that case, arrays are stored efficiently in the computer's memory, and we can compute very efficiently with the array elements.
# * We can compute mathematical operations on whole arrays without loops in Python. For example,

# In[49]:


x = np.linspace(0, 2, 10001)
y = np.zeros(10001)
for i in range(len(x)):
    y[i] = math.sin(x[i])


# can be coded as

# In[ ]:


y = np.sin(x)


# In the latter case, the loop over all elements is now performed in a very efficient C-function. Instead of using Python `for`-loops, operations on whole arrays are called vectorisation, and they are a very **convenient**, **efficient**, and therefore an **important** programming technique to master.

# Let us consider a simple vectorisation example: a loop to compute $x$ coordinates (`x2`) and $y=f(x)$ coordinates (`y2`) along a function curve:

# In[ ]:


x2 = np.linspace(0, 1, n)
y2 = np.zeros(n)
for i in range(n):
    y2[i] = f(x2[i])


# This computation can be replaced by:

# In[ ]:


x2 = np.linspace(0, 1, n)
y2 = f(x2)


# The advantage of this approach is:
# 
# * There is no need to allocate space for `y2` (via the NumPy *zeros* function).
# * There is no need for a loop.
# * It is *much faster*.

# ## How vectorised functions work
# Consider the function

# In[ ]:


def f(x):
    return x**3


# $f(x)$ is intended for a number $x$, i.e. a *scalar*. So, what happens when we call `f(x2)`, where `x2` is a NumPy array? **The function evaluates $x^3$ for an array $x$**. NumPy supports arithmetic operations on arrays, which correspond to the equivalent operations on each element. For example,

# In[ ]:


r1 = x**3                   # x[i]**3 for all i
r2 = np.cos(x)              # cos(x[i]) for all i
r3 = x**3 + x*np.cos(x)     # x[i]**3 + x[i]*cos(x[i]) for all i
r4 = x/3*np.exp(-x*0.5)     # x[i]/3*exp(-x[i]*0.5) for all i


# In each of these cases, a highly optimised C-function is actually called to evaluate the expression. In this example, the *cos* function called for an *array* is imported from *numpy* rather than from the *math* module which only acts on scalars.
# 
# Notes:
# 
# * Functions that can operate on arrays are called **vectorised functions**.
# * Vectorisation is the process of turning a non-vectorised expression/algorithm into a vectorised expression/algorithm.
# * Mathematical functions in Python automatically work for both scalar and array (vector) arguments, i.e. no vectorisation is needed by the programmer.

# ### Watch out for references vs. copies of arrays!
# Consider this code:

# In[50]:


a = x
a[-1] = 42
print(x[-1])


# Notice what happened here - we changed a value in `a`, but the corresponding value in `x` was also changed! This is because `a` refers to the same array as `x`. If we want a separate copy of `x`, then we have to make an explicit copy:

# In[ ]:


a = x.copy()


# ## Exercise 2.8: Fill lists and arrays with function values
# 
# A function with many applications in science is defined as:
# 
# $$h(x) = \frac{1}{\sqrt{2\pi}}\text{e}^{-\frac{1}{2}x^2}$$
# 
# * Implement the above formula as a Python function. Call the function `h` and it should take just one argument, `x`.
# * Create a NumPy array (call it `x`) that has 9 uniformly spaced points in $[−4, 4]$.
# * Create a second NumPy array (call it `y`) with the function `h(x)`.

# In[65]:


# Uncomment and complete this code - keep the names the same for testing purposes.
def h(x):
    x = np.linspace(-4,4,9)
    y = (1/sqrt(2*pi) * np.exp(-1/2*x**2))
    return y
#print(h(5))


# In[66]:


with pybryt.check(pybryt_reference(2, 8)):
    h(5), x, y


# In[64]:


ok.grade('exercise-2_8')


# ## Generalised array indexing
# 
# We can select a slice of an array using `a[start:stop:inc]`, where the slice `start:stop:inc` implies a set of indices starting from `start`, up to `stop` in increments `inc`. Any integer list or array can be used to indicate a set of indices:

# In[67]:


a = np.linspace(1, 8, 8)
print(a)


# In[68]:


a[[1, 6, 7]] = 10  # i.e. set the elements with indicies 1, 6, and 7 in the array to 10.
print(a)


# In[70]:


a[range(2, 8, 3)] = -2   # same as a[2:8:3] = -2
print(a)


# Even boolean expressions can be used to select part of an array(!)

# In[71]:


print(a[a < 0])  # pick out all negative elements


# In[72]:


a[a < 0] = a.max()  # if a[i]<0, set a[i]=10
print(a)


# ## Exercise 2.9: Explore array slicing
# 
# * Create a NumPy array called `w` with 31 uniformly spaced values ranging from 0 to 3.
# * Using array slicing, create a NumPy array called `wbits` that starts from the $4^{th}$ element of `w`, excludes the final element of `w` and selects every $3^{rd}$ element.

# In[82]:


# Uncomment and complete this code - keep the names the same for testing purposes.

w = np.linspace(0,3,31)
wbits = w[range(0,30,3)]
print(w,wbits)


# In[83]:


with pybryt.check(pybryt_reference(2, 9)):
    w, wbits


# In[84]:


ok.grade('exercise-2_9')


# ## 2D arrays
# When we have a table of numbers,
# 
# $$
# \left\lbrack\begin{array}{cccc}
# 0 & 12 & -1 & 5\cr
# -1 & -1 & -1 & 0\cr
# 11 & 5 & 5 & -2
# \end{array}\right\rbrack
# $$
# 
# (i.e. a *matrix*) it is natural to use a two-dimensional array $A_{i, j}$ with one index for the rows and one for the columns:
# 
# $$
# A = 
# \left\lbrack\begin{array}{ccc}
# A_{0,0} & \cdots &  A_{0,n-1}\cr
# \vdots & \ddots &  \vdots\cr
# A_{m-1,0} & \cdots & A_{m-1,n-1}
# \end{array}\right\rbrack
# $$
# 
# Let us recreate this array using NumPy:

# In[85]:


A = np.zeros((3, 4))

A[0, 0] = 0
A[1, 0] = -1
A[2, 0] = 11

A[0, 1] = 12
A[1, 1] = -1
A[2, 1] = 5

A[0, 2] = -1
A[1, 2] = -1
A[2, 2] = 5

# we can also use the same syntax that we used for nested lists

A[0][3] = 5
A[1][3] = 0
A[2][3] = -2

print(A)


# Next, let us convert a nested list from a previous example into a 2D array:

# In[86]:


Cdegrees = range(0, 101, 10)
Fdegrees = [9/5*C + 32 for C in Cdegrees]
table = [[C, F] for C, F in zip(Cdegrees, Fdegrees)]
print(table)


# In[87]:


# Convert this nested list into a NumPy array:
table2 = np.array(table)
print(table2)


# To see the number of elements in each dimension:

# In[88]:


print(table2.shape)


# i.e. our table has 11 rows and 2 columns.
# 
# Let us write a loop over all array elements of A:

# In[95]:


for i in range(table2.shape[0]):
    for j in range(table2.shape[1]):
        print('table2[%d, %d] = %g' % (i, j, table2[i, j]))


# Alternatively:

# In[90]:


for index_tuple, value in np.ndenumerate(table2):
    print('index %s has value %g' % (index_tuple, value))


# We can also extract slices from multi-dimensional arrays as before. For example, extract the second column:

# In[91]:


print(table2[:, 1])  # 2nd column (index 1)


# Play with this more complicated example:

# In[93]:


t = np.linspace(1, 30, 30).reshape(5, 6)
print(t)


# In[94]:


print(t[1:-1:2, 2:])


# ## Exercise 2.10: Matrix-vector multiplication
# A matrix $\mathbf{A}$ and a vector $\mathbf{b}$, represented in Python as a 2D array and a 1D array, respectively, are given by:
# 
# $$
# \mathbf{A} = \left\lbrack\begin{array}{ccc}
# 0 & 12 & -1\cr
# -1 & -1 & -1\cr
# 11 & 5 & 5
# \end{array}\right\rbrack
# $$
# 
# $$
# \mathbf{b} = \left\lbrack\begin{array}{c}
# -2\cr
# 1\cr
# 7
# \end{array}\right\rbrack
# $$
# 
# Multiplying a matrix by a vector results in another vector $\mathbf{c}$, whose components are defined by the general rule:
# 
# $$\mathbf{c}_i = \sum_j\mathbf{A}_{i, j}\mathbf{b}_j$$
# 
# * Define $\mathbf{A}$ and $\mathbf{b}$ as NumPy arrays
# * Write a function called `multiply` that takes two arguments, a matrix and a vector in the form of NumPy arrays, and returns a NumPy array containing their product.
# * Call this function on $\mathbf{A}$ and $\mathbf{b}$, and store the result in a variable $c$.

# In[103]:


# Uncomment and complete this code - keep the names the same for testing purposes.

def multiply(A, b):
    x = np.zeros(b.shape[0])
    for i in range(A.shape[0]):
        for j in range(b.shape[0]):
            x[i] = x[i] + A[i, j]*b[j]
    return x

A = np.array([[0, 12, -1], [-1, -1, -1], [11, 5, 5]])
b = np.array([-2, 1, 7])
c = multiply(A, b)
print(c)


# In[104]:


with pybryt.check(pybryt_reference(2, 10)):
    A, b, c, multiply(A, b)


# In[105]:


ok.grade('exercise-2_10')


# ## Exercise 2.11: Vectorised function
# 
# Let $A_{33}$ be the two-dimensional array
# 
# $$
# \mathbf{A_{33}} = \left\lbrack\begin{array}{ccc}
# 0 & 12 & -1\cr
# -1 & -1 & -1\cr
# 11 & 5 & 5
# \end{array}\right\rbrack
# $$
# 
# Implement and apply the function
# 
# $$f(x) = x^3 + xe^x + 1$$
# 
# to each element in $A_{33}$. Then calculate the result of the array expression ${A_{33}}^3 + A_{33}e^{A_{33}} + 1$, and demonstrate that the end result of the two methods are the same.

# In[127]:


# Uncomment and complete this code - keep the names the same for testing purposes.

A33 = np.array([[0,12,-1],[-1,-1,-1],[11,5,5]])


def f_cubic(A):
    B = np.zeros([A.shape[0], A.shape[1]])
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            B[i,j] = A[i,j]**3 + A[i,j]*np.exp(A[i,j]) + 1
    return B
f_cubic(A33)
A33_3 = A33**3 + A33*np.exp(A33) + 1


# In[128]:


with pybryt.check(pybryt_reference(2, 11)):
    f_cubic(np.array([[1, 2, -6], [2, 2, -5]])), A33


# In[129]:


ok.grade('exercise-2_11')


# ## Exercise 2.12: Matrix-matrix multiplication
# 
# The general rule for multiplying an $n \times m$ matrix $\mathbf{A}$ by a $m \times p$ matrix $\mathbf{B}$ results in a $n \times p$ matrix $\mathbf{C}$, whose components are defined by the general rule
# 
# $$\mathbf{C}_{i,j} = \sum^m_{k=1}\mathbf{A}_{i,k}\mathbf{B}_{k,j}$$
# 
# Again let $\mathbf{A}$ be the two-dimensional array
# 
# $$
# \mathbf{A} = \left\lbrack\begin{array}{ccc}
# 0 & 12 & -1\cr
# -1 & -1 & -1\cr
# 11 & 5 & 5
# \end{array}\right\rbrack
# $$
# 
# and let $\mathbf{B}$ be the two-dimensional array
# 
# $$
# \mathbf{B} = \left\lbrack\begin{array}{ccc}
# -2 & 1 & 7\cr
# 3 & 0 & 6\cr
# 2 & 3 & 5
# \end{array}\right\rbrack.
# $$
# 
# Define `A` and `B` as NumPy arrays, and write a function `f_mult` which multiplies them together using the above rule. Save the result of multiplication `f_mult(A, B)` in variable `C`.

# In[143]:


# Uncomment and complete this code - keep the names the same for testing purposes.

def f_mult(A, B):
    if A.shape[1] != B.shape[0]:
        raise RuntimeError('Matrix A should have the same number of columns as B has rows.')
    res = np.zeros([A.shape[0], B.shape[1]])
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            for k in range(B.shape[0]):
                res[i, j] = res[i, j] + A[i, k]*B[k ,j]
    return res

A = np.array([[0, 12, -1], [-1, -1, -1], [11, 5, 5]])
B = np.array([[-2, 1, 7], [3, 0, 6], [2, 3, 5]])
C = f_mult(A, B)
print(C)


# In[144]:


with pybryt.check(pybryt_reference(2, 12)):
    f_mult(np.array([[5, 6], [11, 17]]), np.array([[91, -6], [21, 14]])), A, B


# In[145]:


ok.grade('exercise-2_12')


# ## Exercise 2.13: 2D array slicing
# 
# 
# * Create a 1D NumPy array called `odd` with all of the odd numbers from 1 to 55
# * Create a 2D NumPy array called `odd_sq` with all of the odd numbers from 1 to 55 in a matrix with 4 rows and 7 columns
# * Using array slicing, create a 2D NumPy array called, `odd_bits`, that starts from the $2^{nd}$ column of `odd_sq` and selects every other column, of only the $2^{nd}$ and $3^{rd}$ rows of `odd_sq`.

# In[153]:


# Uncomment and complete this code - keep the names the same for testing purposes.

odd = np.linspace(1, 55, 28)
print(odd)
odd_sq = np.linspace(1, 55, 28).reshape(4, 7)
print(odd_sq)
odd_bits = odd_sq[1:3, 1:7:2]
print(odd_bits)


# In[154]:


with pybryt.check(pybryt_reference(2, 13)):
    odd, odd_sq, odd_bits


# In[155]:


ok.grade('exercise-2_13')


# In[156]:


ok.score()


# In[ ]:





# In[ ]:




