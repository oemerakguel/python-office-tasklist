tasklist = []

def add_task():
    task = input("Bitte gib eine Aufgabe ein, die in deiner Aufgabenliste hinzugefügt werden soll: \n")
    tasklist.append(task)
    print(f"Die Aufgabe {task} wurde zur Liste hinzugefügt.")


def show_tasklist():
    if tasklist == None:
        print("Your tasklist is empty.")
    else:
        print("Your tasklist:")
        for index, task in tasklist:
            print(f"{index}. {task}")


def main():
    while True:
        print("Deine Optionen: ")
        print("1. Aufgabe hinzufügen")
        print("2. Aufgabenliste anzeigen.")
        print("3. Programm beenden.")

        choice = input("Was möchten Sie tun?")

        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasklist()
        elif choice == "3":
            print("Programm wird beendet! Auf Wiedersehen.")
            ecit()
        elif not choice == "1" or choice == "2" or choice == "3":
            print("Ungültige Auswahl. Bitte wähle 1, 2 oder 3")



