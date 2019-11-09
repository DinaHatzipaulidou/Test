# -------------------------------------------
# NOTE: ex9
# CLASSES
# -------------------------------------------
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

p = Point(3,5)
print(p.x)
print(p.y)

# -------------------------------------------
# NOTE: ex8
# FUNCTIONS
# opou {} pairnei timi apo to format(,)
# orismena me kommata opou oses {}
# toses variables prepei na peraseis
# mesa sto format()
# RESULT
# 0 keimeno 0 is 0
# 1 keimeno 1 is 1
# 2 keimeno 2 is 4
# 3 keimeno 3 is 9
# 4 keimeno 4 is 16
# 5 keimeno 5 is 25
# 6 keimeno 6 is 36
# 7 keimeno 7 is 49
# 8 keimeno 8 is 64
# 9 keimeno 9 is 81
# -------------------------------------------
# def square(x): # NOTE: def new funtion
#     return x * x
#     pass
#
# def main():
# # NOTE: otan kaleitai apo allo
# # arxeio auto to simeio den tha ektlestei
# # para mono otan use to idio to arxeio edo.
# # px
# # python a.py
# # 0 keimeno 0 is 0
# # 1 keimeno 1 is 1
# # klp
# # eno otan tin kaleseis apo to b.py
# # 100
#     for i in range(10):
#         print("{} keimeno {} is {}".format(i,i,square(i)))
#         pass
# # NOTE: ayto to kanei na use meros
# # ton functions
# if __name__ == "__main__":
#     main()
#

# -------------------------------------------
# NOTE: ex7
# Dictionaries
# {'Dina': 23, 'Bob': 27, 'Charlies': 30}
# -------------------------------------------
# ages = {"Dina":22, "Bob":27}
# ages["Charlies"] = 30
# ages["Dina"] +=1
# print(ages)
# -------------------------------------------
# NOTE: ex6
# set dhmioyria lista opoy den bazei idia
# stoixeia an ta briskei. px to 3 den
# tha to xanabalei
# bazei mono unique items
# {1, 3, 5}
# -------------------------------------------
# s = set()
# s.add(1)
# s.add(3)
# s.add(5)
# s.add(3)
# print(s)
# -------------------------------------------
# NOTE: ex5
# Dina
# Bob
# James
# -------------------------------------------
# i = ["Dina","Bob","James"]
# for name in i:
#     print(name)
#     pass

# -------------------------------------------
# NOTE: ex4
# -------------------------------------------
# string variable
# name = "Dina Aloxa"
# # px sintentagmenes
# coordinates = (10.0, 20.0)
# # List Variable
# names = ["Dina Aloxa", "Bob Marley", "James Dean"]
# print(names)
#
# -------------------------------------------
# NOTE: ex3
# -------------------------------------------
# x = 28
# print(x)
# if x > 0:
#     print("x is positive")
# elif x < 0:
#     print("x is negative")
# else:
#     print("x is zero")
#     pass

# -------------------------------------------
# NOTE: ex2
# -------------------------------------------
# i = 28
# print(f"i is {i}")
#
# f = 2.8
# print(f"f is {f}")
#
# b = True
# print(f"b is {b}")
#
# n = None
# print(f"n is {n}")

# -------------------------------------------
# NOTE: ex1 (ex=example)
# -------------------------------------------
# name = input()
# print(f"Hello World, {name}!")
