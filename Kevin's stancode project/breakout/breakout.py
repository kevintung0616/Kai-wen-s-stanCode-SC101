"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This program simulate the breakout game. The goals is to destroy all of the bricks.
Once the number of lives is zero or the number of bricks is zero, the game is over.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.gui.events.mouse import onmouseclicked

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts



def main():
    life = NUM_LIVES
    graphics = BreakoutGraphics()
    # Add the animation loop here!

    # The breakout game will be continue unless the number of lives and the number of bricks is zero.
    while life > 0 and graphics.num_brick > 0:
        while True:

            dx = graphics.get_dx()  # Get the horizontal velocity of the ball

            dy = graphics.get_dy()  # Get the vertical velocity of the ball

            graphics.ball.move(dx, dy)  # Make the ball move in the velocity of dx and dy

            # Call the method "collision" to simulate the situation when the ball hits the paddle or bricks
            graphics.collision()

            # If the ball hits the left and the right boundary, the ball will bounce on the x-axis
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                graphics.set_dx()

            # If the ball hits the top boundary, the ball will bounce on the y-axis
            if graphics.ball.y <= 0:
                graphics.set_dy()

            pause(FRAME_RATE)

            # If the ball fall into the bottom, the number of lives will be reduced by one and the speed
            # and the position of the ball will be reset.
            if graphics.ball.y > graphics.window.height:
                life -= 1
                graphics.reset_ball()
                break

            #  If the ball destroys all of the bricks, the game is over
            if graphics.num_brick == 0:
                graphics.reset_ball()
                break


if __name__ == '__main__':
    main()
