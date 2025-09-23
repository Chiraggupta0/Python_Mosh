#  there are two types of functions
# 1-- perform a task
#  2- return a value

def greet(name):
    print(f"hi {name}")


def get_greeting(name):
    return f"bye {name}"


message=get_greeting("chirag")
print(message)
file= open("content.txt","w")
file.write(message)