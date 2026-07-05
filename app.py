import streamlit as st
from pawpal_system import Task, Pet, Owner, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")
st.title("🐾 PawPal+")

# Step 2: Manage memory — only create Owner once
if "owner" not in st.session_state:
    st.session_state.owner = Owner("", "")

owner = st.session_state.owner

# Owner setup
st.subheader("👤 Owner Info")
owner_name = st.text_input("Owner name", value=owner.name)
preferences = st.text_input("Preferences", value=owner.preferences)
if st.button("Save Owner"):
    st.session_state.owner.name = owner_name
    st.session_state.owner.preferences = preferences
    st.success(f"Owner {owner_name} saved!")

st.divider()

# Add a pet
st.subheader("🐾 Add a Pet")
pet_name = st.text_input("Pet name")
species = st.selectbox("Species", ["dog", "cat", "fish", "bird", "other"])
description = st.text_input("Description")
notes = st.text_input("Notes")
if st.button("Add Pet"):
    new_pet = Pet(pet_name, species, description, notes)
    st.session_state.owner.add_pet(new_pet)
    st.success(f"Added {pet_name}!")

# Show current pets
if owner.pets:
    st.write("Current pets:", [p.name for p in owner.pets])

st.divider()

# Add a task
st.subheader("📋 Add a Task")
if owner.pets:
    pet_choice = st.selectbox("Choose pet", [p.name for p in owner.pets])
    task_desc = st.text_input("Task description")
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
    priority = st.selectbox("Priority", ["high", "medium", "low"])
    due_time = st.text_input("Due time (HH:MM)", value="08:00")
    if st.button("Add Task"):
        pet = next(p for p in owner.pets if p.name == pet_choice)
        pet.add_task(Task(task_desc, duration, priority, due_time))
        st.success(f"Task added to {pet_choice}!")
else:
    st.info("Add a pet first before adding tasks.")

st.divider()

# Generate schedule
st.subheader("📅 Generate Schedule")
available_minutes = st.number_input("Available minutes today", min_value=10, max_value=480, value=90)
if st.button("Generate Schedule"):
    if owner.pets:
        scheduler = Scheduler(owner)
        schedule = scheduler.generate_schedule(available_minutes)
        conflicts = scheduler.detect_conflicts()
        st.markdown("### Today's Schedule")
        for item in schedule:
            st.write(f"• {item}")
        st.write(scheduler.detect_conflicts())
    else:
        st.info("Add pets and tasks first!")