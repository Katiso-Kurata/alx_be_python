# daily_reminder.py

def main():
    # Prompt for a single task
    task = input("Enter your task: ").strip()
    
    # Prompt for the task’s priority
    priority = input("Priority (high/medium/low): ").strip().lower()
    
    # Prompt to check if the task is time-bound
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
    
    # 
    reminder = ""
    
    # 
    match priority:
        case "high":
            reminder = f"Reminder: '{task}' is a high priority task"
        case "medium":
            reminder = f"Reminder: '{task}' is a medium priority task"
        case "low":
            reminder = f"Note: '{task}' is a low priority task"
        case _:
            reminder = "Invalid priority level entered."
    
    # 
    if reminder != "Invalid priority level entered.":
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        elif time_bound == "no":
            reminder += ". Consider completing it when you have free time."
        else:
            reminder += ". Invalid time-bound input."

    #
    print(reminder)

# Call the main function
if __name__ == "__main__":
    main()
