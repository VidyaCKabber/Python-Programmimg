user_details = {
    'user1':'Test@123',
    'user2':'Test@1234'
}

def authentication(func):
    def wrapper(username, password, *args, **kwargs):
        if username in user_details and password == user_details[username]:
            res = func(username)
            return res
        else:
            print("Failed")
    return wrapper
        

@authentication
def login(username):
    return "Login successfull !!"
    
    
a = login('user1', 'Test@123')
print(a)
