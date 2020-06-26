print ("Podaj znak")
usr_inpt = input()

print ("Podaj wielkosc figury")
n = int(input())

i = 0
def triangle (a, b, i):
    # for i in range((b - 1)):
    #     print (a * (i + 1))
    #     pass,

    while b != i:
        print (a * (i + 1))
        i = i + 1
        pass


def square (a, b, i):
    for i in range(b):
        print (a * b)



def rectangle(a, b, i, j):
    for i in range(j):
        print (a * b)







print ("Trojkat z podanych informacji mozesz zobaczyc ponizej ")
triangle (usr_inpt, n, i)
print ("Kwadrat z podanych informacji mozesz zobaczyc ponizej ")
square (usr_inpt, n, i)
print ("Do prostokatu podaj jeszcze wysokosc ")
j = int(input())
rectangle (usr_inpt, n, i, j)