studentname = input("Enter your name: ")
studentscore = int(input("Enter your score: "))
possiblepoints = 100

def scorepercent(possiblepoints, studentscore):
    return((studentscore / possiblepoints) * 100)

def grade(scorepercent):
    if 100 >= scorepercent >= 90:
        return("A")
    elif 89 >= scorepercent >= 80:
        return("B")
    elif 79 >= scorepercent >= 70:
        return("C")
    elif 69 >= scorepercent >= 60:
        return("D")
    else:
        return("F")

print(f"{studentname} has a grade {grade(scorepercent(possiblepoints, studentscore))}")
