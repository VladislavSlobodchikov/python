import sys

num = input("enter the num: ")

max = int(-sys.maxsize)
print(type(max))
for n in num:
    z = int(n)
    if z>max:
        max=z

print(max)
