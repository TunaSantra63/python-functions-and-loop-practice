"""5. Sum of Natural Numbers 
Write a function sum_natural(n) that calculates the sum of numbers from 
1 to n. 
Restriction: Use a for loop. 
Example: 
Enter n: 10 
Sum = 55"""


def sum_natural(n):
    total = 0
    for _ in range(1,n+1):
        total = total+ _
    return total
n = int(input("Enter the n : "))
result = sum_natural(n)
print(f"The sum of the natural number is : {result}")
        