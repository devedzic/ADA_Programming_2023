"""Demonstrates working with strings in Python.
"""

import string

import settings


#%%
def demonstrate_formatting():
    """Demonstrating details of string formatting.
    - using classical formatting
    - \n is the new line char
    - r'...' - raw formatting
    - using \"\"\"...\"\"\" for multi-line formatting
    - string "multiplication"
    - substrings / slicing
    - str() vs. repr() (usually the same, but with whitespace there is a difference)
    """

    year1 = 1943
    year2 = 1958
    city = 'Liverpool, England'
    print('George Harrison was born in %d, in %s.' % (year1, city))
    print()

    print('George Harrison was born in %d, in %s.\nHe joined The Beatles in %d.' % (year1, city, year2))
    print()

    print('C:\nobody')
    print(r'C:\nobody')
    print()

    print("""Oh, well...
    This is a multiline formatting.
    Yeah!""")
    print()

    print('George Harrison     ' * 5)
    print()

    print('George Harrison'[:7])
    print('George Harrison'[:10])
    print('George Harrison'[-8:-7])
    print('George Harrison'[-8:])
    print()

    print('\tGeorge')
    print(repr('\tGeorge'))
    print()


#%%
# Test demonstrate_formatting()
demonstrate_formatting()

#%%


def demonstrate_fancy_formatting():
    """Using "fancy" formatting.
    - format strings like '{0}{1} {2}', '{0}{1} {2}, {3}', etc.
    """

    print('{} was born in {}, in {}.'.format('George Harrison', 'Liverpool', 1943))
    print('{0} was born in {2}, in {1}.'.format('George Harrison', 'Liverpool', 1943))


#%%
# Test demonstrate_fancy_formatting()
demonstrate_fancy_formatting()

#%%


def demonstrate_fancy_formatting_with_f_strings():
    """Using f-strings in formatting.
    - format strings like f'Some text {some var}, more text {another var}...', etc.
    """

    name = 'George Harrison'
    city = 'Liverpool'
    year = 1943
    print(f'{name} was born in {city} in {year}.')


#%%
# Test demonstrate_fancy_formatting_with_f_strings()
demonstrate_fancy_formatting_with_f_strings()

#%%


def demonstrate_string_operations():
    """Using different string operations.
    - endswith(), split(), center(), in (aka contains()), == (aka equals()), len(), ..., strip() (lstrip(), rstrip())
    """

    george = 'George Harrison'
    print(george.startswith('Geo'))
    print(george.endswith('on'))
    print(george.endswith('Harrisonn'))
    print(george.split())
    print(george.split('r'))
    print(george.center(20, '*'))
    print('Harr' in george)
    print('George Harrison' == george)
    print('George Harrison' is george)
    print(len(george))
    print(george.strip('on'))


#%%
# Test demonstrate_string_operations()
demonstrate_string_operations()
