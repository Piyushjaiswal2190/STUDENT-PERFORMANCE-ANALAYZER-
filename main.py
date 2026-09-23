# SMART STUDENT PERFORMANCE ANALYZER

subjects = ["MAT1003", "CSE1021", "ENG1004", "CHY1001"]
students = []

def total_marks(marks):
    total = 0
    for mark in marks:
        total = total + mark
    return total

def average_marks(marks):
    return total_marks(marks) / len(marks)

def highest_marks(marks):
    highest = marks[0]
    for mark in marks:
        if mark > highest:
            highest = mark
    return highest

def lowest_marks(marks):
    lowest = marks[0]
    for mark in marks:
        if mark < lowest:
            lowest = mark
    return lowest

def grade(mark):
    if mark >= 90:
        return "S Grade - 10 Points"
    elif mark >= 80:
        return "A Grade - 9 Points"
    elif mark >= 70:
        return "B Grade - 8 Points"
    elif mark >= 60:
        return "C Grade - 7 Points"
    elif mark >= 50:
        return "D Grade - 6 Points"
    elif mark >= 40:
        return "E Grade - 5 Points"
    else:
        return "F Grade - 0 Points"

def subject_feedback(subject, mark):
    if mark < 40:
        print(subject, ": You need improvement.")
        print("Feedback: Revise basic concepts and practice daily.")
    elif mark < 60:
        print(subject, ": Your performance is average.")
        print("Feedback: Solve more questions and revise regularly.")
    elif mark < 75:
        print(subject, ": Good performance.")
        print("Feedback: Improve your accuracy and weak topics.")
    elif mark < 90:
        print(subject, ": Very good performance.")
        print("Feedback: Practice difficult questions.")
    else:
        print(subject, ": Excellent performance.")
        print("Feedback: Keep maintaining this performance.")

def attendance_feedback(attendance):
    if attendance < 75:
        print("Attendance Warning:")
        print("Your attendance is below 75%.")
        print("Attend classes regularly.")
    elif attendance < 85:
        print("Attendance Feedback:")
        print("Your attendance is acceptable.")
        print("Try to attend more classes.")
    else:
        print("Attendance Feedback:")
        print("Excellent attendance. Keep it up.")

def overall_feedback(average):
    if average < 40:
        print("Overall Feedback:")
        print("Your performance needs serious improvement.")
        print("Focus on basic concepts and daily practice.")
    elif average < 60:
        print("Overall Feedback:")
        print("Your performance is average.")
        print("Prepare a proper study timetable.")
    elif average < 75:
        print("Overall Feedback:")
        print("Your performance is good.")
        print("Focus more on your weak subjects.")
    elif average < 90:
        print("Overall Feedback:")
        print("Your performance is very good.")
        print("Practice advanced questions.")
    else:
        print("Overall Feedback:")
        print("Excellent performance.")
        print("Keep working hard and maintain your score.")

def study_plan(average):
    print("\n========== @ PERSONAL STUDY PLAN ==========")
    if average < 40:
        print("Study 2 hours daily.")
        print("Revise basic concepts.")
        print("Solve easy questions first.")

    elif average < 60:
        print("Study 1.5 hours daily.")
        print("Revise classroom notes.")
        print("Solve practice questions.")

    elif average < 75:
        print("Study 1 hour daily.")
        print("Focus on difficult topics.")
        print("Revise before every test.")

    else:
        print("Revise regularly.")
        print("Practice previous-year questions.")
        print("Focus on advanced problems.")


def add_student():

    print("\n========== ADD STUDENT ==========")

    name = input("Enter your Name: ")
    roll_no = input("Enter your Roll No: ")
    marks = []

    for subject in subjects:
        mark = int(input("Enter your " + subject + " marks: "))
        while mark < 0 or mark > 100:
            print("Marks should be between 0 and 100.")
            mark = int(input("Enter your " + subject + " marks: "))
        marks.append(mark)

    attendance = int(input("Enter your attendance percentage: "))

    while attendance < 0 or attendance > 100:
        print("Attendance should be between 0 and 100.")
        attendance = int(input("Enter your attendance percentage: "))

    student = {"name": name,
        "roll_no": roll_no,
        "marks": marks,
        "attendance": attendance }
    students.append(student)
    print("\nStudent added successfully!")


def display_report():
    print("\n========== DISPLAY STUDENT REPORT ==========")
    roll_no = input("Enter your Roll No: ")
    found = False
    for student in students:
        if student["roll_no"] == roll_no:
            found = True

            print("\n========== STUDENT REPORT ==========")
            print("Name:", student["name"])
            print("Roll No:", student["roll_no"])
            print("Marks:", student["marks"])

            print("Total Marks:", total_marks(student["marks"]))
            print("Average Marks:", average_marks(student["marks"]))
            print("Highest Marks:", highest_marks(student["marks"]))
            print("Lowest Marks:", lowest_marks(student["marks"]))
            print("Attendance:", student["attendance"], "%")


            print("\n========== SUBJECT-WISE REPORT ==========")

            for i in range(len(subjects)):
                print("\nSubject:", subjects[i])
                print("Marks:", student["marks"][i])
                print("Grade:", grade(student["marks"][i]))
                subject_feedback(
                    subjects[i],
                    student["marks"][i])


            print("\n========== ATTENDANCE FEEDBACK ==========")
            attendance_feedback(student["attendance"])

            print("\n========== OVERALL PERFORMANCE ==========")

            overall_feedback(average_marks(student["marks"]))

            study_plan(average_marks(student["marks"]))


            print("\n========== WEAK SUBJECTS ==========")

            weak_found = False

            for i in range(len(subjects)):
                if student["marks"][i] < 60:
                    print( subjects[i], "needs more attention." )
                    weak_found = True

            if weak_found == False:
                print("No major weak subject found.")

    if found == False:
        print("Student not found.")


def class_report():
    print("\n========== CLASS PERFORMANCE ==========")
    if len(students) == 0:
        print("No student data available.")
        return

    total_average = 0
    highest_student = students[0]

    for student in students:
        total_average = total_average + average_marks(student["marks"])
        
        if average_marks(student["marks"]) > average_marks(
            highest_student["marks"]):
            highest_student = student

    class_average = total_average / len(students)
    print("Total Students:", len(students))
    print("Class Average:", class_average)
    print("Highest Performer:", highest_student["name"])

    print("Highest Performer Average:",average_marks(highest_student["marks"]))

def main():
    print("======================================")
    print(" # SMART STUDENT PERFORMANCE ANALYZER ")
    print("======================================")

    while True:
        print("\n========== MENU ==========")

        print("1. Add Student")
        print("2. Display Student Report")
        print("3. Class Performance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_report()

        elif choice == "3":
            class_report()

        elif choice == "4":
            print("Thank you for using the Student Performance Analyzer.")
            break
        else:
            print("Invalid choice. Try again.")

main()
