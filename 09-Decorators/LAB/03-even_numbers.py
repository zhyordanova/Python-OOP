def even_numbers(func):
    def wrapper(numbers):
        result = func(numbers)
        return [x for x in result if x % 2 == 0]

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))
