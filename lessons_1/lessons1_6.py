a = float(input("Введи а:"))
b = float(input("Введи b:"))

i=1
print(i,"-й день: ",a)

while a<b:
    a = a*1.1
    i=i+1
    print(i, "-й день: ", a)

