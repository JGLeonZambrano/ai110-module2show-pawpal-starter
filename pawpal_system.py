# Definition of tasks and other files

class Task:
    def __init__(self, description, duration_minutes, priority, due_time, frequency="none"):
        self.description = description #Stores the description of this Tas
        self.duration_minutes = duration_minutes #Stores the duration of the tasks in minutes
        self.priority = priority #Defines the priority status
        self.due_time = due_time #Defines the due time for this task
        self.is_complete = False #defines the status of the task, ie true (complete) or not
        self.frequency = frequency  # "daily", "weekly", or "none" for each task

    def mark_complete(self):
        """Marks task complete and schedules next occurrence if recurring."""
        from datetime import datetime, timedelta
        self.is_complete = True
        if self.frequency == "daily":
            next_due = datetime.strptime(self.due_time, "%H:%M") + timedelta(days=1)
            return Task(self.description, self.duration_minutes,
                    self.priority, next_due.strftime("%H:%M"), "daily")
        if self.frequency == "weekly":
            next_due = datetime.strptime(self.due_time, "%H:%M") + timedelta(weeks=1)
            return Task(self.description, self.duration_minutes,
                    self.priority, next_due.strftime("%H:%M"), "weekly")
        return None
    
    def get_details(self):
        """Returns the details of the specific task"""
        return f"{self.description} | {self.duration_minutes} minutes | {self.priority} priority | due on {self.due_time}"

class Pet:
    def __init__(self, name, species, description, notes):
        self.name = name # store name onto THIS pet
        self.species = species # store species onto THIS pet
        self.description = description # Defines the description of this pet
        self.notes = notes # Adds any specific notes for the pet
        self.tasks = [] # every new pet starts with empty task list

    def add_task(self, task):
        """Appends the entered to the Task's list"""
        self.tasks.append(task)

    def list_tasks(self):
        """Lists the entered Tasks for this specific pet"""
        return self.tasks

    def get_pending_tasks(self):
        """Returns only tasks where is_complete is False (i.e. not yet done)"""
        return [task for task in self.tasks if not task.is_complete]
     
class Owner:
    def __init__(self, name, preferences):
        self.name = name # Stores the owner's name
        self.preferences = preferences # Details the owner's preferences
        self.pets = [] #Stores all the Owner's pets
    
    def add_pet(self, pet):
        """Adds a pet to the owner"""
        self.pets.append(pet)

    def list_pets(self):
        """Lists the entered Pets of this Owner"""
        return self.pets
    
    def save_to_json(self, filename="data.json"):
        """Saves owner, pets and tasks to a JSON file."""
        import json
        data = {
            "name": self.name,
            "preferences": self.preferences,
            "pets": [
                {
                    "name": pet.name,
                    "species": pet.species,
                    "description": pet.description,
                    "notes": pet.notes,
                    "tasks": [
                        {
                            "description": task.description,
                            "duration_minutes": task.duration_minutes,
                            "priority": task.priority,
                            "due_time": task.due_time,
                            "is_complete": task.is_complete,
                            "frequency": task.frequency
                        }
                        for task in pet.tasks
                    ]
                }
                for pet in self.pets
            ]
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)

    @classmethod
    def load_from_json(cls, filename="data.json"):
        """Loads owner, pets and tasks from a JSON file."""
        import json
        with open(filename, "r") as f:
            data = json.load(f)
        owner = cls(data["name"], data["preferences"])
        for pet_data in data["pets"]:
            pet = Pet(pet_data["name"], pet_data["species"],
                    pet_data["description"], pet_data["notes"])
            for task_data in pet_data["tasks"]:
                pet.add_task(Task(
                    task_data["description"],
                    task_data["duration_minutes"],
                    task_data["priority"],
                    task_data["due_time"],
                    task_data["frequency"]
                ))
            owner.add_pet(pet)
        return owner

    
class Scheduler:
    def __init__(self, owner):
        self.owner = owner # Identifies the Owner for the identified schedule
        self.pets = owner.pets # Lists the pets in the schedule
    
    def get_all_tasks(self):
        """Return the tasks for each pet"""
        return [task for pet in self.pets for task in pet.tasks]
    
    def sort_by_priority(self):
        """Return the sorted list of all tasks, organized by a defined priority"""
        priority_order = {"high": 1, "medium": 2, "low": 3}
        return sorted(self.get_all_tasks(), key=lambda task:priority_order[task.priority])
    
    def sort_by_time(self):
        """Returns all tasks sorted by due time (HH:MM format)"""
        return sorted(self.get_all_tasks(), key=lambda task: task.due_time)

    def filter_by_time(self, available_minutes):
        """Filters tasks based on available minutes so that all are completed"""
        tasks_filtered_by_time = [] # Create new list for the tasks
        minutes_remaining = available_minutes  # start with all available time
        for task in self.sort_by_priority():  # go in priority order through all tasks
            # If time allows, append the task and subtract the time used
            if task.duration_minutes <= minutes_remaining:
                tasks_filtered_by_time.append(task)
                minutes_remaining -= task.duration_minutes
        return tasks_filtered_by_time
    
    def detect_conflicts(self):
        """Returns conflicts and a message if tasks's due times generate issues"""
        tasks_to_check = self.get_all_tasks() # Get all tasks related to the relevant Schedule
        due_times = [task.due_time for task in tasks_to_check] 
        seen = []
        conflicts = []
        for task in tasks_to_check:
            if task.due_time in seen:
                conflicts.append(f"⚠️ Conflict: '{task.description}' overlaps at {task.due_time}")
            seen.append(task.due_time)
        if conflicts:
            return "\n".join(conflicts)
        return "✅ No conflicts detected."
    
    def generate_schedule(self, available_minutes):
        """Generates a schedule after filtering all times"""
        tasks_filtered_by_time = self.filter_by_time(available_minutes) #Get the tasks filtered by time
        return [task.get_details() for task in tasks_filtered_by_time]
    
    def filter_by_pet(self, pet_name):
        """Returns only tasks belonging to a specific pet."""
        for pet in self.pets:
            if pet.name == pet_name:
                return pet.list_tasks()
        return []

    def filter_by_status(self, complete=False):
        """Returns tasks filtered by completion status."""
        return [task for task in self.get_all_tasks() 
                if task.is_complete == complete]
    
