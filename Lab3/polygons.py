import sys
import turtle
import random

COLORS = ['', 'orange', 'yellow', 'green', 'blue', 'blueviolet', 'violet','black','red']

FILL_PEN_WIDTH = 2
UNFILL_PEN_WIDTH = 8

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
    return sides,fill_no_fill


def draw_poly(sides,length):
    if  sides > 2:
        for _ in range(sides):
            turtle.pensize(sides//2)
            turtle.color(COLORS[random.randint(1,8)])
            turtle.fd(length/3)
            turtle.left(10)
            draw_poly(sides-1,length/2)
            turtle.right(10)
            turtle.fd(length/6)
            turtle.left(360/sides)





def stop_program():
    exit(0)
def main():

    sides, fill_no_fill = get_parameters()
    sides = 7
    turtle.tracer(0, 0)
    turtle.setpos(-100,-350)
    draw_poly(sides,SIDE_LENGTH)
    turtle.update()
    turtle.mainloop()
    #TODO use turtle.write to print names on the screen


if __name__ == '__main__':
    main()
