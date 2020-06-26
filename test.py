# import math
# lista = ["jeden", "dwa", 3]
# print (lista)
# lista.insert(2,"adam")
# print (lista)

# krotka =  20202, "text", 31.53
# print (krotka)

# def f(x):
#     if (x % 2 != 0 and x % 3 != 0):
#         return x
#     else:
#         pass
# filter(f, range(2,36))


# tab = [["*"] * 7] * 4
# print (tab)

# w, h = 2, 3
# tab_2 = [[None] * w for i in range(h)]

# import numpy
# fa = numpy.array([1, 2, 3])
# print (fa)




# import numpy
# from numpy.random import rand
# tab = numpy.array([[1, 2, 3, 4, 5, 6, 7],
# [1, 2, 3, 4, 5, 6, 7],
# [1, 2, 3, 4, 5, 6, 7],
# [1, 2, 3, 4, 5, 6, 7]])

# # for g in tab:
# #     print (g)
# print (tab)
# rndm = rand(4, 4) * 50
# print (rndm)





# print ("Podaj znak")
# usr_inpt = input()

# print ("Podaj wielkosc figury")
# n = int(input())

# i = 0
# def triangle (a, b, i):
#     # for i in range((b - 1)):
#     #     print (a * (i + 1))
#     #     pass,

#     while b != i:
#         print (a * (i + 1))
#         i = i + 1
#         pass

# def square (a, b, i):
#     for i in range(b):
#         print (a * b)

# def rectangle(a, b, i, j):
#     for i in range(j):
#         print (a * b)

# print ("Trojkat z podanych informacji mozesz zobaczyc ponizej ")
# triangle (usr_inpt, n, i)
# print ("Kwadrat z podanych informacji mozesz zobaczyc ponizej ")
# square (usr_inpt, n, i)
# print ("Do prostokatu podaj jeszcze wysokosc ")
# j = int(input())
# rectangle (usr_inpt, n, i, j)


# with open("plik123.txt", "r", -1, "utf-8") as file:
#     lines = file.readlines()
#     for line in lines:
#         print(line)


# import os
# print(os.getcwd())
# print(list(os.listdir()))
# print (os.path.getsize("test.py"))

# import time
# f = open("plik123.txt", "w")
# f.write("lul")
# f.close()
# print(time.ctime(os.path.getctime("plik123.txt"))) #data utworzenia pliku
# print(time.ctime(os.path.getmtime("plik123.txt"))) #data modyfikacji pliku

# os.mkdir("folder")
# if os.path.exists("folder"):
#     print("istnieje")

# import tkinter
# import turtle
# turtle.pensize(15)
# angle = 70
# multiple = 200
# turtle.speed(50)

# for i in range(multiple):
#     turtle.pencolor((i/multiple, (multiple - i) / multiple, 0))
#     turtle.forward(i)
#     turtle.circle(i, angle)


# for char in 'magic':
#     print(char)





# word = input()
# let_num = 0
# for _let in word:
#     if word[let_num] == word[-let_num - 1]:
#         if let_num == (len(word) - 1):
#             print("Palindrome")
#         else:
#             pass
#     else:
#         print("Not palindrome")
#         break
#     let_num += 1 



# def cafe_split(cafe):               #Each string contains a café's name followed by a space and the number of cats in it, e.g. Paws 11, Kittens 9.
#     return cafe.split()             #The names would be one-word only. Read input lines until you get a string MEOW (without any number).
#                                     #The café with the maximum number of cats.

# cats_biggest = 0
# while True:
#     cafe_name = input()
#     if cafe_name == "MEOW":
#         break
    
#     cafe_name = cafe_split(cafe_name)
#     cats_current = int(cafe_name[1])
#     if cats_biggest < cats_current:
#         cats_biggest = cats_current
#         cafe_biggest_name = cafe_name[0]
#     else:
#         pass
# print(cafe_biggest_name)



# income = int(input())
# if income < 15527:
#     percent = 0
#     calculated_tax = round((income * (percent / 100)))
# elif income <= 42707:
#     percent = 15
#     calculated_tax = round((income * (percent / 100)))
# elif income <= 132406:
#     percent = 25
#     calculated_tax = round((income * (percent / 100)))
# else:
#     percent = 28
#     calculated_tax = round((income * (percent / 100)))
# print(f'The tax for {income} is {percent}%. That is {calculated_tax} dollars!')



# class RockBand:
#     genre = "rock"
#     key_instruments = ["electric guitar", "drums"]
#     n_members = 4

# guns_roses = RockBand()
# print(getattr(guns_roses, 'genre'))
# print(getattr(guns_roses, 'key_instruments'))
# print(getattr(guns_roses, 'n_members'))


class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        self.id = str(name[0]) + str(last_name) + str(birth_year)  # calculate the id here
student1 = Student("Daniel", "Smith", 1993)
print(student1.id)





