CP= float(input("Enter the cost price: "))
SP= float(input("Enter the selling price: "))
if SP > CP:
 profit= SP-CP
print("Profit is made of Rs.",profit)
elif CP > SP:
  Loss= CP-SP
  print("Loss is made of Rs.",Loss)
else:
  print("No Profit or Loss is Made")

