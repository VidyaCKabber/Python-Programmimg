#*
#**
#***
#****
#*****

def show_stars(rows):
    for i in range(rows):
        for j in range(i+1):
            print("*",end="")
        print("\n")
show_stars(5)
