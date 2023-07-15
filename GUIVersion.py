# Boring imports.
import os
from tkinter import *
from tkinter import ttk

# Setup root window (Main window)
root = Tk()
root.title("Demin's Grading Calculator")
root.resizable(False,False)
root.geometry('380x50')

# Required variables
StudentDB = "StudentScore.txt"
GradeUI = None
GradedDBUI= None
ClearDBW = None
LetterGrade = StringVar()
DB = StringVar()

# Hack-y code to determine the center of the screen
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

# Defining a function to write the Name, Decimal grade, and Letter grade to a file
def StudentAndScores(Student, Grade, LetterGrade):
    if os.path.exists(StudentDB):
        with open(StudentDB, "a") as f: 
            f.write(f"Name: {Student} Number Grade: {Grade} Letter Grade: {LetterGrade}\n")
    else:
        return

# Defining a function to get the letter grade associated to the number grade.
def get_grade(score):
    if score > 100:
        errorMessage = "Score exceeds 100..."
        LetterGrade.set(errorMessage)
        raise ValueError(errorMessage)
    
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


# Defining function for main Grade window
def GradeUIWindow():
    # Checking to see if the window is already open, if it is then close the previous one and open a new one. If not then open the window.
    global GradeUI
    if GradeUI is not None and GradeUI.winfo_exists():
        GradeUI.destroy()
        
    # Defining the window
    GradeUI = Toplevel()
    GradeUI.title("Grades")
    GradeUI.resizable(False, False)
    center_window(GradeUI, 300, 250)
    
    # Create the entry fields
    Name_entry = Entry(GradeUI)
    Grade_Entry = Entry(GradeUI)
    
    # Define a function to run when clicked, this will get the student name and grade decimal number, and return a letter grade. Also writes to the Database.
    def onClick():
        Name = Name_entry.get()
        DecimalGrade = float(Grade_Entry.get())
        Name_entry.delete(0, END)
        Grade_Entry.delete(0, END)
        Letter = get_grade(DecimalGrade)
        LetterGrade.set(f"\nResults\nStudent: {Name} \nDecimal Grade: {DecimalGrade}\nLetter Grade {Letter}\n\nWrote to database..")
        StudentAndScores(Name, DecimalGrade, Letter)
        
    
    # Create buttons and text to place in the window
    BottomText = Label(GradeUI, textvariable=LetterGrade)
    EnterButton = Button(GradeUI, text="Submit score", command=onClick)
    TopText = Label(GradeUI, text="Student Name")
    MiddleText = Label(GradeUI, text="Decimal Grade")
    
    # Place everything on screen
    TopText.pack()
    Name_entry.pack()
    MiddleText.pack()
    Grade_Entry.pack()
    EnterButton.pack(pady=10)
    BottomText.pack()
    
    

# Defining the window to output all grades
def GradedDBWindow():
    global GradedDBUI
    
    if GradedDBUI is not None and GradedDBUI.winfo_exists():
        GradedDBUI.destroy()
        
    GradedDBUI = Toplevel()
    GradedDBUI.title("Graded DB")
    GradedDBUI.resizable(False, False)
    center_window(GradedDBUI, 450, 400)
    
    # Create a text variable
    text = Text(GradedDBUI)
    text.pack()
    
    # Function of the graded DB window
    try:
        with open(StudentDB, "r") as file:
            content = file.read()
            text.insert(END, content)
    except FileNotFoundError:
        text.insert(END, "File not found")

# Function to clear the Database
def ClearDB():
    global ClearDBW
    if ClearDBW is not None and ClearDBW.winfo_exists():
        ClearDBW.destroy()
    ClearDBW = Toplevel()
    ClearDBW.title("DB Purge")
    ClearDBW.resizable(False, False)
    ClearDBW.geometry("100x20")
    ClearLabel = Label(ClearDBW, text="CLEARED DB!")
    with open(StudentDB, 'r+') as clearFile:
        clearFile.truncate(0)
    ClearLabel.pack()

# Create Buttons
Get_Grade_Button = ttk.Button(text="Grade", command=GradeUIWindow)
Get_Grades = ttk.Button(text="Graded DB", command=GradedDBWindow)
Clear = ttk.Button(text="ClearDB", command=ClearDB)
Exit = ttk.Button(text="Exit", command=exit)

# Place buttons
Get_Grade_Button.place(x=10, y=10)
Get_Grades.place(x=100, y=10)
Clear.place(x=190, y=10)
Exit.place(x=280, y=10)


# Run program
root.mainloop()