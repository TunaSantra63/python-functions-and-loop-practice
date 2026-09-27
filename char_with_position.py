"""25. Print Characters with Position 
Write a function display_position(text) that displays every character along 
with its position. 
Example: 
Input: 
JAVA 
Output: 
Position 0 : J 
Position 1 : A 
Position 2 : V 
Position 3 : A 
Concepts: range(), indexing """





def display_position(text):
    for i in range(len(text)):
        print("Position", i, ":", text[i])


text = input("Enter a string: ")

display_position(text)