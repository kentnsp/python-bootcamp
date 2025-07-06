tasks = []

def create(tasks: list[str], task: str):
    tasks.append(task)

def read(tasks: list[str], index: int) -> str:
      return tasks[index]

def update(tasks: list[str], index: int, new_task: str ):
   tasks[index] = new_task

def delete(tasks: list[str], index: int):
    tasks.pop(index)

create(tasks,'asd')
print('create', tasks)

print('read', read(tasks, 0))

update(tasks, 0,'mnb')
print('update', tasks)

delete(tasks,0)
print('deleted', tasks)




