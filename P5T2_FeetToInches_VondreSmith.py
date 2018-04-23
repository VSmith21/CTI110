#This program converts feet to inches
#4.22.18
#CTI-110 P5T2_FeetToInches
#Vondre Smith
#
inches_per_foot = 12

def main():
    feet = int(input('Enter a number of feet: '))
    print(feet, 'equals', feet_to_inches(feet), 'inches.')
def feet_to_inches(feet):
    return feet * 12

main()
