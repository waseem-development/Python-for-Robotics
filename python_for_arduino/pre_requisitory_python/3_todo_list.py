def addTask(tasks):
    task = input("Add a new task: ").lower()
    if task in tasks:
        print("\nTask already added.")
        return
    else:
        tasks.append(task)
        print("\nTask succesfully added to your to-do-list.")


def removeTask(tasks):
    if len(tasks) == 0:
        print("\nTo-Do-List is empty")
        return
    task = input("Enter the task to be deleted: ").lower()
    if not task in tasks:
        print("\nTask does not exist so it cannot be deleted:")
    else:
        tasks.remove(task)
        print("\nTask succesfully removed from to-do-list.")


def viewTask(tasks):
    if len(tasks) == 0:
        print("To-Do-List is empty")
        return
    else:
        print("Your Tasks are listed below:")
        for index, task in enumerate(tasks):
            print(f"{index + 1}) {task.capitalize()}")


tasks = []
print("********* Welcome to the ABC Task App *********")
while(True):
    print("""Press
          1 ==> To add a task
          2 ==> To remove a task
          3 ==> To view all your tasks""")
    option = int(input("Option: "))
    print()
    if option == 1:
        addTask(tasks)
        print()
    elif option == 2:
        removeTask(tasks)
        print()
    elif option == 3:
        viewTask(tasks)
        print()
    else:
        print("Invalid option!!!\n")
        continue