error = 'fatal: [server1]: FAILED! => {"changed": "false", "msg": "No matching package available"}'

err_details_lst = error.split('=>') 

str1 = err_details_lst[1]

output = str1.replace('{', '').replace('}', '')

print(output)
