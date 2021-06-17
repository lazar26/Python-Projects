tracker = {} # empty dictionary is created. data gets inputted here as code runs
choice = 777 # any value not 0
while choice != 0: # while loop will run as long as choice is not 0
    print("Vaccination Tracker")
    print("========================")
    print("1-Enter Vaccination Record")
    print("2-Due for Vaccine Report")
    print("3-Vaccinated Report")
    print("0-Exit")
    print("")
    choice = int(input("choice? "))
    if choice == 1:
        def record(): # record function is created here
            print("")
            name = input("Name: ")
            if name not in tracker: # if the name entered is not found in the tracker dictionary
                print("")
                date = int(input("Enter your vaccination date as a whole number as days since Jan 01, 2021: "))
                tracker[name] = [] # an empty array is created here creating a list dictionary
                tracker[name].append(date)  # date is added in sequential order in the tracker[name] array
            else: # if the name entered is found in the tracker dictionary
                if len(tracker[name]) < 2:  # if the length of the tracker[name] array is less than two
                    print("")
                    date = int(input("Enter your vaccination date as a whole number as days since Jan 01, 2021:  "))
                    tracker[name].append(date)  # date is added in sequential order in the tracker[name] array
                else:  # if the length of the tracker[name] array is 2 or more
                    print("")
                    print("2 shots of the vaccine were already administered. Each person can get at most two shots.")
        record() #calling the record function
    elif choice == 2:
        def vaccine_report(): #vaccine_report is created here
            print("")
            date = int(input("today's date as a whole number as days since Jan 01, 2021:  "))
            if len(tracker) != 0: # if the length of the tracker dictionary is not 0 meaning it contains values
                for i in tracker:# for each value in the tracker dictionary
                    if len(tracker[i]) == 1 and (date - tracker[i][0] > 30):  # if the length is 1 in the list dictionary and the difference between today's date and the date inputted for the key value at 0 index in the list dictionary is greater than 30
                            print(str(i) + " is due for the second shot")
            else: # if the length of the tracker dictionary is 0 meaning it contains no values
                print("couldn't find anyone with second shot due")
        vaccine_report() #calling the vaccine_report function
    elif choice == 3:
        def vaccinated_report(tracker1): # vaccinated_report function is created here taking in a parameter of tracker1
            def percentage(vaccine, total):
                return (vaccine / total) * 100 # returns the value of which creates a percentage based upon those parameters
            if len(tracker1) > 0:  # if the length of the tracker dictionary is greater than 0 meaning if it contains at least one value
                first_vaccine = 0
                second_vaccine = 0
                total = 0
                for i in tracker1: # for each value in the tracker dictionary
                    if len(tracker1[i]) == 1: # if the length of each value in the list dictionary is 1 meaning if it wasn't repeated
                        first_vaccine += 1 # increment it by 1
                    elif len(tracker1[i]) == 2: # if the length of each value in the list dictionary  is 2 meaning if it was repeated
                        second_vaccine += 1 # increment it by 1
                        total += (tracker1[i][1] - tracker1[i][0]) # second value(at first index) minus the first value(at 0 index) in the list dictionary
                print(str(len(tracker1)) + " people are vaccinated")
                print(str(first_vaccine) + " of which pending their second shot [" + str(percentage(first_vaccine, len(tracker1))) + " %]")
                print(str(second_vaccine) + " of which have completed both shots [" + str(percentage(second_vaccine, len(tracker1))) + " %]")
                print("Average days between shots were " + str(total / second_vaccine) + " days")
            else:  #if the length of the tracker dictionary is 0 meaning if it contains no values
                print("no records found")
        vaccinated_report(tracker) # calling the vaccinated report function
    else:  # once choice is 0, while loop exits and this else code is ran
        print("Thank you for using the tracker.")
    if choice == 1 or choice == 2 or choice == 3:
        print("")

