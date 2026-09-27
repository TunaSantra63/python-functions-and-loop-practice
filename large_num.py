"""3. Find Largest of Two Numbers 
Write a function find_largest(a, b) that accepts two numbers and returns 
the largest number. 
Concepts: function, return, conditional statement """



def find_largest(a,b):
    if(a>b):
        return a
    else:
        return b
    
a = int(input("Enter the First number : "))
b = int(input("Enter the second number : "))
result = find_largest(a, b)
print(f"The largest number is {result}")