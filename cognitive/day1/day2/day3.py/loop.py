#10 loop practice questions,
#Print 1 to 10 using a for loop.
"""def number():
    for num in range(1,11):
        print(num)
number()"""
#Print all even numbers from 1 to 50.
"""def even():
    for number in range(1,51):
        if number%2==0:
            print(number)
even()"""
#Print the multiplication table of a number entered by the user.
"""def table():
    for i in range(2,11):
        print(f"Multiplication: {i}")
        for j in range(1,11):
            print(f"{i} * {j} = {i*j}")
table()"""
"""def table():
    table=int(input("Table: ").strip())
    print(f"Multiplication: {table}")
    for j in range(1,11):
       print(f"{table} * {j} = {table*j}")
table()"""

#Ask a user for a word → print each character on a new line.
"""def word():
    word=input("Word: ").strip()
    for char in word:
        print(char)
word()"""
#Sum all numbers from 1 to n (n entered by user).
"""def sum():
    sum=0
    try:
      number=int(input("Number: ").strip())
      for i in range(1,number):
         sum+=i
      print(f"Sum: {sum}")
    except ValueError:
       print("Invalid Input,allow only integers.")
sum()"""
#Print a right-angled triangle pattern with *:
"""def triangle():
    try:
        star=int(input("Star: ").strip())
        for i in range(star):
            print('*' * i)
    except ValueError:
        print("Invalid Input,allow only integers.")
triangle()"""
#Reverse a number using a loop (e.g., 1234 → 4321).
"""def reverse():
    try:
        number=int(input("Number: ").strip())
        reverse=0
        while number >0:
          digit=number//10
          reverse=reverse * 10 + digit
          number//10
        print(f"Reverse: {reverse}")
    except ValueError:
        print("Invalid Input,allow only integers.")
reverse()"""
#Check if a number is prime using a loop.
"""def prime():
    try:
        number=int(input("Number: ").strip())
        if number <=1:
            print(f"Number {number} is not Prime.")
            return
        for i in range(2,number):
                if number %i==0:
                    print(f"Number {number} is not prime.")
                    break
        else:
                print(f"Number {number} is a prime.")
    except ValueError:
        print("Invalid input, allow only integers.")
prime()
"""
"""def fibonnaci_series():
    try:
      number=int(input("Number: ").strip())
      a,b=0,1
      for i in range(a,number+1):
         print(a,end='')
         a,b=b,a+b
         
         
    except ValueError:
       print("Invalid Input, allow only integers.")
fibonnaci_series()"""
"""def factorial():
    try:
        number=int(input("Number: ").strip())
        result=1
        for i in range(1,number+1):
            result *= i
        print(f"Factorial: {result}")
    except ValueError:
        print("Invalid Input, allow only integers.")
factorial()"""
def factorial():
    try:
        number=int(input("Number: ").strip())
        result=1
        for i in range(1,number+1):
            result *=i
        print(f"{number}: {result}")
    except ValueError:
        print("Invalid Input, allow only integers.")
factorial()