sum = count = done = 0
average = 0.0

while done != -1:
    rating = float(input("Enter next rating (1-5), -1 for done : "))
    
    if rating == -1:
        break
    
    sum += rating
    count +=1
    
average = float(sum /count)
print('The average star rating for the new coffee is: {}'.format(average, '.2d'))
    
    
