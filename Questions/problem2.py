# input : aabbccccccaaa
# output : a2b2c6a3

def compressList(string):
    compress_list = []
    
    if not string:
       return ""
    counter = 1
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            counter +=1
        else:
            compress_list.append(string[i-1] + str(counter))
            counter = 1
    compress_list.append(string[-1] + str(counter))  # Append the last character count
    print(''.join(compress_list))
        
compressList("aabbccccccaaa")
