"""The very first module in a more structured version of the project.
"""


#%%
# Moving code from main.py

# Hello world: the print() built-in function and the + operator.

# print('George Harrison')
# print('George Harrison', 'was born in Liverpool, England, in', 1943)
# print('George Harrison', 'was born in Liverpool, England, in ' + '1943')
# print('George Harrison', 'was born in Liverpool, England, in ' + str(1943) + '.')

#%%
# Printing with ' ' and printing without '\n'

# print('George Harrison was born in: ')
# print(1942)
# print('George Harrison was born in: ', end='')
# print(1942)

#%%
# Printing with classical formatting (%)

# print('George Harrison was born in %s in %d.' % ('Liverpool', 1942))

#%%
# Keyboard input

# year = int(input('George Harrison was born in: '))
# print(year)
# print('The type of "year" is:', type(year))

#%%
# break and continue

# for i in range(5):
#     if i == 3:
#         # break
#         continue
#     print(i)


#%%
# A simple function and function call

def year_of_birth():
    """Get George's year of birth
    """
    year = int(input('George Harrison was born in: '))
    print(year)
    print(id(year))
    return year


#%%
# Printing docstrings

# print(__doc__)
# # print(__file__)
# print(year_of_birth.__doc__)

#%%
# Printing a list using enumerate()

# songs = ['Something', 'While My Guitar Gently Weeps', "I Need You"]
# for i, song in enumerate(songs):
#     print(str(i+1) + ':', song)

#%%
# Importing from Standard Library

# Date format strings
# https://docs.python.org/3/library/datetime.html?highlight=date%20format%20strings#strftime-and-strptime-format-codes

# date_format = '%b %d, %Y'
# from datetime import date
# birthday = date(1943, 2, 25)
# print(birthday.strftime(date_format))

#%%
# Testing print(__file__)

# print(__file__)

#%%
# Taking care of the module __name__

if __name__ == "__main__":
    print()
    print()
    print()
    print()
    print()
    print('inception.py')
    print(__name__)
    print()

    print(year_of_birth.__doc__)

