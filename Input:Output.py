f = open("input.txt", "r") # The input txt file is opened in read only mode
lines = f.read().split("\n") #The file is read and then separated/split by new lines
avg = 0      #creates variables line 3 to line 6
total = 0
highest = 0
lowest = 500 # any random large variable
for line in lines: # for each line in separated lines
    columns = line.split(" ")  #each line is separated by an empty space
    total += float(columns[1]) #value at the first index in column variable is added onto total for each iteration
    if float(columns[1]) < lowest: # if value at the first index in columns variable is less than lowest 500
        lowest = float(columns[1]) # sets the them eaual to each other
    elif float(columns[1]) > highest: # if value at the first index in columns variable is greater than highest 0
        highest = float(columns[1]) # sets the them eaual to each other
    avg = total / len(lines) # average is the total divided by the length value of the lines
f.close() # file is closed
f=open("output.txt","w") # open the output.txt file in writing mode
f.write("******************************************" + "\n") # write to the output file
f.write("               TICKET REPORT              " + "\n")
f.write("******************************************" + "\n" + "\n")
f.write("There are " + str(len(lines)) + " tickets in the database." + "\n" + "\n")
f.write("Maximum Ticket price is $" + str(highest) + "." + "\n")
f.write("Minimum Ticket price is $" + str(lowest) + "." + "\n")
f.write("Average Ticket Price is $" + str(avg) + "." + "\n" + "\n")
f.write("Thank you for using our ticket system!" + "\n" + "\n")
f.write("******************************************")
f.close() #close the output file


