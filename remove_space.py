"""19. Remove Spaces 
Write a function remove_spaces(text) that removes all spaces from a 
string. 
Restriction: Use a loop. 
Example: 
Input  : Python Programming Language 
Output : PythonProgrammingLanguage"""


def remove_spaces(text):
    result = ""

    for i in text:
        if i != " ":
            result = result + i

    return result


text = input("Enter a string: ")

result = remove_spaces(text)

print("String without spaces:", result)