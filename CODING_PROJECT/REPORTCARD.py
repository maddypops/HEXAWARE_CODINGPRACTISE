import math

students = {}

def add_student():
    name = input("Student Name: ")
    marks = list(map(int, input("Enter 3 marks (space separated): ").split()))
    students[name] = marks
    print("✅ Student added.")

def view_report_card():
    if not students:
        print("No students yet.")
        return
    for name, marks in students.items():
        total = sum(marks)
        average = math.ceil(total / len(marks))
        grade = (lambda avg: 'A' if avg >= 90 else 'B' if avg >= 75 else 'C' if avg >= 50 else 'F')(average)
        print(f"{name} => Marks: {marks}, Total: {total}, Avg: {average}, Grade: {grade}")

def student_menu():
    while True:
        print("\n--- Student Report Card ---")
        print("1. Add Student")
        print("2. View Report Cards")
        print("3. Exit")
        ch = input("Choice: ")
        if ch == "1":
            add_student()
        elif ch == "2":
            view_report_card()
        elif ch == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    student_menu()
