from task import Task #from filename import class  
from todo_list import TodoList
import db

def load_db_on_boot(todoListObject):
    #load db and store in memory todo_list.py
    rows = db.get_all_task()
    for row in rows:
        #row format (id, title, due, description)
        task = Task(row[1], row[2], row[3]) # skip row[0] (id)
        todoListObject.addTask(task)

    return todoListObject


#now that we get file in essentially we should create a menu function?
def userInput(todoListObject):
    # user inputs tasks
    option = input("Add? (y/n) ").lower()
    while(option != "n"):
        if(option.lower() == "y"):
            title = input("Task Title: ")
            due = input("When is it due? ")
            description = input ("Description (enter to skip) ")

            task = Task(title, due, description if description else None)
            todoListObject.addTask(task) #save to memory
            db.addTask(task)  # Save immediately to DB
        print()
        option = input("Add more? (y/n) ").lower()
    return todoListObject

def main():
    todoListObject = TodoList() #call the class to make the obj / memory
    todoListObject = load_db_on_boot(todoListObject)
    userInput(todoListObject)
    todoListObject.printTask() # printing from memory


if __name__ == "__main__":
    main()