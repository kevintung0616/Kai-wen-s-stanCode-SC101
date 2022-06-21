"""
File: stanCodoshop
.py
Name: 
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    # Calculate the distance a pixel and the average RGB value of the pixels to be compared
    color_dis = ((red - pixel.red) ** 2 + (green - pixel.green) ** 2 + (blue-pixel.blue) ** 2) ** 0.5
    return color_dis


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    r = 0
    g = 0
    b = 0

    # Use a for loop to calculate the sum of red, green, and blue values of a list of pixels
    for i in range(len(pixels)):
        r = r + pixels[i].red
        g = g + pixels[i].green
        b = b + pixels[i].blue

    # Calculate the average red, green, and blue value, and then return a list of RGB values
    rgb = [r//len(pixels), g//len(pixels), b//len(pixels)]
    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    # First, set the default color distance as an infinite value
    dist = float('Inf')
    best_pixel = pixels[0]

    # Create a pixel with the average RGB values of the input list of pixels
    avg_rgb = get_average(pixels)
    avg_red = avg_rgb[0]
    avg_green = avg_rgb[1]
    avg_blue = avg_rgb[2]

    for i in range(len(pixels)):
        # Use a for loop to compare the distance between each pixel in the list and the average point
        if get_pixel_dist(pixels[i], avg_red, avg_green, avg_blue) < dist:
            # If the distance is smaller then the previous value, the previous one will be replaced by the new distance
            dist = get_pixel_dist(pixels[i], avg_red, avg_green, avg_blue)
            # If the distance between the average point and a pixel is smallest, it will be stored as "best_pixel"
            best_pixel = pixels[i]

    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect

    # Use nest for loop to loop over the image
    for x in range(result.width):
        for y in range(result.height):
            # Define a pixels_list to store each pixel among a list of images
            pixels_list = []
            for image in images:
                pixels_list = pixels_list + [image.get_pixel(x, y)]
            pixel = get_best_pixel(pixels_list)

            result.set_pixel(x, y, pixel)
    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
