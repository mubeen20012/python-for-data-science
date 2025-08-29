#🔹 Advanced Loop Challenges
#Number Pyramid

"""number=int(input("Enter number of rows: ").strip())
for i in range(1, number +1):
    print(" " *(number-i),end='')
    for j in range(1, i+1):
        print(j, end='')
    for j in range(i-1,0,-1):
        print(j, end='')
    print()"""


"""def pyramid():
    number = int(input("Enter number of rows: ").strip())

    for i in range(1, number + 1):
        # 1. spaces
        print(" " * (number - i), end="")
        # 2. increasing numbers
        for j in range(1, i + 1):
            print(j, end="")
        # 3. decreasing numbers
        for j in range(i - 1, 0, -1):
            print(j, end="")
        # 4. new line
        print()

pyramid()"""
#Hollow Rectangle with *
"""row=int(input("Enter Row: ").strip())
col=int(input("Enter Column: ").strip())
for i in range(1,row+1):
    for j in range(1,col+1):
        if i==1 or i==row or j==1 or j==col:
            print('*',end='')
        else:
            print(' ',end='')
print()"""
#2️⃣ Armstrong Number
"""def armstrong():
    number=int(input("Number: ").strip())
    num_digit=len(str(number))
    sum_of_power=0
    tem=number
    while tem >0:
        digit=tem%10
        sum_of_power += digit ** num_digit
        tem//=10
    if sum_of_power==number:
        print(f"Number {number} is an Armstrong")
    else:
        print(f"Number {number} is not an Armstrong")
armstrong()  

    
"""
#3️⃣ Word Frequency Counter
"""def frequency():
    freq={}
    text=input("Text: ").strip()
    for word in text:
        if word in freq:
          freq[word] +=1
        else:
          freq[word]=1
    print(freq)
frequency()"""
#traingle Pattern
"""def pattern():
    number=int(input("Number: ").strip())
    for i in range(1,number +1):
        print("*" * i)
pattern()"""
#4️⃣ Diamond Pattern
def diamond():
    number=int(input("Number: ").strip())
    for i in range(1,number +1):
        print(" " *(number-i) +"*" * (2*i-1))
    for i in range(number -1,0,-1):
        print(" " *(number-i) +"*" * (2*i-1))
diamond()


        
