import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pawpal_system import Task, Pet, Owner, Scheduler

def test_task_completion():
    # Verify mark_complete() actually changes is_complete to True
    task = Task("Feed Mochi", 10, "high", "08:00")
    assert task.is_complete == False
    task.mark_complete()
    assert task.is_complete == True

def test_task_addition():
    # Verify adding a task increases the pet's task count
    pet = Pet("Mochi", "cat", "fluffy", "none")
    assert len(pet.tasks) == 0
    pet.add_task(Task("Feed Mochi", 10, "high", "08:00"))
    assert len(pet.tasks) == 1