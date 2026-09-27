"""4. Find Largest of Three Numbers 
Write a function find_largest(a, b, c) that finds the largest among three 
numbers. 
Restriction: Do not use max()."""


def find_largest(a,b,c):
    if (a>b and a>c):
        return a
    elif(b>c):
        return b
    else:
        return c     
a = int(input("ENTER A : "))
b = int(input("ENTER B : "))
c = int(input("ENTER C : "))
result = find_largest(a,b,c)
print(f"The largest number is{result}")