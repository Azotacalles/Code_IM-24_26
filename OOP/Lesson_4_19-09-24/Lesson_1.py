import datetime
print("\033c")


class Counter():
    "My class"

    def __init__(self):
        self.counter = 0

    def __call__(self):
        self.counter += 1

    def __str__(self):
        return f"Counter: {self.counter}"

    def __repr__(self):
        return str({"counter": self.counter})

    def __add__(self, value):
        if (isinstance(value, int)):
            self.counter += value
        elif (isinstance(value, Counter)):
            self.counter += value.counter
        return self

    # +=
    def __iadd__(self, value):
        # print("__iadd__")
        self.counter += value
        return self

    # int + object
    def __radd__(self, value):
        return self + value

    # >
    def __gt__(self, value):
        return self.counter > value.counter

    # <
    def __lt__(self, value):
        return self.counter < value.counter

    # ==
    def __eq__(self, value):
        return self.counter == value.counter

    # !=
    def __ne__(self, value):
        return self.counter != value.counter

    # <=
    def __le__(self, value):
        pass

    # >=
    def __ge__(self, value):
        pass


count = Counter()
count_2 = Counter()
count_2 += 50
count += 100

if (count > count_2):
    print(">")

if (count == count_2):
    print("==")

# count = count + count_2
# count = 50 + count
# print(count)

# count()
# print(count.counter)
# print(count)
# print(str(count))
# print(count.__repr__())

# data = datetime.datetime.now()
# print(data)
# print(data.__repr__())
