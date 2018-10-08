MAXIMUM_INT = 9999


def msort(unsorted_list):
    if len(unsorted_list) == 1:
        return unsorted_list,0
    else:
        left_index = 0
        right_index = len(unsorted_list)
        middle_index = (left_index + right_index + 1) // 2
        return merge(msort(unsorted_list[:middle_index]), msort(unsorted_list[
                                                         middle_index:]))


def merge(left_list, right_list):
    comparisons = 0
    left_index = right_index = 0
    merged_list = []
    while left_index < len(left_list) and right_index < len(right_list):
        if left_list[left_index] <= right_list[right_index]:
            comparisons +=1
            merged_list.append(left_list[left_index])
            left_index += 1
        else:
            merged_list.append(right_list[right_index])
            right_index += 1
            comparisons += 1

    # reaching here means either of the list got exhausted
    if left_index == len(left_list):
        # left list was exhausted
        merged_list.extend(right_list[right_index:])
    else:
        # right list was exhausted
        merged_list.extend(left_list[left_index:])
    return merged_list,  comparisons


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
    elements = [3,4,8,2]
    print("unsorted List:",end='  ')
    print(elements)
    print("sorted List:", end='  ')
    #print(msort(unsorted_list=elements))
    print(ssort(unsorted_list=elements))
