import os

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

    # Read Jenkins parameters (with defaults)
    name = os.getenv("Name", "Pradeep")
    department = os.getenv("Deparement", "BCA")
    semester = os.getenv("Semester", "3")

    m1 = int(os.getenv("M1", 85))
    m2 = int(os.getenv("M2", 90))
    m3 = int(os.getenv("M3", 80))

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
