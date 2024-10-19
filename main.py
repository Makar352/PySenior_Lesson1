print("Hello world!")
# Class клас предмета
# def __infinit__ опис
a = 2
b = "hello"
c = True
d = 2.2


class Marker:

    def __init__(self, color):
        self.color = color
        self.weight = 1.22
        self.price = 3
        self.isPresent = True

    def getInfo(self):
        print(f"{self.color}-{self.price}UAH")


blackMarker = Marker("black")
print(blackMarker.color)


redMarker = Marker("red")
print(redMarker.color)

