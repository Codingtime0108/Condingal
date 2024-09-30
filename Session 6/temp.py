#What is the temp there?
#Is it summer or winter
#Humidity, wind speed
temp = int(input("Please enter the temp in your area today:"))
if temp>20:
    print("Summer season!")
elif temp<20:
    print("Chilly!")
else:
    print("Your temp is the same as 20 degrees")

hum = int(input("Please enter the humidity percentage in your area today:"))
if hum>70:
    print("Quite some humidity!!!")
else:
    print("Your area is not too polluted!")

wind = int(input("Please enter the wind speed in your area today:"))
if wind>4:
    print("Quite windy!!!")
else:
    print("Your area is not too windy!")