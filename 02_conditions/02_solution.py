age = int(input("enter your age : "))
day = input("enter today : ")

price = 12 if age >= 18 else 8
if(day.lower() == "wednesday"):
    price = price-2
print(f'your age is: {age} and  your movie price is : {price}')
          
