def increment(number,by):
    return number+by


print(increment(2,1))


#  default argument
#  here we have defined paramenter by=1 rather than defining it while calling
def increment(number,by=1):
    return number+by


print(increment(2))
