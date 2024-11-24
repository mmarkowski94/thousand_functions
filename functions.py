from collections import Counter


def add(a, b):
	return a + b


assert add(3, 3) == 6
assert add(0, 4) == 4
assert add(1, 6) == 7


def sum_list(numbers):
	return sum(numbers)


assert sum_list([2, 3, 7]) == 12
assert sum_list([4, 5, 8]) == 17
assert sum_list([1, 1, 1]) == 3


def subtract(a, b):
	return a - b


assert subtract(10, 3) == 7
assert subtract(18, 14) == 4
assert subtract(11, 6) == 5


def multiply(a, b):
	return a * b


assert multiply(4, 2) == 8
assert multiply(2, 3) == 6
assert multiply(4, 6) == 24


def divide(a, b):
	return a / b


assert divide(6, 3) == 2
assert divide(14, 7) == 2
assert divide(6, 6) == 1


def avg(numbers):
	return sum(numbers) / len(numbers) if numbers else 0


assert avg([1, 2, 3]) == 2.0
assert avg([2, 8, 5]) == 5.0
assert avg([1, 9, 2]) == 4.0

assert avg([1, 2, 3]) == 2.0
assert avg([2, 8, 5]) == 5.0
assert avg([1, 9, 2]) == 4.0


def avg_positive_numbers(numbers):
	positive_numbers = [number for number in numbers if number > 0]
	return sum(positive_numbers) / len(positive_numbers)


assert avg_positive_numbers([-1, 2, 3]) == 2.5
assert avg_positive_numbers([2, 0, 5]) == 3.5
assert avg_positive_numbers([1, 9, -2]) == 5.0


def avg_negative_numbers(numbers):
	negative_numbers = [number for number in numbers if number < 0]
	return sum(negative_numbers) / len(negative_numbers)


assert avg_negative_numbers([-1, 2, -3]) == -2.0
assert avg_negative_numbers([2, -4, -5]) == -4.5
assert avg_negative_numbers([-1, 9, -2]) == -1.5


def calculate_power(base, exponent):
	return base ** exponent


assert calculate_power(3, 3) == 27
assert calculate_power(2, 2) == 4
assert calculate_power(2, 4) == 16


def power_factory(base):
	def inner(exponent):
		return base ** exponent

	return inner


power2 = power_factory(2)
power3 = power_factory(3)
power4 = power_factory(4)

assert power2(3) == 8
assert power3(4) == 81
assert power4(2) == 16


def sqrt(number):
	return number ** 0.5


assert sqrt(9) == 3
assert sqrt(16) == 4
assert sqrt(25) == 5


def get_max_number(numbers):
	return max(numbers)


assert get_max_number([2, 3, 7]) == 7
assert get_max_number([4, 5, 8]) == 8
assert get_max_number([1, 1, 1]) == 1


def get_min_number(numbers):
	return min(numbers)


assert get_min_number([2, 3, 7]) == 2
assert get_min_number([4, 5, 8]) == 4
assert get_min_number([1, 1, 1]) == 1


def calculate_min_and_max_difference(numbers):
	return max(numbers) - min(numbers)


assert calculate_min_and_max_difference([2, 3, 7]) == 5
assert calculate_min_and_max_difference([4, 5, 8]) == 4
assert calculate_min_and_max_difference([1, 1, 1]) == 0


def is_positive_number(number):
	return number > 0


assert is_positive_number(6) == True
assert is_positive_number(0) == False
assert is_positive_number(-3) == False


def is_negative_number(number):
	return number < 0


assert is_negative_number(-45) == True
assert is_negative_number(0) == False
assert is_negative_number(5) == False


def is_even_number(number):
	return number % 2 == 0


assert is_even_number(22) == True
assert is_even_number(51) == False
assert is_even_number(7) == False


def is_odd_number(number):
	return number % 2 != 0


assert is_odd_number(11) == True
assert is_odd_number(6) == False
assert is_odd_number(4) == False


def square_perimeter(side_length):
	return side_length * 4


assert square_perimeter(3) == 12
assert square_perimeter(7) == 28
assert square_perimeter(6) == 24


def square_area(side_length):
	return side_length ** 2


assert square_area(3) == 9
assert square_area(8) == 64
assert square_area(11) == 121


def rectangle_perimeter(side_length, side_height):
	return (side_height + side_length) * 2


assert rectangle_perimeter(3, 6) == 18
assert rectangle_perimeter(4, 3) == 14
assert rectangle_perimeter(2, 1) == 6


def rectangle_area(side_length, side_height):
	return side_length * side_height


assert rectangle_area(3, 6) == 18
assert rectangle_area(4, 3) == 12
assert rectangle_area(2, 1) == 2


def circle_perimeter(r):
	return 2 * 3.14 * r


assert circle_perimeter(1) == 6.28
assert circle_perimeter(2) == 12.56
assert circle_perimeter(4) == 25.12


def circle_area(r):
	return 3.14 * r ** 2


assert circle_area(1) == 3.14
assert circle_area(2) == 12.56
assert circle_area(4) == 50.24


def upper_first_letter(name):
	return name.capitalize()


assert upper_first_letter("piotr") == "Piotr"
assert upper_first_letter("ania") == "Ania"
assert upper_first_letter("rafał") == "Rafał"


def get_first_letter(word):
	return word[0]


assert get_first_letter("piotr") == "p"
assert get_first_letter("marta") == "m"
assert get_first_letter("rafał") == "r"


def get_last_letter(word):
	return word[-1]


assert get_last_letter("piotr") == "r"
assert get_last_letter("marta") == "a"
assert get_last_letter("rafał") == "ł"


