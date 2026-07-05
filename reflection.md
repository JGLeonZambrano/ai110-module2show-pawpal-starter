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
Note that Owver.preferences is never used for any Shceduling logic, and this could later on create conflicts or be a springboard for another feature.
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
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
