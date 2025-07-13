class GroceryList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: str):
        self.tasks.append(task)

    def save(self, filepath: str):
        with open(filepath, "w") as file:
            for task in self.tasks:
                file.write(task)
                file.write('\n')
