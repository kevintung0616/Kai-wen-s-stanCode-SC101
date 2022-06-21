"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

"""
Define constants that determine the velocity, acceleration, deceleration, size, start position of the ball 
"""
VX = 3
DELAY = 10
GRAVITY = 1

SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')

# Create a binary variable "click" to define the condition before and after clicking the mouse
click = False
# Create a variable "num_click" to count how many time an user clicks the mouse
num_click = 0
# Draw the ball
ball = GOval(SIZE, SIZE, x = START_X, y = START_Y)

def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """

    # Fill the ball with the black color
    ball.filled = True
    ball.fill_color = 'black'

    # Add the ball to the window
    window.add(ball)

    # Define a function "bounce" within a mouse event-driven program 'onmouseclicked'
    # The ball will drop and then bounce after clicking your mouse
    onmouseclicked(bounce)


def bounce(event):
    """
    This function defines how the ball moves. The ball will drops and bounces and then bounce after the first click.
    When reaching the right end, the ball will move back to the start point. If clicking again, the ball will repeat
    the bounce. The ball will stop moving agter clikcing three times.
    """

    # Define a variable 'vy' as the ball's velocity on the y axis. The start value is 0
    vy = 0

    # Make the binary variable "click" as global
    global click
    # Make a variable "num_click" as global
    global num_click

    # If the program is not under the status of "click", the program will turn into the status of "click" and the number
    # of clicks will be increased by one after clicking your mouse.
    if not click:
        click = True
        num_click = num_click + 1

        while True:

            # The velocity on the y axis will be increased by the constant "GRAVITY" every frame
            vy = vy + GRAVITY
            ball.move(VX, vy)

            # When reaching the ground, the ball will bounce
            if ball.y + ball.height >= window.height:

                vy = -vy * REDUCE
                ball.move(VX, vy)

            pause(DELAY)

            # When reaching the right end, the ball will return to the start point
            if ball.x >= window.width:

                # The status of click becomes false, so the ball will move again when clicking the mouse
                click = False
                ball.x = START_X
                ball.y = START_Y
                break

            # If an user clicking the mouse more then three times, the ball will stop moving even if the users
            # clicking his/her mouse
            if num_click > 3:

                # The status of click becomes true, so the ball will never move
                click = True
                ball.x = START_X
                ball.y = START_Y
                break




if __name__ == "__main__":
    main()
