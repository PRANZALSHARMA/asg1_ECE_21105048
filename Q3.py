'''Q3. Write a python program to store different data type values into a list. (For an
example: Student [SID, Name, Gender, Course Name, CGPA]).
Note: Use Gender values: ‘F’, ‘M’, ‘U’ (For Unknown).
CGPA should have floating type values (example: 7.5).'''

student_lst=[]

N=int(input('Enter the number of students in class: '))

for i in range(N):
    sid=int(input('Student ID: '))
    name=input("Student's Name: ")
    gender=input("Student's Gender\n[Note: Use Gender values: ‘F’, ‘M’, ‘U’ (For Unknown).]: ")
    course=input("Student's course: ")
    cgpa=float(input("Student's CGPA: "))

    student=[sid,name,gender,course,cgpa]

    student_lst=student_lst+[student]
print('\n\nStudent List:-\n',student_lst)
