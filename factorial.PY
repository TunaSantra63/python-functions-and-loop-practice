""" Factorial Using Function 
Write a function factorial(n) that calculates the factorial of a number. 
Restriction: Use a loop. Do not use recursion. """


def factorial(n):
    fact = 1
    for _ in range(1,n+1):
        fact = fact*_
    return fact
    

n = int(input("Enter the number : "))
result=factorial(n)
print(f"The factorial of {n} is {result}")