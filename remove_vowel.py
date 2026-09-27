"""26. Remove Vowels 
Write a function remove_vowels(text) that removes all vowels from a 
string. 
Example: 
Input: 
Python Programming 
Output: 
Pythn Prgrmmng 
Restriction: Use a loop. Do not use replace()."""




def remove_vowels(text):
    result = ""

    for i in text:
        if i not in "aeiouAEIOU":
            result = result + i

    return result


text = input("Enter a string: ")

result = remove_vowels(text)

print("After removing vowels:", result)