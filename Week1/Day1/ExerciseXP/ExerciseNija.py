#Exercise 1

3 <= 3 < 9 #true

3 == 3 == 3 #true

bool(0) #false

bool(5 == "5") #false

bool(4 == 4) == bool("4" == "4") #true

bool(bool(None)) #false

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)