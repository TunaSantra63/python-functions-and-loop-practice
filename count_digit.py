"""Count Digits 
Write a function count_digits(n) that counts the number of digits in a 
number. 
Restriction: Use a while loop. """


def count_digit(n):
    count = 0
    while n>0:
        digit = n % 10
        print(digit)
        n = n // 10
        count=count+1
    return count
    

n = int(input("Enter the number : "))
a = count_digit(n)
print(f"the count of the number is {a}")