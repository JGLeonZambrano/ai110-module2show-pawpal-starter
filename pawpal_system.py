# Definition of tasks and other files

class Task:
    def __init__(self, description, duration_minutes, priority, due_time):
        self.description = description #Stores the description of this Tas
        self.duration_minutes = duration_minutes #Stores the duration of the tasks in minutes
        self.priority = priority #Defines the priority status
        self.due_time = due_time #Defines the due time for this task
        self.is_complete = False #defines the status of the task, ie true (complete) or not

    def mark_complete(self):
        """Changes the Task into is_complete == True when complete"""
        self.is_complete = True
    
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
        """Returns conflicts if tasks's due times generate issues"""
        tasks_to_check = self.get_all_tasks() # Get all tasks related to the relevant Schedule
        due_times = [task.due_time for task in tasks_to_check] 
        #There will be a conflict if the length of due_times is not equal to their set
        conflicts = len(due_times) != len(set(due_times))
        return conflicts
    
    def generate_schedule(self, available_minutes):
        """Generates a schedule after filtering all times"""
        tasks_filtered_by_time = self.filter_by_time(available_minutes) #Get the tasks filtered by time
        return [task.get_details() for task in tasks_filtered_by_time]
    
