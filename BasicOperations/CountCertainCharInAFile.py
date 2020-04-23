#Write a Python Program to Count the Number of Words in a Text File
try:
    char_count = 0
    find_char = input("Enter character that you want to count it's occurance in a file : ")
    f = open("test.txt","r")
    while 1:
        char = f.read(1)
        if not char:
            break
        else:
            if(find_char == char):
                char_count = char_count + 1
    if(char_count > 0):
        print("Number of characters in a file : ",char_count)
    else:
        print(find_char," character not found in the file")
except IOError:
    print("File not accessible")
finally:
    f.close()