""" Prime Number 
Write a function check_prime(n) that checks whether a number is prime. 
Restriction: Use a loop and do not use any external library."""


def check_prime(n):
    if n<=1:
        return False
    for _ in range(2, n):
        if (n % _ == 0):
            return False
    return True

n = int(input("Enter the number : "))
result = check_prime(n)
if result:
    print(f"It is a prime number")
else : 
    print(f"It is not a prime number")
