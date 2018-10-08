import random
from datetime import datetime



MAXIMUM_INT = 9999

def generate_arrays(n):
    generated_list = list(range(n))
    random.shuffle(generated_list)
    return generated_list

def msort(unsorted_list,comparisons = 0):
    if len(unsorted_list) == 1:
        return unsorted_list,0
    else:
        left_index = 0
        right_index = len(unsorted_list)
        middle_index = (left_index + right_index + 1) // 2
        return merge(msort(unsorted_list[:middle_index],comparisons),msort(unsorted_list[
                                                               middle_index:]), comparisons)


def merge(left_list, right_list,comparisons):
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
    min = MAXIMUM_INT
    min_element_index = 0
    for index in range(from_index,len(unsorted_list)):
        comparisons += 1
        if unsorted_list[index] < min:
            min = unsorted_list[index]
            min_element_index = index
    return min,min_element_index,comparisons


def ssort(unsorted_list):
    comparisons = 0
    for position_to_sort in range(len(unsorted_list)-1):
        min,index ,comparisons = find_min(unsorted_list,position_to_sort,comparisons)
        comparisons += 1
        if unsorted_list[position_to_sort]  > min:
            unsorted_list[position_to_sort], unsorted_list[index] = unsorted_list[index], unsorted_list[position_to_sort]
    return  unsorted_list,comparisons

if __name__ == '__main__':
    print('\tALGORITHM'.ljust(20), 'N'.ljust(6), 'COMPARISONS'.ljust(10),
          'MICROSECS'.ljust(10))
    for N in [1,10,100,1000,10000]:

        print('\tSELECTION SORT'.ljust(20), end='\t')
        print(str(N).ljust(6),end='\t')
        start = datetime.now()
        print(str(ssort(unsorted_list=generate_arrays(N))[1]).ljust(10),
              end='\t')
        end = datetime.now()
        print((end - start).microseconds)
        print('\tMERGE SORT'.ljust(20),end='\t')
        print(str(N).ljust(6), end='\t')
        start = datetime.now()
        print(str(msort(unsorted_list=generate_arrays(N))[1]).ljust(10),
              end='\t')
        end = datetime.now()
        print((end - start).microseconds)