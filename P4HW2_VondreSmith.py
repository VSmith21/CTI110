#Vondre Smith
#CTI - 110
#P4HW2 - Running Total
#03.27.2018

total = 0
counter = 0

while True:
    ask = float(input("Enter grade: "))
    total += ask
    counter += 1
    if ask < 0: break
total = total*1.0
avg = total/counter
print("Grade average: ", avg, "%")


