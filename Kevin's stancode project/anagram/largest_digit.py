"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:
	:return:
	"""
	# Make all integer positive
	if n < 0:
		n = -n

	first_digit = n % 10  # first_digit is the units digit, which is the remainder of 10

	n = (n - first_digit)//10  # Remove the units digit

	next_digit = n % 10  # next_digit is the tens digit, which is the remainder of 10 after removing the units digit

	if n > 0:
		if first_digit > next_digit:  # If the units digit is greater than the tens digit, it will replace the tens digits
			n = n - next_digit + first_digit
			return find_largest_digit(n)  # Recursion

		else:
			n = n  # This code is redundant but can help me understand that n will remain unchanged if first_digit <= next_digit
			return find_largest_digit(n)  # Recursion

	else:  # Base case
		if first_digit > next_digit:
			return first_digit

		else:
			return next_digit


if __name__ == '__main__':
	main()
