#Take 5 test scores, give a letter grade, and find the student's total using user input.
#4.22.18
#CTI-110 P5HW1 - Test Average and Grade
#Vondre Smith
#


def main():
    grades = []
    for i in range(1,6):
        grade = int(input('Enter score {0}: '.format(i)))
        print('That\'s a(n): ' + determine_grade(grade))

    total = sum(grades)
    avg = calc_average(total)
    abc_grade = determine_grade(avg)

    print('Average grade is: ' + str(avg))
    print("That's a(n): " + str(abc_grade))

def calc_average(total):
    return total / 5

def determine_grade(grade):
    if 90 <= grade <= 100:
        return 'A'
    elif 80 <= grade <= 89:
        return 'B'
    elif 70 <= grade <= 79:
        return 'C'
    elif 60 <= grade <= 69:
        return 'D'
    else:
        return 'F'

main()
    
