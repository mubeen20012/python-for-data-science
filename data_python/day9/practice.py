#factorial
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
#prime
"""def prime():
    try:
        number=int(input("Number: ").strip())
        if number <=1:
            print(f"Number {number} is not a prime.")
            return
        for i in range(2,number):
           if number %i==0:
              print(f"Number {number} is not a prime.")
              break
        else:
            print(f"Number {number} is  a prime.")
    except ValueError:
        print("Invalid Input, allow only integers.")
prime()"""
#fibonnaci
"""def fibonnaci():
    try:
        number=int(input("Number: ").strip())
        a,b=0,1
        for i in range(a,number+1):
            print(a,end='')
            a,b=b,a+b
    except ValueError:
        print("Invalid Input, allow only integers.")
fibonnaci()"""
#largest
"""def largest():
    numbers=[]
    try:
        for number in range(5):
          number=int(input("Number: ").strip())
          numbers.append(number)
    except ValueError:
        print("Invalid Input, allow only integers.")
    largest=max(numbers)
    print(f"Largest: {largest}")
largest()"""
"""def largest():
    numbers=[]
    try:
        for number in range(5):
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
        for number in range(5):
          number=int(input("Number: ").strip())
          numbers.append(number)
    except ValueError:
        print("Invalid Input, allow only integers.")
    largest= second = numbers[0]
    for num in numbers:
        if num > largest:
          second = largest
          largest=num
        elif num> second and num != second:
           second = num
    print(f"Second Largest: {second}")
largest()
"""
#1️⃣ Palindrome Checker
"""def palindrome():
    word=input("Word: ").strip()
    reverse=word[::-1]
    if word == reverse:
        print(f"This word {word} is palindrome.")
    else:
        print(f"This word {word} is not palindrome.")


palindrome()"""
"""def reverse():
    try:
        number=int(input("Number: ").strip())
        reverse=0
        while number >0:
          digit= number % 10
          reverse=reverse* 10 + digit
          number //=10
        print(f"Reverse: {reverse}")
    except ValueError:
        print("Invalid Input, allow only integers.")
reverse()"""
#armstrong
def armstrong():
    num=int(input("Number: ").strip())
    num_digit=len(str(num))
    sum=0
    temp= num
    while temp >0:
        digit= temp % 10
        sum += digit ** num_digit
        temp//=10
    if sum == num:
        print(f"Number {num} is an Armstrong.")
    else:
        print(f"Number {num} is not an Armstrong.")
armstrong()


