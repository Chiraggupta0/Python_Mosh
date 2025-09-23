x=input("x:")
print(type(x))
#  input always comes as string 
# y=x+1 to print this first we need to convert x to int to add 1 to it

y=int(x)+1
print(y)
print(f"x: {x}, y: {y}")

#  if we use this we will get false in boolean type
# ""          empty string
# 0
# None
print(bool(0))
print(bool(""))
