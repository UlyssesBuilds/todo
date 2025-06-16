# easy to do task to bring everything together
# ORM, SQL


#user in: Add task: Name, When its do (add alert later), description, (add priority rating later?)
#user out: Updated form of things to do, ordered by date (priority later?)
# process: Put into ArrayList then when another one is added 2d Arrays

#> we might want to allow it to create multiple entities so thats maps?
# so we can add another classs and then do task for this class

## main is often client; we will build it out all here  
# then we create a class later for todoList and OOP it


#print ("Add?")
todoLists = []

option = input("Add? ").lower()
while(option != "n"):
    if(option.lower() == "y"):
        title = input("Task Title: ")
        due = input("When is it due? ")
        description = input ("Description (enter to skip)")
        
        task = {
            "title": title,
            "due": due,
            "description": description if description else None
        }

        todoLists.append(task)
        option = input("Add more task? ").lower()


print("\nToDo list:")
for i, task in enumerate(todoLists, start = 1):
    print(f"Task {i}:")
    print(f"Title {task['title']}:")
    print(f"Due: {task['due']}")
    if task['description']:
        print(f"Description {task ['description']}")