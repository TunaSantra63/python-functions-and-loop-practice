"""24. Print Each Character 
Write a function display_characters(text) that prints every character of a 
string on a separate line. 
Example: 
Input: 
PYTHON 
Output: 
P 
Y 
T 
H 
O 
N 
Use: for loop. """



def display_characters(text):
    for i in text:
        print(i)


text = input("Enter a string: ")

display_characters(text)