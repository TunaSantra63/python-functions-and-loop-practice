"""12. Count Vowels 
Write a function count_vowels(text) that counts the number of vowels in a 
string. 
Example: 
Input  : education 
Output : 5 
Restriction: Use a loop. """


def count_vowels(A):
    count = 0
    for i in A:
        if(i == "a" or i == "A" or i == "e" or i == "E" or i == "i" or i == "I" 
           or i == "O" or i == "o" or i == "U" or i == "u"):
            count = count+1
    return count

A = input("Enter the string : ")
outcome = count_vowels(A)
print(f"The number of the vowels is {outcome}")
            