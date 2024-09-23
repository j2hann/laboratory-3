salary = int(input("Enter your monthly salary: "))

if salary < 30000:
    print("You are not eligible for a loan. Reason: Your salary is less than 30000")
else:
    loan = int(input("Enter your desired loan: "))

    loanLimit = salary * 10

    if loan > loanLimit:
        print("You are not eligible for a loan. Reason: Your loan is 10 times higher than your monthly salary.")
    else:
        print("You are eligible for a loan.")
        
        months = int(input("How many months to pay?: "))
        interest = loan * 0.10
        totalPayback = interest + loan
        monthlyLoanPayment = totalPayback / months
        monthlyLoanPayment = round(monthlyLoanPayment, 2)

        print("You are going to pay " + str(totalPayback) + " within " + str(months) + " months.")
        print("Your monthly payment is: " + str(monthlyLoanPayment))
