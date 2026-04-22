"""
Write a function called `calculate_bill` that calculates the total cost (price * quantity)
- Run the function against quantities that we ordered on different days:
    Monday: price: 20, quantity: 5
    Wednesday: price: 21, quantity: 7
    Friday: price: 25, quantity: 3

Calculate our total costs on Saturday.
"""
def calculate_bill(price, quantity) : 
    return price * quantity

Monday=calculate_bill(20,5)
#print (Monday)
Wednesday=calculate_bill(21,7)
Friday=calculate_bill(25,3)
Saturday=Monday+Wednesday+Friday
print (Saturday)


