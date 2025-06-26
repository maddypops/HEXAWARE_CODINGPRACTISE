
class Person:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


# Create an object of the class
person1 = Person("Vishnu", 25)
person1.greet()


# Encapsulation Method in Python

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"${amount} deposited. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"${amount} withdrawn. New balance: ${self.__balance}")
        else:
            print("Insufficient balance or invalid amount.")



account = BankAccount("John", 100)
account.deposit(50)
account.withdraw(30)




class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"${amount} deposited. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"${amount} withdrawn. New balance: ${self.__balance}")
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.__balance


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.03):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest added: ${interest}")


# Usage
acc = SavingsAccount("Vishnu", 1000)
acc.deposit(500)
acc.add_interest()
acc.withdraw(200)



class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def borrow_book(self):
        if self.copies > 0:
            self.copies -= 1
            print(f"You borrowed '{self.title}'. Copies left: {self.copies}")
        else:
            print(f"'{self.title}' is currently unavailable.")

    def return_book(self):
        self.copies += 1
        print(f"You returned '{self.title}'. Copies available: {self.copies}")


# Usage
book = Book("1984", "George Orwell", 3)

book.borrow_book()
book.borrow_book()
book.return_book()




class Patient:
    def __init__(self, name, age, ailment):
        self.name = name
        self.age = age
        self.ailment = ailment

    def display_info(self):
        print(f"Patient Name: {self.name}, Age: {self.age}, Ailment: {self.ailment}")


class Doctor:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty

    def diagnose(self, patient):
        print(f"Dr. {self.name} ({self.specialty}) is diagnosing {patient.name}.")


# Usage
patient = Patient("John Doe", 45, "Fever")
doctor = Doctor("Dr. Smith", "General Physician")

patient.display_info()
doctor.diagnose(patient)




try:
    file = open("filepath", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
else:
    print("File content read successfully.")
finally:
    print("Closing file.")
    if 'file' in locals() and not file.closed:
        file.close()



try:
    file = open("filepath", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
else:
    print("File content read successfully.")
finally:
    print("Closing file.")
    if 'file' in locals() and not file.closed:
        file.close()



with open(r"C:\HEXAWARE\HEXAWARE-CODINGPRACTISE\GITHUB REPOS.txt", "r") as file:
    print(file.tell())  # Initial position: 0
    file.read(5)  # Read the first 5 characters
    print(file.tell())  # Current position: 5



with open(r"C:\HEXAWARE\HEXAWARE-CODINGPRACTISE\GITHUB REPOS.txt", "r") as file:
    file.seek(5)  # Move pointer to the 5th byte
    print(file.read(1))  # Read the 6th character
    file.seek(-3, 2)  # Move pointer 3 bytes before the end
    print(file.read(1))  # Read the character at this position



# Create a sample file
with open(r"C:\HEXAWARE\HEXAWARE-CODINGPRACTISE\GITHUB REPOS.txt", "w") as file:
    file.write("Learning Python in Hexa!")

# Open the file for reading
with open(r"C:\HEXAWARE\HEXAWARE-CODINGPRACTISE\GITHUB REPOS.txt", "r") as file:
    print(f"Initial position: {file.tell()}")  # Position: 0
    print(file.read(5))  # Read first 5 characters
    print(f"After reading 5 bytes: {file.tell()}")  # Position: 5

    file.seek(0)  # Move back to the beginning
    print(f"Position after seek(0): {file.tell()}")  # Position: 0

    file.seek(7)  # Move to the 7th byte
    print(f"Character at position 7: {file.read(1)}")  # Read one character
    print(f"Final position: {file.tell()}")  # Position: 8

with open(r"C:\HEXAWARE\HEXAWARE-CODINGPRACTISE\GITHUB REPOS.txt", "r") as file:
    # Read the entire content
    print(file.read())

    # Reset pointer
    file.seek(0)
    print(file.readline())  # Read the first line

    file.seek(0)
    print(file.readlines())  # Read all lines into a list

with open(r"C:\HEXAWARE\HEXAWARE-CODINGPRACTISE\GITHUB REPOS.txt", "w") as file:
    file.write("Hello, World!\n")  # Write a single string
    file.writelines(["This is line 1.\n", "This is line 2.\n"])  # Write a list of strings

with open(r"C:\HEXAWARE\HEXAWARE-CODINGPRACTISE\GITHUB REPOS.txt", "a") as file:
    file.write("This is some extra data.")
    file.truncate(10)  # File will now contain only the first 10 characters

with open(r"C:\HEXAWARE\HEXAWARE-CODINGPRACTISE\GITHUB REPOS.txt", "r") as file:
    file.seek(5)  # Move pointer to the 5th byte
    print(file.tell())  # Output the current position (5)
    print(file.read(1))  # Read one character from position 5

with open(r"C:\HEXAWARE\HEXAWARE-CODINGPRACTISE\GITHUB REPOS.txt", "w") as file:
    file.write("Buffered content.")
    file.flush()  # Write the buffer to disk immediately

with open(r"C:\HEXAWARE\HEXAWARE-CODINGPRACTISE\GITHUB REPOS.txt", "r") as file:
    print(file.fileno())  # Outputs the file descriptor, a unique OS identifier


import sqlite3


connection = sqlite3.connect("example.db")


cursor = connection.cursor()


cursor.execute("""
               CREATE TABLE IF NOT EXISTS users (
                                                    id INTEGER PRIMARY KEY,
                                                    name TEXT,
                                                    age INTEGER
               )
               """)

cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))


connection.commit()


cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

cursor.close()
connection.close()



















