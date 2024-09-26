# class Car():

#     def __init__(self):
#         self.color = "red"
#         self.speed = 100


# car_1 = Car()
# print(car_1.__dict__)
print("\033c")

item = {"name": "Zina", "age": 17}
print(item["name"])
item["length"] = 180
print(item["length"])

car = {"model": "lada",
       "age": 50,
       "color": ["red", "green", "pink"],
       10: "ten",
       (1, 2, 3): 1234}

for key in car.keys():
    print(key, end=" ")
print()
for value in car.values():
    print(value, end=" ")
print()
for key, value in car.items():
    print(f"{key} : {value}")

car["age"] = 51
print(car["age"])
car["age"] += 10
print(car["age"])
print(car[(1, 2, 3)])
print(car.get("ahjdg", False))

print(car.pop("model"))
print(car)
del car["age"]
print(car)


for k, v in car.items():
    if (v == "ten"):
        del car[k]
        break
print(car)

d1 = {"apple": 10,
      "orange": 45,
      "banana": 5}

sorted_d1 = dict(sorted(d1.items(),
              key=lambda item: item[1]))
print(sorted_d1)
