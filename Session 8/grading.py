a = int(input("Enter marks obtained in maths"))
b = int(input("Enter marks obtained in geo"))
c = int(input("Enter marks obtained in cs"))

print("These are your grades according to your scores:")
d = (a+b+c)/3
if d<=100 or d>=90:
    print("A")
elif d<90 or d>=75:
    print("B")
elif d<75 or d>=60:
    print("C")
elif d<60 or d>=45:
    print("D")
else:
    print("F")