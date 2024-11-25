from collections import Counter

"""
Math functions
"""


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


def mod(a, b):
	return a % b


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


def cube_volume(side_length):
	return side_length ** 3


assert cube_volume(3) == 27
assert cube_volume(4) == 64
assert cube_volume(2) == 8


def cube_surface_area(side_length):
	return 6 * side_length ** 2


assert cube_surface_area(3) == 54
assert cube_surface_area(2) == 24
assert cube_surface_area(11) == 726


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


def triangle_perimeter(a, b, c):
	return a + b + c


assert triangle_perimeter(6, 5, 4) == 15
assert triangle_perimeter(2, 3, 5) == 10
assert triangle_perimeter(5, 6, 3) == 14


def triangle_area(a, h):
	return a * h / 2


assert triangle_area(10, 4) == 20
assert triangle_area(2, 4) == 4
assert triangle_area(12, 6) == 36


def is_correct_triangle(a, b, c):
	return a + b > c and a + c > b and b + c > a


assert is_correct_triangle(3, 4, 5) == True
assert is_correct_triangle(4, 6, 6) == True
assert is_correct_triangle(12, 6, 40) == False

"""
Physics functions
"""

# todo:add funcions


"""
String functions
"""


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


def get_str_from_list(str_):
	return " ".join(str_)


assert get_str_from_list(["Ania", "ma", "kajak"]) == "Ania ma kajak"
assert get_str_from_list(["pies", "i", "kot"]) == "pies i kot"
assert get_str_from_list(["To", "jest", "zdanie"]) == "To jest zdanie"

"""
List functions
"""


def reverse_list(lst):
	return lst[::-1]


