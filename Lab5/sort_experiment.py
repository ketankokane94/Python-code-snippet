__author__ = 'KK'
__author__ = 'SB'


"""
CSCI-603 : sorting_experiment.py Lab-5 (week 6)
Author : Ketan Kokane
Author : Siddharth Bapat

This programs explores the time comparisons of merge and selection sort 
algorithm
"""


import random
from datetime import datetime
import instrumentation_sort


def generate_arrays(n):
    """
    This is a helper function which generates shuffled list of elements from
    0 upto n
    :param n:
    :return:
    """
    generated_list = list(range(n))
    random.shuffle(generated_list)
    return generated_list


def check_sort(sorted_list):
    """
    A helper function which checks if all the elements in the sorted are in
    strict ascending order
    :param sorted_list:
    :return:
    """
    for index in range(len(sorted_list)-1):
        if sorted_list[index] > sorted_list[index+1]:
            return False
    return True


def print_result(table):
    """
    a helper function to print the generated output
    :param table:
    :return:
    """
    for row in table:
        for element in row:
            print(element.ljust(15),end='')
        print()


if __name__ == '__main__':
    result = [['ALGORITHM','N','COMPARISONS','MICROSECS','IS SORTED']]
    for N in [1,10,100,1000,10000]:
        if N == 10000:
            print(' running selection and merge on list of length: ',N)
        start = datetime.now()
        sorted_list = instrumentation_sort.ssort(
            unsorted_list=generate_arrays(
                N))
        end = datetime.now()
        sorted_list, comparisons = sorted_list[0], sorted_list[1]

        result.append(['SELECTION', str(N), str(comparisons), str((end -
                                                              start).microseconds),str(check_sort(sorted_list))])

        start = datetime.now()
        sorted_list = instrumentation_sort.msort(
            unsorted_list=generate_arrays(
            N))
        end = datetime.now()
        sorted_list, comparisons = sorted_list[0], sorted_list[1]

        result.append(
            ['MERGE SORT', str(N), str(comparisons), str((end -
                                                      start).microseconds),str(check_sort(sorted_list))])
    print_result(result)




