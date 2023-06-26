class personal_details:
    def __init__(self, name, roll_number, klass):
        self.name = name
        self.roll_number = roll_number
        self.klass = klass

    def define(self):
        print(f'Name: {name}, \nRoll Number: {roll_number},\nClass: {klass}')


class Marks:
    def __init__(self, math, social):
        self.math = math
        self.social = social

    def sub(self):
        print("Marks Obtained")
        print(f'Math= {self.math}, \nSocial= {self.social}')

    def total(self):
        return self.math + self.social

    def percent(self):
        return self.total() / 2

    def condition(self):
        if self.percent() == 100:
            print("first division")
        elif self.percent() == 50:
            print("second division")
        else:
            print("thankyou")
            exit()


# To record details of the student
name: str = input('enter the name: ').upper()
roll_number: int = input("enter the roll number: ")
klass: str = (input("which class do you study? : "))
Personal_detail = personal_details(name, roll_number, klass)
print(Personal_detail.define())

# To calculate marks.
math = 50
social = 50
calculate = Marks(math, social)
print(calculate.sub())
print("total:", calculate.total())
print("percentage:", calculate.percent(), "%")
print(calculate.condition())
