
class Student_manager:
    def __init__(self):
        self.student = {}
    def addstudent(self,rollnumber,student_name,grade):
        if rollnumber in self.student:
            print(f'{rollnumber} is already registered')
        else:
            self.student[rollnumber] = {"student_name":student_name,"grade":grade}
            print(f'{rollnumber} is registered for {student_name}')
    def getstudent(self,rollnumber):
        if rollnumber in self.student:
            return self.student[rollnumber]
        else:
            return f"roll number {rollnumber} is not registered"
    def gettopstudent(self, criteria):
        topstudents = [
            {"rollnumber": rollnumber, "student_name": data['student_name'],"grade": data['grade']}
            for rollnumber, data in self.student.items()
            if data['grade']> criteria
        ]
        return topstudents
result = Student_manager()
student_data=[
    {"rollnumber":20049,"student_name":"Madhansai", "marks":86},
{"rollnumber":20054,"student_name":"jello", "marks":70},
{"rollnumber":20039,"student_name":"bob", "marks":50},
{"rollnumber":20040,"student_name":"joe", "marks":60},
]
for student in student_data:
    result.addstudent(student["rollnumber"],student["student_name"],student["marks"])
print(result.getstudent(20040))
top_student = result.gettopstudent(60)
print(top_student)
for student in top_student:
    print(student)



#...........ENCAPSULATION....................

class bankaccount:
    def __init__(self,accountholder,balance=0):
        self.accountholder=accountholder
        self._balance=balance
    def deposit(self,amount):
        if amount > 0:
            self._balance += amount
            print(f'Deposited {amount}, and balance is {self._balance}')
        else:
            print(f'deposit amount {amount} is invalid')
    def checkbalance(self):
        return self._balance
account1 = bankaccount(accountholder="Madhansai",balance=100)
print(account1.accountholder)
account1.deposit(100000)
print(account1.checkbalance())
print(account1._balance)


#...........INHERITANCE........

class bankaccount:
    def __init__(self,accountholder,balance=0):
        self.accountholder=accountholder
        self._balance=balance
    def deposit(self,amount):
        if amount > 0:
            self._balance += amount
            print(f'Deposited {amount}, and balance is {self._balance}')
        else:
            print(f'deposit amount {amount} is invalid')
    def checkbalance(self):
        return self._balance

class savingsaccount(bankaccount):
    def __init__(self,accountholder,balance=0,interest=0.5):
        super().__init__(accountholder,balance)
        self._interest=interest
    def calculate_interest(self):
        interest = self._balance * self._interest
        self._balance += interest
        print(f'Interest is added {interest} and the balance is {self._balance}')

savings = savingsaccount(accountholder="Madhansai",balance =2000000, interest=0.8)
savings.deposit(10000)
savings.calculate_interest()
print(f"after deposit the final balance is {savings.checkbalance()}")


###############################################################################################

class bankaccount:
    def __init__(self,accountholder,balance=0):
        self.accountholder=accountholder
        self._balance=balance
    def deposit(self,amount,currency='INR'):
        if amount > 0:
            self._balance += amount
            print(f'Deposited {amount}, and balance is {self._balance}')
        else:
            print(f'deposit amount {amount} is invalid')

    def withdraw(self,amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f'Withdrawed {amount}, and balance is {self._balance}')

class savingsaccount(bankaccount):
    def __init__(self,accountholder,balance=0,overdraft_limit=1000):
        super().__init__(accountholder,balance)
        self.overdraft_limit=overdraft_limit

    def withdraw(self,amount):
        if amount <= self._balance + self.overdraft_limit:
            self._balance -= amount
            print(f"Withdrawed {amount}, and balance is {self._balance}")
        else:
            print('exceeded overdraft limit')

basic_acc = bankaccount(accountholder="Madhansai",balance=20000)
basic_acc.deposit(10000)
basic_acc.deposit(20000,"USD") #method overloading by adding currency

sav_acc = savingsaccount(accountholder="Madhansai",balance=20000, overdraft_limit=3000)
sav_acc.withdraw(10000)  #method overridding by using same method
sav_acc.withdraw(20000)




