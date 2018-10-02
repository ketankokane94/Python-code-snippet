"""
Python provides theordfunction to convert a single character to an integer
ASCIIvalue, and thechrfunction to convert from an ASCII integer to a character.
Withthat in mind, show how to implement shifting of a single uppercase charactercbya
 positive  amountk,  keeping  in  mind  that  if  this  takes  you  past  the  end  of
  thealphabet, it should wrap around.
"""


def shift(message, index=0, exponent=1):
    '''
    this program takes a string and shifts the character at the index
    by exponent units to right or left depending on + -
    :param message:
    :param k:
    :return:
    '''
    # take the ascii value of the given index in the string
    ascii_value_of_character = ord(message[index])
    # shift it by the exponent
    shifted_char = ascii_value_of_character + exponent
    # adjust the ascii value to keep it between the range of 65 and 90
    if shifted_char > 90:
        (shifted_char % 90)  + 65
    elif shifted_char < 65:
        shifted_char += 26
    # convert the string to the list so the character at the given index can
    # be changed with the new shifted character
    message = list(message)
    message[index] = chr(shifted_char)
    # convert the list using into string using the join operation
    return "".join(message)


def rotate(message, characters_to_rotate=1):
    """
    this function takes in a string and rotates it by given characters
    :param message:
    :param characters_to_rotate:
    :return:
    """
    # find the message to be prefixed to the new string
    prefix = message[-(characters_to_rotate % len(message)):]
    # get the remaining part of the message
    remaining_part = message[:-(characters_to_rotate % len(message))]
    # concatenate the prefix and remaining part of the string
    return prefix + remaining_part


def duplicate(message,index,exponent=1):
    """
    this function takes in a message and simply duplicates the character at
    the given index exponent times
    :param message:
    :param index:
    :param exponent:
    :return:
    """
    # convert the message to a string so cane be updated
    message = list(message)
    duplicated_character = message[index] * exponent
    result = message[:index]
    result += duplicated_character
    result += message[index:]
    return "".join(result)


def swap(message, left, right):
    """
    this function swaps the characters at index left and right of the given
    message
    :param message:
    :param left:
    :param right:
    :return:
    """
    # check if indexes are in required range
    if 0 <= left < right < len(message):
        # convert string into a list, so letters can be swapped
        message = list(message)
        message[left],message[right] = message[right],message[left]
        return "".join(message)
    else:
        return message


def get_groups(message, group_size):
    """
    this function gets a string and a positive group size and returns the
    chunks of the same size
    :param message:
    :param group_size:
    :return:
    """
    result = []
    for index in range(0,len(message),group_size):
        result.append(message[index:group_size+index])
    return result


def group_swap(message,left,right,group_size):
    # in case of message length is odd we add one $ character so the string
    # is even length and can be reversed
    """
    This function handles a special case of swap wherein instead of swapping
    characters in the list, the string is divided into groups and then the
    individual list elements are swapped
    :param message:
    :param left:
    :param right:
    :param group_size:
    :return:
    """

    if group_size == 1:
        return swap(message, left, right)
    else:
        # in case of message length is odd we add one $ character so the string
        # is even length and can be reversed
        if len(message) % 2 == 1:
            message = message + "$"
        message = get_groups(message,group_size)
        return swap(message, left, right)


def get_file_names():
    pass


def process_output(output):
    print(output)



def generate_call(message,operator):
    """
    this is a helper function which splits the operator to the required
    format to make call to the shift function and returns its ouput
    :param message:
    :param operator:
    :return:
    """
    # the operator is always of the form S8, 9

    if ',' in operator:
        operator, exponent = operator.split(',')
    else:
        exponent = 1
    if operator[0] == "S":
        return shift(message,int(operator[1:]),int(exponent))
    elif operator[0] == "R":
        if len(operator) == 1:
            return rotate(message)
        return rotate(message, int(operator[1:]))
    elif operator[0] == "D":
        return duplicate(message,int(operator[1:]),int(exponent))
    elif operator[0] == "T":
        if "(" in operator:
            group_size, left = operator.split(')')
            group_size = group_size[group_size.index('(')+1:]
            return group_swap(message,int(left),int(exponent),int(group_size) )
        else:
            return swap(message, int(operator[1:]), int(exponent))



def process_message(message, operations):
    operations = operations.strip().split(';')
    message = message.strip('\n')
    for operation in operations:
        if len(operation) > 0:
             message = generate_call(message,operation)
    return message


def read_files(message_file,operations_file):
    # need top open 3 files message file and operations files
    with open(message_file,'r') as message_lines,open(operations_file,'r') as operaions_lines :
        for message,operations in zip(message_lines,operaions_lines):
            output = process_message(message,operations)
            process_output(output)


read_files('messages.txt','operations.txt')