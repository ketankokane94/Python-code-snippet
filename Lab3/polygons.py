import sys


def get_parameters():
    """
    reads parameters from command line argument, converts them to the required types and returns
    :return:
    """
    if len(sys.argv) < 3:
        print("this program requires two command line parameters to be passed, sides and fill or no fill")
    try:
        sides = int(sys.argv[1])
    except ValueError:
        print("wrong value entered for number of sides, terminating the program")
        sides = 0
        exit(1)
    fill_no_fill = sys.argv[2]
    return sides,fill_no_fill


def main():
    sides, fill_no_fill = get_parameters()
    #TODO use turtle.write to print names on the screen


if __name__ =='__main__':
    main()

    