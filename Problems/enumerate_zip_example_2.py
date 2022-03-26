# You are given with lists of years and births. You need to return year, birth and running_average as a list of tuple
# running_average --> Ex : Running average of 2019 is average of total births of 2018 and 2019

years = [2018, 2019, 2020, 2021, 2022]
births = [988991, 989134132, 999321341, 9994231, 99953143]
sum_ = 0
result = []

# enumerate --> The enumerate() function allows you to loop over an iterable object and keep track of how many iterations have occurred.

for index, (year, birth) in enumerate(zip(years, births), start =1):
    sum_ += birth
    result.append((year, birth, round(sum_)/index))
print(result)
