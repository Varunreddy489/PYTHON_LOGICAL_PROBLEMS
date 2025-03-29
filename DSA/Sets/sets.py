#  create a set

def create_set(list):
    my_set =set()

    for i in list:
        my_set.add(i)

    return my_set

list=[1,2,4,5,2,2]
print(create_set(list))

#  iteration over sets.

def iterate_set(set):

    for i in set:
        print(i)


set = {1, 2, 3, 4, 5, 3}
iterate_set(set)

#  add member(s) in a set.

def add_item_set(list):

    my_set=set()

    for i in list:
        my_set.add(i)

    return my_set

list=[1,2,3,4,5,6,6,6]
print(add_item_set(list))


#  remove item(s) from set

def remove_items(set,ele):

    set.discard(ele)

    return set

set={1, 2, 3, 4, 5}
ele=4

print(remove_items(set,ele))

#  remove an item from a set if it is present in the set.

def remove_present_item(set,ele):

    set.discard(ele)

    return set

set={1, 2, 3, 4, 5}
ele=4

print(remove_present_item(set,ele))

#  create an intersection of sets.

def intersection_sets(set1, set2):

    if set2.issubset(set1):
        return set2


set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}

print(intersection_sets(set1, set2))

#  create a union of sets.


def set_union(set1, set2):
    return set1.union(set2)


set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3, 6, 7}

result = set_union(set1, set2)
print(result)


#  create set difference.

def set_diff(set1, set2):

    set3 = set1.difference(set2)

    return set3


set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3, 6, 7}

print(set_diff(set1, set2))

#   create a symmetric difference


def symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)


set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3, 6, 7}

result = symmetric_difference(set1, set2)
print(result)

#  program to clear a set


def clear_set(set1):
    z = set1.clear()
    return z


set1 = {1, 2, 3, 4, 5}

print(clear_set(set1))


#  program to use of frozensets.


def frozenset_union(frozenset1, frozenset2):

    return frozenset1.union(frozenset2)


set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3, 6, 7}

frozenset1 = frozenset(set1)
frozenset2 = frozenset(set2)

result = frozenset_union(frozenset1, frozenset2)
print(result)

#   find maximum and the minimum value in a set


def min_max_set(set1):

    return (min(set1), max(set1))


set1 = {1, 2, 3, 4, 5}

print(min_max_set(set1))
