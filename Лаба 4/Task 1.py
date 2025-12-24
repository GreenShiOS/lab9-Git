import math
from datetime import datetime

num = int(input("Введите число: "))
print(f"Квадратный корень из {num} = {math.sqrt(num)}")
print("Сейчас:", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))