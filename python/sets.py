"""Demonstrates sets.
"""


#%%
def demonstrate_sets():
    """Creating and using sets.
    - create a set and make an attempt to duplicate items
    - demonstrate some typical set operators:
        & (intersection)
        | (union)
        - (difference)
        ^ (disjoint)
    """

    george = set()
    # if george:
    #     print(True)
    # else:
    #     print(False)
    print(True) if george else print(False)
    print()

    george.add('George')
    george.update({'Liverpool', 1943})
    print(george)
    print()

    george.update({'Ringo', 'Liverpool'})
    print(george)
    print()

    george = {'George', 'Liverpool', 1943}
    ringo = {'Ringo', 'Liverpool', 1940}

    print('Intersection:', george & ringo)
    print('Union:', george | ringo)
    print('Difference:', george - ringo)
    print('Disjoint:', george ^ ringo)
    print()

    the_beatles = 'John', 'Paul', 'George', 'Ringo'
    print(the_beatles)
    print(set(the_beatles))


#%%
# Test demonstrate_sets()
demonstrate_sets()


