course="Python programming"
print(course.upper())
print(course)
print(course.lower())
print(course.title()) 
# title gives first letter as capital
course="   Python programming"
print(course)
print(course.strip())
#  strip method will remove all the blank spaces
course="python programming"
print(course.find("pro"))
# find is used to find the index of a given substring
print(course.replace("p","j"))
#  replacing p with j
print("pro" in course)
# to check if substring is present in string or not
print("swift" not in course)
