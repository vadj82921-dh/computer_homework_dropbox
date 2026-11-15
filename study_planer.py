subjects = []
tasks = []
status = []

def load_tasks():

    try:
        file = open("tasks.txt", "r")

        for line in file:
            data = line.strip().split(",")

            subjects.append(data[0])
            tasks.append(data[1])
            status.append(data[2])

        file.close()

    except FileNotFoundError:
        print("Starting a new study planner.")


def save_tasks():

    file = open("tasks.txt", "w")

    for i in range(len(tasks)):
        file.write(subjects[i] + "," + tasks[i] + "," + status[i] + "\n")

    file.close()

load_tasks()

while True:

    print("\n===== PERSONAL STUDY PLANNER =====")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Complete a task")
    print("4. Delete a task")
    print("5. View progress")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":

        subject = input("Enter subject: ")
        task = input("Enter homework: ")

        subjects.append(subject)
        tasks.append(task)
        status.append("Pending")

        save_tasks()

        print("Task added successfully!")

    elif choice == "2":

        if len(tasks) == 0:
            print("No tasks available.")

        else:
            for i in range(len(tasks)):

                print("\nTask number:", i + 1)
                print("Subject:", subjects[i])
                print("Homework:", tasks[i])
                print("Status:", status[i])

    elif choice == "3":

        for i in range(len(tasks)):
            print(i + 1, tasks[i], "-", status[i])

        if len(tasks) > 0:

            number = int(input("Enter task number: "))

            if number >= 1 and number <= len(tasks):

                status[number - 1] = "Completed"

                save_tasks()

                print("Task completed!")

            else:
                print("Invalid task number.")

        else:
            print("No tasks to complete.")

    elif choice == "4":

        for i in range(len(tasks)):
            print(i + 1, tasks[i])

        if len(tasks) > 0:

            number = int(input("Enter task number to delete: "))

            if number >= 1 and number <= len(tasks):

                subjects.pop(number - 1)
                tasks.pop(number - 1)
                status.pop(number - 1)

                save_tasks()

                print("Task deleted!")

            else:
                print("Invalid task number.")

        else:
            print("No tasks to delete.")

    elif choice == "5":

        completed = 0

        for i in range(len(tasks)):

            if status[i] == "Completed":
                completed = completed + 1

        total = len(tasks)
        pending = total - completed

        print("\n===== STUDY PROGRESS =====")
        print("Total tasks:", total)
        print("Completed tasks:", completed)
        print("Pending tasks:", pending)

        if total > 0:

            percentage = (completed / total) * 100

            print("Completion:", round(percentage), "%")

    elif choice == "6":

        save_tasks()

        print("Your tasks have been saved.")
        print("Goodbye!")

        break


    else:
        print("Invalid choice. Please try again.")
