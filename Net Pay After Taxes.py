pay_per_hour = 16.78
regular_hours = 40
overtime_rate = 10.78
insurance = 60
state_tax = .05
federal_tax = .14


overtime_pay = pay_per_hour + overtime_rate

employee_name = input("Employee Name: ")
hours_worked = int(input("Number of hours worked this week: "))
dependents = int(input("Number of dependents: "))

overtime_hours = hours_worked - regular_hours

print("--------------------------------------------------")
if hours_worked <= regular_hours:
    gross_income = hours_worked*pay_per_hour
else:
    gross_income = (regular_hours*pay_per_hour) + (overtime_hours*overtime_pay)

print("Employee's name          : " + str(employee_name))
print("Number of dependents     : " + str(dependents))
print("Hours worked             : " + str(hours_worked))

if hours_worked >= regular_hours:
    print("Overtime Hours           : " + str(overtime_hours))
else:
    print("Overtime Hours           : 0")

print("Gross Income             : $%.2f" % float(gross_income))

state_tax = gross_income*state_tax

print("State Tax Withheld @ 5%%      : $%.2f " % float(state_tax))

federal_tax = gross_income*federal_tax
print("Federal Tax Withheld  @ 14%%   : $%.2f " % float(federal_tax))

print("Worker and 2 dependents insurance     : $%.2f " % float(insurance))

if dependents > 2:
    add_insurance = (dependents-2)*35
    print("Additional dependent insurance    : $%.2f " % float(add_insurance))
else:
    add_insurance = 0
    print("Additional dependent insurance    :$%.2f " % float(add_insurance))
print("--------------------------------------")

net_pay = gross_income - state_tax - federal_tax - insurance - add_insurance
print("Net take home pay           : $%.2f" % net_pay)
