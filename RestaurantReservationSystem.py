# Reservation System for a Restaurant
tables = []
repeat = "y"
for i in range(20): # creates 19 values (0-19)
    tables.append("Available") # available is used in each position 0-19. It's added as a individual item to the end of the list.
while repeat == "y": # code will run as long as repeat is y
    print("1 - Reserve a Table")
    print("2 - Clear Reservation")
    print("3 - Report")
    print("0 - Exit Program")
    choice = int(input("Choose an option: ")) # gives user the choice to input a value in the console
    if choice == 1:
        table_no = int(input("Input a table number [0-19]: "))
        if tables[table_no] != "Available":
            print("Selected table is not available. It has been reserved. Pick a different table number.")
        elif tables[table_no] == "Available":
            name = input("Input a name: ")
            tables[table_no] = name
            print("You have reserved this table number.")
    elif choice == 2:
        table_no = int(input("Input a table number: "))
        if tables[table_no] == "Available":
            print("Selected table is already available (nothing to clear).")
        elif tables[table_no] != "Available":
            tables[table_no] = "Available"
            print("Table is cleared and is no longer reserved.")
    elif choice == 3:
        i = 0
        for j in tables:
            i += 1
            print("Table " + str(i-1) + " " + j)
    elif choice == 0: # if user wants to exit
        repeat = "n" # repeat will be n and the while loop will exit.
