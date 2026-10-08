row = int(input("enter the number of the row: "))

for i in range(1,row + 1):
    for j in range(0,i):
        print("*",end=" ")
    print("")  