import sys


MINIMUM = 'zzzzzzzzzzzzzzzz'


def get_file_name():
    """
    simply returns the name of the file to be read
    :return:
    """
    return sys.argv[1]


def get_words_in_this_line(line):
    """
    returns space seperated words in a line
    :param line:
    :return:
    """
    return line.strip().split()


def find_min(list,from_index):
    """
    finds the min element from the array from the given index
    :param list:
    :param from_index:
    :return:
    """
    min_ele = MINIMUM
    required_index = 0
    for index in range(from_index,len(list)):
        if list[index] < min_ele:
            required_index = index
            min_ele = list[index]
    return required_index


def sort_using_selectin_sort(unsorted_words):
    # no need to sort the last position as would already be sorted
    for position_to_sort in range(len(unsorted_words)-1):
        index_of_min_ele = find_min(unsorted_words,position_to_sort)
        unsorted_words[position_to_sort],unsorted_words[index_of_min_ele] = \
            unsorted_words[index_of_min_ele],unsorted_words[position_to_sort]

    return unsorted_words


def bin_search(element,list, left, right):
    if left > right:
        return -1
    else:
        mid = (left + right) // 2
        if list[mid] == element:
            return mid
        elif element < list[mid]:
            return bin_search(element,list,left,mid)
        else:
            return bin_search(element,list,mid,right)


def search(sorted_list, word_at_required_index):
    return bin_search(word_at_required_index,sorted_list,left=0,right=len(
        sorted_list))


if __name__ == '__main__':
    unsorted_words = []
    with open(get_file_name(),'r') as src:
        for line in src:
            unsorted_words.extend(get_words_in_this_line(line))
    word_at_required_index = unsorted_words[10]
    print(unsorted_words)
    sorted_list = sort_using_selectin_sort(unsorted_words)
    print(sorted_list)
    print(search(sorted_list,word_at_required_index))
