"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10       # Number of rows of bricks
BRICK_COLS = 10       # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'Black'
        self.window.add(self.paddle, x=(window_width - paddle_width)/2, y=window_height-paddle_offset-paddle_height)

        # Center a filled ball in the graphical window
        self.ball = GOval(2 * ball_radius, 2 * ball_radius)
        self.ball.filled = True
        self.ball.fill_color = 'Black'
        self.window.add(self.ball, x=(window_width - ball_radius*2)/2, y=(window_height-ball_radius*2)/2)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)
        onmouseclicked(self.ball_fall)

        # Draw bricks
        color = ['red', 'orange', 'yellow', 'green', 'blue']
        for i in range(brick_cols):
            for j in range(brick_rows):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick.fill_color = color[j // 2]
                self.window.add(self.brick, x=i*(brick_width + brick_spacing), y=j*(brick_height + brick_spacing)+brick_offset)

        self.click = False  # Create a binary variable 'click'. The default value is False
        self.num_brick = brick_rows * brick_cols  # Create a variable num_brick to count how many bricks are left

    # Define a method 'paddle_move' to make the paddle follow the mouse
    def paddle_move(self, mouse):
        self.paddle.x = mouse.x - self.paddle.width / 2

        # Even if the mouse is out of the left and right boundaries,
        # the whole paddle should be still inside the window
        if mouse.x - self.paddle.width / 2 < 0: # If the mouse is out of the left boundary
            self.paddle.x = 0
        if mouse.x + self.paddle.width / 2 > self.window.width: # If the mouse is out of the right boundary
            self.paddle.x = self.window.width - self.paddle.width

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    # Define a method 'ball_fall' to define the velocity of ball
    def ball_fall(self, mouse):
        if not self.click:
            # Give the ball a random velocity on the x-axis
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = self.__dx * -1
            # Give the ball the default velocity on the y-axis
            self.__dy = INITIAL_Y_SPEED
            self.click = True

    def reset_ball(self): # Reset the velocity and the position of the ball
        self.ball.x = (self.window.width - self.ball.width) / 2
        self.ball.y = (self.window.height - self.ball.height) / 2
        # Reset the velocity to zero, so the ball will stop moving
        self.__dx = 0
        self.__dy = 0
        self.click = False

    def set_dx(self):
        self.__dx = -self.__dx

    def set_dy(self):
        self.__dy = -self.__dy

    def collision(self):
        # To prevent the ball from sticking to the paddle, make sure the ball will bounce only when hitting the top of the paddle
        if self.ball.y +  self.ball.height <= self.window.height - PADDLE_OFFSET - 0.8*self.paddle.height:

            # If the top left corner of the ball hit an object
            if self.window.get_object_at(self.ball.x, self.ball.y) is not None:
                self.set_dy()
                # If the ball hits an object whose y-coordinate is lower t han the paddle, this object must be a brick
                # Therefore, the brick should be removed if it is hit by the ball
                if self.ball.y + self.ball.height < self.window.height-PADDLE_OFFSET-self.paddle.height:
                    self.window.remove(self.window.get_object_at(self.ball.x, self.ball.y))
                    self.num_brick -= 1

            # If the top right corner of the ball hit an object
            elif self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y) is not None:

                self.set_dy()

                if self.ball.y + self.ball.height < self.window.height-PADDLE_OFFSET-self.paddle.height:
                    self.window.remove(self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y))
                    self.num_brick -= 1

            # If the bottom left corner of the ball hit an object
            elif self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height) is not None:

                self.set_dy()

                if self.ball.y + self.ball.height < self.window.height-PADDLE_OFFSET-self.paddle.height:
                    self.window.remove(self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height))
                    self.num_brick -= 1

            # If the bottom right corner of the ball hit an object
            elif self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height) is not None:

                self.set_dy()

                if self.ball.y + self.ball.height < self.window.height-PADDLE_OFFSET-self.paddle.height:
                    self.window.remove(self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height))
                    self.num_brick -= 1



