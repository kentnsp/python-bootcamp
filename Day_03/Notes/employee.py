class Employee:
    """class representation for employee data"""
    def __init__(self,name, id):
        self.name =name
        self.id = id
        self.tasks = []
        print(f"Employee {self.name} created with id {self.id}")

    def add_work(self, task):
        self.tasks.append(task)

employee1 = Employee("Ken","123")
employee2 = Employee("Leo","456")

print(f"Employee 1: ", employee1.name)
print(f"Employee 2: ", employee2.name)
print(employee1.tasks)
