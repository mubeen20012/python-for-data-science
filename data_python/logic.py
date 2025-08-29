#Factorial
def factorial():
    number=int(input("Number: ").strip())
    result=1
    for i in range(1,number + 1):
        result *=i
    print(f"Factorial: {result}")
factorial()
#Prime Numbers
"""def prime():
    number=int(input("Number: ").strip())
    if number <=1:
        print(f"Number {number} is not prime.")
        return

    for i in range(2,number):
        if number%i==0:
            print(f"Number {number} is not prime.")
            break
    else:
      print(f"Number {number} is a prime.")
prime()"""
#Prime Numbers in a Range
"""def prime():
 try:
    a=int(input("Number: ").strip())
    b=int(input("Number: ").strip())
    print(f"Prime number between {a} and {b} are: ")

    for num in range(a,b+1):
        if num >1:
            for i in range(2,int(num**0.5) +1):
                if num%i==0:
                    break
            else:
                print(num)
 except ValueError:
    print("Invalid Input, allow only integers.")
prime()"""
"""def fibonacci():
    try:
        number=int(input("Number: ").strip())
        a,b=0,1
        for i in range(number):
            print(a, end='')
            a,b = b, a+b
    except ValueError:
        print("Invalid Input, allow only integers.")
fibonacci()

"""
#Second Largest in a List
"""def largest():
    largest=[]
    for number in range(7):
        try:
            number=int(input("Number: ").strip())
            largest.append(number)
        except ValueError:
            print("Invalid Input, allow only integers.")
    largest=max(largest)
    print(f"Largest: {largest}")

largest()"""
"""def largest():
    numbers=[]
    for number in range(7):
        try:
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
    for number in range(7):
        try:
            number=int(input("Number: ").strip())
            numbers.append(number)
        except ValueError:
            print("Invalid Input, allow only integers.")
    largest=second =float('-inf')
    for num in numbers:
        if num > largest:
            second= largest
            largest=num
        elif num > second and num!=second:
                second = num
    print(f"Largest: {largest}")
    print(f"Second Largest: {second}")


largest()"""
#Pattern Printing
def pattern():
    number=int(input("Number: ").strip())
    for i in range(1,number +1):
       print(f"*" * i)
        
   
pattern()






