"""Check Palindrome String 
Write a function check_palindrome(text) that checks whether a string is a 
palindrome. 
Example: 
madam → Palindrome 
hello → Not Palindrome"""



def check_palindrome(text):
    reverse = text[::-1]

    if text == reverse:
        return "Palindrome"
    else:
        return "Not Palindrome"


text = input("Enter a string: ")

result = check_palindrome(text)

print(result)