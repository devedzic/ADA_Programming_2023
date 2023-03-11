"""Demonstrates how operators and expressions work in Python.
"""

from settings import *
# print(PROJECT_DIR)

#%%
def demonstrate_arithmetic_operators():
    """Working with arithmetic operators.
    Arithmetic operators in Python are pretty much the same as in other programming languages.
    The integer division operator: //
    """

    print(3 / 28 + 45 // 23 - (-35476 % 345))
    print(round(3 / 28 + 45 // 23 - (-35476 % 345), 2))


#%%
# Test demonstrate_arithmetic_operators()
demonstrate_arithmetic_operators()

#%%


def demonstrate_relational_operators():
    """Working with relational operators.
    - simple comparisons
    - comparing dates (== vs. is)
    - comparing dates (>, <, etc. with dates)
    - None in comparisons, type(None)
    """

    print(2 > 3)
    print()

    from datetime import date
    d1 = date(1943, 2, 25)
    d2 = date.today()
    print(f'd1: {d1}, d2: {d2}\nd2 > d1:', d2 > d1)
    d3 = date.today()
    print(f'd2: {d2}, d3: {d3}\nd3 == d2:', d2 == d3)
    print(f'd2: {d2}, d3: {d3}\nd3 is d2:', d2 is d3)
    a = 12343
    b = 12345
    print(id(a), id(b))
    print(a is b)
    print()

    print(type(None))
    print(d2 == None)
    print()


#%%
# Test demonstrate_relational_operators()
demonstrate_relational_operators()

#%%


def demonstrate_logical_operators():
    """Working with logical operators.
    - logical operations with True, False and None
    - logical operations with dates
        - make sure to read this: https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not !!!
          (or just this: https://stackoverflow.com/questions/44612144/logical-operators-in-python)
    - logical operations with None (incl. None and int, None and date, etc.)
    - None and date vs. None > date
    """

    print((10 > 3) and (4 < 2))
    print((10 > 3) and True)
    print((10 > 3) and 4)
    print((10 > 3) and None)
    print()

    print(10 or False)
    print(None or None)
    print(None or 4)
    print([] or 0)
    print([] or [])
    print()

    from datetime import date
    d1 = date(1943, 2, 25, )
    d2 = date.today()
    print(d1 and d2)
    print(not d1)
    print()

    print(None and d1)
    print(None or d1)
    print(d1 and None)
    # print(d1 > None)              # compile error


#%%
# Test demonstrate_logical_operators()
demonstrate_logical_operators()

