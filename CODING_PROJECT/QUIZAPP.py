questions = {
    "Capital of France?": ("Paris", "London", "Rome", "Berlin"),
    "2 + 2 = ?": ("3", "4", "5", "6"),
    "Color of the sky?": ("Blue", "Green", "Red", "Yellow"),
}
answers = ["Paris", "4", "Blue"]

def take_quiz():
    score = 0
    for idx, (q, opts) in enumerate(questions.items()):
        print(f"\n{q}")
        for i, opt in enumerate(opts, 1):
            print(f"{i}. {opt}")
        try:
            sel = int(input("Choice (1-4): "))
            if opts[sel - 1] == answers[idx]:
                score += 1
        except:
            print("Invalid input.")
    print(f"\n🎉 Final Score: {score}/{len(questions)}")

def quiz_menu():
    while True:
        print("\n--- Quiz App ---")
        print("1. Take Quiz")
        print("2. Exit")
        ch = input("Choice: ")
        if ch == "1":
            take_quiz()
        elif ch == "2":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    quiz_menu()
