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