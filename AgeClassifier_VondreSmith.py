#Vondre Smith
#CTI - 110
#Age Classifier
#03.12.18

# add def main() now, so that's it's easier to do test runs or import in C or JAVA scripts
   
def main():
    print("Thank you for participating in this government sanctioned survey!")

main()

# time for the actual program :-)

age= float(input("Enter age here for AGE CLASSIFICATION: "))

if age <= 1:
        print("You're an infant, little terrestrial!")
elif age < 13:
        print("You're a child...")
elif age == 13 or age < 20:
        print("You're a teenager. Good luck, homie.")
elif age == 20 or age > 20:
        print("You're a grown a** adult. Peace.")
