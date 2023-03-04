#PROBLEM CASE
"""
Employees  of a certain firm are paid on hourly basis.
If an employee works for not more than 40 hours a week,
the hours worked is considered regular and Overtime for hours worked beyond 40.
Regular hours are paid at 5 cedis per hour while the overtime rate is one and half times the regular rate per hour.
All employees are to pay 15% of their gross pay as Income Tax,
2.5% as National Health Contribution Levy, 1% as District Tax.
Employees who have more than three children are to pay 50 pesewas per child in excess of three towards Educational Fund
For All.
Devise a computer solution that can be used to calculate the necessary deductions as well as the Net Pay of employees.
Your display for each employee should include each deduction, net pay, and gross pay with appropriate captions.
"""

NoOfEmployees = int(input('How many employees are in the firm: '))

for i in range(NoOfEmployees):
    HoursWorked = int(input('Total Hours worked employee{}: '.format(i+1)))
    RegularRate = 5
    OvertimeRate = 1.5 * RegularRate

    if HoursWorked <= 40:
        GrossPay = RegularRate * HoursWorked
    else:
        GrossPay = RegularRate * 40 + (OvertimeRate * (HoursWorked - 40))

    NoOfChildren = int(input('Number of children per employee{}: '.format(i + 1)))

    if NoOfChildren > 3:
        EduFund = 0.5 * (NoOfChildren - 3)

        IncomeTax = 0.15 * GrossPay
        NHIL = 0.025 * GrossPay
        DistrictTax = 0.01 * GrossPay
        TotalDeductions = IncomeTax + NHIL + DistrictTax + EduFund
        NetPay = (GrossPay - TotalDeductions)

    print("Gross pay for employee {} is ${:.2f}".format(i + 1, GrossPay))
    print("Total deductions for employee {} are ${:.2f}".format(i + 1, TotalDeductions))
    print("Net pay of employee {} is ${:.2f}".format(1 + i, NetPay))

