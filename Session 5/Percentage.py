print("Enter marks obtained in 4 subjects:")

maths = int(input("Enter marks obtained in maths:"))
english = int(input("Enter marks obtained in english:"))
science = int(input("Enter marks obtained in science:"))
computer = int(input("Enter marks obtained in computer:"))

total = maths+english+science+computer

print("These are your total marks out of 400 are", total)
percent = (total/400)*100
print("This is your total percent",percent)