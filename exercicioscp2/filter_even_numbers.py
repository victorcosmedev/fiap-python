def filter_even_numbers(*numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers


numbers = [i for i in range(10)]
print(filter_even_numbers(*numbers))
