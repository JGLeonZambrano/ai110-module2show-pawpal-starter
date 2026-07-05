import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pawpal_system import Task, Pet, Owner, Scheduler

def test_task_completion():
    """Verify mark_complete() actually changes is_complete to True"""
    task = Task("Feed Mochi", 10, "high", "08:00")
    assert task.is_complete == False
    task.mark_complete()
    assert task.is_complete == True

def test_task_addition():
    """Verify adding a task increases the pet's task count"""
    pet = Pet("Mochi", "cat", "fluffy", "none")
    assert len(pet.tasks) == 0
    pet.add_task(Task("Feed Mochi", 10, "high", "08:00"))
    assert len(pet.tasks) == 1

def test_sort_by_time():
    """Verify tasks are returned in chronological order."""
    owner = Owner("Jordan", "prefers morning tasks")
    pet = Pet("Mochi", "cat", "fluffy", "none")
    owner.add_pet(pet)
    pet.add_task(Task("Evening task", 10, "high", "17:00"))
    pet.add_task(Task("Morning task", 10, "high", "07:00"))
    scheduler = Scheduler(owner)
    sorted_tasks = scheduler.sort_by_time()
    assert sorted_tasks[0].due_time == "07:00"
    assert sorted_tasks[1].due_time == "17:00"

def test_recurrence_logic():
    """Verify marking a daily task complete creates a new task."""
    task = Task("Feed Mochi", 10, "high", "08:00", "daily")
    new_task = task.mark_complete()
    assert task.is_complete == True
    assert new_task is not None
    assert new_task.is_complete == False

def test_conflict_detection():
    """Verify scheduler flags duplicate due times."""
    owner = Owner("Jordan", "prefers morning tasks")
    pet = Pet("Mochi", "cat", "fluffy", "none")
    owner.add_pet(pet)
    pet.add_task(Task("Feed Mochi", 10, "high", "08:00"))
    pet.add_task(Task("Give meds", 5, "high", "08:00"))
    scheduler = Scheduler(owner)
    result = scheduler.detect_conflicts()
    assert "Conflict" in result

def test_empty_pet_task_list():
    """Verify scheduler handles a pet with no tasks gracefully."""
    owner = Owner("Jordan", "preferences")
    pet = Pet("Mochi", "cat", "fluffy", "none")
    owner.add_pet(pet)
    scheduler = Scheduler(owner)
    assert scheduler.get_all_tasks() == []

def test_filter_by_time_empty():
    """Verify filter_by_time returns empty list when no tasks fit."""
    owner = Owner("Jordan", "preferences")
    pet = Pet("Mochi", "cat", "fluffy", "none")
    owner.add_pet(pet)
    pet.add_task(Task("Long task", 120, "high", "08:00"))
    scheduler = Scheduler(owner)
    result = scheduler.filter_by_time(10)
    assert result == []