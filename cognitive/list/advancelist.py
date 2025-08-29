#1. Flatten a Nested List
"""def flattern():
    nested=[1, [2, 3], 4]
    flat=[]
    for item in nested:
        if isinstance(item,list):
            for i in item:
                flat.append(i)
        else:
            flat.append(item)
    print(flat)
flattern()"""
"""def flattern():
    nested=[1, [2, 3], [4, [5, 6]], 7]
    while any(isinstance(i,list)for i in nested):
        flat=[]
        for item in nested:
            if isinstance(item, list):
                flat.extend(item)
            else:
                flat.append(item)
        nested=flat
    print(nested)
flattern()"""
#[1, [2, 3], 4]
"""def flattern():
    nested=[1, [2, 3], 4]
    flat=[]
    for item in nested:
        if isinstance(item,list):
            for i in item:
                flat.append(i)
        else:
            flat.append(item)
    print(flat)
flattern()"""
#[1, [2, 3], [4, [5, 6]], 7]
"""def flattern():
    nested=[1, [2, 3], [4, [5, 6]], 7]

    while any(isinstance(i,list)for i in nested):
        flat=[]
        for item in nested:
            if isinstance(item,list):
                flat.extend(item)
            else:
                flat.append(item)
        nested=flat
    print(nested)
flattern()"""
"""def rotate():
    numbers=[1,2,3,4,5]
    first=numbers[0]
    reset=numbers[1:]
    rotate=reset + [first]
    print(rotate)
rotate()"""
#Remove Duplicates
"""def duplicate():
    duplicate=[]
    numbers= [1,2,2,3,4,4,5]
    for num in numbers:
         if num not in duplicate:
           duplicate.append(num)
    print(f"Duplicate: {duplicate}")
duplicate()"""
def pair():
  numbers= [2, 4, 3, 7, 5, -1]
  target=6
  pair=[]
  for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
      if numbers[i] + numbers[j]==target:
        pair.append((numbers[i],numbers[j]))
  print(pair)
pair()