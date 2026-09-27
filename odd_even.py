"""Even or Odd 
Write a function check_even_odd(n) that accepts a number and prints 
whether the number is even or odd. 
Concepts: function, if-else, %"""



def check_even_odd (n):
    if (n % 2 == 0):
        print("It is a Even number")
    else:
        print("It is a Odd number")
        
n = int(input("Enter the number : "))
check_even_odd(n)


    