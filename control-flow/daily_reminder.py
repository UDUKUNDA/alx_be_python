task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

if priority not in ["high", "medium", "low"]:
    print("You have to enter high, medium, or low to let us know your task's priority.")
if time_bound not in ["yes", "no"]:
    print("You have to enter yes or no to let us know your task's time sensitivity.")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention.")
        elif time_bound == "no":
            print(f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires immediate attention.")
        elif time_bound == "no":
            print(f"Reminder: '{task}' is a medium priority task. Consider completing it when you have free time.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task that requires immediate attention.")
        elif time_bound == "no":
            print(f"Reminder: '{description}' is a low priority task. Consider completing it when you have free time.")