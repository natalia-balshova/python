from itertools import cycle
from time import sleep
from colorama import Fore


class TrafficLight:
    __color = ['красный', 'желтый', 'зеленый', 'желтый']

    def running(self):
        i = 0
        for light_color in cycle(self.__color):
            if i > 12:
                break
            elif light_color == 'красный':
                print(Fore.RED + light_color)
                sleep(7)
            elif light_color == 'зеленый':
                print(Fore.GREEN + light_color)
                sleep(7)
            else:
                print(Fore.YELLOW + light_color)
                sleep(2)
            i += 1


a = TrafficLight()
a.running()
