"""Reverse a Number 
Write a function reverse_number(n) that reverses a given number. 
Example: 
Input  : 12345 
Output : 54321 
Concepts: while, %, //"""



def reverse_number(n):
    rev = 0
    while n>0:
        a = n % 10
        rev = rev* 10 + a
        n = n // 10
    print(rev)
        
n = int(input("Enter the number : "))
reverse_number(n)
    
