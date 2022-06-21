"""
File: 
Name: Kevin Tung
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
from campy.gui.events.mouse import onmousemoved

# This constant controls the size of the pen stroke
SIZE = 15
window = GWindow()

# Create a variable "num_click " to count the number of clicks
num_click = 0

# draw the circle
circle = GOval(SIZE, SIZE)


def click(mouse):

    # Make the variable "num_click as global
    global num_click

    # If the number of clicks is even before clicking the mouse, the program will draw a circle at the cursor mouse
    if num_click % 2 == 0:

        window.add(circle, x=mouse.x - SIZE / 2, y=mouse.y - SIZE / 2)

        # The number of click will be increased by 1 after an user clicks his/her mouse
        num_click = num_click + 1

    # If the number of clicks is odd before clicking the mouse, the program will draw a line between the last click
    # and the cursor mouse
    else:
        # Remove the circle after clicking the mouse
        window.remove(circle)

        # Draw a line. The start point is the center of the circle. The end point is the current cursor mouse
        line = GLine(circle.x + SIZE / 2, circle.y + SIZE / 2, mouse.x, mouse.y)
        window.add(line)

        # The number of click will be increased by 1 after an user clicks his/her mouse
        num_click = num_click + 1


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """

    onmouseclicked(click)



if __name__ == "__main__":
    main()
