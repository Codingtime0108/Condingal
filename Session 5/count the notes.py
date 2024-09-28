amount = int(input("Please enter amount for withdrawal:"))

note_1 = amount//100
note_2 = (amount%100)//50
note_3 = ((amount%100)%50)//10
note_4 = ((amount%100)%50%10)//1

print("notes of 100 rupee", note_1)
print("notes of 50 rupee", note_2)
print("notes of 10 rupee", note_3)
print("notes of 1 rupee", note_4)