password ="123456"
password_len =len(password)
if password_len<6:
    strength ="weak"
elif password_len<=10:
    strength ="medium"
else:
    strength ="strong"
    
print("password strength is",strength)
