__author__ = 'KK'
__author__ = 'SB'

"""
CSCI-603 : Forest Lab-2 (week 3)
Author : Ketan Kokane
Author : Siddharth Bapat

This program first prompts the user for the number of trees required.
The program then asks the user whether he wants a house at night.
Based on the input provided, the program draws the trees of types chosen
in random.
The house is placed between 2 trees.
The star is drawn 10 pixels higher than the top of the tallest tree.

The total amount of wood is calculated using the heights of all trees drawn

This value is used to construct a house in the day.
The sun is drawn above and beside the house.

"""
#before execution, turtle, math, and random modules are importedd
import random
import math
import turtle

left_point = -400
right_point = 400

pine_leaf_length = 50
maple_leaf_length = 25
palm_leaf_length = 50

tree_types = ['maple', 'pine', 'palm']
tre_types_length = [200, 150, 120]
difference_between_trees = 100



def draw_trunk(trunk_length):
    """
    This code draws the tree trunk of height provided

    :param      trunk_length:       Height of tree

    :pre: pos (0,0) (relative), heading east, down
    :post: pos (0,trunk_length), heading north, up
    :return:
    """
    t.down()
    t.left(90)
    t.fd(trunk_length)
    t.up()


def draw_triangle(side_length):
    """
    This block of code draws the triangle for the pine tree

    :param      side_length:        The length of the side

    :pre: pos (0,0) (relative), heading north, up
    :post: pos (0,0) (relative), heading north, up
    :return:
    """
    t.down()
    for _ in range(3):
        t.fd(side_length)
        t.right(120)
    t.up()


