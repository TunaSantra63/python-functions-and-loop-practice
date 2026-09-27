"""6. Multiplication Table 
Write a function multiplication_table(n) that prints the multiplication table 
of a given number from 1 to 10. 
Concepts: for, range() """




def multiplication_table(n):
    for _ in range(1,11):
        mult = _ * n
        print(f" {n} * {_} = {mult}")

n = int(input("Enter your number : "))
multiplication_table(n)


