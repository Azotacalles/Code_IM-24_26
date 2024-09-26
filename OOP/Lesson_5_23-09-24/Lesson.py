from typing import *

number: int = 56

numbers1: List[int] = [1, 2, 3]
numbers2: list[str] = ["1", "2"]

tuple1: tuple[int, str] = (1, "4")
dict1: dict[str, int] = {"1": 1, "2": 2}
set1: set[int] = {1, 2, 3}

email: Optional[str] = None
id: Union[int, str] = 1

e: str | None = None
i: int | str = "4"

value: Any = 67


# функция
def test1(name: str) -> None:
    print(name)


def test2(n1: int, n2: int) -> int:
    return n1 + n2


def test3(id: int, /, name: str, *, level: int = 0):
    pass


# test3(100, "anna", level=10)


def test4(*args: int, **kwargs: str) -> None:
    print(args)
    print(kwargs)


# data = [1, 2, 3]
# print(*data)
# test4(1, 2, 3, name="oleg", id="567")


# Классы
class Car():
    color = "red"


class Person():
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def say(self, person: "Person"):
        print(f"Hello, {person.age}")

# p1 = Person("Elena", 67)
# p2 = Person("Olga", 65)
# c = Car()
# p1.say(c)


# Обобщения (Generic)

T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items: list[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

stack = Stack[int]()
stack.push(1)
stack.push(2)

str_stack = Stack[str]()
str_stack.push("1")
str_stack.push("2")
print(stack.items)


R = TypeVar("R", int, float)
def test5(a: R, b: R) -> R:
  return a + b

print(test5(1, 3))
print(test5(1.8, 9.8))
print(test5(89, 6.5))