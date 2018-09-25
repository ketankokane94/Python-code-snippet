__author__ = 'KK'
"""
CSCI-603 : Polygons Lab-3 (week 4)
Author : Ketan Kokane

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
#before execution, turtle, sys, and random modules are importedd
import sys
import turtle
import random
#[,3,4,5,6,7,8]
COLORS = ['', '', '', 'blue', 'orange', 'purple', 'yellow','green','red']
PEN_SIZE = [2,25]
WINDOW_LENGTH = 800
SIDE_LENGTH = 200

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
    return sides,fill_no_fill == 'fill'


def draw_poly(sides, length):
    turtle.color(COLORS[sides])
    turtle.begin_fill()
    for _ in range(sides):
        turtle.fd(length)
        turtle.left(360/sides)
    turtle.end_fill()


def draw_pattern(sides,length,fill_no_fill):
    """
    :param sides:
    :param length:
    :param fill_no_fill:
    :return:
    """
    length_drawn = 0
    if sides > 2:
        turn = 20
        if fill_no_fill:
            draw_poly(sides,length)
        for _ in range(sides):
            turtle.fd(length/3)
            turtle.left(turn)
            length_drawn = length_drawn + draw_pattern(sides - 1, length / 2, fill_no_fill)
            turtle.right(turn)
            turtle.fd(length/3)
            turtle.fd(length / 3)
            turtle.left(360/sides)

        return (length * sides) + length_drawn
    return 0



def init():
    """

    :return:
    """
    turtle.setup(width=WINDOW_LENGTH, height=WINDOW_LENGTH, startx=00, starty=00)
    turtle.up()
    turtle.setpos(250,250)
    turtle.write("ketan kokane",font=("Arial", 20, "italic"))
    turtle.setpos(-100, -200)
    turtle.down()


def main():
    """

    :return:
    """
    init()
    sides, fill_no_fill = get_parameters()
    turtle.tracer(0, 0)
    print(draw_pattern(sides, SIDE_LENGTH, fill_no_fill))
    turtle.update()
    turtle.exitonclick()

if __name__ == '__main__':
    main()
