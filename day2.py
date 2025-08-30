#📅 Day 2 – Functions, Loops, File Handling, Exception Handling
#🕐 Part 1 – Practice Problems (3 Hours)
#1️⃣ Functions & Loops
#Write a function to check if a number is prime.
"""def prime():
    try:
        number =int(input("Number: ").strip())
        if number <=1:
            print(f"Number {number} is not a prime")
            return
    
        for i in range(2, number):
            number%i==0
            print(f"Number {number} is not a prime")
            return
        
        print(f"Number {number} is a prime")
    except ValueError:
        print("Invalid Input,allow only integers.")
prime()
"""
#Write a function to return factorial of a number using recursion.
"""def factorial():
    try:
        number =int(input("Number: ").strip())
        result=1
        for i in range(1,number+1):
            result*=i
        print(f"Factorial Of 5: {result}")
    except ValueError:
        print("Invalid Input,allow only integers.")    
factorial()"""
#Write a function to print all prime numbers between 1 and 100.
"""def prime():
    for num in range(2,101):
        is_prime=True
        for i in range(2,int(num**0.5)+1):
            if num %i==0:
                is_prime=False
                break
        if is_prime:
            print(num, end='')
prime()"""
#Write a function that generates the Fibonacci series up to n terms using a loop.
"""def fibonnaci():
    try:
       number=int(input("Enter Number: ").strip())
       a,b=0,1
       for i in range(a,number +1):
           print(a,end='')
           a,b=b,a+b
    except ValueError:
        print("Invalid Input,allow only integers.") 
fibonnaci()"""
#Write a function that takes a list of numbers and returns the sum of even numbers.
"""def sum():
    sum=0
    numbers=[1,2,3,4,5,6,7,8,9]
    for number in numbers:
        if number%2==0:
            sum+=number
    print(f"Sum Of all even: {sum}")
sum()"""
#2️⃣ File Handling
#Create a file data.txt and write 10 random numbers into it.
"""import random
numbers=[random.randint(1,100) for i in range(10)]
#create the file in write mode
with open('data.txt','w') as file:
    for num in numbers:
        file.write(f"{num}\n")
print("!0 random Number have been written to data.txt")
#open the file in read mode
with open('data.txt','r') as file:
    numbers=file.readlines()
numbers=[int(num.strip()) for num in numbers]
total=sum(numbers)
average=total/len(numbers)
print(f"Numbers: {numbers}")
print(f"sum: {total}")
print(f"average: {average:.2f}")
new_number=[11,45,89]
with open('data.txt','a') as file:
    for num in new_number:
        file.write(f"{num}\n")
with open('data.txt','r') as file:
    numbers = [int(num.strip()) for num in file.readlines()]
total=sum(numbers)
average=total/len(numbers)
print(f"Updated Numbers: {numbers}")
print(f"Updated sum: {total}")
print(f"Updated average: {average:.2f}")

"""
"""with open('data.txt','r') as file:
    numbers=[int(num.strip()) for num in file.readlines()]
freq={}
for num in numbers:
    if num in freq:
        freq[num] +=1
    else:
        freq[num] =1
print("Number Frequency")
for num, freq in freq.items():
    print(f'{num} : {freq}')"""
#3️⃣ Exception Handling

#Take input from the user for a number and handle invalid inputs using try-except.
"""def numbers():
    try:
        number=int(input("Number: ").strip())
        print(number)
    except ValueError:
        print('Invalid Input,allow only integers.')
numbers()
"""
#Write a function to divide two numbers and handle ZeroDivisionError.
"""def division():
    try:
        num1=int(input("Num1: ").strip())
        num2=int(input("Num2: ").strip())
        result=num1/num2
        print(f"Result: {result}")
    except ValueError:
        print("Invalid input,allow only integers.")
    except ZeroDivisionError:
        print("Cannot Divide by Zero")
division()"""
#Read numbers from a file and handle FileNotFoundError.
def read_file():
    filename=input("Enter Filename: ").strip()
    try:
        with open(filename,'r') as file:
            numbers=[]
            for line in file:
                line=line.strip()
                if line.isdigit():
                    numbers.append(int(line))
            print(f"Numbers in the File: {numbers}")
    except FileNotFoundError:
        print(f"File {filename} not found.")
read_file()



