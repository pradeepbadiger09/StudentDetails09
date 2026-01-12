# student_grade.py

def calculate_grade(avg):
    if 90 <= avg <= 100:
        return "S"
    elif 80 <= avg <= 89:
        return "A"
    elif 65 <= avg <= 79:
        return "B"
    elif 50 <= avg <= 64:
        return "C"
    elif 40 <= avg <= 49:
        return "D"
    else:
        return "F"


def main():
    print("=== Student Grade Management System ===")

    name = input("Enter student name: ")
    department = input("Enter department: ")
    semester = input("Enter semester: ")

    try:
        m1 = float(input("Enter marks in Subject 1: "))
        m2 = float(input("Enter marks in Subject 2: "))
        m3 = float(input("Enter marks in Subject 3: "))
    except ValueError:
        print("Invalid marks! Please enter numbers only.")
        return

    total = m1 + m2 + m3
    average = total / 3

    grade = calculate_grade(average)

    print("\n----- Student Report -----")
    print(f"Name       : {name}")
    print(f"Department : {department}")
    print(f"Semester   : {semester}")
    print(f"Marks      : {m1}, {m2}, {m3}")
    print(f"Average    : {average:.2f}")
    print(f"Grade      : {grade}")
    print("--------------------------")


if __name__ == "__main__":
    main()