#  // Mortgage Calculator //

#  primary costs
print('Welcome! Want to purchase a property? Get a quick monthly mortgage estimate!')
print('Note: PMI is not implement yet.\n')

Price = int(input('1. What is the total value of the property? '))
DownPay = int(input('2. How many dollars as down payment? '))
Interest = (input('3. What is the current percent interest rate? '))
Period = int(input('4. How many years do you want to mortgage? '))
PropertyTax = int(input('5. What is the estimated percent of property tax? '))
HOA = int(input('6. Is there a monthly HOA? '))

# // PMI cost - need to refer to lender's chart conversion
#if DownPay not >= Price*0.2:
#   PMI = ((Price - DownPay) / Price) * 100

#  calculations

r = ((float(Interest) / 100) / 12)
n = (Period * 12)
pTax = PropertyTax/100 * Price / 12
hIns = 0.00238 * Price / 12

Monthly = (Price - DownPay) * r * ((1 + r) ** n) / (((1 + r) ** n) - 1) + (pTax + hIns + HOA)

print('Monthly cost: %s' % int(Monthly))
