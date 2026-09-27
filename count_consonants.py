"""13. Count Consonants 
Write a function count_consonants(text) that counts the number of 
consonants in a string. 
Assume: Input contains alphabetic characters and spaces."""


def count_consonants(text):
    count = 0

    for _ in text:
        if _.isalpha() and _ not in "aeiouAEIOU":
            count = count + 1

    return count


text = input("Enter a string: ")
result = count_consonants(text)
print(f"Number of consonants: {result}")