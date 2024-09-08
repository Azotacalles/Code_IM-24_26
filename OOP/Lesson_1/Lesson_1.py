class Figure():
    color = "blue"
    width = 10

    def __init__(self):
        self.fill = "black"


circle = Figure()
square = Figure()
triangle = Figure()
print(square.color)
square.color = "red"
Figure.color = "yellow"

Figure.fill = "white"
circle.fill = "pink"
print()
