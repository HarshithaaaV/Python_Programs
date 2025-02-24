"""WAP to enter marks of 3 subjects from the user and store them in a dictionary.
Start with an empty dictionary & add one by one.Use subject name as key & marks as value. """

marks = {}
x = int(input("Enter marks: "))
marks.update({"Maths":x})
x = int(input("Enter marks: "))         
marks.update({"English":x})
x = int(input("Enter marks: "))
marks.update({"Science":x})
print(marks)