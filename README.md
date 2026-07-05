# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## ✨ Features
- Add owners, pets, and care tasks via a web UI
- Generate daily schedules sorted by priority or time
- Detect scheduling conflicts with warning messages
- Filter tasks by pet, completion status, or available time
- Recurring task support (daily and weekly)
- 7 automated tests verifying core behaviors

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

```
📅 Today's Schedule for Jordan:
╭─────────────────────────┬────────────┬────────────┬───────╮
│ Task                    │ Duration   │ Priority   │ Due   │
├─────────────────────────┼────────────┼────────────┼───────┤
│ Feed Mochi              │ 10 min     │ high       │ 08:00 │
│ Morning walk            │ 30 min     │ high       │ 07:00 │
│ Clean litter box        │ 15 min     │ medium     │ 09:00 │
│ Play with automated toy │ 10 min     │ medium     │ 09:30 │
╰─────────────────────────┴────────────┴────────────┴───────╯

✅ No conflicts detected.

🕐 Tasks sorted by time:
╭─────────────────────────┬────────────┬────────────┬───────╮
│ Task                    │ Duration   │ Priority   │ Due   │
├─────────────────────────┼────────────┼────────────┼───────┤
│ Morning walk            │ 30 min     │ high       │ 07:00 │
│ Feed Mochi              │ 10 min     │ high       │ 08:00 │
│ Clean litter box        │ 15 min     │ medium     │ 09:00 │
│ Play with automated toy │ 10 min     │ medium     │ 09:30 │
│ Grooming                │ 45 min     │ low        │ 10:00 │
│ Evening walk            │ 30 min     │ medium     │ 17:00 │
╰─────────────────────────┴────────────┴────────────┴───────╯

🐱 Tasks for Mochi only:
╭─────────────────────────┬────────────┬────────────┬───────╮
│ Task                    │ Duration   │ Priority   │ Due   │
├─────────────────────────┼────────────┼────────────┼───────┤
│ Feed Mochi              │ 10 min     │ high       │ 08:00 │
│ Clean litter box        │ 15 min     │ medium     │ 09:00 │
│ Play with automated toy │ 10 min     │ medium     │ 09:30 │
╰─────────────────────────┴────────────┴────────────┴───────╯
```

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
python3 -m pytest tests/test_pawpal.py -v
```
Sample test output:

```
===== test session starts =====
tests/test_pawpal.py::test_task_completion PASSED         [ 14%]
tests/test_pawpal.py::test_task_addition PASSED           [ 28%]
tests/test_pawpal.py::test_sort_by_time PASSED            [ 42%]
tests/test_pawpal.py::test_recurrence_logic PASSED        [ 57%]
tests/test_pawpal.py::test_conflict_detection PASSED      [ 71%]
tests/test_pawpal.py::test_empty_pet_task_list PASSED     [ 85%]
tests/test_pawpal.py::test_filter_by_time_empty PASSED    [100%]
===== 7 passed in 0.02s =====
```
**Confidence Level:** ⭐⭐⭐⭐ (4/5) — Core behaviors and edge cases 
verified. Invalid priority values not yet tested.

## 📐 Smarter Scheduling

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `sort_by_priority()`, `sort_by_time()` | Sorts high→medium→low or by HH:MM |
| Filtering | `filter_by_time()`, `filter_by_pet()`, `filter_by_status()` | By time, pet name, or completion |
| Conflict handling | `detect_conflicts()` | Returns warning message for duplicate times |
| Recurring tasks | `mark_complete()` | Returns next Task instance if daily/weekly |

## 🎨 Output Formatting

PawPal+ uses the `tabulate` library to display schedules as professional rounded tables in the CLI, with columns for Task, Duration, Priority, and Due time.

Functions using tabulate formatting:
- `filter_by_time()` — main schedule display
- `sort_by_time()` — chronological view
- `filter_by_pet()` — per-pet task view

Install: `pip3 install tabulate`

## 📸 Demo Walkthrough

1. Run `python3 -m streamlit run app.py` to launch the app
2. Enter owner name and preferences, click "Save Owner"
3. Add a pet (name, species, description, notes), click "Add Pet"
4. Add tasks to the pet (description, duration, priority, due time)
5. Choose to sort by Priority or Time, set available minutes, click "Generate Schedule"
6. App displays today's schedule as a table with conflict detection

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
