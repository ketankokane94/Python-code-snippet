__author__ = 'KK'
__author__ = 'SB'


"""
CSCI-603 : transformer Lab-4 (week 5)
Author : Ketan Kokane
Author : Siddharth Bapat

"""

import sys


OPERATIONS_SEPERATOR = ';'

def shift(message, index = 0, exponent = 1):
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


def split_into_groups(message, group_size):
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
        message = split_into_groups(message, group_size)
        return swap(message, left, right)


def make_call_rotate(message, operator, encrypt_message):
    """
    this function is responsible to use the rotate transformation for encrypt and decrypt
    by preprocessing it a little

    :param message:
    :param operator:
    :param encrypt_message:
    :return:
    """
    if len(operator) == 1:
        if encrypt_message:
            return rotate(message)
        else:
            return rotate(message, -1)
    characters_to_rotate = int(operator[1:])
    if encrypt_message:
        return rotate(message, characters_to_rotate)
    else:
        return rotate(message, -characters_to_rotate)


def generate_call(message,operator,encrypt_message):
    """
      this method is responsible for spliting the operation based on their
      formats and call the appropriate transformation function
    :param message:
    :param operator:
    :param encrypt_message:
    :return:
    """

    if ',' in operator:
        # format of exponents are ",exponent"
        operator, exponent = operator.split(',')
        exponent = int(exponent)
    else:
        exponent = 1
    if not encrypt_message:
        # if message is to be decrypted then we reverse the exponents
        exponent = -exponent
    if operator[0] == "S":
        return shift(message,int(operator[1:]),exponent)
    elif operator[0] == "R":
        return make_call_rotate(message,operator,encrypt_message)
    elif operator[0] == "D":
        if not encrypt_message:
            return "Messages encrypted with duplcate tranformation cannot be " \
                   "decrypted"
        else:
            return duplicate(message,int(operator[1:]),exponent)
    elif operator[0] == "T":
        # need to handle decryption
        if "(" in operator:
            group_size, left = operator.split(')')
            group_size = group_size[group_size.index('(') + 1:]
            if encrypt_message:
                result = group_swap(message,int(left),exponent,int(group_size))
                return result
            else:
                # decrypt
                result = group_swap(message,int(left),-exponent,
                                     int(group_size))
                return result.replace('$','')
        else:
            if encrypt_message:
                return swap(message, int(operator[1:]), exponent)
            else:
                return swap(message, int(operator[1:]), -exponent)


def process_message(message, operations,encrypt_message):
    """
    This is an intermediary method to stack up the result of multiple
    transformation
    :param message:
    :param operations:
    :param encrypt_message:
    :return:
    """
    # multiple transformations are seperated by semi colon
    operations = operations.strip().split(OPERATIONS_SEPERATOR)
    # remove new line characters from the end of the message
    message = message.strip('\n')
    # if the message is to be decrypted then the transformation needs to be
    # applied in reverse order to get the original message back
    if not encrypt_message:
        operations.reverse()
    for operation in operations:
        if len(operation) > 0:
            # generate call to the actual transformation function
             message = generate_call(message,operation,encrypt_message)
    return message


def prompt_user_for_input():
    """
    this method prompts user to get the parameters required to carry out
    transformation of messages
    :return:
    """
    message_file = input("please enter the file name of mesages\n")
    instruction_file = input("please enter the file name of intructions\n")
    output_file = input("please provide a name for the generated output file\n")
    encrypt_message = input("are the messages to be encrypted or decrypted "
                         "<press e "
          "or d>\n")
    return message_file,instruction_file,output_file,encrypt_message


def get_required_params_and_execute():
    """
    this method is responsible for getting the main parameters required for
    the program and trigger the encryption or decryption mechanism
    :return:
    """
    if len(sys.argv) == 5:
        # means user provided all the required params in the command line
        read_files_and_process(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[
            4] == 'e')
    else:
        # user did not provide all the required parameters thus will be
        # asking user for each input
        message_file, instruction_file, output_file, encrypt_message = prompt_user_for_input()
        # once the parameters are received from the user, initiate the file
        # processing
        read_files_and_process(message_file,instruction_file,output_file,
                               encrypt_message=='e')


def process_output(output,output_file):
    """
    this method simply deals with how to show user the out put.
    writes output to terminal and to the provided output file
    :param output:
    :param output_file:
    :return:
    """
    with open(output_file,'a') as out:
        out.write(output + '\n')
    print(output)


def create_output_file(output_file):
    """
    this method creates the output file
    :param output_file:
    :return:
    """
    with open(output_file,'w') as f:
        f.close()


def check_file_exists(list_of_input_files):
    """
    this method receives the list of files which the program is suppose to
    read and process,
    this method ensures that the mentioned files are present if not then
    terminate the program
    :param list_of_input_files:
    :return:
    """
    for file in list_of_input_files:
        try:
            with open(file,'r') as input_file:
                input_file.close()
        except FileNotFoundError:
            print(file + " does not exist")
            exit(1)


def read_files_and_process(message_file,operations_file,output_file,
                           encrypt_message):
    """
    this method is the main driver method responsible for transformation of
    messages, execution is done line by line, one line from messages and
    instruction files are read and processed

    :param message_file:
    :param operations_file:
    :param output_file:
    :param encrypt_message: is the flag used to determine whether the
    instructions are to be applied for encryption or decryption
    :return:
    """
    files = [message_file,operations_file]
    # check if all the files that are to be read or present or not
    check_file_exists(files)
    # create a output file specified by the user
    create_output_file(output_file)
    # open both the message and instruction files, and iterate over each line
    #  and process message based on the instructions provided
    with open(message_file,'r') as message_lines,open(operations_file,'r') as operaions_lines :
        # to make iteration over both file possible, combined both the lines
        # into a tuple, this is only for the purpose of iteration
        for message,operations in zip(message_lines,operaions_lines):
            # process the message based on the operations given
            output = process_message(message,operations,encrypt_message)
            # process the output
            process_output(output,output_file)




if __name__ == '__main__':
    """
    main driver method
    """
    get_required_params_and_execute()