import time

def decorator(func):
    def wrapper():
        str_time = time.time()
        print(f"Start time {str_time}")
        func()
        end_time = time.time()
        print(f"End time {end_time}")
        
        time_taken = end_time - str_time
        return time_taken
    return  wrapper
    
@decorator
def myFun():
    time.sleep(1)
    print("hello !")

a = myFun()
print(a)
