# Программа угадай число

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

a = GuessTheNumber(1, 10, 5)
a.game_number()


# 2. Задача про треугольники

class Triangle:
    def __init__(self, a:int, b:int, c:int)->None:
        self.a = a
        self.b = b
        self.c = c


    def triangle_true(self)->str:
        if self.a < self.b + self.c and self.b < self.a + self.c and self.c < self.a + self.b:
            if a == self.b == self.c:
                return ("Треугольник равносторонний")
            elif a == self.b or self.b == self.c or self.c == a:
                return ("Треугольник равнобедренный")
        else:
            return ("Треугольник не существует")


a = Triangle(6, 5, 5)
print(a.triangle_true())


# Задание кол-во встечаемых слов


text = """Универсальный фиксатор для бровей PÚSY Brow Fix PROFESSIONAL by Илона Дрожь —
это не только женская косметика класса люкс, но и новое слово в beauty индустрии.
"""


class WordFrequency:
    def __init__(self, word:str, word_frequency:int)->None:
        self.word = word
        self.word_frequency = word_frequency
    def word_count(self):
        for i in self.word:
            if i in ",.!:-—":
                self.word = self.word.replace(i, ' ')
        self.word = self.word.lower().split()
        res = {}
        for i in self.word:
            res[i] = self.word.count(i)
        res = sorted(res.items(), key=lambda item: item[1], reverse=True)
        for i in range(self.word_frequency):
            print(f"{res[i][0]} - встречяется {res[i][1]} раз")


a = WordFrequency(text, 5)
a.word_count()