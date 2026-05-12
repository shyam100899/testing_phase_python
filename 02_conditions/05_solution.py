weather = input("enter type of weather\n")
weathertype = weather.lower()

if weathertype  == "sunny":
    activity ="go for a walk"
elif weathertype == "rainy":
    activity =" read a book"
elif weathertype == "snowy":
    activity ="build a snowman"
print(activity)