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

**ANTIQUE CAR SEARCH**

Your task is to write a python program that would read the provided file containing a list of Antique cars. For each car, the file provides the Model, MPG, Horsepower and Origin. Given the information in the file, implement the following features:

Feature #1: Search Car:
This feature allows user to search the database based on the minimum mile per gallon (MPG) and Horsepower. Once user input the minimum required MPG and horsepower, the program should display the cars that match the criteria.

Feature #2: Best and Worst Green Cars:
This feature would report the average MPG of all the cars in the system along with the car that has the best and the worst MPG.

Feature #3: Inventory By Origin:
We time to time would like to see how many american, european, japanese, taiwanese etc. cars in the inventory. Ask user for the origin and display how many cars from that origin we have in the database.

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

*******************************************

**VACCINATION TRACKER**

Our task is to write a program to track vaccination in our community.

Feature 1: This feature allows us to enter vaccination records for a person. We enter the name of the person (there is no-one with the same name in our community) along with the date at which he/she was vaccinated. The date is entered as an integer (a number) as days since Jan 01, 2021. This makes it easier for you to do date calculations. For example, 200 means 200 days past Jan 01, 2021 -- which happens to be July 20, 2021. From your perspective, you will only work with the integer numbers (days) and you don’t have to worry about the actual date (month/day/year). If the person already has 2 vaccines, warn the user and do not allow entering a new vaccination record. Each person can get at most two shots of the vaccine.

Feature 2: Let the user enter today’s date as a number (as explained above) and then find those people who had received one shot over 30 days ago. They are due for the second shot, report the person on screen. If no one is found, display an appropriate message.

Feature 3: display the number of people (along with percentage) who received one shot and both shots. For those received both shots display the average days between their shots. Make sure to create a function called “Percentage” -- this function takes in 2 numbers as input arguments and returns the percentage. For example, if I call this function with values 10 and 20, it returns back 50 -- where 10 is 50% of 20. Use the “Percentage” function to calculate the percentage of one whot and two shots to total vaccinated. If no vaccination records are found display appropriate messages on screen. Your program should not crash if no one had two shots.

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
