#  write a program to accept marks of 6 student and display them in a store d manner.

mark = []

f1 = int(input("Enter the first student marks : "))
mark.append(f1)

f2 = int(input("Enter the second student marks : "))
mark.append(f2)

f3 = int(input("Enter the third student marks : "))
mark.append(f3)

f4 = int(input("Enter the forth student marks : "))
mark.append(f4)

f5 = int(input("Enter the fifth student marks : "))
mark.append(f5)

f6 = int(input("Enter the sisth student marks : "))
mark.append(f6)

mark.sort()

print(mark)


