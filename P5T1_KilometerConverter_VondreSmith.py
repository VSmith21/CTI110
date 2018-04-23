#This tutorial creates a program that converts kilometers to miles
#CTI-110
#P5T1-Kilometer Converter
#Vondre  Smith
#4.22.18

conversion_factor = 0.6214

def main():
    kilometers = float(input('Enter a distance in kilometers: '))
    show_miles(kilometers)
def show_miles(km):
    miles = km * conversion_factor
    print(km, 'kilometer equals', miles, 'miles.')

                       

main()
