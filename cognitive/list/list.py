#🔹 Beginner (1–3) – Basic creation & access
#Create a list of 5 numbers and print it.
"""def list():
    numbers=[1,2,3,4,5]
    print(numbers)
    for number in numbers:
        print(number)
list()"""
#Access elements: print the first, last, and middle element.
"""def list():
    numbers=[1,2,3,4,5]
    print(numbers[0])
    print(numbers[2])
    print(numbers[4])

    
list()"""
#Modify a list: change the 2nd element to a new value.
"""def list():
    numbers=[1,2,3,4,5]
    numbers[1]=6
    print(numbers)    
list()"""
#🔹 Easy (4–5) – Adding & removing
#Add a new element at the end and at the beginning of a list.
"""def list():
    numbers=[1,2,3,4,5]
    numbers.append(9)
    numbers.insert(0,8)
    print(numbers)    
list()"""
#Remove an element by value and by index.
"""def list():
    numbers=[1,2,3,4,5]
    numbers.append(9)
    numbers.insert(0,8)
    numbers.remove(3)
    print(numbers)    
list()"""
#🔹 Intermediate (6–7) – Loop + list
#Take a list of numbers → print only even numbers using a loop.
"""def even():
    numbers=[1,2,3,4,5,6,7,8,9]
    for number in numbers:
        if number %2==0:
            print(number)
even()"""
"""def even():
    numbers=[]
    for number in range(1,30):
        numbers.append(number)
        for num in numbers:
            if num%2==0:
                print("Even")
            else:
                print(number)

even()"""
#Find the sum and average of a list of numbers.
"""def sum():
    sum=0
    numbers=[1,2,3,4,5,6,7,8,9]
    for number in numbers:
        sum+=number
    average=sum/len(numbers)
    print(f"Sum of all number is: {sum}")
    print(f"Average: {average}")
sum()
"""
#🔹 Advanced (8–10) – Logic + nested lists
#Find largest and smallest number in a list without using max() or min().
"""def largest():
    numbers=[]
    for number in range(5):
        try:
            number=int(input("Number: ").strip())
            numbers.append(number)
        except ValueError:
            print("Invalid Input,allow only integers.")
    largest=numbers[0]
    for num in numbers:
        if num>largest:
            largest = num
    print(f"Largest: {largest}")
largest()
"""
"""def second_largest():
    numbers=[]
    for number in range(5):
        try:
            number=int(input("Number: ").strip())
            numbers.append(number)
        except ValueError:
            print("Invalid Input,allow only integers.")
    largest=second=numbers[0]
    for num in numbers:
        if num>largest:
            second= largest
            largest = num
        
        elif num > second and num!= second:
                num= second
    print(f"Second_Largest: {second}")
second_largest()"""
#Reverse a list using a loop (don’t use [::-1] or reverse()).
"""def reverse():
    numbers=[1,2,3,4,5]
    reverse=[]
    for num in numbers:
        reverse.insert(0,num)
    print(f"Reverse: {reverse}")
reverse()"""
"""def reverse():
    text=input("Text: ").strip() 
    reverse=''
    for char in text:
        reverse= char + reverse
    print(f"Reverse: {reverse}")
reverse()"""
"""def reverse():
    numbers=[1,2,3,4,5]
    reverse=numbers[::-1]
    print(f"Reverse: {reverse}")
reverse()"""
"""def reverse():
    try:
        number=int(input("Numbers: "))
        reverse=0
        while number>0:
            digit=number%10
            reverse=reverse *10 + digit
            number//=10
        print(f"{number} : {reverse}")
    except ValueError:
        print("Invalid Input,allow only integers.")
reverse()"""
#armstrong
"""def armstrong():
    try:
        number=int(input("Number: ").strip())
        number_digit=len(str(number))
        sum=0
        temp=number
        while temp>0:

          digit=temp%10
          sum+=digit ** number_digit
          temp//=10
        if sum==number:
            print(f"{number} is armstrong.")
        else:
            print(f"{number} is not armstrong.")

    except ValueError:
        print("Invalid Input, allow only integers.")
armstrong()"""
"""def factorial():
    try:
        number=int(input("Number: ").strip())
        result=1
        for i in range(1,number+1):
            result*=i
        print(f"Factorial of number {number}: {result}")
    except ValueError:
        print("Invalid Input,allow only integers.")
factorial()"""
#fibonnaci
def fibonnaci():
    try:
        number=int(input("Number: ").strip())
        a,b=0,1
        for i in range(a,number+1):
            print(a,end='')
            a,b=b,a+b
        
    except ValueError:
        print("Invalid input,allow only integers.")
fibonnaci()
    