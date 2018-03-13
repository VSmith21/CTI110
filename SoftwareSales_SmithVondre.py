#Vondre Smith
#CTI - 110
#Software Sales
#03.12.2018

def main():
    print("Thank you for shopping with our software company.")

main()

software = 99
quantity = float(input("Enter how many products you need: "))
total_cost = quantity * software

if quantity > 10 and quantity < 20:
    print("You pay: $ ", total_cost-(total_cost*.1))
elif quantity > 20 and quantity < 50:
    print("You pay: $ ", total_cost-(total_cost*.2))
elif quantity > 50 and quantity < 99:
    print("You pay: $ ", total_cost-(total_cost*.3))
elif quantity >= 100:
    print("You pay: $ ", total_cost-(total_cost*.4))
else:
    print("ERROR")
