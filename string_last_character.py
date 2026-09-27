"""23. Find Last Character 
Write a function last_character(text) that prints the last character of a 
string. 
Restriction: Demonstrate: 
text[-1] 
and a loop-based approach."""


def last_character(text):
    return text[-1]


text = input("Enter a string: ")

result = last_character(text)

print("Last character:", result)