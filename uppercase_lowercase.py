"""20. Convert Lowercase to Uppercase 
Write a function convert_uppercase(text) that converts a string to 
uppercase. 
Task: First solve using upper() and then demonstrate a loop-based 
solution using character processing."""




def convert_uppercase(text):
    return text.upper()


text = input("Enter a string: ")

result = convert_uppercase(text)

print("Uppercase:", result)

def convert_uppercase(text):
    result = ""

    for i in text:
        if "a" <= i <= "z":
            result = result + chr(ord(i) - 32)
        else:
            result = result + i

    return result


text = input("Enter a string: ")

result = convert_uppercase(text)

print("Uppercase:", result)