assert reverse_list([1, 2, 3]) == [3, 2, 1]
assert reverse_list([1, 2, 3, 4]) == [4, 3, 2, 1]
assert reverse_list([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]


def is_in_list(item, lst):
	return item in lst


assert is_in_list(2, [1, 2, 3]) == True
assert is_in_list(5, [1, 2, 3, 4]) == False
assert is_in_list(5, [1, 2, 3, 4, 5]) == True

"""
Other functions
"""


def html_p(text):
	return f"<p>{text}</p>"


assert html_p("kajak") == "<p>kajak</p>"
assert html_p("pies") == "<p>pies</p>"
assert html_p("kot") == "<p>kot</p>"

"""
Codewars functions
"""


# https://www.codewars.com/kata/559d2284b5bb6799e9000047/train/python


def add_length(str_):
	return [f"{word} {len(word)}" for word in str_.split(" ")]


assert add_length("Hello World") == ["Hello 5", "World 5"]
assert add_length("apple ban") == ["apple 5", "ban 3"]
assert add_length("you will win") == ["you 3", "will 4", "win 3"]


# https://www.codewars.com/kata/54147087d5c2ebe4f1000805/train/python


def _if(bool_, func1, func2):
	if bool_:
		return func1()
	else:
		return func2()


assert _if(True, lambda: True, lambda: False) == True
assert _if(False, lambda: True, lambda: False) == False


# https://www.codewars.com/kata/57f222ce69e09c3630000212/train/python


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


# https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b/train/python


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


# https://www.codewars.com/kata/563b74ddd19a3ad462000054/train/python


def stringy(size):
	return "".join("1" if i % 2 == 0 else "0" for i in range(size))


assert stringy(6) == "101010"
assert stringy(4) == "1010"
assert stringy(12) == "101010101010"


# https://www.codewars.com/kata/5d5ee4c35162d9001af7d699/train/python


def sum_of_minimums(numbers):
	return sum(min(arr) for arr in numbers)


assert sum_of_minimums([[1, 2, 3, 4, 5], [5, 6, 7, 8, 9], [20, 21, 34, 56, 100]]) == 26
assert sum_of_minimums([[5, 8, 13, 4, 5], [5, 6, 7, 2, 9], [20, 4, 34, 56, 2]]) == 8
assert sum_of_minimums([[7, 2, 3, 4, 5], [23, 6, 4, 8, 9], [27, 21, 34, 56, 100]]) == 27


# https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python


def find_uniq(arr):
	counts = Counter(arr)

	for value, count in counts.items():
		if count == 1:
			return value


assert find_uniq(["a", "b", "b"]) == "a"
assert find_uniq(["a", "b", "b", "a", "c"]) == "c"
assert find_uniq(["a", "b", "a", "c", "c"]) == "b"


# https://www.codewars.com/kata/596c6eb85b0f515834000049/train/python


def replace_dots(s):
	return s.replace('.', '-')


assert replace_dots("Ala.ma.kota") == "Ala-ma-kota"
assert replace_dots("...") == "---"
assert replace_dots("Kot.ma.Ale") == "Kot-ma-Ale"


# https://www.codewars.com/kata/596c6eb85b0f515834000049/train/python


def digits(n):
	return len(str(n))


assert digits(1222) == 4
assert digits(12) == 2
assert digits(777666) == 6


# https://www.codewars.com/kata/565f5825379664a26b00007c/train/python


def get_size(w, h, d):
	return [2 * (w * h + w * d + h * d), w * h * d]


assert get_size(2, 2, 4) == [40, 16]
assert get_size(4, 5, 2) == [76, 40]
assert get_size(3, 5, 6) == [126, 90]


# https://www.codewars.com/kata/59dd3ccdded72fc78b000b25/train/python


def whatday(num):
	if 0 < num < 8:
		days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
		return days_of_week[num - 1]
	return "Wrong, please enter a number between 1 and 7"


assert whatday(4) == "Wednesday"
assert whatday(1) == "Sunday"
assert whatday(23) == "Wrong, please enter a number between 1 and 7"


# https://www.codewars.com/kata/59dd3ccdded72fc78b000b25/train/python


def reverse_words(st):
	return " ".join(st.split()[::-1])


assert reverse_words("Hello World") == "World Hello"
assert reverse_words("Ala ma Kota") == "Kota ma Ala"
assert reverse_words("Test revers") == "revers Test"


def gen_id():
	idx = 0

	def gen_next_id():
		nonlocal idx
		result = idx
		idx += 1
		return result

	return gen_next_id


id_generator = gen_id()

assert id_generator() == 0
assert id_generator() == 1
assert id_generator() == 2


# https://www.codewars.com/kata/580a094553bd9ec5d800007d


def apple(x):
	return "It's hotter than the sun!!" if int(
		x) ** 2 > 1000 else "Help yourself to a honeycomb Yorkie for the glovebox."


apple_true_result = "It's hotter than the sun!!"
apple_false_result = "Help yourself to a honeycomb Yorkie for the glovebox."

assert apple("2") == apple_false_result
assert apple(2) == apple_false_result
assert apple(40) == apple_true_result


def generate_hashtag(s):
	result = "".join(word.capitalize() for word in s.split())
	return "#" + result if result != "" and len(result) < 140 else False


assert generate_hashtag("") == False
assert generate_hashtag(
	"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et "
	"dolore magna aliqua. Ut enim ad minim veniam wiec hashtah bedzie za dlugi") == False
assert generate_hashtag("Hello World and Python") == "#HelloWorldAndPython"


# https://www.codewars.com/kata/5388f0e00b24c5635e000fc6/train/python

def swap_values(args):
	first_value = args[0]
	args[0] = args[1]
	args[1] = first_value


swap_values_test_list = ["a", "b"]

assert swap_values_test_list[0] == "a"
assert swap_values_test_list[1] == "b"
swap_values(swap_values_test_list)
assert swap_values_test_list[0] == "b"
assert swap_values_test_list[1] == "a"


# https://www.codewars.com/kata/534d0a229345375d520006a0/train/python

def power_of_two(x):
	exponent = 0
	while 2 ** exponent <= x:
		if 2 ** exponent == x:
			return True
		exponent += 1
	return False


assert power_of_two(0) == False
assert power_of_two(1) == True
assert power_of_two(4096) == True


# https://www.codewars.com/kata/5625618b1fe21ab49f00001f/train/python

def say_hello(name):
	return f"Hello, {name}"


assert say_hello("Anna") == "Hello, Anna"
assert say_hello("Adam") == "Hello, Adam"
assert say_hello("Michał") == "Hello, Michał"


# https://www.codewars.com/kata/539ee3b6757843632d00026b/train/python

def capitals(word):
	return [index for index, letter in enumerate(word) if letter.isupper()]


assert capitals("CodEWaRs") == [0, 3, 4, 6]
assert capitals("AMC") == [0, 1, 2]
assert capitals("Michał M") == [0, 7]


# https://www.codewars.com/kata/58cb43f4256836ed95000f97/train/python

def find_difference(a, b):
	(a1, b1, c1) = a
	(a2, b2, c2) = b
	return abs((a1 * b1 * c1) - (a2 * b2 * c2))


assert find_difference([3, 2, 5], [1, 4, 4]) == 14
assert find_difference([4, 2, 10], [1, 4, 4]) == 64
assert find_difference([2, 2, 5], [1, 2, 5]) == 10


# https://www.codewars.com/kata/545afd0761aa4c3055001386/train/python

def take(arr, n):
	return arr[:n]


assert take([3, 2, 5, 6, 7, 3, 1, 2], 3) == [3, 2, 5]
assert take([4, 2, 10], 2) == [4, 2]
assert take([2, 2, 5], 1) == [2]


# https://www.codewars.com/kata/53cf459503f9bbb774000003

class Python_class_cw:
	def __init__(self, name):
		self.name = name


named_python = Python_class_cw("Pajtonik")
assert named_python.name == "Pajtonik"


# https://www.codewars.com/kata/563a631f7cbbc236cf0000c2/train/python

def move(position, roll):
	return position + roll * 2


assert move(3, 6) == 15
assert move(0, 4) == 8
assert move(1, 5) == 11


# https://www.codewars.com/kata/57cfdf34902f6ba3d300001e/train/python

def two_sort(array):
	array.sort()
	return "***".join([letter for letter in array[0]])


assert two_sort(
	["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]) == "b***i***t***c***o***i***n"
assert two_sort(["turns", "out", "random", "test", "cases", "are", "easier", "than", "writing", "out", "basic",
				 "ones"]) == 'a***r***e'
assert two_sort(["lets", "talk", "about", "javascript", "the", "best", "language"]) == 'a***b***o***u***t'


# https://www.codewars.com/kata/582cb0224e56e068d800003c/train/python

def litres(time):
	return time // 2


assert litres(2) == 1
assert litres(1.4) == 0
assert litres(11.8) == 5


# https://www.codewars.com/kata/5583090cbe83f4fd8c000051
def digitize(n):
	return ([int(digit) for digit in str(n)])[::-1]


assert digitize(35231) == [1, 3, 2, 5, 3]
assert digitize(0) == [0]
assert digitize(23582357) == [7, 5, 3, 2, 8, 5, 3, 2]


# https://www.codewars.com/kata/545991b4cbae2a5fda000158/train/python

def include(arr, item):
	return item in arr


assert include(["a", "b", "c"], "a") == True
assert include(["a", "b", "c"], "b") == True
assert include(["a", "b", "c"], "d") == False


def string_clean(s):
	return "".join([letter for letter in s if letter not in "0123456789"])


assert string_clean("Te11st23") == "Test"
assert string_clean("123next34Test") == "nextTest"
assert string_clean("clear324Stri412ng") == "clearString"


# https://www.codewars.com/kata/5933a1f8552bc2750a0000ed/train/python

def nth_even(n):
	return (n - 1) * 2


assert nth_even(1) == 0
assert nth_even(2) == 2
assert nth_even(3) == 4


# https://www.codewars.com/kata/5963c18ecb97be020b0000a2/train/python

def derive(coefficient, exponent):
	return f"{coefficient * exponent}x^{exponent - 1 if exponent != 2 else exponent}"


assert derive(7, 8) == "56x^7"
assert derive(5, 9) == "45x^8"
assert derive(5, 2) == "10x^2"


# https://www.codewars.com/kata/56f695399400f5d9ef000af5/train/python

def correct_tail(body, tail):
	return body[-1] == tail


assert correct_tail("Fox", "x") == True
assert correct_tail("Rhino", "o") == True
assert correct_tail("Meerkat", "t") == True


# https://www.codewars.com/kata/570597e258b58f6edc00230d/train/python

def array(string):
	return " ".join(string.split(','))[1:-1].strip() if len(string.split(",")) > 2 else None


assert array('1,2,3') == '2'
assert array('1,2') is None
assert array('1,2,3,4,5') == '2 3 4'


# https://www.codewars.com/kata/57241e0f440cd279b5000829/train/python

# def sum_mul(n, m): todo: fix that
# 	if n >= m:
# 		return "INVALID"
#
# 	result = 0
# 	count  = 1
#
# 	while n * count <= m:
# 		result += n * count
# 		count += 1
# 	return result
#
#
#
# assert sum_mul(0, 0) == 'INVALID'
# assert sum_mul(2, 9) == 20
# assert sum_mul(4, -7) == 'INVALID'
# assert sum_mul(4, 123) == 1860


# https://www.codewars.com/kata/57a049e253ba33ac5e000212/train/python

def factorial(n):
	if n in (0, 1):
		return 1
	return n * factorial(n - 1)


assert factorial(2) == 2
assert factorial(3) == 6
assert factorial(4) == 24


# https://www.codewars.com/kata/56e2f59fb2ed128081001328/train/python

def print_array(arr):
	return ",".join(map(str, arr))


assert print_array([1, 2, 3]) == "1,2,3"
assert print_array([4, 5, 6, 7]) == "4,5,6,7"
assert print_array([8, 9]) == "8,9"


# https://www.codewars.com/kata/56f6919a6b88de18ff000b36/train/python

def how_many_dalmatians(n):
	dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]

	response = dogs[0] if n <= 10 else dogs[1] if (n <= 50) else dogs[3] if n == 101 else dogs[2]
	return response


assert how_many_dalmatians(100) == "Woah that's a lot of dogs!"
assert how_many_dalmatians(50) == "More than a handful!"
assert how_many_dalmatians(10) == "Hardly any"
assert how_many_dalmatians(101) == "101 DALMATIONS!!!"


# https://www.codewars.com/kata/56a3f08aa9a6cc9b75000023/train/python

def validate_usr(username):
	if 4 <= len(username) < 17:
		return all((char.isalpha() and char.islower()) or char.isdigit() or char == '_' for char in username)
	return False


assert validate_usr('p1pp1') == True
assert validate_usr('asd43 34') == False
assert validate_usr('asd43_34') == True


# https://www.codewars.com/kata/5641a03210e973055a00000d/train/python

def two_decimal_places(n):
	return round(n, 2)


assert two_decimal_places(4.659725356) == 4.66
assert two_decimal_places(173735326.3783732637948948) == 173735326.38
assert two_decimal_places(4.653725356) == 4.65


# https://www.codewars.com/kata/55902c5eaa8069a5b4000083/train/python


def format_money(amount):
	return f"${amount:.2f}"


assert format_money(0) == '$0.00'
assert format_money(39.99) == '$39.99'
assert format_money(81) == '$81.00'


def generate_range(start, stop, step):
	return list(range(start, stop + 1, step))


assert generate_range(1, 10, 1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert generate_range(-10, 1, 1) == [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1]
assert generate_range(1, 15, 20) == [1]
assert generate_range(1, 7, 2) == [1, 3, 5, 7]


# https://www.codewars.com/kata/55d277882e139d0b6000005d/train/python duplicat metody avr

def find_average(nums):
	return sum(nums) / len(nums) if nums else 0


assert find_average([1, 3, 5, 7]) == 4
assert find_average([-1, 3, 5, -7]) == 0
assert find_average([5, 7, 3, 7]) == 5.5


# https://www.codewars.com/kata/5dd462a573ee6d0014ce715b/train/python

def same_case(a, b):
	if a.isalpha() and b.isalpha():
		return 1 if (a.islower() and b.islower()) or (a.isupper() and b.isupper()) else 0
	return -1


assert same_case('d', 'd') == 1
assert same_case('A', 's') == 0
assert same_case('\t', 'Z') == -1


# https://www.codewars.com/kata/57a5b0dfcf1fa526bb000118/train/python

def distinct(seq):
	result = []
	for elem in seq:
		if elem not in result:
			result.append(elem)
	return result


assert distinct([1, 2]) == [1, 2]
assert distinct([1, 1, 2]) == [1, 2]
assert distinct([1, 1, 1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]