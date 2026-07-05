# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
As per the design spec, there are four boxes: Owner, Pet, Scheduler, and Task. Each detail appropriate methods and attributes, and display the relationships between them. Scheduler reads what Owner defines about their Pet(s), then manages those pets using their Tasks.
- What classes did you include, and what responsibilities did you assign to each?
• Owner: holds name and preferences, owns one or more Pets, with an add_pet() method.
• Pet: holds identifying info (name, species, description, notes) and a list of tasks, with add_task() and list_tasks() methods.
• Task: defines whether it is complete or not, holding description, duration, priority, due time, and a mark_complete() method.
• Scheduler: reads Owner and manages Pets based on owner preferences and each pet's tasks, with methods to sort by priority, detect conflicts, filter by time, and generate a schedule.

**b. Design changes**

- Did your design change during implementation?
No: the implementation matches the initial UML design exactly.
Note that Owner.preferences is never used for any Scheduling logic, and this could later on create conflicts or be a springboard for another feature.
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
Time (ie minutes) available in the day, completion status (whether the task is pending or done), and priority (See below)
- How did you decide which constraints mattered most?
Through the priority, as defined by the user. The logic is coded so that priority_order = {"high": 1, "medium": 2, "low": 3}, from which all else is organized around. This, because a pet owner should always complete critical care tasks (feeding, medication) before others (grooming, enrichment), regardless of time available.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
The scheduler stores data in memory via st.session_state, which means all pets and tasks are lost when the session ends.
- Why is that tradeoff reasonable for this scenario?
This is a reasonable tradeoff for a prototype but would need file or database persistence for real-world use. The scheduler checks for conflicts using exact due time matches only. If two tasks are at '08:00' it flags a conflict, but it does not detect overlapping durations (e.g., a 30-minute task at 08:00 and a 15-minute task at 08:20 would not be flagged). This is reasonable for a prototype where simplicity matters more than precision.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
Design, debugging, but also going over basics that require practice: I can ask for help in minutiae and can practice.
- What kinds of prompts or questions were most helpful?
Meditated ones that explicitly define what to do and what not to do.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
When asking for improvements on the Priorities: I was given an option that skipped the dictionary approach implemented as it was a bit more human readable, but prefered to keep the original design as it would be more efficient should this project grow in scope
- How did you evaluate or verify what the AI suggested?
First, reasoning based on context and knowledge. Then testing the suggestion outright in a controlled environment.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
The core class behaviors: task completion status changes, task addition to pets, sorting correctness by time, recurrence logic for daily tasks, conflict detection for duplicate due times, and edge cases like empty task lists and time-constrained filtering. 
- Why were these tests important?
These are important because they verify that the scheduler's core logic works as designed before connecting it to the UI.

**b. Confidence**

- How confident are you that your scheduler works correctly?
Confident in core behaviors, as 7 tests pass consistently. Less confident in edge cases involving invalid priority values or malformed time strings, which could cause KeyErrors or crashes.
- What edge cases would you test next if you had more time?
Next I would test: a pet with tasks spanning midnight (e.g., "23:00" and "00:30"), invalid priority strings, and concurrent sessions with multiple owners.
---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
The conflict resolution: it took me time to understand the sugggested logic and then implement it, so it is nice seeing it in place

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
I'd make the display of stored pets a bit more final-user friendly.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
There is no point in using AI without a clear understanding of both overall goals and the grand architecture, because there is a tendency to baloon elements that and thus you can lose focus.