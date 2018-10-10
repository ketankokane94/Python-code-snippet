__author__ = 'KK'
__author__ = 'SB'


"""
CSCI-603 : intrumentation_sort.py Lab-5 (week 6)
Author : Ketan Kokane
Author : Siddharth Bapat

This file provides the implementation to merge and selection sort

"""
MAXIMUM_INT = 99999999999


def msort(unsorted_list,comparisons = 0):
    """
    this is function which sorts the given list using merge sort and also
    notes the number of comparisons done during sorting
    :param unsorted_list:
    :param comparisons:
    :return: a tuple of sorted list and number of comparisons, eg ([1,2],3)
    """
    # establish base to come out of recursion
    if len(unsorted_list) == 1:
        return unsorted_list,0
    else:

        left_index = 0
        right_index = len(unsorted_list)
        # to divide the list in half find the index of middle element and
        # using slice notation divide the array
        # eg. [0,1] left = 0, right = 2, mid = 3//2 = 1 so merge ([0]),merge(1)
        middle_index = (left_index + right_index + 1) // 2
        return merge(msort(unsorted_list[:middle_index],comparisons),msort(unsorted_list[
                                                               middle_index:]), comparisons)


def merge(left_list, right_list,comparisons):
    """
    This is a helper function used by merge sort to merge to array in
    ascending order, it also maintains the number of comparisons made during
    sorting
    :param left_list:
    :param right_list:
    :param comparisons:
    :return:
    """
    left_list, left_compares = left_list[0],left_list[1]
    right_list, right_compares = right_list[0], right_list[1]
    left_index = right_index = 0
    merged_list = []
    comparisons = comparisons + left_compares + right_compares
    while left_index < len(left_list) and right_index < len(right_list):
        comparisons += 1
        if left_list[left_index] <= right_list[right_index]:
            merged_list.append(left_list[left_index])
            left_index += 1
        else:
            merged_list.append(right_list[right_index])
            right_index += 1


    # reaching here means either of the list got exhausted
    comparisons += 1
    if left_index == len(left_list):
        # left list was exhausted
        merged_list.extend(right_list[right_index:])
    else:
        # right list was exhausted
        merged_list.extend(left_list[left_index:])
    return merged_list, comparisons


def find_min(unsorted_list,from_index=1,comparisons=0):
    """
    This function returns a minimum element in a list from given index also
    notes the number of comparisons made during finding the min element
    :param unsorted_list:
    :param from_index:
    :param comparisons:
    :return:
    """
    # assign initial min value to the maximum possible number in this
    # scenario anything more than 100000 is fine
    min = MAXIMUM_INT
    min_element_index = 0
    # iterate from given index upto the length of list
    for index in range(from_index,len(unsorted_list)):
        # every if condition can be considered as an comparison made
        comparisons += 1
        if unsorted_list[index] < min:
            # if a smaller element compared to min is found then update it
            min = unsorted_list[index]
            min_element_index = index
    # return the minimum element, its zero based index from the list and
    # number of comparisons required to find the min element
    return min,min_element_index,comparisons


def ssort(unsorted_list):
    """
    this function sorts an unsorted list using selection sort
    :param unsorted_list:
    :return:  a tuple of sorted list and number of comparisons, eg ([1,2],3)
    """
    comparisons = 0
    for position_to_sort in range(len(unsorted_list)-1):
        min,index ,comparisons = find_min(unsorted_list,position_to_sort,comparisons)
        comparisons += 1
        if unsorted_list[position_to_sort]  > min:
            unsorted_list[position_to_sort], unsorted_list[index] = unsorted_list[index], unsorted_list[position_to_sort]
    return  unsorted_list,comparisons