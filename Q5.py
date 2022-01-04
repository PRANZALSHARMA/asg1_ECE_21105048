'''5. List: color ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
a. Write a Python program to print a specified list after removing 4th element.
Expected output: color [Red', 'Green', 'White', 'Pink', 'Yellow']
b. Remove ‘Black’ and ‘Pink’ from the list and replace them with ‘Purple’.
Do that in one line code.'''

#a
color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color.pop(3)
print("a.\n",color)

#b
color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
del color[3:5]
print("\nb.\n",color)
