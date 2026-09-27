"""28. Count Occurrence of Each Vowel 
Write a function that separately counts: 
a 
e 
i 
o 
u 
Example: 
Input: 
education 
Output: 
a = 1 
e = 1 
i = 1 
o = 1 
u = 1 
Restriction: Use loops and conditions. """




def count_vowels(text):
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0

    for ch in text:
        if ch == "a" or ch == "A":
            a = a + 1
        elif ch == "e" or ch == "E":
            e = e + 1
        elif ch == "i" or ch == "I":
            i = i + 1
        elif ch == "o" or ch == "O":
            o = o + 1
        elif ch == "u" or ch == "U":
            u = u + 1

    print("a =", a)
    print("e =", e)
    print("i =", i)
    print("o =", o)
    print("u =", u)


text = input("Enter a string: ")

count_vowels(text)