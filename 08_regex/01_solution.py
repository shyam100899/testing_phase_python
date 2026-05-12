import re

pattern = r"hello"
text = "hello world"
match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")



pattern = r"world"
text = "hello world"
search = re.search(pattern, text)
if search:
    print("Found:", search.group())
else:
    print("Not found")


pattern = r"\d+"  # to find all numbers
text = "There are 12 apples and 5 oranges"
result = re.findall(pattern, text)
print(result)  # Output: ['12', '5']


import re

pattern = r"\d+"
text = "There are 12 apples and 5 oranges"
matches = re.finditer(pattern, text)

for match in matches:
    print(match.group(),match.span())
    print("Found:", match.group())

import re

pattern = r"\d+"
text = "I have 12 apples and 5 oranges"
new_text = re.sub(pattern, "number", text)
print(new_text)  # Output: I have number apples and number oranges

import re

pattern = r"\s+"  # split on any whitespace
text = "This is a test"
result = re.split(pattern, text)
print(result)  # Output: ['This', 'is', 'a', 'test']


import re

pattern = re.compile(r"\d+")
text = "There are 12 apples and 5 oranges"
matches = pattern.findall(text)
print(matches)  # Output: ['12', '5']
