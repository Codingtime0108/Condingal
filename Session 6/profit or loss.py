buying = int(input("How much are you buying oranges for?"))
earning = int(input("How much are you selling oranges for?"))
if buying<earning:
    print("Wow, you are having a profit")
    profit = earning - buying
    print("Here's how much your profit is:",profit)
else:
    print("Oops, you are in loss")
    loss = buying - earning
    print("Here's how much your loss is:",loss)