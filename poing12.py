# import time
# from random import randint
# import asyncio


# def foo(start, stop):
#     for odd in range(start, stop +5):
#         yield odd

# def randn():
#     time.sleep(3)
#     return randint(1,10)

# def bar():
#     odd1 = [odd for odd in foo(5,10)]
#     print(odd1)

# bar()


# # out


# $ ipython -i poing12.py
# Python 3.7.1rc2 (v3.7.1rc2:6c06ef7dc3, Oct 13 2018, 15:44:37) [MSC v.1914 64 bit (AMD64)]
# Type "copyright", "credits" or "license" for more information.

# IPython 5.5.0 -- An enhanced Interactive Python.
# ?         -> Introduction and overview of IPython's features.
# %quickref -> Quick reference.
# help      -> Python's own help system.
# object?   -> Details about 'object', use 'object??' for extra details.
# [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

# In [1]: whos
# Variable   Type        Data/Info
# --------------------------------
# asyncio    module      <module 'asyncio' from 'c<...>b\\asyncio\\__init__.py'>
# bar        function    <function bar at 0x000001E84E198AE8>
# foo        function    <function foo at 0x000001E84E0EEEA0>
# randint    method      <bound method Random.rand<...>t at 0x000001E84C2F3768>>
# randn      function    <function randn at 0x000001E84E043D08>
# time       module      <module 'time' (built-in)>

# In [2]:

# In [2]: randn
# Out[2]: <function __main__.randn>

# In [3]: %time randn()
# Wall time: 3 s
# Out[3]: 9

# In [4]: %time randn()
# Wall time: 3 s
# Out[4]: 9

# In [5]: %time randn()
# Wall time: 3 s
# Out[5]: 9

# In [6]: randn()
# Out[6]: 6

# In [7]: randn()
# Out[7]: 2

# In [8]: randn()
# Out[8]: 1

# In [9]: %time [randn() for _ in range(5)]
# Wall time: 15 s
# Out[9]: [1, 10, 4, 9, 3]
