from threading import Thread
import time

ENEMY = 100


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        count_day = 0
        for i in range(ENEMY, 0, -self.power):
            time.sleep(1)
            count_day += 1
            print(f'{self.name} сражается {count_day} , осталось {i} воинов.')
        print(f'{self.name} одержал победу спустя {count_day} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
