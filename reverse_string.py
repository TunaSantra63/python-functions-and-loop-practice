"""15. Reverse a String 
Write a function reverse_string(text) that reverses a string. 
Restriction: Demonstrate both approaches: 
Approach 1: Using a loop 
Approach 2: Using string slicing 
text[::-1]"""


def reverse_string_slicing(text):
    return text[::-1]


text = input("Enter a string: ")

result = reverse_string_slicing(text)

print("Reversed string:", result)