"""Demonstrates dictionaries.
From: https://qr.ae/TWCAvj:
Python uses dictionaries all over the place:
- the variables and functions in a module - stored in a dictionary  # can be shown using globals()
- the local variables in a function - stored in a dictionary        # can be shown using locals(); see functions.py
- the implementation of a function - a dictionary
- a class is a dictionary
- an instance of a class is another dictionary
- the modules your program has imported - you guessed it - another dictionary
- even Python set objects are implemented as modified dictionaries
To paraphrase Tim Peter's 'Zen of Python': "dictionaries are great - let's do more of them".
Read more at https://qr.ae/TWCAvj.
"""


#%%
def demonstrate_dictionaries():
    """Creating and using dictionaries.
    - create a blank (empty) dictionary
    - create a non-empty dictionary
    - access dictionary values by the corresponding keys (syntax: value = d[key])
    - print a non-empty dictionary
        - print all items using the items() function
        - print one item per line
    - pprint dictionary in one column
    - add/remove items to/from a dictionary
    - update a dictionary with the items from another dictionary or from an iterable of (k, v) pairs using dict.update()
    - using the keys() and values() functions
    """

    d = {}
    print(d)
    print(type(d))
    print()

    george = {'name': 'George Harrison', 11: 'whatever'}
    print(george)
    print(george[11])
    print()

    george['city'] = 'Liverpool'
    print(george)
    del george[11]
    george.pop('city')
    print(george)
    print()

    george = {'name': 'George Harrison', 11: 'whatever'}
    print(george.items())
    print(list(george.items()))
    for k, v in george.items():
        print((k, v))
    print()

    from pprint import pprint
    pprint(george, width=1)
    print()

    george.update({'city': 'Liverpool'})
    print(george)
    george.update([('year', 1943), ('instrument', 'lead guitar')])
    print(george)
    print()

    print(george.keys())
    print(george.values())
    print(list(george.values()))


#%%
# Test demonstrate_dictionaries()
demonstrate_dictionaries()


#%%
def sort_dictionary(d, by):
    """Sorting a dictionary by keys or by values.
    - using zip()
    - using operator.itemgetter()
    - using lambda
    """

    # if (by == 'K') or (by == 'k'):
    #     return dict(sorted(zip(d.keys(), d.values())))
    # elif (by == 'V') or (by == 'v'):
    #     return dict(sorted(zip(d.values(), d.keys())))
    # else:
    #     return None

    # from operator import itemgetter
    # if (by == 'K') or (by == 'k'):
    #     return dict(sorted(d.items(), key=itemgetter(0)))
    # elif (by == 'V') or (by == 'v'):
    #     return dict(sorted(d.items(), key=itemgetter(1)))
    # else:
    #     return None

    if (by == 'K') or (by == 'k'):
        return dict(sorted(d.items(), key=lambda x: x[0]))
    elif (by == 'V') or (by == 'v'):
        return dict(sorted(d.items(), key=lambda x: x[1]))
    else:
        return None


#%%
def demonstrate_dict_sorting():
    """Demonstrate sorting a dictionary.
    """

    from pprint import pprint

    songs = {2: 'Something', 1: 'While My Guitar Gently Weeps', 3: 'If I Needed Someone'}
    george = {'name': 'George Harrison', 'city': 'Liverpool', 'year': str(1943)}

    print(sort_dictionary(george, 'v'))


#%%
# Test demonstrate_dict_sorting()
demonstrate_dict_sorting()
