__author__ = 'KK'
__author__ = 'SB'

# for the polygon of side 8 the program takes around ~15 secs to complete
"""
CSCI-603 : Polygons Lab-3 (week 4)
Author : Ketan Kokane
Author : Siddharth Bapat

This program draws the name of the authors on top right corner,
reads the parameters sides and fill no fill from command line and
draws the polygons with the given sides, with fill no fill option also,
creates pattern by drawing the polygons of reducing sides and length until
no more polygons can be drawn.

The basic pattern used is to draw smaller polygon on one third length of the
main polygon at an angle of 20 degree.

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
    reads parameters from command line argument, converts them to the
    required types and returns
    :return:
    """

    if len(sys.argv) < 3:
        print("this program requires two command line parameters to be passed,"
              " sides and fill or no fill")
        exit(1)
    else:
        try:
            sides = int(sys.argv[1])
        except ValueError:
            print("wrong value entered for number of sides, terminating the program")
            sides = 0
            exit(1)
        fill_no_fill = sys.argv[2]
        return sides,fill_no_fill == 'fill'


def draw_polygon(sides, length):
    """
    pre: (0,0) east, down
    pos: (0,0) east, down

    this is a generic function which draws the polygon with give side
    and length, also fills it with the color. by accessing the color at the
    side index of COLOR array
    :param sides:
    :param length:
    :return:
    """
    turtle.color(COLORS[sides])
    turtle.begin_fill()
    for _ in range(sides):
        turtle.fd(length)
        turtle.left(360/sides)
    turtle.end_fill()


def draw_pattern(sides,length,fill_no_fill):
    """
    pre: (0,0) east, down
    pos: (0,0) east, down

    This function is the main driver function which draws the one third length
    of given polygon, then turns at an angle of 20 degree and recursively
    draws the polygon of reduced side length. till the side is 2.

    Depending on the fill no fill paramters decides if the polygon is to be
    filled or not
    :param sides:
    :param length:
    :param fill_no_fill:
    :return:
    """
    length_drawn = 0
    if sides > 2:
        turn = 20
        if fill_no_fill:
            draw_polygon(sides,length)
        for _ in range(sides):
            turtle.color(COLORS[random.randint(3,8)])
            turtle.fd(length/3)
            turtle.left(turn)
            length_drawn += draw_pattern(sides - 1, length / 2, fill_no_fill)
            turtle.right(turn)
            turtle.fd(length/3)
            turtle.fd(length / 3)
            turtle.left(360/sides)

        return (length * sides) + length_drawn
    return 0



def init():
    """
    Initialisation function to initialize the turtle window and writes the
    names of the authors on the screen
    :return:
    """
    turtle.setup(width=WINDOW_LENGTH, height=WINDOW_LENGTH, startx=00, starty=00)
    turtle.up()
    turtle.setpos(150,250)
    turtle.write("ketan kokane",font=("Arial", 20, "italic"))
    turtle.setpos(150, 300)
    turtle.write("siddharth bapat", font=("Arial", 20, "italic"))
    turtle.setpos(-100, -200)
    turtle.down()


def main():
    """
    Main driver function of the program
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