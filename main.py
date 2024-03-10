# # # try:
# # #     a = int(input("a = "))
# # #     b = int(input("b = "))
# # #     result = a/b
# # # except ZeroDivisionError:
# # #     print("Can't divide by zero")
# # # except ValueError:
# # #     print("Please enter an integer")
# # # else:
# # #     print(result)
# #
# # arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# #
# # l1 = [3**i for i in range(1, 6)]
# # l2 = [i**2 for i in arr]
# # l3 = [i for i in arr if i % 2 == 0]
# # l4 = [(x, y) for x in l2 for y in l3]
# # l5 = []
# # for i in l1:
# #     for j in l2:
# #         l5.append((i, j))
# # print(l1, l2, l3, l4, l5, sep="\n")
#
# s1 = {'a': 1, 'b': 2, 'c': 4}
# s2 = {}
# for key, value in s1.items():
#     s2[value] = key
#
# s3 = {v: k for k, v in s1.items()}
#
# print(s1, s2, s3, sep="\n")

# def rownanie_kwadratowe(a, b, c):
#     delta = b**2 - 4*a*c
#     if delta < 0:
#         print('Brak pierwiastkow')
#         return 0
#     elif delta == 0:
#         x = (-b / 2*a)
#         print('x = ', x)
#         return x
#     elif delta > 0:
#         x1 = (-b + math.sqrt(delta)) / (2*a)
#         x2 = (-b - math.sqrt(delta)) / (2*a)
#         print('x1 = ', x1)
#         print('x2 = ', x2)
#         return x1, x2
#
# print(rownanie_kwadratowe(3, 4, 5))
# print(rownanie_kwadratowe(4, 5, 2))
# print(rownanie_kwadratowe(1, -5, 1))


# def dlugosc_odcinka(x1=1, x2=2, y1=3, y2=4):
#     return math.sqrt((x1-x2)**2 + (y1-y2)**2)
#
# plik = open("plik.txt", "r", encoding='utf-8')
# znak = plik.read(10)
# linia = plik.readline()
# wszystko = plik.readlines()
# plik.close()
#
# print(znak, linia, wszystko, sep="\n")

# plik = open("plik.txt", "a", encoding='utf-8')
# plik.write("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
# plik.close()

# with open("plik.txt", "r", encoding='utf-8') as f:
#     for line in f.readlines():
#         print(line)


# Zad 1
A = [1-x for x in range(1, 11)]
B = [4**x for x in range(0, 8)]
C = {x for x in B if x % 2 == 0}

# Zad 2
import random
lista1 = random.sample(range(1, 1000), 10)
parzysta_lista = [x for x in lista1 if x % 2 == 0]

# Zad 3
produkty = {"mleko": "ml", "jajka": "szt", "masło": "g", "ser": "dg"}
lista2 = {value: key for key, value in produkty.items()}\

# Zad 4
def prostakotny(a, b, c):
    if a >= b and a >= c:
        if a**2 == (b**2 + c**2):
            return True
    elif b >= a and b >= c:
        if b ** 2 == (a ** 2 + c ** 2):
            return True
    elif c >= a and c >= b:
        if c ** 2 == (b ** 2 + a ** 2):
            return True
    return False


# Zad 5
def pole_trapeza(a=1, b=1, h=1):
    return ((a+b)/2) * h

# Zad 6
def iloczyn_ciagu(a=1, b=4, ile=10):
    iloczyn = 1
    for i in range(a, ile+1):
        iloczyn *= b
    return iloczyn

# Zad 7
import math
def pierwiastek(num):
    try:
        math.sqrt(num)
    except ValueError:
        print("Nie można obliczyć pierwiastka z ujemnej wartości")


