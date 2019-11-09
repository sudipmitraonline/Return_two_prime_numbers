#Given an even number (greater than 2), return two prime numbers whose sum will be equal to given number.
#@Author : Sudip Mitra
#Contact : 7003720931
#E-mail : sudipmitraonline@gmail.com

def findprime(y): #operation function
    if y == 2:
        return True
    elif y == 1 or y % 2 == 0:
        return False
    else:
        for j in range(3, int(y / 2)):
            if y % j == 0:
                return False
    return True

n = int(input("Enter the number of inputs to be given : "))
for i in range(0, n):
    x = int(input("Enter the number :"))
    for j in range(1, int(x / 2)):
        if (findprime(j) and findprime(x - j)):
            print("Result :" ,j, x - j)
            break
input()