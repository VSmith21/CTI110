#Vondre Smith
#CTI - 110
#P3LAB - Debugging
#03.12.2018

def main():
    #This program takes a number grade and outputs a letter grade.
    #This system uses a 10-point grading scale
    #TO DO: define the rest of the scores
    print("Hey there!")
    
main()
    
score = int(input("Enter grade: "))
if score >= 90:
    print("Your grade is: A")
        
elif score >= 80:
    print("Your grade is: B")
        
elif score >= 70:
    print("Your grade is: C")
        
elif score >= 61:
    print("Your grade is: D")
        
else:
    print("Your grade is: F")
    
