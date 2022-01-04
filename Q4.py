#Q4. Write a python program to enter marks of 5 students into a list and display them in sorted manner.

lst=[]

for i in range(5):
    name=input("Student name: ")
    lst.append(name)
lst.sort()
print("\nSorted List Of Students:-",lst,sep='\n')
