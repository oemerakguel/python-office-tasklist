tasklist = []

def add_task():
    task = input("Bitte gib eine Aufgabe ein, die in deiner Aufgabenliste hinzugefügt werden soll: \n")
    tasklist.append(task)
    print(f"Die Aufgabe {task} wurde zur Liste hinzugefügt.")
add_task()

print(tasklist)