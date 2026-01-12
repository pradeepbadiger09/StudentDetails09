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

    # Static data for CI/CD (no input)
    name = "Pradeep"
    department = "bca"
    semester = "3"

    m1 = 85
    m2 = 90
    m3 = 80

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
