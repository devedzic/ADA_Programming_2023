"""Demonstrates tuples.
"""


#%%
def demonstrate_tuples():
    """Creating and using tuples.
    - create and print empty tuple, 1-tuple, 2-tuple, mixed-type n-tuple
    - accessing elements of a tuple using []
    - demonstrate that tuples are immutable
    """

    empty_tuple = ()                            # alternatively: empty_tuple = tuple()
    print(empty_tuple)
    print(type(empty_tuple))
    if empty_tuple:
        print(True)
    else:
        print(False)
    print()

    one_tuple = 3,
    print(one_tuple)
    print()

    two_tuple = (2, 3)
    print(two_tuple)
    print()

    mixed_tuple = (2, True, '444')
    print(mixed_tuple)
    print(mixed_tuple[2])
    for t in mixed_tuple:
        print(t)
    print()

    # mixed_tuple[0] = 22                       # error! tuples are immutable!


#%%
# Test demonstrate_tuples()
demonstrate_tuples()


#%%
def demonstrate_packing():
    """Packing and unpacking tuples.
    """

    t = 1, 2, 3
    one, two, three = t
    print(t, one, two, three)


#%%
# Test demonstrate_packing()
demonstrate_packing()


#%%
def demonstrate_zip():
    """Using the built-in zip() function with tuples and multi-counter for-loop.
    - demonstrate zip object
    - demonstrate converting a zip object to a list object
    - demonstrate that a zip object is an iterator (must be re-initialized after looping)
    """

    members = ('John Lennon', 'Paul McCartney', 'George Harrison', 'Ringo Starr')
    birth_years = (1940, 1942, 1943, 1940)
    birth_places = ('Liverpool', 'Liverpool', 'Liverpool', 'Liverpool', )

    the_beatles = zip(members, birth_years, birth_places)
    print(the_beatles)
    print(list(the_beatles))                                    # exhausts the iterator

    the_beatles = zip(members, birth_years, birth_places)       # re-initiate the iterator, it is exhausted now
    for m, y, p in the_beatles:
        print(m, y, p)


#%%
# Test demonstrate_zip
demonstrate_zip()

