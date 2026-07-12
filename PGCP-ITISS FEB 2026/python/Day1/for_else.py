#Take list of student marks. 
#Print “All Pass” if all students 
#have marks greater than 50.

marks=[86,99,100,90,67,70,68,79]
for m in marks:
    print(m)
    if m <= 50:
        print("fail")
        break
else:
    print("All pass")