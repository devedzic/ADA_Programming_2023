"""Demonstrates working with lists.
"""


#%%
def demonstrate_lists():
    """Using just the simplest operations with lists.
    - create a non-empty list with different kinds of elements
    - accessing/slicing a list
    - comparing 2 lists (== vs. is)
    - concatenating 2 lists (the + operator)
    - looping through a list
    """

    george = ['George Harrison', 1943, 'Liverpool', True]
    print(george)
    print()

    print(george[2])
    print()

    print(george[1:-1])
    print()

    harrison = ['George Harrison', 1943, 'Liverpool', True]
    print('george == harrison:', george == harrison)
    print('george is harrison:', george is harrison)
    print()

    print(george + ['The Beatles'])
    print()

    for element in george:
        print(element)
    print()

    for element in george[:-2]:
        print(element)
    print()


#%%
# Test demonstrate_lists()
demonstrate_lists()

#%%
def demonstrate_list_methods():
    """Using
    append()
    insert()
    remove()
    pop()
    extend()
    count()
    index()
    reverse()
    len()
    ...
    Also, "in" and "not in" operators can be used to search lists
    for the occurrence of a given element.
    """

    harrison = ['George Harrison', 1943, 'Liverpool', True]
    the_beatles = ['The Beatles', 'lead guitar']

    print(harrison)
    print(harrison.append('Fab Four'))
    print(harrison)
    print()

    print(harrison)
    print(harrison.pop())
    print(harrison)
    print()

    print(harrison)
    print(harrison.extend(the_beatles))
    print(harrison)
    print()

    print(harrison)
    print(harrison.pop(-3))
    print(harrison)
    print()

    print(harrison)
    print(harrison.remove(1943))
    print(harrison)
    print()

    print(harrison)
    print(harrison.pop(1))
    print(harrison)
    print()

    print(harrison)
    print(harrison.count('The Beatles'))
    print(harrison)
    print()

    print(harrison)
    print(harrison.index('The Beatles'))
    print(harrison)
    print()

    print(harrison)
    print(harrison.reverse())
    print(harrison)
    print()

    print(harrison)
    print(len(harrison))
    print()

    print(harrison)
    print('The Beatles' in harrison)
    print('Liverpool' not in harrison)
    print()


#%%
# Test demonstrate_list_methods()
demonstrate_list_methods()

#%%


def demonstrate_arrays():
    """Using array.array() to build list-based numeric arrays.
    Demonstrating that lists and arrays are different types.
    """

    from array import array
    b = [2, 5, 8, 2, 3, 4]
    a = array('i', b)

    print(type(b))
    print(type(a))
    print()

    for element in a:
        print(element)
    print()


#%%
# Test demonstrate_arrays()
demonstrate_arrays()

#%%


def populate_empty_list():
    """Creating an empty list and populating it with random values
    using random.seed() and random.randint()
    """

    from random import randint, seed
    seed(12)
    l = []
    for i in range(10):
        l.append(randint(1, 10))
    print(l)


#%%
# Test populate_empty_list()
populate_empty_list()

#%%


def duplicate_list():
    """Duplicating lists (carefully :)).
    Don't use l2 = l1, but either of the following:
    - l2 = l1.copy()
    - l2 = l1 + []
    - l2 = l1[:]
    """

    george = ['George Harrison', 1943, 'Liverpool', True]

    harrison = george
    print(harrison == george)
    print(harrison is george)
    print()

    harrison = george.copy()
    print(harrison == george)
    print(harrison is george)
    print()

    harrison = george + []
    print(harrison == george)
    print(harrison is george)
    print()

    harrison = george[:]
    print(harrison == george)
    print(harrison is george)
    print()


#%%
# Test duplicate_list()
duplicate_list()

#%%


def demonstrate_list_comprehension():
    """Showing examples of list comprehension.
    - list comprehension over a list of strings
    - list comprehension with enumerate(), to find indices of all occurrences of an element in a list
    Using str() and join() in printing results.
    """

    songs = ["Don't Bother Me", 'If I Needed Someone', 'Think for Yourself', 'Taxman', 'Only a Northern Song']

    # fw = [w.split()[0] for w in songs]
    # fl = [w[0] for w in fw]
    # print(''.join(fl).capitalize())

    all_george = [i for i, name in enumerate(['John', 'Paul', 'George', 'Ringo', 'George']) if name == 'George']
    print(all_george)

    fl = [w.split()[0][0] for w in songs]
    # fl = [w[0] for w in fw]
    print(''.join(fl).capitalize())

    all_o_in_first_song = [i for i, characters in enumerate(songs[0]) if 'o' in characters]
    print(all_o_in_first_song)

    all_o = [i for i, title in enumerate(songs) if 'o' in title]
    print(all_o)
    print('; '.join([str(i) for i in all_o]))


#%%
# Test demonstrate_list_comprehension()
demonstrate_list_comprehension()