def draw_pine_tree_top():
    """
    This block of code draws the top of the pine tree (triangle)

    :pre: pos (0,0) (relative), heading north, up
    :post: pos (0,0) (relative), heading north, up
    :return:
    """

    t.left(90)
    t.fd(pine_leaf_length // 2)
    t.right(120)
    t.up()
    draw_triangle(pine_leaf_length)
    t.right(60)
    t.fd(pine_leaf_length // 2)
    t.left(90)


def draw_maple_tree_top():
    """
    This block of code draws the top of the maple tree (circle)

    :pre: pos (0,0) (relative), heading north, up
    :post: pos (0,0) (relative), heading north, up
    :return:
    """

    t.down()
    t.right(90)
    t.circle(maple_leaf_length)
    t.left(90)
    t.up()


def draw_palm_tree_top():
    """
    This block of code draws the top of the palm tree (semi-circle)

    :pre: pos (0,0) (relative), heading north, up
    :post: pos (0,0) (relative), heading north, up
    :return:
    """
    t.down()
    t.right(90)
    t.fd(palm_leaf_length)
    t.left(90)
    t.circle(palm_leaf_length,180)
    t.left(90)
    t.fd(palm_leaf_length)
    t.left(90)


def draw_tree_top(tree_type):
    """
    This block code draws the tree top as per the tree type chosen in random

    :param      tree_type:      The tree type chosen in random

    :pre: pos (0,0) (relative), heading north, up
    :post: pos (0,0) (relative), heading north, up

    :return:
    """
    if tree_type == 'pine':
        draw_pine_tree_top()
    elif tree_type == 'maple':
        draw_maple_tree_top()
    elif tree_type == 'palm':
        draw_palm_tree_top()


def draw_tree(length, tree_type):
    """
    This block of code draws a tree of a specific type that was
    selected randomly.
    The trunk and tree top functions are invoked to draw the tree
    parts.

    :param      length:     The random length chosen for the tree trunk
    :param      tree_type:  The tree type chosen in random

    :pre: pos (0,0) (relative to previous position), heading east, up
    :post: pos (0,0) (relative to previous position), heading east, up

    :return:                Returns the height of the tree drawn
    """
    t.up()
    draw_trunk(length)
    draw_tree_top(tree_type)
    t.bk(length)
    t.right(90)
    t.up()
    return length


def draw_picture_base():
    """
    This block of code draws the initial ground line (grass) before
    the execution of the main program

    :pre: pos (-390,-350), heading east, down
    :post: pos (-440,-350), heading east, up

    :return:
    """
    t.up()
    t.speed('normal')
    t.setpos(left_point + 10,left_point + 50)
    t.down()
    t.fd(right_point - left_point )
    t.bk(right_point - left_point - 50)
    t.up()


def initialise_screen():
    """
    This block of code initializes the pop up window to width 1200 and height
    800
    THe world coordinates are set as specified
    :return:
    """
    turtle.setup(width=1200, height=800, startx=0, starty=0)
    turtle.setworldcoordinates(left_point,left_point,right_point,right_point)


def draw_square(length):
    """
    This block of code draws the base of the house at night

    :param      length:     The length of each side

    :pre: pos (0,0) (relative), heading east, up
    :post: pos (length, 0) (relative), headin east, up
    :return:
    """
    t.down()
    for _ in range(4):
        if _ == 2:
            t.up()
        else:
            t.down()
        t.fd(length)
        t.left(90)
    t.fd(length)
    t.up()


def draw_roof_top(length):
    """
    This block of code draws the roof of the house at night

    :param      length:     The length of each roof side

    :pre: pos (0,0) (relative), heading north, down
    :post: pos (0-wall_height, 0), heading southwest, down
    :return:
    """
    t.left(45)
    t.down()
    t.fd(length)
    t.left(90)
    t.fd(length)


def draw_house(wall_height):
    """
    This block of code draws the house if requested by the user
    This block of code is invoked again to draw the house in the day

    :param      wall_height:        The height of the house excluding the roof

    :pre: pos (0,0) (relative), heading east, up
    :post: pos (wall_height, 0), heading east, up

    :return:
    """
    draw_square(wall_height)
    t.left(90)
    t.fd(wall_height)
    draw_roof_top(wall_height / math.sqrt(2))
    t.up()
    t.left(45)
    t.fd(wall_height)
    t.left(90)
    t.fd(wall_height)


def draw_star(sky_height):
    """
    This block of code draws the star

    :param      sky_height:     The height of the star

    :pre: pos (0,0) (relative), heading east, up
    :post: pos (0,0) (relative), heading east, up

    :return:
    """
    star_size = 20
    t.left(90)
    t.fd(sky_height)
    t.down()
    for _ in range(4):
        t.fd(star_size)
        t.bk(star_size)
        t.right(90)
        t.up()
        t.circle(star_size//2, 45)
        t.down()
        t.left(90)
    t.up()
    t.fd(star_size)
    t.left(90)


def get_drawing_sequence(noOfTrees, house):
    """
    This block of code determines the sequence of the elements to be drawn
    based on the user's input.
    If there is no house, the sequence is the number of trees specified by
    the user.
    If there is a house, this block of code ensures the house is between two
    trees.
    The sequence then begins and ends with a tree of random type.
    In between, the order of trees and house is randomly decided.

    :param      noOfTrees:      The number of trees specified by the user.
    :param      house:          The user decides whether he wants a house or
                                not and assigns the answer to the variable.
    :return:                    Returns the final sequence of trees and house
    """
    if house == 'n':
        return ['tree'] * noOfTrees
    draw_sequence = ['tree'] * (noOfTrees-2)
    draw_sequence.append('house')
    random.shuffle(draw_sequence)
    return ['tree'] + draw_sequence + ['tree']


def calculate_wall_height(available_wood):
    """
    This block of code computes the height of the house in the day using the
    wood from the trees drawn

    :param      available_wood:     Total wood from the trees

    :return:
    """
    return (available_wood / (2 + math.sqrt(2)))


def draw_sun(height):
    """
    This block of code draws the sun

    :param      height:     The height of the sun

    :pre: pos (0,0) (relative), heading east, up
    :post: pos (500,height) (relative), heading east, down

    :return:
    """
    t.up()
    t.left(90)
    t.fd(height)
    t.right(90)
    t.fd(300)
    t.down()
    t.circle(30)


def go_to_maximum_tree(index_of_tallest_tree,draw_sequence):
    """
    this block of code moves the turtle from last tree to the tree with the maximum height
    :param index_of_tallest_tree:
    :param draw_sequence: used to find the sequence in which the forest was drawn
    :return:
    :pre: pos (0,0) (relative), heading east, up
    :post: pos (backward_distance,0) (relative), heading east, down

    """
    length_of_draw_sequence = (len(draw_sequence))
    backward_distance = (length_of_draw_sequence - index_of_tallest_tree)  * difference_between_trees
    if 'house' not in (draw_sequence[index_of_tallest_tree:-1]):
        t.bk(backward_distance)
    else:
        t.bk(backward_distance + difference_between_trees)


if __name__ == '__main__':
    """
    This is the main function.
    The distance between each tree and house is set as 100.
    From this function, the screen coordinates and the base ground functions
    are set up.
    The function then prompts the user for the number of trees and whether
    there includes a house.
    Based on the users input, the code invokes functions to draw the trees
    in random as well as the house if specified by the user.
    The highest tree is calculated.
    """

    t = turtle.Turtle()
    t.up()
    initialise_screen()
    draw_picture_base()

    noOfTrees = int(input("How many trees in your forest? "))
    #noOfTrees = 4
    house = input("Is there a house in the forest (y/n)? ")
    #house = 'n'
    draw_sequence = get_drawing_sequence(noOfTrees, house)
    available_wood = 0
    max_tree_height = 0
    index_of_tallest_tree = 0
    for _ in range(len(draw_sequence)):
        if draw_sequence[_] == 'tree':
            index = random.randint(0, len(tree_types) - 1)
            tree_height = draw_tree(random.randint(50,tre_types_length[index]),
                                    tree_types[index])
            available_wood = available_wood + tree_height
            if tree_height > max_tree_height:
                max_tree_height = tree_height
                index_of_tallest_tree = _
        else:
            draw_house(100)
        t.fd(difference_between_trees)
    go_to_maximum_tree(index_of_tallest_tree,draw_sequence)
    draw_star(max_tree_height + 60)
    t.setpos(left_point + 10, left_point + 50)

    key = input("Night is done, press enter for the day")
    # user presses enter key
    if key == '':
        if house == 'y':
            available_wood = available_wood + (200 + (100 * math.sqrt(2)))
        print("We have {0} units of lumber for building".format(available_wood))
        wall_height = calculate_wall_height(available_wood)
        print("we will build a house with walls {0} tall".format(wall_height))
        t.reset()  # clears
        initialise_screen()
        draw_picture_base()
        draw_house(wall_height)
        draw_sun(wall_height + (wall_height / 2) + 300)
        t.up()
        t.setpos(left_point + 10, left_point + 50)
        key = input("Day is done, press enter to quit") # user presses enter key

        if key == '':
            exit(1)
    turtle.done()
