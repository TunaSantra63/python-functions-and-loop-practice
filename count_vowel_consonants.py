"""14. Count Vowels and Consonants 
Write a function count_vowels_consonants(text) that separately counts 
vowels and consonants. 
Example: 
Input  : Python Programming 
Vowels    
 : 4 
Consonants : 14 """



def count_vowels_consonants(text):
    vowels = 0
    consonants = 0

    for i in text:
        if i.isalpha():
            if i in "aeiouAEIOU":
                vowels = vowels + 1
            else:
                consonants = consonants + 1

    return vowels, consonants


text = input("Enter a string: ")

v, c = count_vowels_consonants(text)

print("Vowels:", v)
print("Consonants:", c)