# create a tuple.


def create(list):

    my_tuple = tuple(list)
    return my_tuple


list = [1, 2, 3, 4, 5]
print(create(list))

# create a tuple with different data types.


def mixed_tuple(list):

    my_tuple = tuple(list)
    return my_tuple


list = [1, 2.1, "3", 4.5, 5342432]
print(mixed_tuple(list))

# unpack a tuple in several variables.


def unpack_tuple(my_tuple):
    a, b, c = my_tuple
    return a, b, c


my_tuple = ("a", "b", "c")

result = unpack_tuple(my_tuple)

print("Unpacked Values:", result)

#  create the copy of a tuple


def copy_tuple(tple):
    return tple[:]


tple = (1, 2, 3)
print(copy_tuple(tple))


#  find the repeated items of a tuple.


def repeated_ele(tuple):

    my_set = set()

    for i in tuple:

        if tuple.count(i) > 1:
            my_set.add(i)

    return my_set


tuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(repeated_ele(tuple))

#  check whether an element exists within a tuple.


def is_element(tuple, ele):

    for i in range(len(tuple)):

        if ele == tuple[i]:
            return True

    return False


tuple = (1, 2, 34, 5, 6)
ele = 2

print(is_element(tuple, ele))

#  convert a list to a tuple


# def list_to_tuple(lst):
#     return tuple(lst)


# lst = [1, 2, 3, 4]
# print(list_to_tuple(lst))

# slice a tuple.


def slice_tuple(tple, index):
    return tple[index:]


tple = (1, 2, 3, 4, 5, 6)
index = 2

print(slice_tuple(tple, index))


# remove an item from a tuple.


def remove_ele(tple, ele):

    my_list = list(tple)

    my_list.remove(ele)

    return my_list


tple = (1, 2, 3, 4, 5)
ele = 2

print(remove_ele(tple, ele))

# reverse a tuple.


def reverse_tuple(tple):

    mylist = list(tple)

    mylist.reverse()

    my_tuple = tuple(mylist)

    return my_tuple


tple = (1, 2, 3, 4, 5)

print(reverse_tuple(tple))
