"""21. Count Uppercase and Lowercase Characters 
Write a function count_case(text) that counts: 
• uppercase characters  
• lowercase characters  
• digits  
• spaces  
Example: 
Input: Python123 ABC 
Uppercase : 3 
Lowercase : 6 
Digits    
: 3 
Spaces    
: 1 """


def count_case(text):
    uppercase = 0
    lowercase = 0
    digits = 0
    spaces = 0

    for i in text:
        if i.isupper():
            uppercase = uppercase + 1
        elif i.islower():
            lowercase = lowercase + 1
        elif i.isdigit():
            digits = digits + 1
        elif i == " ":
            spaces = spaces + 1

    return uppercase, lowercase, digits, spaces


text = input("Enter a string: ")

u, l, d, s = count_case(text)

print("Uppercase:", u)
print("Lowercase:", l)
print("Digits:", d)
print("Spaces:", s)