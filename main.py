from pawpal_system import Task, Pet, Owner, Scheduler

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
# Task to test overlapping tasks:
# mochi.add_task(Task("Extra feeding", 10, "high", "07:00"))

# Add tasks to Biscuit
biscuit.add_task(Task("Morning walk", 30, "high", "07:00"))
biscuit.add_task(Task("Evening walk", 30, "medium", "17:00"))
biscuit.add_task(Task("Grooming", 45, "low", "10:00"))

# Create Scheduler
scheduler = Scheduler(jordan)

# Generate schedule with 90 minutes available
print(f"\n📅 Today's Schedule for {jordan.name}:")
print("-" * 40)
schedule = scheduler.generate_schedule(90)
for item in schedule:
    print(f"  • {item}")

# Check conflicts
print(f"\n{scheduler.detect_conflicts()}")

# Demonstrate sort_by_time
print(f"\n🕐 Tasks sorted by time:")
for task in scheduler.sort_by_time():
    print(f"  • {task.get_details()}")

# Demonstrate filter_by_pet
print(f"\n🐱 Tasks for Mochi only:")
for task in scheduler.filter_by_pet("Mochi"):
    print(f"  • {task.get_details()}")