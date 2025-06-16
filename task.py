class Task:
    # since I am unsure of the ID this task will inherit initalize as None
    def __init__(self, title, due, description = None, isComplete = False, task_id= None):
        self.title = title
        self.due = due
        self.description = description
        self.isComplete = isComplete
        self.id= task_id

    def __str__(self):
        stringOutput = f"Title: {self.title}\nDue: {self.due}"
        if self.description:
            stringOutput += f"\nDescription: {self.description}"
        
        return stringOutput
    
    def to_dict(self):
        return {
            "title": self.title,
            "due": self.due,
            "description": self.description,
            "isComplete": self.isComplete,
        }