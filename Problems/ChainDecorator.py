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

# When you call display_msg(msg), Python first looks at the innermost decorator, which is decorator1.
# It then looks at the next decorator, which is decorator2.
# Finally, it looks at the outermost decorator, which is decorator1.
# The display_msg function is wrapped in decorator1, so the wrapper function of decorator1 is called.
# Inside wrapper of decorator1, it prints "*******************".
# Then, it calls the next decorator in the chain, which is decorator2.
# Since display_msg is wrapped in decorator2 now, the wrapper function of decorator2 is called.
# Inside wrapper of decorator2, it prints "^^^^^^^^^^^^^^^^^^^^".
# Then, it calls the next decorator in the chain, which is decorator1.
# Again, display_msg is wrapped in decorator1, so the wrapper function of decorator1 is called.
# Inside wrapper of decorator1, it prints "*******************".
# Now, it finally calls the original display_msg function, passing the message msg to it.
# Inside display_msg, it simply prints the message passed to it.
# After executing the original function, it starts returning back up the chain of decorators.
# It exits decorator1 and prints "*******************" again.
# Then, it exits decorator2 and prints "^^^^^^^^^^^^^^^^^^^^" again.
# Finally, it exits the outermost decorator1 and prints "*******************" one last time.
