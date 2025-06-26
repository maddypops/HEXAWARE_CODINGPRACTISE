def split_bill():
    people = input("Enter names (comma separated): ").split(',')
    amounts = list(map(float, input("Enter amounts paid by each (space separated): ").split()))
    if len(people) != len(amounts):
        print("Count mismatch.")
        return

    total = sum(amounts)
    share = total / len(people)
    print(f"\nTotal Bill: {total:.2f} | Each should pay: {share:.2f}")
    for person, paid in zip(people, amounts):
        bal = round(paid - share, 2)
        if bal > 0:
            print(f"{person.strip()} should receive {bal}")
        elif bal < 0:
            print(f"{person.strip()} owes {-bal}")
        else:
            print(f"{person.strip()} is settled")

def splitter_menu():
    while True:
        print("\n--- Bill Splitter ---")
        print("1. Split a Bill")
        print("2. Exit")
        ch = input("Choice: ")
        if ch == "1":
            split_bill()
        elif ch == "2":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    splitter_menu()
