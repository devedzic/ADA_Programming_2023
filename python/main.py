"""The very first Python script - main.py.
"""


#%%
# Hello world: the print() built-in function and the + operator.

print('George Harrison')
print('George Harrison', 'was born in Liverpool, England, in', 1943)
print('George Harrison', 'was born in Liverpool, England, in ' + '1943')
print('George Harrison', 'was born in Liverpool, England, in ' + str(1943) + '.')

#%%
# The input() built-in function

# # print('George Harrison was born in: ')
# print('George Harrison was born in: ', end='')
# year = input()
# print(year)
# print()
#
# print(type(year))
# year = int(year)
# print(type(year))
# print()

year = int(input('George Harrison was born in: '))
print(year)
print('The type of "year" is:', type(year))


#%%
# A simple function and function call

def year_of_birth():
    year = int(input('George Harrison was born in: '))
    print(year)
    print(id(year))
    return year


year1 = year_of_birth()
print(year1)
print(id(year1))

#%%
# A simple loop and the range() built-in function

# for i in range(5):
#     print(i)

# for i in range(12, 19, 2):
#     print(i)

i = 0
while i < 5:
    print(i)
    i += 1

#%%
# A simple list, accessing list elements, printing lists

george = ['George', 'Harrison', 1943, True]
print(george)
print(george[0])
print()

songs = ['Something', 'While My Guitar Gently Weeps', "I Need You"]
print('; '.join(songs))

#%%
# Looping through list elements - for and enumerate()

for i, song in enumerate(songs):
    print(str(i+1) + ':', song)

#%%
# Global variables: __name__, __file__, __doc__,...

print(__name__)
print(__doc__)
# print(__file__)
print(globals())

#%%
# Importing from another script

from python.inception import year_of_birth

print()
print()
print()
print()
print(year_of_birth())

