class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self):
        result = (self._length * self._width * 25 * 5) / 1000
        print(f"Масса асфальта, необходимого для покрытия всей дороги: {result} тонн")


my_road = Road(20, 5000)
my_road.mass()
