# Dictionary is created here to keep track how many $5, $4,$3,$2,$1 there are. It starts with 0 and gets incremented as the program runs.
card_dict = {
    "$5": 0,
    "$4": 0,
    "$3": 0,
    "$2": 0,
    "$1": 0
}
choice = 777 #random value for choice as long as it is not 0
while choice!= 0: # Program will run as long as user does not enter 0 as the choice.
    print("Gift Card Tracker")
    print("==================")
    print("1- Add Gift Card")
    print("2- Remove Gift Card")
    print("3- Report")
    print("0- Exit")
    choice = int(input("Choice: "))  # Gives user the choice to select which option he/she desires
    if choice in range(4): #If choice is in the range of 0 to 3. If choice is not in this range, code will execute the else part of the program in line 73.
        if choice == 1:
            code = int(input("Code: "))
            def add(code1, card_dict1): #Add function is created here. It takes parameters of code1 and card_dict1.
                if code1 >= 50000:
                    value = "$5"
                elif code1 in range(40000, 50000):
                    value = "$4"
                elif code1 in range(30000, 40000):
                    value = "$3"
                elif code1 in range(20000, 30000):
                    value = "$2"
                elif code1 in range(10000, 20000):
                    value = "$1"
                elif code1 < 10000:
                    print("Invalid code!")
                    return # exits the add function calling and returns the value
                if value in card_dict:
                    card_dict1[value] += 1  #If the value is found in the dictionary, it gets incremented by 1 based on the add function.
            add(code, card_dict) #Calls the add function
        elif choice == 2:
            code = int(input("Code: "))
            def remove(code1, card_dict1): #Remove function is created here. It takes parameters of code1 and card_dict1.
                if code1 >= 50000:
                    value = "$5"
                elif code1 in range(40000, 50000):
                    value = "$4"
                elif code1 in range(30000, 40000):
                    value = "$3"
                elif code1 in range(20000, 30000):
                    value = "$2"
                elif code1 in range(10000, 20000):
                    value = "$1"
                elif code1 < 10000:
                    print("Invalid code")
                    return
                if value in card_dict1:
                    card_dict1[value] -= 1 #If the value is found in the dictionary, it gets decreased by 1 based on the remove function.
            remove(code, card_dict) # Calls the remove function
        elif choice == 3:
            def report(card_dict1): # Creates a report function with a parameter of card_dict1
                print("You have:")
                a = 0
                b = 0
                c = 0
                for i in card_dict1: #For each value in card_dict1
                    print("    " + str(card_dict1[i]) + " " + str(i) + "-card")
                    a += card_dict1[i] # Each value in card_dict1
                    b += card_dict1[i] * int(i[-1])  # Each value in card_dict1 * the value at the end.
                    if card_dict1[i] > 0:
                        c += 1
                avg = b / c #creates an average equation
                print("Total:" + str(a) + " cards.")
                print("Average:$" + str(int(avg)))
            report(card_dict) #Calls the card_dict function
    else:
        print("Invalid entry")  # If choice is not in range (4)
        print("")
    if choice == 1 or choice== 2 or choice == 3:
        print("")
