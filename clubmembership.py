#Club Membership Application
# 3 list of arrays are created here. Values will be added here as code runs.
id_number = []
age_member = []
member_fees = []
choice = 777 #random value for choice as long as it is not 0
while choice != 0: #Code will run as long as user does not answer 0 as the choice
    print("CLUB MEMBERSHIP TRACKER")
    print("=======================")
    print("1 - Add Member")
    print("2 - Report")
    print("0 - Exit")
    choice = int(input("Choice: "))
    if choice in range(3): #If choice is between 0 - 2
        if choice == 1:
            num = int(input("Member Id: "))
            age = int(input("Member Age: "))
            def add(num1,age1): #Creates an add function taking in num1 and age1 as two parameters
                id_number.append(num1) #id number is added to the id_number array in the order of sequential input
                age_member.append(age1) #age is added to the age_member array in the order of sequential input
                if age == age_member[0]: #If age is the first value in the array
                    print("You are the first member thus you are the oldest member of the club so far.")
                    print("You are the first member thus you are the youngest member of the club so far.")
                elif age == min(age_member): # If age is the smallest in the age_member array
                    print("You are the youngest member of the club so far.")
                elif age == max(age_member): #If age is the largest in the age_member array
                    print("You are the oldest member of the club so far.")
                fee = 50
                if age1 <= 25:
                    fee = 30
                    print("Your monthly fee is" + " $" + str(fee))
                elif 25 < age1 < 55:
                    fee = 50
                    print("Your monthly fee is" + " $" + str(fee))
                elif age1 >= 55:
                    fee = 15
                    print("Your monthly fee is" + " $" + str(fee))
                member_fees.append(fee)  #fees are added to the member_fees array in the order of sequential input
            add(num,age) #calls the add function
        if choice == 2:
            def report(): # Creates a report function
                print("There are " + str(len(id_number)) + " members.") #Length of the id_number array which is a number
                print("Total fees $" + str(sum(member_fees)) + " from members.") #Adds all the values in the member_fees array together.
                print("Average fee per member is $" + str(int(sum(member_fees) / len(id_number))) + ".") #Divides the sum of all values in the member_fees array together by the length of the id_number array.
                print("Average member age is " + str(int(sum(age_member) / len(id_number))) + ".") #Divides the sum of all values in the age_member array together by the length of the id_number array.
                print("Youngest member is " + str(min(age_member)) + " years old.") #Minimum value in the age_member array
                print("Oldest member is " + str(max(age_member)) + " years old.") #Maximum value in the age_member array
            report() #calls the report function
    else: #if choice is not in range(3)
        print("Invalid Entry")
        print("")
    if choice == 1 or choice ==2:
        print("")
print("bye bye!") #outside of the while loop. will run once while loop exits.


