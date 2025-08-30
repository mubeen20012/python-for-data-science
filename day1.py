#📅 Day 1 – Core Python Recap
#✅ Strings
#Reverse a string without using slicing.
"""def reverse():
    text=input("Text: ").strip()
    reverse=text[::-1]
    print(f"Reverse: {reverse}")
reverse()"""
"""def reverse():
    text=input("Text: ").strip()
    reverse=''
    for char in text:
        reverse=char + reverse
    print(f"Reverse: {reverse}")
reverse()"""
"""def reverse():
    try:
        number=int(input("Number: "))
        reverse=0
        while number>0:
            digit=number%10
            reverse=reverse *10 +digit
            number//=10
        print(f"Reverse: {reverse}")
    except ValueError:
        print("Invalid Input, allow only integers.")
reverse()"""
#Check if a string is a palindrome.
"""def palindrome():
    text=input("Text: ").strip()
    reverse=text[::-1]
    if text==reverse:
        print(f"{text}: Palindrome")
    else:
        print(f"{text}:Not Palindrome")
palindrome()"""
#Count vowels and consonants in a string.
"""def count():
    count=0
    word=input("Word: ").strip()
    vowel='AEIOUaeiou'
    for char in word:
        if char in vowel:
            count+=1
        
    print(f"vowel: {count}")
count()"""
"""def count():
    count=0
    word=input("Word: ").strip()
    vowel='AEIOUaeiou'
    for char in word:
        if char not in vowel:
            count+=1
        
    print(f"Consonent: {count}")
count()"""
#Find the frequency of each character in a string (hello → {h:1, e:1, l:2, o:1}).
"""def freq():
    freq={}
    word=input("Word: ").strip()
    for char in word:
        if char in freq:
           freq[char]+=1
        else:
            freq[char]=1
    print(freq)
freq()"""
#Extract digits from a string ("abc123def45" → 12345).
"""def extract():
    string="abc123def45"
    digit_only=''
    for char in string:
        if char.isdigit():
           digit_only += char
    print(digit_only)
    if digit_only:
        number=int(digit_only)
        print(number)
extract()"""
#✅ Lists
#Find the largest and smallest number in a list.
"""def largest():
    numbers=[]
    try:
        for i in range(5):
            number=int(input("Number: ").strip())
            numbers.append(number)
    except ValueError:
        print("Invalid Input, allow only integers.")
    largest=numbers[0]
    for num in numbers:
        if num > largest:
            largest=num
    print(f"Largest: {largest}")
largest()"""
"""def largest():
    numbers=[]
    try:
        for i in range(5):
            number=int(input("Number: ").strip())
            numbers.append(number)
    except ValueError:
        print("Invalid Input, allow only integers.")
    largest=second=numbers[0]
    for num in numbers:
        if num > largest:
            second=largest
            largest=num
        elif num>second and num !=second:
            second=num
    print(f"Second: {second}")
largest()"""
"""def largest():
    numbers=[]
    try:
        for i in range(5):
            number=int(input("Number: ").strip())
            numbers.append(number)
    except ValueError:
        print("Invalid Input, allow only integers.")
    largest=max(numbers)
    
    print(f"largest: {largest}")
largest()"""
#Remove duplicates from a list.
"""def duplicate():
    duplicate=[]
    numbers=[1,1,2,3,3,4,5,6,6]
    for num in numbers:
        if num not in duplicate:
            duplicate.append(num)
    print(f"Duplicate: {duplicate}")
duplicate()"""
#Merge two lists into one without duplicates.
"""def merge():
    name=['Ali','Bilal','Ahmed']
    age=[4,7,9]
    student=list(set(name + age))
    print(student)
merge()"""
"""def merge():
    name=['Ali','Bilal','Ahmed']
    full=['amina']
    student=name +  full
    print(student)
merge()"""
#Count frequency of each element in a list ([1,2,2,3,1,4] → {1:2, 2:2, 3:1, 4:1}).
"""def freq():
    
    freq={}
    try:
        for i in range(5):
           number=int(input("Enter Number: ").strip())
           if number in freq:
                freq[number] +=1
           else:
                freq[number] =1
        print(freq)
    except ValueError:
        print("Invalid Input,allow only integers.")
freq()"""
#rotate
"""def rotate():
    number=[1,2,3,4,5]
    first=number[0]
    reset=number[1:]
    rotate=reset + [first]
    print(rotate)
rotate()"""
#✅ Dictionaries
#Create a dictionary from two lists (['a','b','c'] and [1,2,3]).
"""keys=['a','b','c']
values=[1,2,3]
result={}
for i in range(len(keys)):
    result[keys[i]]=values[i]
print(result)"""
#Find the key with the maximum value in a dictionary.
"""scores = {
    "Ali": 85,
    "Sara": 92,
    "Omer": 78,
    "Hina": 95
}
highest=max(scores,key=scores.get)
print(f"Highest Score: {highest} with {scores[highest]}")"""
#Merge two dictionaries.
"""student={'Name':"Musfira"}
marks={'Age':'22'}
information={**student ,** marks}
print(information)"""
#Count frequency of words in a sentence using dictionary.
"""def freq():
    freq={}
    words=input("Word: ").strip().split()
    for word in words:
        if word in freq:
           freq[word] +=1
        else:
           freq[word] =1
    print(freq)
freq()"""
#Sort a dictionary by values (ascending & descending).
"""students_marks = {
    'Ali': 85,
    'Sara': 92,
    'Ahmed': 78,
    'Zara': 90
}
sorted_asc=dict(sorted(students_marks.items(),key=lambda item: item[1]))
print(f"Ascending: {sorted_asc}")"""
students = {
    'Ali': 85,
    'Sara': 92,
    'Ahmed': 78,
    'Zara': 90
}
sorted=dict(sorted(students.items(),key=lambda item: item[1],reverse=True))
print(f"Descending: {sorted}")






                   



