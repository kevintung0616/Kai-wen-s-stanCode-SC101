"""
File: babygraphics.py
Name: Kevin Tung
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """

    # Calculate the x-coordinate of the vertical line associated with every year in the YEARS list
    x = year_index * width / (len(YEARS)) + GRAPH_MARGIN_SIZE

    return x



def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Create the top background line in the canvas
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)

    # Create the bottom background line in the canvas
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)

    for i in range(len(YEARS)):  # Loop over every year in the YEARS list

        # Get the x-coordinate of the vertical line in the canvas
        vertical_line_x = get_x_coordinate(CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE, i)

        # Create the vertical line according to the x-coordinate
        canvas.create_line(vertical_line_x, 0, vertical_line_x, CANVAS_HEIGHT)

        # Create the text of each year in the YEARS list according to the x-coordinate
        canvas.create_text(vertical_line_x + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Set the distance between two neighbor x coordinates
    x_dis = int((CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE) / len(YEARS))

    # Set the distance between two neighbor y coordinates
    y_dis = (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / 1000

    for j in range(len(lookup_names)):  # Loop over each name in the list "lookup_names"

        # Loop over every year from the first year to the second-to-last one
        for i in range(len(YEARS)-1):

            # If the current year of the name exist in name_data, get the rank
            if str(YEARS[i]) in name_data[lookup_names[j]]:
                rank = int(name_data[lookup_names[j]][str(YEARS[i])])

            else:  # If the current year of the name doesn't exist in name_data, ignore the rank
                rank = float('inf')

            # if the next year of the name exist in name_data, get the rank
            if str(YEARS[i+1]) in name_data[lookup_names[j]]:
                next_rank = int(name_data[lookup_names[j]][str(YEARS[i+1])])

            else:  # If the next year of the name doesn't exist in name_data, ignore the rank
                next_rank = float('inf')

            # If a name ranks below the top 1000 in both the current and the next year,
            # the y coordinates of the both years are at the bottom of the canvas
            if rank > 1000 and next_rank > 1000:
                canvas.create_line(GRAPH_MARGIN_SIZE + i * x_dis, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE
                                   + (i + 1) * x_dis, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH, fill=COLORS[j % len(lookup_names)])

                canvas.create_text(GRAPH_MARGIN_SIZE + TEXT_DX + i * x_dis, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                   text=lookup_names[j] + ' *', anchor=tkinter.SW)

            # If a name ranks above the top 1000 in the current year but below the top 1000 in the next year,
            # only the y coordinate of the next year is at the bottom of the canvas
            elif rank < 1000 and next_rank > 1000:
                canvas.create_line(GRAPH_MARGIN_SIZE + i * x_dis, GRAPH_MARGIN_SIZE + rank * y_dis, GRAPH_MARGIN_SIZE
                                   + (i + 1) * x_dis, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH, fill=COLORS[j % len(lookup_names)])

                canvas.create_text(GRAPH_MARGIN_SIZE + TEXT_DX + i * x_dis, GRAPH_MARGIN_SIZE + rank * y_dis,
                                   text=lookup_names[j] + ' ' + str(rank), anchor=tkinter.SW)

            # If a name ranks below the top 1000 in the current year but above the top 1000 in the next year,
            # only the y coordinate of the current year is at the bottom of the canvas
            elif rank > 1000 and next_rank < 1000:
                canvas.create_line(GRAPH_MARGIN_SIZE + i * x_dis, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE
                                   + (i + 1) * x_dis, GRAPH_MARGIN_SIZE + next_rank * y_dis, width=LINE_WIDTH, fill=COLORS[j % len(lookup_names)])

                canvas.create_text(GRAPH_MARGIN_SIZE + TEXT_DX + i * x_dis, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                   text=lookup_names[j] + ' *', anchor=tkinter.SW)

            else:  # If a name ranks above the top 1000 in both the current and the next year,
                   # the y coordinates of the both years lie between the top and the bottom line
                canvas.create_line(GRAPH_MARGIN_SIZE + i * x_dis, GRAPH_MARGIN_SIZE + rank * y_dis, GRAPH_MARGIN_SIZE
                                   + (i + 1) * x_dis, GRAPH_MARGIN_SIZE + next_rank * y_dis, width=LINE_WIDTH, fill=COLORS[j % len(lookup_names)])

                canvas.create_text(GRAPH_MARGIN_SIZE + TEXT_DX + i * x_dis, GRAPH_MARGIN_SIZE + rank * y_dis,
                                   text=lookup_names[j] + ' ' + str(rank), anchor=tkinter.SW)

        # Draw the last year data
        # If a name ranks above the top 1000 in the last year, its y coordinates lies between the top and the bottom line
        if next_rank < 1000:
            canvas.create_text(GRAPH_MARGIN_SIZE + TEXT_DX + (len(YEARS)-1) * x_dis, GRAPH_MARGIN_SIZE + next_rank * y_dis,
                               text=lookup_names[j] + ' ' + str(next_rank), anchor=tkinter.SW)

        else:  # If a name ranks below the top 1000 in the last year, its y coordinates is at the bottom of the canvas
            canvas.create_text(GRAPH_MARGIN_SIZE + TEXT_DX + (len(YEARS)-1) * x_dis, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                               text=lookup_names[j] + ' *', anchor=tkinter.SW)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)


    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
