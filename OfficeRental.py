quote_estimate = 0
iteration = 0
rent = 0
while True:
    print("Need Office Space?")
    print("==================")
    print("1 - Private Office")
    print("2 - Colocation")
    print("3 - Temporary Workspace")
    type_space = input("What type of space? Select 1, 2, or 3. ")
    # Rent calculation based on user input selection of office
    if type_space == "1":
        rent = 1000
    elif type_space == "2":
        rent = 500
    else:
        Days_per_month_needed = int(input("How many whole days per month you need the office? We charge $60 per day. "))
        rent = 60 * Days_per_month_needed
    # Criteria if user requires phone service
    request = input("Phone service? (y/n) ")
    if request == "y":
        num_minutes = int(input("How many minute(s) do you need? "))
        phone_bill = .50 * num_minutes
    else:
        phone_bill = 0

    charge = rent + phone_bill
    from math import *
    print("Your monthly charge is " + "$" + str(floor(charge)))

    quote_estimate += charge  # Adds charges together of each iteration. This culminates to a combined quote estimate
    iteration += 1          # For every loop, iteration increases by 1
    repeat = input("Another quote (y/n)? ")
    if repeat == "y":
        print("")
    else:
        break  # Will exit out of while loop if user selects no for another quote.
print("Average quotation provided " + "$" + str(quote_estimate/iteration))    # calculates the average quote
print("Press any key to continue ...")
