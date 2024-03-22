def decorator1(func):
    def wrapper(m):
        print("*******************")
        func(m)
        print("*******************")
    return wrapper
    
def decorator2(func):
    def wrapper(s):
        print("^^^^^^^^^^^^^^^^^^^^")
        func(s)
        print("^^^^^^^^^^^^^^^^^^^^")
    return wrapper

@decorator1
@decorator2
@decorator1
def display_msg(msg):
    print(msg)
   
msg = "Hey, I'm here...."
display_msg(msg)
