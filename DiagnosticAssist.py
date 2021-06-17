class Diagnostic:  # a diagnostic class is created here
    def __init__(self,name,symptoms): # a constructor that allows us to create 2 attributes within the class. Self allows for internal access for its own attributes in the class.
        self.name=name # each attribute is assigned to a self value to a new name in line 3 - 4
        self.symptoms=symptoms
    def name(self): #creates a function of its own class attribute. Applies to line 5 and 7
        return self.name  # returns the assigned self value. Applies to line 8
    def symptoms(self):
        return self.symptoms

f = open("diagnostic.txt", "r") # The diagnostic txt file is opened in read only mode
lines = f.read().split("\n")  #The file is read and then separated/split by new lines
f.close() # The file is closed
diseases=[] #creates an empty array of which values will be inputed as code runs
for line in lines: # for each line in separated lines
    column = line.split()  #each line is separated by an empty space. each section separated is called a column
    disease = column[0] #disease is the first column at the 0th index
    symptom = column[1] # symptom is the second column at the first index
    if len(diseases)==0 or disease != diseases[-1].name: #if the length of the diseases list is 0 or if the name of the disease is not equal to the last disease name
        diseases.append(Diagnostic(disease,[str(symptom)])) # diseases in the diagnostic class along with the symptoms in str format as a list is appended to the list in sequential order
    else:
        diseases[-1].symptoms.append(str(symptom)) #symptoms in str format is added to symptoms attribute from the last element in the diseases list
while True:  # Code will run until if a break condition is satisfied later in the code
    print("1- Display Disease Count")
    print("2- Symptom Count by Disease")
    print("3- Diagnose")
    print("0- Exit")
    choice = int(input("What do you want to do: ")) #gives user the choice to select option 0-3
    print("")
    if choice==1:
        def display(diseases1): #creates a display function that takes in diseases1 as its parameter. Added numbers to the end of names to avoid global variables
            print("There are " + str(len(diseases1)) + " diseases in the database.") # prints the lengths of the array. This value is the number of diseases.
        display(diseases) #calls the display function that takes in the diseases parameter
    elif choice==2:
        def num_symptoms(diseases2): #creates a num_symptoms function that takes in diseases2 as its parameter. Number is 2 because it conflicts with diseases1 if choice is 1
            for disease1 in diseases2:# for each disease in the list of diseases
                print("There are " + str(len(disease1.symptoms)) + " symptoms for " + disease1.name) #prints the number of symptoms for each disease name.
        num_symptoms(diseases) #calls the num_symptoms parameter that takes in the diseases parameter
    elif choice==3:
        def diagnose(diseases3): #creates a diagnose function that takes in diseases3 as its parameter. Number is 3 because it conflicts  with diseases2 if choice is 2
            symptom1 = input("What is your symptom? ") #asks user to input the symptom he or she is feeling
            for disease2 in diseases3:  #for each disease in the list of diseases
                if symptom1 in disease2.symptoms:  # if the inputed symptom is in the symptoms self attribute in the class
                    print("You may have " + disease2.name + ".")   #prints the name of the disease
        diagnose(diseases) #calls the diagnose function that takes in diseases as its parameter
    if choice == 1 or choice == 2 or choice == 3 or choice == 4:
        print("")
    if choice == 0:
        break
