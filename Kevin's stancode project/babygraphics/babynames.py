"""
File: babynames.py
Name:

test:
py babynames.py data/small/small-2000.txt data/small/small-2010.txt
py babynames.py -search aa data/full/baby-2000.txt data/full/baby-2010.txt
py babygraphics.py
--------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import sys


def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given year and rank to the associated name in the name_data dict.

    Input:
        name_data (dict): dict holding baby name data
        year (str): the year of the data entry to add
        rank (str): the rank of the data entry to add
        name (str): the name of the data entry to add

    Output:
        This function modifies the name_data dict to store the provided
        name, year, and rank. This function does not return any value.
    """
    if name in name_data:  # If the input name already exists in name data

        if year not in name_data[name]:  # If the name has been ranked in name data
            name_data[name][year] = rank

        # If the name is already ranked but there is a higher rank, the higher rank should the previous rank
        if year in name_data[name] and int(rank) < int(name_data[name][year]):
            name_data[name][year] = rank

    # If the name hasn't existed in name data, the new name and its year as well as value should be stored in name data
    else:
        name_data[name] = {year: rank}


def add_file(name_data, filename):
    """
    Reads the information from the specified file and populates the name_data
    dict with the data found in the file.

    Input:
        name_data (dict): dict holding baby name data
        filename (str): name of the file holding baby name data

    Output:
        This function modifies the name_data dict to store information from
        the provided file name. This function does not return any value.
    """

    with open(filename, 'r') as f:
        row = 0  # Define the variable 'row' and its default value is 0

        for line in f:  # Loop over every row in the file
            name_list = line.split(',')  # Tokenize the CSV file as strings and store these string into a list

            if row == 0:  # The first row in the file is the year
                year = name_list[0].strip()
                row += 1  # Change to the next row after getting the year

            else:  # Data are sorted by rank, name1, and name2 after the first row
                rank = name_list[0].strip()

                name1 = name_list[1].strip()

                name2 = name_list[2].strip()

                # Add year, rank, and name1 into the dictionary "name_data"
                add_data_for_name(name_data, year, rank, name1)
                # Add year, rank, and name2 into the dictionary "name_data"
                add_data_for_name(name_data, year, rank, name2)




def read_files(filenames):
    """
    Reads the data from all files specified in the provided list
    into a single name_data dict and then returns that dict.

    Input:
        filenames (List[str]): a list of filenames containing baby name data

    Returns:
        name_data (dict): the dict storing all baby name data in a structured manner
    """

    name_data = {}  # Create an empty dictionary "name_data"

    for txt in filenames:  # Loop over every txt file in the list of filenames

        add_file(name_data, txt)  # Add year, rank, and name from each txt file into the dictionary "name_data"

    return name_data





def search_names(name_data, target):
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        name_data (dict): a dict containing baby name data organized by name
        target (str): a string to look for in the names contained within name_data

    Returns:
        matching_names (List[str]): a list of all names from name_data that contain
                                    the target string
    """

    # To make the input target string case-insensitive, it is necessary to create a new target string
    n_target = ''

    for ch in target:  # Loop over every character in the input target string
        n_target = n_target + ch.lower()  # Turn each character into lower case and store it in the new target string

    matching_names = []  # Create an empty list "matching_names"

    for name in name_data:  # Loop over every name in the dictionary "name_data"
        if n_target in name.lower():  # If a name contain the target string, add the name into the list "matching_names"
            matching_names.append(name)

    return matching_names




def print_names(name_data):
    """
    (provided, DO NOT MODIFY)
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
