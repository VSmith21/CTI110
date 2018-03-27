#Vondre Smith
#CTI - 110
#P4HW1 - Distance Traveled
#03.27.2018


def main():
    print("Hour \t Distance")
    print("___________________")

x = "y"

while x == "y":
    speed = int(input("Enter MPH: "))
    time = int(input("Enter hours: "))

    if time <= 0 or speed <= 0:
        print("ERROR")

    else:
        main()
        for t in range(time):
            distance = speed * (t+1)
            print(t+1, "\t", distance)




          
    
