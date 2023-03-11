"""Demonstrates peculiarities of if, for, while and other statements.
"""


#%%
def demonstrate_branching():
    """Details and peculiarities of if statements.
    - is compares id()'s, == compares contents
    - id()'s are the same for equal strings and numbers, but not for lists, user class instances,...
    - the condition of an if-statement need not necessarily be a boolean
    - there can be more than one elif after if (no switch statement, use multiple elif instead)
    """

    a = 1
    b = 1
    str_a = 'George Harrison'
    str_b = 'George Harrison'
    list_a = [1, 2]
    list_b = [1, 2]

    if a == b:
        print('a == b')
    else:
        print('a != b')
    if a is b:
        print('a is b')
    else:
        print('a is not b')
    print()

    if str_a == str_b:
        print('str_a == str_b')
    else:
        print('str_a != str_b')
    if str_a is str_b:
        print('str_a is str_b')
    else:
        print('str_a is not str_b')
    print()

    if list_a == list_b:
        print('list_a == list_b')
    else:
        print('list_a != list_b')
    if list_a is list_b:
        print('list_a is list_b')
    else:
        print('list_a is not list_b')
    print()

    if 34:
        print('True')
    else:
        print(False)

    while True:
        i = int(input('Enter an int between 1 and 4: '))
        if not (1 <= i <= 4):
            continue
        if i == 1:
            print('You entered 1')
        elif i == 2:
            print('You entered 2')
        elif i == 3:
            print('You entered 3')
        elif i == 4:
            print('You entered 4')
        else:
            pass
        break


#%%
# Test demonstrate_branching()
demonstrate_branching()

#%%


def demonstrate_loops():
    """Different kinds of loops. Also break and continue.
    - it is not necessary to iterate through all elements of an iterable
    - step in range()
    - unimportant counter (_)
    - break and continue
    - while loop
    """

    from random import randint, seed

    seed(12)
    l = []
    for i in range(100):
        l.append(randint(1, 10))
    print(l)
    l = []
    for _ in range(0, 100, 10):
        l.append(randint(1, 10))
    print(l)


#%%
# Test demonstrate_loops()
demonstrate_loops()
