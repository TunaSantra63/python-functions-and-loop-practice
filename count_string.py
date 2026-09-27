"""Section B – String-Based Assignments 
11. Count Characters in a String 
Write a function count_characters(text) that counts the number of 
characters in a string. 
Restriction: Do not use len(). 
Concepts: for loop, counter """




def count_characters(n):
    count = 0
    for _ in n:
        count = count+1
    return count
n = input("Enter the string : ")
result = count_characters(n)
print(f"The count of the character is {result}")
