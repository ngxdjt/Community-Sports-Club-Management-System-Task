from random import randint

class Person:
    def __init__(self, name, age, contact_number):
        self.name = name
        self.age = age
        self.number = contact_number

    def set_details(self, name, age, contact_number):
        self.name = name
        self.age = age
        self.number = contact_number

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Contact Number: {self.number}"

class Member(Person):
    def __init__(self, name, age, contact_number, membership_id, sport):
        super().__init__(name, age, contact_number)
        self.id = membership_id
        self.sport = sport
        self.scores = []

    def set_member_details(self, membership_id, sport):
        self.id = membership_id
        self.sport = sport

    def add_performance_score(self, score):
        self.scores.append(score)
    
    def calculate_average_score(self):
        if not self.scores:
            return 0
        else:
            return sum(self.scores)/len(self.scores)

    def get_member_summary(self):
        return f"{self.get_details()}, Membership ID: {self.id}, Sport: {self.sport}, Average Performance Scores: {self.calculate_average_score()}"

class Coach(Person):
    def __init__(self, name, age, contact_number, coach_id, specialisation, salary):
        super().__init__(name, age, contact_number)
        self.id = coach_id
        self.specialisation = specialisation
        self.salary = salary
        self.mentees = []
        self.mentorship_group = []

    def set_coach_details(self, coach_id, specialisation, salary):
        self.id = coach_id
        self.specialisation = specialisation
        self.salary = salary
    
    def assign_mentee(self, member: Member):
        self.mentees.append(member)
        print(f"Coach {self.name} is now mentoring {member.name} in {member.sport}")

    def get_mentees(self):
        return [student.name for student in self.mentees]

    def increase_salary(self, percentage):
        self.salary * (percentage/100)

    def mentor_coach(self, coach):
        self.mentorship_group.append(coach)
        print(f"{self.name} is now mentoring Coach {coach.name} in {coach.specialisation}")

    def get_mentorship_group(self):
        group = []
        for coach in self.mentorship_group:
            group.append(f"{coach.name} ({coach.specialisation})")
        return group

    def get_coach_summary(self):
        return f"{self.get_details()}, Specialisation: {self.specialisation}, Salary: {self.salary}"
    
class Staff(Person):
    def __init__(self, name, age, contact_number, staff_id, position, years_of_service):
        super().__init__(name, age, contact_number)
        self.id = staff_id
        self.position = position
        self.yoe = years_of_service

    def set_staff_details(self, staff_id, position, years_of_service):
        self.id = staff_id
        self.position = position
        self.yoe = years_of_service

    def increment_years_of_service(self):
        self.yoe += 1

    def assist_member(self, member: Member):
        print(f"Staff {self.name} assisted {member.name} in resolving an issue.")
        
    def get_staff_summary(self):
        return f"{self.get_details()}, YoE: {self.yoe}"



member1 = Member("Bob", 23, "214512512", "325", "Basketball")
member2 = Member("Dave", 25, "786934", "352", "Football")

coach1 = Coach("Eve", 35, "34463", "C2235", "Basketball", 40000)
coach2 = Coach("Paul", 64, "124532", "C6261", "Football", 45000)

staff = Staff("Callum", 48, "5374346", "S4235", "Club Secretary", 10)

coach1.assign_mentee(member1)
for i in range(1,5):
    member1.add_performance_score(randint(1,10))
print(member1.calculate_average_score())
staff.assist_member(coach2)
coach1.increase_salary(15)
staff.increment_years_of_service()

print(member1.get_member_summary())
print(member2.get_member_summary())
print(coach1.get_coach_summary())
print(coach2.get_coach_summary())
print(staff.get_staff_summary())

coach1.mentor_coach(coach2)
coach1.assign_mentee(member1)

print(coach1.get_mentorship_group())
print(coach1.get_mentees())