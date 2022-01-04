'''Q2. Write a python program to compute a person's income tax. Assume following
tax laws:
• All taxpayers are charged a flat tax rate of 20%.
• All taxpayers are allowed a $10,000 standard deduction.
• For each dependent, a taxpayer is allowed an additional $3,000 deduction.
• Gross income must be entered to the nearest penny.
Gross Income and the number of dependents must be asked from the user.'''

print('___INCOME TAX___')

print('''• All taxpayers are charged a flat tax rate of 20%.
• All taxpayers are allowed a $10,000 standard deduction.
• For each dependent, a taxpayer is allowed an additional $3,000 deduction.
• Gross income must be entered to the nearest penny.''')

incm=float(input('\n\nEnter your income to the nearest penny(without commas): $'))

dpnd=int(input('Enter the number of dependents in family: '))

taxable_incm=incm-10000.00-(dpnd*3000)

if taxable_incm>0:
    print('Your taxable income is $',taxable_incm,sep='')
    tax=taxable_incm*0.2
    print('Income Tax =$',round(tax,2),sep='')
else:
    print("You don't have to pay income tax.\nThanks for using our service.")
