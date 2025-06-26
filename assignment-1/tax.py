# gross_salary 
# taxable_income
# tax_payable
# net_salary

name=input("Enter your name: ")
emp_Id=int(input("Enter you ID: "))
basic_salary=float(input("Enter Basic Monthly Salary: "))
special_allowances = float(input("Enter Special Allowances (Monthly): "))
bonus_percentage = float(input("Enter Bonus Percentage (Annual, as % of Gross Salary): "))
gross_monthly_salary = basic_salary + special_allowances
annual_salary_without_bonus = gross_monthly_salary * 12
bonus_amount = (bonus_percentage / 100) * annual_salary_without_bonus
total_annual_gross_salary = annual_salary_without_bonus + bonus_amount

print(" SALARY OF EMPLOYEE")
print("Name of employee: ",name)
print("Employee id :",emp_Id)
print("Gross monthly salary is: ",gross_monthly_salary)
print("Annual gross salary is: ",total_annual_gross_salary)

#LEVEL 2
standard_deduction=50000
taxable_income=total_annual_gross_salary+standard_deduction
print("taxable income(in Rs.) : ",taxable_income)



# LEVEL 3
tax = 0

# Calculate tax based on slabs
if taxable_income <= 300000:
    tax = 0
elif taxable_income <= 600000:
    tax = (taxable_income - 300000) * 0.05
elif taxable_income <= 900000:
    tax = (300000 * 0) + (300000 * 0.05) + (taxable_income - 600000) * 0.10
elif taxable_income <= 1200000:
    tax = (300000 * 0) + (300000 * 0.05) + (300000 * 0.10) + (taxable_income - 900000) * 0.15
elif taxable_income <= 1500000:
    tax = (300000 * 0) + (300000 * 0.05) + (300000 * 0.10) + (300000 * 0.15) + (taxable_income - 1200000) * 0.20
else:
    tax = (300000 * 0) + (300000 * 0.05) + (300000 * 0.10) + (300000 * 0.15) + (300000 * 0.20) + (taxable_income - 1500000) * 0.30

# Section 87A Rebate
if taxable_income <= 700000:
    tax = 0

# 4% Health and Education Cess
cess = tax * 0.04
total_tax_payable = tax + cess


print(f"Total tax payable: ₹{total_tax_payable:.2f}")

#level 4
net_salary = total_annual_gross_salary - total_tax_payable
print("Annual Gross Salary: ",total_annual_gross_salary)
print("Total Tax Payable (including cess): ",total_tax_payable)
print("Annual Net Salary is :",net_salary)

