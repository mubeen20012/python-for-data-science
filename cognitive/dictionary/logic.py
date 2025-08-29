#✅ Beginner (Warm-up)
#Create a dictionary of 3 students with their ages. Print all names and ages.
"""def students():
    students={
        'amin':{'Age':22},
        'ali':{'Age':24},
        'bilal':{'Age':26}

    }
    for name,info in students.items():
        print(f"Name: {name} ,Age: {info['Age']}")
students()"""
#Add a new key "city" to the dictionary and update its value.
"""def students():
    students={
        'amin':{'Age':22},
        'ali':{'Age':24},
        'bilal':{'Age':26}

    }
    for name,info in students.items():
        info['City']='Lahore'
    for name,info in students.items():
        print(f"Name: {name} ,Age: {info['Age']}, City:{info['City']}")
students()"""
#Create a dictionary of 3 students with their marks in Math. Print it.
"""def students():
    students={
        'Ayesha':{'marks':22},
        'Amin':{'marks':24},
        'Anaya':{'marks':26}

    }
    for name,info in students.items():
        print(f"Name:{name} ,Marks: {info['marks']}")
students()"""
"""def students():
    students={
        'Ayesha':{'marks':22},
        'Amin':{'marks':24},
        'Anaya':{'marks':26}

    }
    print(students['Amin'])
students()"""
#Update a value:
"""def students():
    students={
        'Ayesha':{'marks':22},
        'Amin':{'marks':24},
        'Anaya':{'marks':26}

    }
    students['Ayesha']['marks']=50
    for name,info in students.items():
        print(f"Name:{name} ,Marks: {info['marks']}")
students()"""
#Add a new key-value pair: Add "Usman": 95 to the dictionary.
"""def students():
    students={
        'Ayesha':{'marks':22},
        'Amin':{'marks':24},
        'Anaya':{'marks':26}

    }
    students['usman']={'marks':45}
    for name,info in students.items():
        print(f"Name:{name} ,Marks: {info['marks']}")
students()"""
#Delete a key
"""def students():
    students={
        'Ayesha':{'marks':22},
        'Amin':{'marks':24},
        'Anaya':{'marks':26}

    }
    del students['Amin']
    for name,info in students.items():
        print(f"Name:{name} ,Marks: {info['marks']}")
students()"""
#Check if a key exists: Write a program that asks for a student name and checks if it exists in the dictionary.
"""def students():
    students={
        'Ayesha':{'marks':22},
        'Amin':{'marks':24},
        'Anaya':{'marks':26}

    }
    name=input("Enter name:  ").title()
    if name in students:
        print(f"Name:{name}, Marks: {students[name]['marks']}")
    else:
        print("Student not found.")
students()"""
#Count frequency of words in a sentence using a dictionary.
"""def frequency():
    freq={}
    words=input("Words: ").strip().title().split()
    for word in words:
      if word in freq:
        
         freq[word]+=1
      else:
         freq[word]=1
    print(freq)
frequency()"""
#Create a dictionary of squares for numbers 1–5.
"""def square():
    square={}
    for i in range(1,6):
        square[i]=i **2
    print(square)
square()"""
"""#Merge two dictionaries into one.
def merge():
    student={
        'name':'Musfira'
    }
    information={
        "city": 'Lahore'

    }
    merged={**student,**information}
    print(merged)
merge()"""
#Find the student with the highest marks from a dictionary of students.
"""def largest():
    students={
        'Ayesha':{'marks':78},
        'Amin':{'marks':68},
        'Anaya':{'marks':88}
    }
    students['Anaya']['marks']=95
    del students['Amin']
    print(students['Ayesha'])
    students['Usman']={'marks':90}
    for name,info in students.items():
        print(f"Name: {name} ,Marks: {info['marks']}")
    name=input("Name: ").strip().title()
    if name in students:
        print(f"Name: {name} , Marks: {students[name]['marks']}")
    else:
        print(f"Name {name} is not found.")
largest()"""
def square():
    square={}
    for i in range(1,6):
        square[i]=i**2
    print(square)
square()

         