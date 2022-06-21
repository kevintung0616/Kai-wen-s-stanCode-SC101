"""
File: webcrawler.py
Name: Kai-wen Tung
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #
        table = soup.find_all('tbody')[0].find_all('tr')

        lst = []  # Create a list to store data

        for row in table:  # Loop over every row in the website's table
            for td in row.find_all('td'):  # Loop over every character in the row
                lst.append(td.text)  # Store names and numbers in the list
            print(lst)

        boy_num = 0
        girl_num = 0

        for i in range(len(lst)):  # Loop over every index in the list
            if i % 5 == 2:  # The index of boys' number is 2
                boy = ''
                for ch in lst[i]:  # Loop over every character in each index of the list
                    if ch.isdigit():  # Only choose digits in the characters
                        boy = boy + ch  # Loop over each character in the Number of boys' name (which is a string)
                boy_num = boy_num + int(boy)  # Convert the strings into digits

            elif i % 5 == 4:  # The index of boys' number is 4
                girl = ''
                for ch in lst[i]:  # Loop over every character in each index of the list
                    if ch.isdigit():    # Only choose digits in the characters
                        girl = girl + ch    # Loop over each character in the Number of girls' name (string)
                girl_num = girl_num + int(girl)  # Convert the strings into digits

        print('Male Number:', boy_num)
        print('Female Number:', girl_num)


if __name__ == '__main__':
    main()
