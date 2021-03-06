# Python-Projects

**PARKING TICKET**

1) Create a New Parking Ticket: 

The police officers use this feature to enter parking tickets they write every day into the system. For each ticket, system asks for the ticket number (a number between 1­20000), the dollar amount on the ticket (currency) and the plate number of the car (it is really a text with no spaces). Each ticket has a status flag associated with it ­­ either paid or unpaid. Upon entering a ticket into the system, the status of that ticket is automatically set to unpaid.

2) Pay a Parking Ticket:

Upon payment received, we would like to mark the tickets as paid. The officer enters the ticket number, the program should find the ticket and change its status to paid. 

3) Report by Plate Number: 

The officer enters a plate number and the program lists all tickets associated with that plate number and displays the total money owed ­­ sum the amounts on each ticket and display the result as total amount owed.

4) Grand Report: 

Displays all the tickets in the program along with their paid/unpaid status. It also reports the number of paid tickets and the number of unpaid are in the system. 

5) Exit: 

Exits the program.

-----------------------------------------

**DIAGNOSTIC ASSIST**

Your job is to write a program that would allow us to diagnose diseases based on a given symptom.

Feature #1:
Display # of Diseases:
This will display the number of diseases in the system -- NOT the symptoms!
Notice that diseases are in order in the file -- you can take advantage of this. Go through each disease in the system and whenever you see that the current record’s disease name is different than the previous record’s disease name, then increment a counter. 

Feature 2: 
Number of Symptoms per Disease Report:
This will display how many symptoms are in the system for ​each disease.

Feature 3: 
Diagnose:
This will ask user for a symptom and display all diseases that have that symptom.

-----------------------------------------
**ANTIQUE CAR SEARCH**

Your task is to write a python program that would read the provided file containing a list of Antique cars. For each car, the file provides the Model, MPG, Horsepower and Origin. Given the information in the file, implement the following features:

Feature #1: Search Car:
This feature allows user to search the database based on the minimum mile per gallon (MPG) and Horsepower. Once user input the minimum required MPG and horsepower, the program should display the cars that match the criteria.

Feature #2: Best and Worst Green Cars:
This feature would report the average MPG of all the cars in the system along with the car that has the best and the worst MPG.

Feature #3: Inventory By Origin:
We time to time would like to see how many american, european, japanese, taiwanese etc. cars in the inventory. Ask user for the origin and display how many cars from that origin we have in the database.

-----------------------------------------
**Input/Output Files**

INPUT:

A31 149.99
B31 49.99
A41 179.99
F31 169.99
A35 179.99
A44 169.99

OUTPUT: 

*******************************************
               TICKET REPORT
*******************************************

There are 6 tickets in the database. 

Maximum Ticket price is $179.99.
Minimum Ticket price is $49.99.
Average Ticket Price is $XXX.XX.

Thank you for using our ticket system!

-----------------------------------------

**VACCINATION TRACKER**

Our task is to write a program to track vaccination in our community.

Feature 1: This feature allows us to enter vaccination records for a person. We enter the name of the person (there is no-one with the same name in our community) along with the date at which he/she was vaccinated. The date is entered as an integer (a number) as days since Jan 01, 2021. This makes it easier for you to do date calculations. For example, 200 means 200 days past Jan 01, 2021 -- which happens to be July 20, 2021. From your perspective, you will only work with the integer numbers (days) and you don’t have to worry about the actual date (month/day/year). If the person already has 2 vaccines, warn the user and do not allow entering a new vaccination record. Each person can get at most two shots of the vaccine.

Feature 2: Let the user enter today’s date as a number (as explained above) and then find those people who had received one shot over 30 days ago. They are due for the second shot, report the person on screen. If no one is found, display an appropriate message.

Feature 3: display the number of people (along with percentage) who received one shot and both shots. For those received both shots display the average days between their shots. Make sure to create a function called “Percentage” -- this function takes in 2 numbers as input arguments and returns the percentage. For example, if I call this function with values 10 and 20, it returns back 50 -- where 10 is 50% of 20. Use the “Percentage” function to calculate the percentage of one whot and two shots to total vaccinated. If no vaccination records are found display appropriate messages on screen. Your program should not crash if no one had two shots.

-----------------------------------------
**CLUB MEMBERSHIP APPLICATION**

