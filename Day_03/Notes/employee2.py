class Employee:
    def __init__(self,name, id):
        self.name =name
        self.id = id
        self.tasks = []
        print(f"Employee {self.name} created with id {self.id}")

    def add_work(self, task):
        self.tasks.append(task)

    def time_in(self):
        print(f"TIME IN: Employee {self.name} created with id {self.id}")

    def time_out(self):
        print(f"TIME OUT: Employee {self.name} created with id {self.id}\n")

class Recruiter(Employee):

    def recruit(self):
        print(f"Recruitment {self.name}, {self.id} ")

class Developer(Employee):

    def develop(self):
        print(f"Development {self.name}, {self.id} ")


class Manager(Employee):

    def manage(self):
        print(f"Management {self.name}, {self.id}")


employee1 = Recruiter("Ken", 123)
employee1.time_in()
employee1.recruit()
employee1.time_out()

employee2 = Developer("Leo", 456)
employee2.time_in()
employee2.develop()
employee2.time_out()

employee3 = Manager("Mhar", 789)
employee3.time_in()
employee3.manage()
employee3.time_out()