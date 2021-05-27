class Ticket: # a parking class is created here
    def __init__(self,tnumber,amount,pnumber): # a constructor that allows us to create 3 attributes within the class. Self allows for internal access for its own attributes in the class.
        self.ticket_number = tnumber # each attribute is assigned to a self value to a new name in line 3 - 5
        self.plate_number = pnumber
        self.dollar_amount = amount
        self.status = "Unpaid"
    def tnumber(self): #creates a function of its own class attribute. Applies to line 9, 11, and 13
        return self.ticket_number  # returns the assigned self value. Applies to line 10, 12, 14
    def pnumber(self):
        return self.plate_number
    def amount(self):
        return self.dollar_amount
    def status(self):
        return self.status
    def change_in_status(self): #creates a function of its own class attribute
        self.status="Paid" # "Paid" is assigned to its own status attribute if change_in_status called
list_of_tickets = [] # an empty array of which values will be placed as code runs
while True: # Code will run until if a break condition is satisfied later in the code
    print("PARKING TICKET SYSTEM")
    print("1 - Create a New Parking Ticket")
    print("2 - Pay a Parking Ticket")
    print("3 - Report by Plate Number")
    print("4 - Grand Report")
    print("5 - Exit")
    choice = int(input("Select an option: ")) #gives user the choice to select option 1-5
    if choice == 1:
        def create(): # creates a Create function
            ticket_number = int(input("What is the ticket number (a number between 1-20000?: "))
            amount = int(input("What is the dollar amount on the ticket(currency)?: "))
            plate_number = input("What is the plate number of the car?:  ")
            list_of_tickets.append(Ticket(ticket_number,amount,plate_number)) #inputed values are assigned to the class attributes and are appended to the list in sequential order
        create() # calls the create function
    elif choice == 2:
        ticket_number1 = int(input("What is the ticket number (a number between 1-20000?: "))
        def pay(ticket_number2): #creates a pay function with ticket_number2 as its parameter
            for each_ticket in list_of_tickets: # for each ticket in the list of multiple tickets
                if each_ticket.tnumber() == ticket_number2: #if each ticket number is equal to inputed ticket number
                    each_ticket.change_in_status() #the status of each ticket is changed to Paid from Unpaid
                    print("You have payed the parking ticket.")
                    return #returns the condition
        pay(ticket_number1) # calls the pay function with the inputed ticket number as its parameter
    elif choice == 3:
        plate_number1  = input("What is the plate number of the car?: ")
        def report(plate_number2): # creates a report function with plate_number 2 as parameter. Added numbers at the end to avoid global variables.
            total = 0 # starts with 0
            #print("Tickets associated with the above plate: ")
            for each_ticket in list_of_tickets:  # for each ticket in the list of multiple tickets
                if each_ticket.pnumber() == plate_number2: # if plate number for each ticket is equal to the inputed value
                    print("Tickets associated with the above plate: " + str(each_ticket.tnumber())) # prints the number of tickets with that certain plate numbers
                    total += float(each_ticket.amount()) #the amount of each ticket is added to the total for each iteration if satisfied. Float because value can contain decimals
                    if each_ticket.status == "Paid": # if the status of each ticket is paid
                        total = 0 #total goes back to 0 for that iteration
            print("Total amount owed: " + str(total)) #prints out the total
        report(plate_number1) #calls the report function with the inputed plate number as the parameter
    elif choice == 4:
        def grand_report(): # creates a new function called grand report
            unpaid = 0 # 0 for now, essentially creates the variable
            paid = 0 # 0 for now, essentially creates the variable
            for each_ticket in list_of_tickets: # for each ticket in the list of tickets
                if each_ticket.status == "Paid": # if the status of each ticket is paid
                    paid +=1 #paid value increases by one for each iteration
                    print("Ticket Number: " + str(each_ticket.tnumber())) #prints ticket number
                    print("Plate Number: " + str(each_ticket.pnumber())) #prints plate number
                    print("Amount: " + str(each_ticket.amount())) #prints the amount for each ticket
                    print("Status: " + "Paid"+ "\n") # prints paid
                elif each_ticket.status == "Unpaid": # if the status of each ticket is unpaid
                    unpaid +=1 #unpaid value increases by one for each iteration
                    print("Ticket Number: " + str(each_ticket.tnumber())) #prints ticket number
                    print("Plate Number: " + str(each_ticket.pnumber())) #prints plate number
                    print("Amount: " + str(each_ticket.amount())) #prints the amount for each ticket
                    print("Status: " + "Unpaid" + "\n")  # prints unpaid
            print("Number of Paid Tickets: " + str(paid)) # prints number of paid tickets
            print("Number of Unpaid Tickets: " + str(unpaid)) # prints number of unpaid tickets
        grand_report() #calls the grand report function
    if choice == 1 or choice ==2 or choice == 3 or choice == 4:
        print("")
    if choice == 5:
        break