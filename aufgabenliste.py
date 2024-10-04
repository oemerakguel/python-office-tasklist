tasklist = []

def add_task():
    task = input("Bitte gib eine Aufgabe ein, die in deiner Aufgabenliste hinzugefügt werden soll: \n")
    tasklist.append(task)
    print(f"Die Aufgabe {task} wurde zur Liste hinzugefügt.")
add_task()

def show_tasklist():
    if tasklist == None:
        print("Your tasklist is empty.")
    else:
        print("Your tasklist:")
        for task in tasklist:
            print(task)
show_tasklist()
