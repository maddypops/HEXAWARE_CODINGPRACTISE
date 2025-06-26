def main_menu():
    while True:
        print("\n=== Mini Apps Launcher ===")
        print("1. Student Report Card")
        print("2. Quiz App")
        print("3. Bill Splitter")
        print("4. Exit")
        choice = input("Choice: ")
        if choice == "1":
            import REPORTCARD;
            REPORTCARD.student_menu()
        elif choice == "2":
            import QUIZAPP;
            QUIZAPP.quiz_menu()
        elif choice == "3":
            import BILLSPLITTER
            BILLSPLITTER.splitter_menu()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main_menu()
