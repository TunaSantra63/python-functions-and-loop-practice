"""29. Star Pattern 
Write a function star_pattern(n) that prints: 
* 
** 
*** 
**** 
***** 
For n = 5. 
Concepts: nested loops."""


def star_pattern(n):
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end="")
        print()


n = int(input("Enter n: "))

star_pattern(n)