#Q4. Write a python program to enter marks of 5 students into a list and display them in sorted manner.

lst=[]

for i in range(5):
    marks=float(input("Student marks: "))
    lst.append(marks)
lst.sort()
print("\nSorted List Of marks:-",lst,sep='\n')
