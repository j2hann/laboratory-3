salary = int(input("Enter your monthly salary: "))
loan = int(input("Enter your desired loan: "))

loanLimit = salary * 10
if loan > loanLimit:
    print("You are not qualified for the loan. Reason: Your loan is 10 times higher than your monthly salary.")
else:
    months = int(input("How many months to pay?: "))

interest = loan * 0.10
totalPayback = interest + loan
monthlyLoanPayment = totalPayback / months
monthlyLoanPayment = round(monthlyLoanPayment, 2)

print("You are going to pay " + str(totalPayback) + " within " + str(months) + " months.")
print("Your monthly payment is: " + str(monthlyLoanPayment))