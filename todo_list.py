from task import Task #from task.py import Task class
class TodoList:
    
    def __init__(self):
        self.tasks = []

    def addTask(self, task):
        self.tasks.append(task)
        return task.id


    def printTask(self): # Since it is not in memory and in the db I need to pull from db first 
        if not self.tasks:
            print("no task yet")
            return

        for i, task in enumerate(self.tasks, start = 1):
            print(f"Task {i}: \n{task}\n")


    def getTask(self, task_id):
        for task in self.tasks:
            if task.id == int(task_id):
                return task
        return None