# Grading calculator by Demin.
# Not required at all to be ran. Still here for preferance though.
import pyfiglet
import os

'''
Grade translation:

A+: 98
A: 95
A-: 92
B+: 88
B: 85
B-: 82
C+: 79
C: 76
C-: 73
D+: 70
D: 65
F: <65
'''

StudentDB = "StudentScore.txt"

def Main():
    Intro = pyfiglet.figlet_format("Demins Grading")
    print(Intro)
    print("""\nOptions: 
          1) Calculate Grades
          2) View Student DB
          3) Clear Student DB (Clear for next class)
          4) Exit
          """)
    
    Option = input("\nPlease select an option: ")
    if Option == "1":
        Grade()
    if Option == "2":
        PrintDB()
    if Option == "3":
        ClearDB()
    if Option == "4":
        exit()


def Grade():
    Name = input("Enter the student name: ")
    Grade = input("Enter the student decimal grade: ")
    try:
        LetterGrade = get_grade(float(Grade))
        print(f"Grade: {LetterGrade}")
        StudentAndScores(Name, Grade, LetterGrade)
    except ValueError:
        print("Invalid number...")


def get_grade(score):
    grade_keylist = {
        'A+': 98,
        'A': 95,
        'A-': 92,
        'B+': 88,
        'B': 85,
        'B-': 82,
        'C+': 79,
        'C': 76,
        'C-': 73,
        'D+': 70,
        'D': 65,
        'F': 0
    }

    for grade, min_score in grade_keylist.items():
        if score >= min_score:
            return grade

def StudentAndScores(Student, Grade, LetterGrade):
    if os.path.exists(StudentDB):
        with open(StudentDB, "a") as f: 
            f.write(f"Name: {Student} Number Grade: {Grade} Letter Grade: {LetterGrade}\n")
    else:
        return
        
def PrintDB():
    with open(StudentDB, 'r') as DBFile:
        print(DBFile.read())
        input("Press ENTER to continue...")
        
def ClearDB():
    with open(StudentDB, 'r+') as clearFile:
        clearFile.truncate(0)
        print("Cleared DB..")
        input("Press ENTER to continue...")
    
while True:
    Main()