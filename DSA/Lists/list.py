# *  sum all the items in a list.


def add_list_items(list):

    sum = 0

    for i in list:
        sum += i

    return sum


list = [1, 2, 3, 4, 5, 56]
print(add_list_items(list))

# multiplies all the items in a list.


def multiply_listItems(list):

    mul = 1
    for i in list:
        mul *= i

    return mul


list = [1, 2, 3, 4, 5, 6]
print(multiply_listItems(list))

#  get the smallest number from a list.


def smallest_num(list):

    list.sort()

    return list[0]


list = [9, 9, 9, 1, 2, 3, 4, 5, 6]
print(smallest_num(list))

# count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings


def count_freq_str(list):
    count = 0
    for i in list:
        if len(i) >= 2 and (i[0] == i[len(i) - 1]):
            count += 1

    return count


list = ["abc", "xyz", "aba", "1221"]
print(count_freq_str(list))


# program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.


def sort_tuple_list(list):
    n = len(list)

    for i in range(n):
        for j in range(n - i - 1):
            if list[j][-1] > list[j + 1][-1]:
                list[j], list[j + 1] = list[j + 1], list[j]

    return list


list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

print(sort_tuple_list(list))

#  remove duplicates in a list


def remove_duplicates(list):
    n = len(list)

    i = 0
    while i < n:
        j = i + 1
        while j < n:
            if list[i] == list[j]:
                list.pop(j)
                n -= 1
            else:
                j += 1
        i += 1

    return list


list = [1, 2, 3, 4, 5, 6, 6, 6]
print(remove_duplicates(list))

# clone or copy a list.


def clone_list(list):

    new_list = list.copy()

    return new_list


list = [1, 2, 3, 4, 5, 6, 6, 6]
print(clone_list(list))


# program to find the list of words that are longer than n from a given list of words.


def len_longerThan_size(list, n):

    newList = []

    for i in list:
        if len(i) > n:
            newList.append(i)

    return newList


list = ["abc", "xyz", "aba", "1221"]
n = 3
print(len_longerThan_size(list, n))


# take two lists and return True if they have at least one common member.


def common_ele(list1, list2):

    n = len(list1)
    m = len(list2)

    for i in list1:
        for j in list2:
            if i == j:
                return True

    return False


list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 7, 8, 9]

print(common_ele(list1, list2))


#  print a specified list after removing the 0th, 4th and 5th elements.


def remove_specified_ele(list, index):

    for i in range(len(index)):
        list.remove(i)

    return list


index = [0, 4, 5]
list = ["Red", "Green", "White", "Black", "Pink", "Yellow"]


print(remove_specified_ele(list, index))

#  generate all permutations of a list in Python

from itertools import permutations

data = ["1", "2", "3", "4"]
for p in permutations(data):
    print(list(p))


#  get the difference between the two lists.


def list_difference_set(list1, list2):
    return list(set(list1) - set(list2))


list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]

print(list_difference_set(list1, list2))
print(list_difference_set(list2, list1))

# append a list to the second list.


def append_lists(list1, list2):

    for i in list2:

        list1.append(i)

    return list1


list1 = [1, 2, 3, 4, 5, 6]
list2 = [7, 8, 9]

print(append_lists(list1, list2))

# check whether two lists are circularly identical.


def are_circularly_identical(list1, list2):
    if len(list1) != len(list2):
        return False
    return str(list2) in str(list1 + list1)


list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 1, 2]
list3 = [1, 3, 2, 4, 5]

print(are_circularly_identical(list1, list2))
print(are_circularly_identical(list1, list3))


#  find common items from two lists.


def common_items_set(list1, list2):
    return list(set(list1) & set(list2))


print(common_items_set(list1, list2))

#  split a list based on first character of word.


def remove_duplicates(list_of_lists):

    unique_lists = []
    seen = set()

    for sublist in list_of_lists:

        sublist_tuple = tuple(sublist)
        if sublist_tuple not in seen:
            unique_lists.append(sublist)
            seen.add(sublist_tuple)

    return unique_lists


sample_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
new_list = remove_duplicates(sample_list)
print(new_list)
