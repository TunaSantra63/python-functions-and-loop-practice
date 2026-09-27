"""18. Find Frequency of a Character 
Write a function character_frequency(text, ch) that counts how many 
times a particular character occurs. 
Restriction: Do not use count(). 
Example: 
Text      
: programming 
Character : g 
Frequency : 2"""



def character_frequency(text, ch):
    frequency = 0

    for i in text:
        if i == ch:
            frequency = frequency + 1

    return frequency


text = input("Enter a text: ")
ch = input("Enter a character: ")

result = character_frequency(text, ch)

print("Frequency:", result)