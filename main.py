from pawpal_system import Task, Pet, Owner, Scheduler
from tabulate import tabulate

# Create Owner
jordan = Owner("Jordan", "prefers morning tasks")

# Create two Pets
mochi = Pet("Mochi", "cat", "fluffy and shy", "allergic to fish")
biscuit = Pet("Biscuit", "dog", "energetic golden retriever", "needs two walks daily")

# Add pets to owner
jordan.add_pet(mochi)
jordan.add_pet(biscuit)

# Add tasks to Mochi
mochi.add_task(Task("Feed Mochi", 10, "high", "08:00"))
mochi.add_task(Task("Clean litter box", 15, "medium", "09:00"))
mochi.add_task(Task("Play with automated toy", 10, "medium", "09:30"))

# Add tasks to Biscuit
biscuit.add_task(Task("Morning walk", 30, "high", "07:00"))
biscuit.add_task(Task("Evening walk", 30, "medium", "17:00"))
biscuit.add_task(Task("Grooming", 45, "low", "10:00"))

# Create Scheduler
scheduler = Scheduler(jordan)

# Generate schedule with tabulate formatting
print(f"\n📅 Today's Schedule for {jordan.name}:")
schedule = scheduler.filter_by_time(90)
table_data = [
    [task.description, f"{task.duration_minutes} min", 
     task.priority, task.due_time]
    for task in schedule
]
headers = ["Task", "Duration", "Priority", "Due"]
print(tabulate(table_data, headers=headers, tablefmt="rounded_outline"))

# Conflict detection
print(f"\n{scheduler.detect_conflicts()}")

# Sort by time with tabulate
print(f"\n🕐 Tasks sorted by time:")
time_data = [
    [task.description, f"{task.duration_minutes} min",
     task.priority, task.due_time]
    for task in scheduler.sort_by_time()
]
print(tabulate(time_data, headers=headers, tablefmt="rounded_outline"))

# Filter by pet
print(f"\n🐱 Tasks for Mochi only:")
mochi_data = [
    [task.description, f"{task.duration_minutes} min",
     task.priority, task.due_time]
    for task in scheduler.filter_by_pet("Mochi")
]
print(tabulate(mochi_data, headers=headers, tablefmt="rounded_outline"))