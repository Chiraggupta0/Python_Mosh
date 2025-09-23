def multiply(*numbers):
    total=1
    for number in numbers:
        total *=number
    return total

print(multiply(2,3,4,5))

# here we have passed tuple as argument and used it as parameter we can use it by passing it by using * in parameter of the function
