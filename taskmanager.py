tasks = []

print("\n\nWelcome To Task Manager :)\n")

def addTask(): 
    new = input("Enter the Task : ")
    tasks.append(new)
    print("Task Added Successfully!!\n")

def myTask():
    for index , task in enumerate(tasks):
        print(index + 1, tasks[index])
    

def removeTask():
    print("Select the Task to be Removed : ")
    myTask()
    delete = int(input("Enter # of the Task : "))
    try :
        delete > 0 & delete < len(tasks) 
        tasks.pop(delete - 1)
        print("Task Removed Successfully\n")
    except:
        print("Task not found!!\n")


while True:
    print("\nPick One Action (Number Only): ")
    print("--------------------------------------------")
    print("1. Add a New Task")
    print("2. Delete a Task")
    print("3. List Of My Tasks")
    print("4. Exit Task Manager")
    
    try:
        option = int(input("\nYour Choice : "))
        if option == 1:
            print("Processing.....\n")
            addTask()
            continue
        elif option == 2:
            print("Processing.....\n")
            removeTask()
            continue
        elif option == 3:
            print("Processing.....\n")
            print("--------------------------------------------")
            print("Current Tasks : ")
            myTask()
            print("--------------------------------------------")
            continue
        elif option == 4:
            print("Thank You :) ")
            break
        else:
            print("\n--------------------------------------------")
            print("Invalid Input!!")
            print("--------------------------------------------\n")
            continue
    except:
        print("--------------------------------------------\n")
        print("Enter Numbers Only!!")
        print("--------------------------------------------\n")
        continue

