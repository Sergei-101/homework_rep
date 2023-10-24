# Игра угадай число

import random as rd
class GuessTheNumber:
    def __init__(self, lower_limit:int, upper_limit:int, number_of_attempts:int )->None:
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit
        self.number_of_attempts = number_of_attempts


    def game_number(self):
        num = rd.randint(self.lower_limit, self.upper_limit)
        count_num = 1
        while count_num <= self.number_of_attempts:
            a = int(input(f"{count_num})попытка Угадайте число от {self.lower_limit} до {self.upper_limit} c {self.number_of_attempts} попыток - "))
            if a == num:
                print(f"Вы победили угаданное число = {a}, вам понадобилось {count_num} попытки")
                break
            elif a > num:
                print(f"Введите число меньше {a}")
            elif a < num:
                print(f"Введите число больше {a}")
            count_num += 1
        else:
            print("Вы проиграли")

a = GuessTheNumber(1, 100, 15)
a.game_number()

