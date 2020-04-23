Write a Python Program to detect if Two Strings are Anagrams
#Anagrams => An anagram of a string is another string that contains the same characters.Ex : listen and silent
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

def checkAnagrams(string1,string2):
    mainCounter = 0
    for fchar in string1:
        charCounter = 0
        for schar in string2:
            if(fchar.upper() == schar.upper()):
                #if char found in second string no need to do further verification
                charCounter = charCounter+1
                break
        if(charCounter != 1):
            break
        else:
            mainCounter = mainCounter +charCounter
    return mainCounter

if(len(string1) == len(string2)):
    result = checkAnagrams(string1,string2)
    if(result == len(string1)):
        print("Entered strings are Anagrams")
    else:
        print("Entered strings are Anagrams")
else:
    print("Entered strings are not Anagrams")

