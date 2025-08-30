#Mini-Project – Student Record System
students={
    1:{'name':'Ali','Age':22,'marks':77},
    2:{'name':'bilal','Age':22,'marks':77},
    3:{'name':'ayesha','Age':22,'marks':77},
    4:{'name':'Amin','Age':22,'marks':77}

}
def display_students():
 for id,information in students.items():
    print(f"ID: {id},Name: {information['name']},Age: {information['Age']},Marks: {information['marks']},")
def add_students():
  try:
    new_id=max(students.keys()) +1
    name=input("Name: ").strip().title()
    age=int(input("Age: ").strip())
    marks=int(input("marks: ").strip())
    students[new_id]={"name": name,"Age": age,'marks':marks}
    print(f"student {name} addedsuccessfully.")
  except ValueError:
    print("Invalid Input, allow only integers.")
def update_marks():
  try:
    student_id=int(input("Enter Student id to update marks: ").strip())
    if student_id in students:
      new_marks=int(input("Enter New Marks: ").strip())
      students[student_id]['marks']= new_marks
      print(f"Marks updated for {students[student_id]['name']}")
    else:
      print("Student ID not Found.")
  except ValueError:
    print("Invalid Input,allow only integers.")
def delete_students():
  try:
    student_id=int(input("Enter student id: ").strip())
    if student_id in students:
      name=students[student_id]['name']
      del students[student_id]
      print(f"Student {name} deleted Successfully.")
    else:
      print("Student ID not found.")
  except ValueError:
    print("Invalid Input,allow only integers.")
def search_students():
  name=input("Enter Student Name to search: ").strip().title()
  found=False
  for id,iformation in students.items():
    if iformation['name']==name:
      print(f"ID: {id}, Name: {iformation['name']}, Age: {iformation['Age']}, Marks: {iformation['marks']},")
      found=True
  if not found:
    print("Student not found.")
def class_average():
  if students:
    total=sum(iformation['marks'] for iformation in students.values())
    average=total/ len(students)
    print(f"Class Average Marks: {average:.2f}")
  else:
    print("No students in the system.")


  
while True:
  print("\n---Student Record System---")
  print("1.Display Student")
  print("2.Add Student")
  print("3.Update Student")
  print("4.Delete Student")
  print("5.Search Student")
  print("6.Class Average")
  print("7.Exit")





  choice=int(input("Choice: ").strip())
  if choice==1:
    display_students()
  elif choice==2:
    add_students()
  elif choice==3:
    update_marks()
  elif choice==4:
    delete_students()
  elif choice==5:
    search_students()
  elif choice ==6:
    class_average()
  else:
    print("Invalid Choice! please Select a Valid option.")



