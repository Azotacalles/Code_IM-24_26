import math


class Circle():
    unit = "cm"

    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    @classmethod
    def set_unit(cls, unit: str) -> None:
        cls.unit = unit

    @staticmethod
    def get_area(radius: float) -> float:
        return math.pi * radius ** 2


c1 = Circle(5)
print(round(c1.area(), 2))
c1.set_unit("m")
print(c1.unit)
Circle.set_unit("km")
r = c1.get_area(40)
print(r)


class Config():
    pass


data = {"host": "localhost",
        "port": 8000,
        "debug": True}

config = Config()
for k, v in data.items():
    setattr(config, k, v)

print(config.host)
if (hasattr(config, "debug")):
    delattr(config, "debug")
print(config.__dict__)
print(getattr(config, "test", "NO"))