def get_letter_by_index(word):
	def inner(index):
		return word[index]

	return inner


get_letters = get_letter_by_index("Sławomir")

assert get_letters(0) == "S"
assert get_letters(4) == "o"
assert get_letters(-1) == "r"


def reverse(coll):
	return coll[::-1]


assert reverse("kot") == "tok"
assert reverse("pies") == "seip"
assert reverse("ryba") == "abyr"


def is_palindrome(word):
	return word.lower() == word.lower()[::-1]


assert is_palindrome("kajak") == True
assert is_palindrome("pies") == False
assert is_palindrome("Anna") == True

"""
https://www.codewars.com/kata/559d2284b5bb6799e9000047/train/python
"""


def add_length(str_):
	return [f"{word} {len(word)}" for word in str_.split(" ")]


assert add_length("Hello World") == ["Hello 5", "World 5"]
assert add_length("apple ban") == ["apple 5", "ban 3"]
assert add_length("you will win") == ["you 3", "will 4", "win 3"]

"""
https://www.codewars.com/kata/54147087d5c2ebe4f1000805/train/python
"""


def _if(bool_, func1, func2):
	if bool_:
		return func1()
	else:
		return func2()


assert _if(True, lambda: True, lambda: False) == True
assert _if(False, lambda: True, lambda: False) == False

"""
https://www.codewars.com/kata/57f222ce69e09c3630000212/train/python
"""


def well(x):
	good_ideas = x.count('good')
	if good_ideas > 2:
		return "I smell a series!"
	if good_ideas > 0:
		return "Publish!"
	return "Fail!"


assert well(['bad', 'bad', 'bad']) == "Fail!"
assert well(['good', 'bad', 'bad', 'bad', 'bad']) == "Publish!"
assert well(['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']) == "I smell a series!"

"""
https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b/train/python
"""


def human_years_cat_years_dog_years(human_years):
	if human_years == 1:
		return [human_years, 15, 15]
	elif human_years == 2:
		return [human_years, 24, 24]

	years_to_multiply = (human_years - 2)
	return [human_years, 24 + years_to_multiply * 4, 24 + years_to_multiply * 5]


assert human_years_cat_years_dog_years(1) == [1, 15, 15]
assert human_years_cat_years_dog_years(2) == [2, 24, 24]
assert human_years_cat_years_dog_years(5) == [5, 36, 39]

"""
https://www.codewars.com/kata/563b74ddd19a3ad462000054/train/python
"""


def stringy(size):
	return "".join("1" if i % 2 == 0 else "0" for i in range(size))


assert stringy(6) == "101010"
assert stringy(4) == "1010"
assert stringy(12) == "101010101010"

"""
https://www.codewars.com/kata/5d5ee4c35162d9001af7d699/train/python
"""


def sum_of_minimums(numbers):
	return sum(min(arr) for arr in numbers)


assert sum_of_minimums([[1, 2, 3, 4, 5], [5, 6, 7, 8, 9], [20, 21, 34, 56, 100]]) == 26
assert sum_of_minimums([[5, 8, 13, 4, 5], [5, 6, 7, 2, 9], [20, 4, 34, 56, 2]]) == 8
assert sum_of_minimums([[7, 2, 3, 4, 5], [23, 6, 4, 8, 9], [27, 21, 34, 56, 100]]) == 27

"""
https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python
"""


def find_uniq(arr):
	counts = Counter(arr)

	for value, count in counts.items():
		if count == 1:
			return value


##todo:assercje

"""
https://www.codewars.com/kata/596c6eb85b0f515834000049/train/python
"""


def replace_dots(s):
	return s.replace('.', '-')


assert replace_dots("Ala.ma.kota") == "Ala-ma-kota"
assert replace_dots("...") == "---"
assert replace_dots("Kot.ma.Ale") == "Kot-ma-Ale"

"""
https://www.codewars.com/kata/596c6eb85b0f515834000049/train/python
"""


def digits(n):
	return len(str(n))


assert digits(1222) == 4
assert digits(12) == 2
assert digits(777666) == 6

"""
https://www.codewars.com/kata/565f5825379664a26b00007c/train/python
"""


def get_size(w, h, d):
	return [2 * (w * h + w * d + h * d), w * h * d]


##todo:assercje

"""
https://www.codewars.com/kata/59dd3ccdded72fc78b000b25/train/python
"""


def whatday(num):
	if 0 < num < 8:
		days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
		return days_of_week[num - 1]
	return "Wrong, please enter a number between 1 and 7"


assert whatday(4) == "Wednesday"
assert whatday(1) == "Sunday"
assert whatday(23) == "Wrong, please enter a number between 1 and 7"

"""
https://www.codewars.com/kata/59dd3ccdded72fc78b000b25/train/python
"""


def reverse_words(st):
	return " ".join(st.split()[::-1])


##todo:assercje


def gen_id():
	idx = 0

	def gen_next_id():
		nonlocal idx
		result = idx
		idx += 1
		return result

	return gen_next_id


"""
https://www.codewars.com/kata/580a094553bd9ec5d800007d
"""


def apple(x):
	return "It's hotter than the sun!!" if int(
		x) ** 2 > 1000 else "Help yourself to a honeycomb Yorkie for the glovebox."


##todo assercje

def generate_hashtag(s):
	result = "".join(word.capitalize() for word in s.split())
	return "#" + result if result != "" and len(result) < 140 else False


##todo assercje


# https://www.codewars.com/kata/5388f0e00b24c5635e000fc6/train/python

def swap_values(args):
	first_value = args[0]
	args[0] = args[1]
	args[1] = first_value
# return args
