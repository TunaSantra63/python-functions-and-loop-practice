"""17. Count Words 
Write a function count_words(text) that counts the number of words in a 
sentence. 
Restriction: Do not use split(). 
Example: 
Input: 
Python is easy to learn 
Output: 
5 
Hint: Count spaces carefully."""



def count_words(text):
    count = 0
    in_word = False

    for i in text:
        if i != " ":
            if in_word == False:
                count = count + 1
                in_word = True
        else:
            in_word = False

    return count


text = input("Enter a sentence: ")

result = count_words(text)

print("Number of words:", result)