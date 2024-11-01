
print ("Welcome to meal daily")
chield_meal = float (input("What is the price of a chield's meal?: "))
adult_meal = float(input("What is the price of an adult's meal?: "))
many_chidern = int(input("How many children are there?: "))
many_adults = int(input("How many adults are there?: "))
sale_tax_rate = float(input("What is the sale tax rate?: "))

sub_total = (chield_meal*many_chidern) + (adult_meal*many_adults)
sale_tax = sub_total * (sale_tax_rate / 100)
total = sub_total + sale_tax

print("\nSubtotal: ${:.2f}".format(sub_total))
print("Sales Tax: ${:.2f}".format(sale_tax))
print("Total: ${:.2f}".format(total))

payment_amount = float(input("\nWhat is the payment amount?: "))
change = payment_amount-total

print("Change: ${:.2f}".format(change))