"""30. Number Pattern 
Write a function number_pattern(n) that prints: 
1 
12 
123 
1234 
12345 
Concepts: nested for loops."""



def number_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()


n = int(input("Enter n: "))

number_pattern(n)