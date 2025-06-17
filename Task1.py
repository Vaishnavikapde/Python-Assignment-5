student_marks = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "David": 88,
    "Eva": 76
}
name= input("enter student name : ")
if name in student_marks:
    print(f"{name}'s marks : {student_marks[name]}")
else:
    print("Student not found in records")