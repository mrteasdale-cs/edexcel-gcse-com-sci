#Globals
adults = 0
children = 0
crispsToOrder = 0
rollsToOrder = 0
cheeseToOrder = 0

#main
adults = 30 #int(input("Enter number of adults: "))
children = 40 #  int(input("Enter number of children: "))

partialCrisps = (adults * 0.75) + (children * 0.33)
print(f"Partial bags of crisps: {partialCrisps:.1f}")

crispsToOrder = (adults + children) * 1
print(f"Full bags of crisps to order: {crispsToOrder}")

cheeseRequired = (adults * 40) + (children * 30)

if cheeseRequired <= 500:
    print("order one pack of cheese")
else:
    cheeseToOrder = (cheeseRequired // 500) + 1  # get the number of cheese to order using integer division and adding 1 to solve for the logic
    print(f"Full packs of cheese to order: {cheeseToOrder}.")

rollsRequired = (adults * 1.5) + (children * 0.5)

if rollsRequired <= 24:
    print("order one pack of rolls")
else:
    rollsToOrder = round(rollsRequired / 24) + 1 # get the number of rolls to order using integer division and adding 1 to solve for the logic
    print(f"Full packs of rolls to order: {rollsToOrder}.")


