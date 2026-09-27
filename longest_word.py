"""27. Find Longest Word 
Write a function find_longest_word(text) that finds the longest word in a 
sentence. 
Restriction: 
• Do not use dictionaries.  
• Do not use max().  
• Do not use advanced collections.  
• Use loops and string processing. """




def find_longest_word(text):
    longest = ""
    word = ""

    for i in text + " ":
        if i != " ":
            word = word + i
        else:
            if len(word) > len(longest):
                longest = word

            word = ""

    return longest


text = input("Enter a sentence: ")

result = find_longest_word(text)

print("Longest word:", result)