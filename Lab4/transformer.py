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
    return result


def generate_call(message,operator):
    """
    this is a helper function which splits the operator to the required
    format to make call to the shift function and returns its ouput
    :param message:
    :param operator:
    :return:
    """
    # the operator is always of the form S8, 9
    if operator[0] == "S":
        operator, exponent = operator.strip().split(',')
        return shift(message,int(operator[1:]),int(exponent))
    elif operator[0] == "R":
        return rotate(message,int(operator[1:]))
    elif operator[0] == "D":
        operator, exponent = operator.strip().split(',')
        return duplicate(message,int(operator[1:]),int(exponent))




#print(generate_call("hello","D0,6"))
#print(generate_call("ketan","S3,1"))


