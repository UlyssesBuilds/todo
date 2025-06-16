from flask import Flask, render_template, request, redirect ##from the pip install flask, use library Flask for route making
    #render: , request: lib for making HTTP request, redirect:
from task import Task #from filename import class  
from todo_list import TodoList
import db
from datetime import datetime

app = Flask(__name__)


def load_db_on_boot(todoListObject):
    #load db and store in memory todo_list.py
    rows = db.get_all_task()
    for row in rows:
        # row format (id, title, due, description, isComplete)
        task = Task(row[1], row[2], row[3], row[4], row[0])  # row[0] (id)
        # (self, title, due, description = None, isComplete = False, task_id= None
        todoListObject.addTask(task)
    return todoListObject



todoListObject = TodoList() #creating the object from class
todoListObject = load_db_on_boot(todoListObject) # filling it up 


# output display
@app.route('/')
def index(): 
    today = datetime.today().date()
    upComingTask = []
    overDueTask = []
    completedTask = []


    for task in todoListObject.tasks:            
        if task.isComplete: # checks first if done if not then it puts in todo
            completedTask.append(task)
        elif task.due >= today:  #use task.due to get date obj
            upComingTask.append(task)
        elif task.due < today:
            overDueTask.append(task)
        

    # sort    

    return render_template('index.html', upcoming = upComingTask, overDue= overDueTask, completed = completedTask)
    # this is what I am returning so I need to change it on HTML side

# input display
@app.route('/add', methods=['POST'])
def userInput():
    try:  # to do something risky
        # user inputs tasks. no need for while loop as when it redirect it serves a fresh page to resubmit for            

        title = request.form['title'] # from HTML form field named "title"
        due_str = request.form['due']
        due = datetime.strptime(due_str, "%Y-%m-%d").date()
        description = request.form.get('description', '') #key, default as user now passes emptyString


        task = Task(title, due, description) #no need to handle None
        task.id = db.addTask(task)  # Save immediately to DB, returns ID (incremented)
        todoListObject.addTask(task) #save to memory; use the global variable

        return redirect('/') #reloads index with new info essentially printing as well
    except Exception as e:  #didn't work? heres the error
        return f"Error: {e}"  

@app.route('/completed', methods=['POST'])
def completedTask():
    try:  # to do something risky
        # user inputs tasks. no need for while loop as when it redirect it serves a fresh page to resubmit for            

        task_id  = int(request.form['task_id']) # I am passing back the task.id

        # use todolist to find which task to change the isCompelted in SQL
        task = todoListObject.getTask(task_id)

        if task: # if not returned None which it shouldn't 
            task.isComplete = True # add this to memory
            db.updateCompletedTask(task.id) # changed in SQL


        return redirect('/') #reloads and should be caught in the '/' route
    except Exception as e:  
        return f"Error: {e}"  




if __name__ == "__main__":
    app.run(debug=True)