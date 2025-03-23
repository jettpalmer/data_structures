# Implements linear searches.
# CSC 202, Lab 1
# Given code, Summer '22


def iterative_search(lst, key):
    """
    Iteratively find the index of an element in a list.
    TODO: Get this function under 100% coverage.

    :param lst: A list to search
    :param key: An element for which to search
    :return: The index of the element, or None if it is not in the list
    """
    for index in range(len(lst)):
        if lst[index] == key:
            return index

    return None


def recursive_search(lst, key):
    """
    Recursively find the index of an element in a list.
    TODO: Get this function's complexity down to O(n).

    :param lst: A list to search
    :param key: An element for which to search
    :return: The index of the element, or None if it is not in the list
    """
    if len(lst) == 0:
        return None
    elif lst[0] == key:
        return 0

    i = recursive_search(lst[1:], key)

    if i is not None:
        return 1 + i
    else:
        return None
