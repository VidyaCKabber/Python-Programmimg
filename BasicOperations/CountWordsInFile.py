#Write a Python Program to Count the Number of Words in a Text File
try:
    word_count = 0
    f = open("test.txt","r")
    for line in f:
        words = line.split()
        word_count += len(words) 
    print("Number of words in a given file: ",word_count)
except IOError:
    print("File not accessible")
finally:
    f.close()