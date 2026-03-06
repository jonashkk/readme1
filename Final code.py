listOfTasks = []

def createTask():
    taskName = input("Task Name: ")
    taskDescription = input("Description: ")
    
    print("Would you like to provide instructions or steps?")
    print("1. Instructions")
    print("2. Steps")
    taskChoice = input("Your choice (type the number): ")
    
    taskProcedureInstructions = None
    taskProcedureSteps = None
    
    if taskChoice == "1":
        taskProcedureInstructions = input("Enter your instructions: ")
        
    elif taskChoice == "2":
        taskProcedureSteps = []
        print("Enter steps (type DONE to finish):")
        
        while True:
            taskProcedureStep = input("- ")
            
            if taskProcedureStep.upper() == "DONE":
                break
                
            taskProcedureSteps.append(taskProcedureStep)
            
    else:
        print("Please enter appropriate input")
    
    taskTime = input("Time to finish (1:30PM - 2:30PM): ")
    
    print("What would this task be classified as?")
    print("1. Daily Task")
    print("2. Weekly Task")
    
    taskCategorychoice = input("Your choice (type the number): ")
    
    if taskCategorychoice == "1":
        taskCategory = "Daily Task"
    elif taskCategorychoice == "2":
        taskCategory = "Weekly Task"
    else:
        print("Please enter appropriate input")
        taskCategory = "Unspecified"
    
    print("Please enter the deadline:")
    taskDeadline = input("")
    
    newTask = {
        "taskName": taskName,
        "taskDescription": taskDescription,
        "taskProcedureInstructions": taskProcedureInstructions,
        "taskProcedureSteps": taskProcedureSteps,
        "taskTime": taskTime,
        "taskCategory": taskCategory,
        "taskDeadline": taskDeadline
    }
    
    return newTask


def addTasks(listOfTasks):
    newTask = createTask()
    listOfTasks.append(newTask)


def taskDisplay(listOfTasks):
    print("\n||||| Display of Tasks |||||")
    
    for task in listOfTasks:
        print("\n---------------------------")
        print("Task:", task["taskName"])
        print("Description:", task["taskDescription"])
        
        if task["taskProcedureInstructions"] is not None:
            print("Procedure:", task["taskProcedureInstructions"])
            
        if task["taskProcedureSteps"] is not None:
            print("Procedure Steps:")
            for taskProcedureStep in task["taskProcedureSteps"]:
                print("-", taskProcedureStep)
        
        print("Time Duration:", task["taskTime"])
        print("Category:", task["taskCategory"])
        print("Deadline:", task["taskDeadline"])


while True:
    addTasks(listOfTasks)
    
    moreTasks = input("Add another task? (y/n): ")
    
    if moreTasks.lower() == "n":
        break

taskDisplay(listOfTasks)