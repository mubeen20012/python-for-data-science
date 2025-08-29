#master conditions (if, elif, else)
#Ask the user for a number → print if it’s positive, negative, or zero.
"""def number():
    try:
        number=int(input("Number: ").strip())
        if number >0:
            print(f"Number: {number} is Positive.")
        elif number <0:
            print(f"Number: {number} is Negative.")
        else:
            print(f"Number: {number} is 0.")
    except ValueError:
        print("Invalid Input,allow only integers.")
number()"""
#Ask age → print “Child”, “Teenager”, “Adult”, “Senior”.
"""def age():
    try:
        age=int(input("Age: ").strip())
        if age>0 and age <=10:
            print("Child")
        elif age>10 and age <=18:
            print("Teenager")
        elif age>18 and age <=40:
            print("Adult")
        elif age>40 and age <100:
            print("Senior")
        else:
            print(f"Your age is {age},you live in golden era")
    except ValueError:
        print("Invalid Input, allow only Integers.")
age()"""
#Ask a number → check if it’s even or odd.
"""def even():
    try:
        number=int(input("Number: ").strip())
        if number %2==0:
            print(f"Number {number} is even.")
        else:
            print(f"Number {number} is odd.")
    except ValueError:
        print("Invalid Input, allow only Integers.")
even()"""
#Ask the user for a year → check if it’s a leap year.
"""def leap_year():
    try:
        year=int(input("Enter Year To Check Leap Year: ").strip())
        if year % 4==0 and year%400==0:
            print(f"This Year {year} is a leap Year.")
        elif year %100==0:
            print(f"This Year {year} is not a leap Year.")
        else:
            print(f"This Year {year} is not a leap Year.")

    except ValueError:
        print("Invalid Input,allow only Integers.")
leap_year()
"""
#Ask marks (0–100) → print Grade (A, B, C, D, F) with conditions.
"""def marks():
    try:
        marks=int(input("Marks: ").strip())
        if marks >=90:
            print("A+")
        elif marks >=80:
            print("A")
        elif marks >=70:
            print("B")
        elif marks >=60:
            print("C")
        elif marks >=50:
            print("A+")
        else:
            print("F\nTry Again")
    except ValueError:
        print("Invalid Input, allow only Integers.")
marks()"""
#Ask a number → check if it is divisible by both 3 and 5 (FizzBuzz logic).
"""def fizzbuzz():
    try:
        for number in range(30):
          if number%3==0 and number%5==0:
            print("FizzBuzz")
          elif number%3==0:
            print("Fizz")
          elif number%5==0:
            print("Buzz")
          else:
            print(number)
    except ValueError:
        print("Invalid Input,allow only Integers.")
fizzbuzz()
"""
#Ask the user for temperature →
"""def temperature():
    try:
        temperature=int(input("Temperature: ").strip())
        if temperature <0:
            print(f"Temperature {temperature}: Freezing")
        elif temperature >0 and temperature <=20:
            print(f"Temperature {temperature}: Cold")
        elif temperature >21 and temperature <=30:
            print(f"Temperature {temperature}: Warm")
        else:
            print(f"Temperature {temperature}: Hot")
    except ValueError:
            print("Invalid Input,allow only Integers.")
temperature()"""
#Ask for 3 numbers → print the largest.
"""def largest():
    numbers=[]
    for number in range(3):
        numbers.append(number)
    print(number)
    largest=max(numbers)
    print(f"Largest: {largest}")
largest()"""
"""def largest():
    numbers=[]
    for i in range(3):
        try:
          number=int(input("Enter Number: ").strip())
          numbers.append(number)
        except ValueError:
            print("Invalid Input,allow only integers.")
    print(number)
    largest=numbers[0]
    for num in numbers:
        if num > largest:
            largest=num
    print(f"Largest: {largest}")
largest()"""
#2nd Largest
"""def largest():
    numbers=[]
    for i in range(3):
        try:
          number=int(input("Enter Number: ").strip())
          numbers.append(number)
        except ValueError:
            print("Invalid Input,allow only integers.")
    print(number)
    largest=second=numbers[0]
    for num in numbers:
        if num > largest:
            second=largest
            largest=num
        elif num < second and num !=largest:
            second=num
    print(f"Largest: {largest}")
    print(f"Second Largest: {second}")

largest()"""
#Write a calculator: ask num1, operator, num2 (operators: +, -, *, /, **). Use if-elif-else to perform operation.
"""def calculator():
    while True:
        try:
            num1=int(input("Num1: ").strip())
            num2=int(input("Num2: ").strip())
            operator=input("Operator(+,-,*,/)or q to quit: ").strip()
            if operator.lower()=='q':
                print("Existing----")
                break
            else:
                operation={
                    '+' : num1 + num2,
                    '-' : num1 - num2,
                    '*' : num1 * num2,
                    '/' : num1 / num2
                     if num2!=0 else "Error Division By Zero"
                }
                print(f"Operation")
        except ValueError:
            print("Invalid Input,allow only integers.")
calculator()

                

"""
#Ask for a person’s salary:
"""def salary():
    try:
        salary=int(input("Salary: ").strip())
        if salary >100000:
            print(f"Salary {salary}:High Income.")
        elif salary>=50000 and salary<=100000:
            print(f"Salary {salary}:Medium Income.")
        else:
            print(f"Salary {salary}:Low Income.")
    except ValueError:
        print("Invalid Input,allow only integers.")
salary()"""
#ATM simulation:
def ATM():
    balance=4000
    try:
       amount=int(input("Enter Amount: ").strip())
       if amount <= balance:
           balance-=amount
           print(f"Money Withdrawn {amount}\nNew Balance: {balance}")
       else:
           print(f"Insufficient Balance {balance}.\nrecharge Your account.")
    except ValueError:
        print("Invalid Input,allow only integers.")
ATM()









        
        


        





