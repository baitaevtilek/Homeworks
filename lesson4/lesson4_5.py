import random


num = random.randint(0, 10)
inp = int(input())

while inp != num:
    print("Неправильно")
    inp = int(input())