Our club needs a software that can keep track of our members. Here are the features of the program

1) Add Member:
a) Using this feature, we will input the ID number (an integer number) of the member along with the age of the member into the program. [30 points]
b) If this is the youngest or the oldest member that has ever been entered into the system, then the program should output either “You are the youngest member of the club so far.” or “You are the oldest member of the club so far.” respectively. [30 points]
c) The program should determine the monthly membership fee for the member based on member’s age and display on the screen upon entering the new member. Normally the fee is $50 per month per member, but if the member is younger than or equal to 25, the fee is $30 per month. If the member is older than and equal to 55, the fee is $15 per month.

2) Report:
a) Display the total number of members entered into the system. [30 points]
b) Display the total monthly membership fees to be collected and average membership fee per member. [30 points]
c) Display the average age of the members along with the youngest and oldest age. [30 points]

3) Exit

-----------------------------------------
**TARGET GIFT CARD TRACKER**

Your task is to write a simple app that allows to keep track of my gift cards from Target store. Here are the features of this program:

Feature #1 (60 points):​ ​Add a Gift Card:​ I should be able to add a gift card to the program. I will enter the gift card code which is a number. The value of the gift card (the amount of money in it) can be determined by this number.
If the card code is above (or equal) 50000, then it has $5 value in it. The cards with code at 40000s (40000 to 49999) has $4 in it. The cards with code at 30000s (30000 to 39999) has $3 and so on all the way down to 10000s (10000 to 19999) has $1 in it. Any code less than 10000 is an invalid code number -- let the user know with a message.

Feature #2 (50 points): ​Remove a Gift Card:​ Sometimes, I may give my gift card away or spend it, in which case, I need to be able to remove the card from the system. I will enter the card code and you will determine what value the card has from the code (just like in feature #1) and remove from the system.

Feature #3 (50 points):​ ​Report: ​I should be able to get a detailed report from the program displaying how many of each type of cards ($1, $2, $3, $4 or $5 cards) I have and the total number of cards and as well as the average value of cards. This report changes as I add/remove cards from the system.


Feature #0 (20 points):​ I should be able to exit out of the program when I am done.
User will pick one of the 4 features -- if user makes an invalid choice (enters a number other than these 4 options), let the user know that it is an invalid entry. (20 points)

-----------------------------------------

**RESTARUANT RESERVATION SYSTEM**

Your job is to create a reservation system for a restaurant. The restaurant has 20 tables. Here is the functionality required for this system (you may want to display a menu and let user choose options 1 to 4, make sure to put your program in a loop so program does not exit until user chooses menu 0):

1- Reserve a Table:

User needs to input the table number (Tables are numbered from 0 to 19). If the table is not available (reserved), inform the user that the selected table is not available. If the table is available, then ask for the name (name is a single word, no space) and mark the table as reserved. 
    
2- Clear Reservation:

User needs to input the table number (Tables are numbered from 0 to 19). If the table is not reserved, inform the user that the selected table is already available (nothing to clear). If the table is reserved, mark it as available. That table is no longer reserved. 

3- Report:

Prints out the state of each table. Each table is printed on a separate line -- so your report will print out 20 rows. If reserved, it will print out the name on the reservation next to the table number. If available, it should print out "available". 
    
0- Exit Program. 

-----------------------------------------

**OFFICE RENTAL**

Your task is to write a program that will compute the monthly cost of renting an office space in our building.

We offer 3 types of offices.

1- Private Office space where customer would have his own private assigned room. The monthly rent for our private offices are $1000.

2- Coworking space where customer would share a room with one or more customers. The monthly rent for coworking is $500.

3- We also provide temporary workspaces. These spaces are rented daily (as opposed to monthly). Customer will enter how many days per month they need the office. 

We charge $60 per day.
We also provide phone service to every client regardless of their office type. If interested in our phone service, the customer should enter the estimated number of minutes they will use monthly. We charge $0.50 per minute.
Office rental charge (based on the office type) plus the phone service charge makes up the monthly charge for the customer.
The program should allow us to get an estimate without exiting the program. At the end, when we do exit, the program should tell us what was the average of estimates provided in that session. This is basically the sum of all the estimates provided divided by the number of estimates provided.

-----------------------------------------
