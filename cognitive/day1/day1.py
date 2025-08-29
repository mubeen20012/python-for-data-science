#🔹 Part 1 – Data Types & Variables (15 min)
"""name=input("Name: ")
print(type(name))"""
"""b=5
print(type(b))"""
"""c=0.7
print(type(c))"""
"""d=[9]
print(type(d))"""
"""e={"num":7}
print(type(e))"""
#Swap values of two variables without using a third variable.
"""a=5
b=7
c=a
a=b
b=c
print(f"a: {a}")
print(f"b: {b}")"""
"""a=5
b=7
a=a+b
b=a-b
a=a-b
print(f"a: {a}")
print(f"b: {b}")
"""
#Convert a float into int, and int into string. Print results.
"""a=int(0.8)
print(type(a))
b=str(6)
print(type(b))
"""
#Write a program to check the type of user input.
"""name=input("Name: ").strip().title()
print(type(name))
print(name)"""
#Store your age in a variable and calculate how many days you’ve lived (approx).
"""age=int(input("Age: ").strip())
days_lived=age * 365
print(f"You Have Lived Approximately: {days_lived}")"""
#🔹 Part 2 – Expressions (15 min)
#Write a program that takes two numbers and prints: sum, difference, product, quotient, and remainder
"""a=int(input("Number 1: ").strip())
b=int(input("Number 2: ").strip())
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b)
print(a // b)"""
#Evaluate this expression step by step:
#print((10 + 5) * 3 / 2 ** 2 % 4)
#Write a program that calculates simple interest:
"""Principal=6
Rate=4
Time=3
SI = (Principal * Rate * Time) / 100.
print(SI)"""
#Ask the user for temperature in Celsius and convert it to Fahrenheit.
"""def temperature():
    try:
        celcius=int(input("Enter Temperature: ").strip())
        Fehrenheit=(9/5 + celcius) + 32
        print(f"Temperature In Fehrenheit: {Fehrenheit}")
    except ValueError:
        print("Invalid Input, allow only integers.")
temperature()"""
#Part 3 – String Operations (30 min)
#Take a string "Python for Data Science". Practice:
"""text="Python for Data Science"
#Print length of string.
print(len(text))
#Print length of string.
upper=text.upper()
print(upper)
#Convert to uppercase & lowercase.
lower=text.lower()
print(lower)
#Count how many times "a" appears.
count=0
appear='a'
for word in text:
    if word== 'a':
        count +=1
print(f"a appear: {count}")
#Replace "Python" with "Machine Learning".
replace=text.replace("Python","Machine Learning")
print(replace)
#Slice first 6 characters and last 6 characters.
slice=text[:6]
print(slice)
slice=text[-6:]
print(slice)"""
#Check if a string is palindrome (same forward and backward). Example: "madam".
"""def palindrome():
    text=input("Text: ").strip()
    reverse=text[::-1]
    if text == reverse:
        print(f"Word {text} is a palindrome.")
    else:
        print(f"Word {text} is not a palindrome.")

palindrome()"""
#Split a sentence into words and join them back with -.
"""word=input("Word: ").strip()
split=word.split()
print(split)
join='-'.join(split)
print(join)"""
#Ask the user for their full name → print initials in capital letters (e.g., "musfira mubeen" → "M.M.").
"""def title():
    name=input("Enter Your name: ").strip().title()
    print(f"Hello! {name}")
title()"""
#Remove all vowels from a string entered by user.
"""def remove():
        name=input("Enter Your name: ").strip().title()
        vowel='AEIOUaeiou'
        result=''
        for char in name:
                if char not in vowel:
                        result += char
                        
        print(f"Remove Vowels: {result}")

remove()"""
#Write a program to count how many words, characters, and digits are in a string.
def count():
    
    text=input("Enter item: ").strip()
    char=len(text)
    words=len(text.split())
    digit=sum(char.isdigit() for char in text)
    print(f"Character: {char}")
    print(f"Word: {words}")
    print(f"Digit: {digit}")
    
count()













