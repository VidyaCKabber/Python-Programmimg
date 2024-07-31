class Welcome:
    def welcomeMsg(self):
        print("Wecome !!")
        

def updatedWelcomeMsg(self, name):
    print(f"Welcome {name} !!")
    
Welcome.welcomeMsg =  lambda self : updatedWelcomeMsg(self, "Vidya")

w = Welcome()
w.welcomeMsg()
