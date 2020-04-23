for i in range(no_of_strings):
    name = input("Enter words: ")
    Words.append(name)
#print(Words)
def LogestLenWord():
    max_len = 0
    for word in Words:
        if(len(word) > max_len):
            max_len = len(word)
            max_len_word = word
    return max_len,max_len_word

print("Longest word length along with word: ",LogestLenWord())

