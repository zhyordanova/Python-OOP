class countdown_iterator:
    def __init__(self, count):
        self.current_number = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_number < 0:
            raise StopIteration
        temp = self.current_number
        self.current_number -= 1
        return temp


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
