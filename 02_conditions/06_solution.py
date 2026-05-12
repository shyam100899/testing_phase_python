distance = int(input("enter distance in km\n"))

if distance  < 3:
    transport ="walk"
elif distance < 15:
    transport ="bike"
else:
    transport ="car"
print("Ai recommends you the transport of:",transport)