year = int(input("Enter year to check, it's leap year or not : "))
if(year%4 == 0):
    if(year%100 == 0):
        if(year%400 == 0):
            print(year, " is a leap year ")
        else:
            print(year, " is not a leap year ")
    else:
        print(year, " is a leap year ")
else:
    print(year, " is not a leap year ")
