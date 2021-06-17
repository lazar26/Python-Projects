f = open("cars.txt", 'r') # The cars txt file is opened in read only mode
lines = f.read().split("\n") #The file is read and then separated/split by new lines
f.close() # The file is now closed
cars_data = [] # Creating an empty list/array for values to be entered here as code runs
for line in lines: # for each line in separated lines
    cars_data.append(line.split())  #each line is separated by an empty space of which is added onto the cars_data array
while True:
    print("Welcome to Antique Car Search") # gives user options in the form of a menu ( line 8 - 13)
    print("=============================")
    print("1 - Search Car")
    print("2 - Green Best/Worst Report")
    print("3 - Car Origin Report")
    print("0 - Exit")
    choice = int(input("What do you want to do? ")) # asks the user for his choice
    if choice == 1:
        mpg = int(input("Required Min. MPG: "))     # asks the user for required minimum mpg
        horsepower = int(input("Required Min. Horsepower: "))  # asks the user for required minimum horsepower
        def search_car(cars_data1, mpg1, horsepower1): # a search_car function is created here that takes in three parameters
            repetition = 0
            for i in cars_data1: # for each value in the array
                if float(i[1]) >= mpg1 and float(i[2]) >= horsepower1: # if the the second value at first index is greater than or equal to mpg and if the third value at second index is greater than or equal to horsepower. Float because values contain decimals
                    repetition += 1 # adding one to a repetition variable for each iteration of the for loop
                    print(str(repetition) + "-  " + i[0]) #prints the current value of the repetition + the first value at the 0th index
            print("Found " + str(repetition) + " cars matching the criteria.")
        search_car(cars_data, mpg, horsepower) #calls the search_car function taking in these three parameters (array and the two values inputed by user)
    if choice == 2:
        def best_worst(cars_data1):  # a best_worst function is created here that takes in one parameter
            best = 0 # creates best variable
            total = 0 # creates total variable
            worst = 77777 # any random large value creating worst variable
            for i in range(len(cars_data1)): # for each value in the range of the length of the cars_data array
                amount = float(cars_data1[i][1]) #sets the the second value (at first index) at the ith position int he cars_data array to an amount variable
                if amount < worst:# if the amount is less than a significantly large number
                    worst = amount # sets the values for both of these variables as the same
                    worst_mpg = i #sets the ith index to the worst_mpg variable of which is created
                elif amount > best: # if the amount is greater than 0
                    best = amount # sets the values for both of these variables as the same
                    best_mpg = i #sets the ith index to the best_mpg variable of which is created
                total += amount #total variable is incremented by amount for each iteration
            print("Avg. MPG of all cars is:", round(total / len(cars_data1), 4)) #Average is the total divided by the length of the cars_data array. Round for 4 decimal places
            print("Greenest car is: " + str(cars_data1[best_mpg][0]) + " with " + str(cars_data1[best_mpg][1])) #prints the first value based upon the ith index criteria in the previous for loop for best_mpg
            print("Worst car is: "  + str(cars_data1[worst_mpg][0]) + " with " + str(cars_data1[worst_mpg][1])) #prints the first value based upon the ith index criteria in the previous for loop for worst_mpg
        best_worst(cars_data) #calls the best_worst function taking in the array as the parameter
    if choice == 3:
        origin = input("Enter Origin: ") #asks user for origin of choice
        def invent_origin(cars_data1, origin1):  # a invest_origin function is created here that takes in two parameters
            amount = 0 # creates amount variable
            for i in cars_data1: # for each value in the cars_data array
                if i[3] == origin1: # if the 4th item at the 3rd index is equal to the user origin
                    amount += 1 #amount gets incremented by 1
            print("We have " + str(amount) + " " + str(origin) + " cars in the inventory.") #Adds amount and origin into a sentence together
        invent_origin(cars_data, origin) #calls the invent_origin function taking in the array and inputed origin as the parameter
    if choice == 1 or choice == 2 or choice == 3:
        print("")
    if choice == 0:
        break
print("Thank you for using Antique Car Search")
print("Press any key to continue . . . _")