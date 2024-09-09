print("\033c")


class Car():
    "Это машина"
    name = "BMW"

    def __init__(self, model, speed=200, radio=True):
        self.color = "red"
        self.speed = speed
        self.model = model
        self.radio = radio

    def info(self, number):
        result = number * 2
        print(f"INFO: {self.color}, {self.name}")
        return result


car_1 = Car("RT-90")
car_2 = Car("UI-56", radio=False)
print(car_1.color)
car_2.color = "green"
print(car_2.color)
print(car_1.info(100))
car_2.info(200)


print()
