#1
#Prompts the user for the number of Tests
#Note that this function will include call(s) to the input function
#Keep prompting until the number is an integer. Each grade is in between 0 and 100..
#Returns the number of Tests
def getNumberOfTests():
    while True:                                                                 
        try:                                                                   
            number = int(input("Enter the number of Tests: "))                  

        except ValueError:
            print("Please enter an integer number")    
        else:
            if(0 <= number <= 100):                                            
                break
    return number    


#2
#Prompts the user for the weigth of Assignments
#Note that this function will include call(s) to the input function
#Keep prompting until the number is a float >= 0 and <= 1
#Returns the weight of assignments
def getWeightOfAssignments():
    while True: 
        try:
            number = float(input("Enter the number for the weigth of Assignments: "))
        except ValueError:
            print("Please enter a number between 0 to 1")
        else:
            if(0 <= number <= 1):
                break
            else:
                print("Please enter a number between 0 to 1")  
    return number            


#3
#Prompts the user for the weigth of Midterms
#Note that this function will include call(s) to the input function
#Keep prompting until the number is a float >= 0 and <= 1
#Returns the weight of midterms
def getWeightOfMidTerms():
    while True: 
        try:
            number = float(input("Enter the number for the weigth of Midterms: "))
        except ValueError:
            print("Please enter a number between 0 to 1")
        else:
            if(0 <= number <= 1):
                break
            else:
                print("Please enter a number between 0 to 1")  
    return number


#4
#Prompts the user for the weigth of the final
#Note that this function will include call(s) to the input function
#Keep prompting until the number is a float >= 0 and <= 1
#Returns the weight of final
def getWeightOfFinal():
    while True: 
        try:
            number = float(input("Enter the number for the weigth of final: "))
        except ValueError:
            print("Please enter a number between 0 to 1")
        else:
            if(0 <= number <= 1):                                           
                break
    return number   


#5
#returns True if the sum of the 3 arguments is 1, False otherwise
#Assign the default values 0.4 0.35 0.25 to wAssign, wMidtern and wFinal respectively
def checkWeights(weightAssign = 0.4, weightMidterm = 0.35, wFinal = 0.25):
    if weightAssign + weightMidterm + wFinal == 1:
        return True
    return False
    


#6    
#calculate the numeric grade as specified in the course outline
def calculateNumericGrade(AvgAssignments,AvgTests,final,wOfAssign,wOfMidTerms,wFinal):                      
    percent_grade = ((AvgAssignments * wOfAssign) + (AvgTests * wOfMidTerms) + (final * wFinal))            
                                                                                                        
    print(percent_grade)
    
    if  90 <= percent_grade <= 100 :
        result = 4.0
    elif 85 <= percent_grade <= 89 :
        result = 3.8
    elif 80 <= percent_grade <= 84 :
        result = 3.6
    elif 77 <= percent_grade <= 79 :
        result = 3.3
    elif 73 <= percent_grade <= 76 :
        result = 3.0
    elif 70 <= percent_grade <= 72 :
        result = 2.7
    elif 67 <= percent_grade <= 69 :
        result = 2.3
    elif 63 <= percent_grade <= 66 :
        result = 2.0
    elif 60 <= percent_grade <= 62 :
        result = 1.7
    elif 57 <= percent_grade <= 59 :
        result = 1.4
    elif 53 <= percent_grade <= 56:
        result = 1.2
    elif 50 <= percent_grade <= 52 :
        result = 1.0
    else:
        result = 0
    return result

#7
#convert the numeric grade to a letter according to the conversion table 
#in the course outline
def calculateLetterGrade(numericGrade):
    if 3.8 < numericGrade <= 4.0 :
        result = 'A+'
    elif 3.6 < numericGrade <= 3.8 :
        result = 'A'
    elif 3.3 < numericGrade <= 3.6 :
        result = 'A-'
    elif 3.0 < numericGrade <= 3.3 :
        result = 'B+'
    elif 2.7 < numericGrade <= 3.0 :
        result = 'B'
    elif 2.3 < numericGrade <= 2.7 :
        result = 'B-'
    elif 2.0 < numericGrade <= 2.3 :
        result = 'C+'
    elif 1.7 < numericGrade <= 2.0 :
        result = 'C'
    elif 1.4 < numericGrade <= 1.7 :
        result = 'C-'
    elif 1.2 < numericGrade <= 1.4 :
        result = 'D+'
    elif 1.0 < numericGrade <= 1.2:
        result = 'D'
    elif 0.0 < numericGrade <= 1.0 :
        result = 'D-'
    else:
        result = 'F'
    return result

#8
#Get the weight value of the assignments (call the appropriate function)
#Get the weight value of tests (call the appropriate function)
#Get the weight value of the final (call the appropriate function)
#Check the sum of weight values is 1 (call the appropriate function)
#Repeat the last four lines if not equal to 1
while True:
    wOfAssign = getWeightOfAssignments()
    wOfMidTerms = getWeightOfMidTerms()
    wFinal = getWeightOfFinal()
    if checkWeights(wOfAssign, wOfMidTerms, wFinal):                                    
        break                                                                            
    else:
        print("Please enter the values equals to 1")
#9
#Get the average grade obtained on the assignments
#Validate the input as a float between 0 and 100
while True:
    try:
        AvgAssignments = float(input("Enter the average grade obtained on the assignments: ")) 
    except ValueError:
        print("Please enter a number")
    else:                                                                                  
        if 0 > AvgAssignments or AvgAssignments > 100:                                     
            print("Please enter the number between 0 and 100")
        else:
            break

#10
#Get the number of tests (call the appropriate function)
#Prompt the user for each test grades and accumulate the value
#Validate the input as a float between 0 and 100
#Calculate the average test grade.
num_test = getNumberOfTests()
acc_value = 0

for i in range(num_test):                                                              
    while True:
        try:
            test_grade = float(input("Enter the test grade: "))                        
        except ValueError:
            print("Please enter a number: ")
        else:
            if 0 > test_grade or test_grade  > 100:     
                print("Please enter the number between 0 and 100")           
            else:
                acc_value += test_grade                                                
                break

AvgTests = acc_value / num_test

#11
#Prompt and get the final grade
#Validate the input as a float between 0 and 100

while True:
    try:
        final = float(input("Enter the number obtained on the final grade: ")) 
    except ValueError:
        print("Please enter a number between 0 to 100")
    else:
        if(0 <= final <= 100):                                         
            break
    
#12
#Calculate and display the final numeric grade (call the appropriate function)
# AvgAssignments,AvgTests,final,wOfAssign,wOfMidTerms,wFinal
numeric_grade = calculateNumericGrade(AvgAssignments,AvgTests,final,wOfAssign,wOfMidTerms,wFinal)
print(numeric_grade)


#13
#Calculate and display the final alphabetical grade (call the appropriate function)

print(calculateLetterGrade(numeric_grade))
