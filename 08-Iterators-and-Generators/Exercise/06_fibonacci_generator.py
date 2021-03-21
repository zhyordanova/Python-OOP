def fibonacci():
    previous_number, current_number = 0, 1
    while True:
        yield previous_number
        previous_number, current_number = current_number, previous_number + current_number


generator = fibonacci()
for i in range(5):
    print(next(generator))
