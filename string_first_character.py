"""22. Find First Character 
Write a function first_character(text) that prints the first character of a 
string. 
Restriction: Do not directly use text[0]. 
Use a loop and break."""



def first_character(text):
    for i in text:
        print("First character:", i)
        break


text = input("Enter a string: ")

first_character(text)
