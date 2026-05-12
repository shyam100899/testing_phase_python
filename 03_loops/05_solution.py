# find the first non repeated character
input_string='teeterabab'
for char in input_string:
    print(char)
    if input_string.count(char)==1:
        print("char is :",char)
        break