
r =  int(input("enter range: "))
counter = 0

for i in range(1,r+1):
    while i > 0:
        digit = i%10
        if digit == 9:
            counter += 15
        i = i//10

print("no. of 9s are", counter)

