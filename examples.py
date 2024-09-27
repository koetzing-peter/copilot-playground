# Create a list of 100 numbers
numbers = list(range(1, 101))


def get_even_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers
