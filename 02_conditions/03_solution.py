score = 85
if score>=101:
    print("please verify grade")
    exit()
if score>=90:
    grade ="A"
elif score>=80:
    grade ="B"
elif score>=70:
    grade ="C"
elif score>=60:
    grade ="D"
else :
    grade ="E"
print(f"your grade is :{grade} ")


