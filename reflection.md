# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- The Owner class stores the owner's name and a list of pets they own. It includes methods to add a pet, remove a pet by name, and return the list of pets.

- The Pet class stores a pet's name, species, and a list of tasks. Its methods allow tasks to be added, removed by name, and returned when needed.

- The Task class stores information about a task, including its description, due date, priority, and whether it has been completed. It also has a method to mark the task as complete.

- The Scheduler class creates a schedule using the tasks from an owner's pets. It stores a reference to an owner and includes methods to build and sort the schedule.

- The relationships are one-to-many from Owner to Pet, meaning one owner can have many pets, one-to-many from Pet to Task, meaning one pet can have many tasks, and one-to-one from Scheduler to Owner, meaning each scheduler works with one owner.


**b. Design changes**

 Yes:

- Added Task.name to fix the mismatch with Pet.remove_task(task_name) — there was no field to match against before. 

- Changed Task.due_date from str to datetime.date so date comparisons work correctly in sorting. 

- Added PRIORITY_ORDER dict (high → 0, medium → 1, low → 2) and a comment on sort_tasks() to document the intended sort key (priority first, then due_date).

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

**Exact-time conflict detection instead of duration-aware overlap**

`get_conflicts()` flags two tasks as conflicting only when their `(due_date, time)` slots match exactly — for example, both at `2026-06-21 07:00 AM`. It does not consider how long each task takes, so a 30-minute Morning Walk starting at 7:00 AM and a 15-minute Morning Feed starting at 7:20 AM would *not* be flagged, even though they overlap in real life.

This is a reasonable tradeoff for this stage of the project for two reasons:

1. **Task has no duration field.** Detecting overlap requires knowing when each task *ends*, which means storing a duration or end time. Adding that field would ripple through every constructor call, the sorting logic, the UI form, and the auto-reschedule logic. The exact-match check gives meaningful warnings with zero additional data.

2. **Pet care tasks are typically point-in-time reminders, not calendar blocks.** "Feed at 7:00 AM" is a prompt, not a meeting. Exact-time conflicts (two reminders at the same moment) are the most actionable warning for an owner — they signal a scheduling mistake, not a tight but feasible back-to-back sequence.

The cost of this tradeoff is that genuinely overlapping tasks with different start times go undetected. If duration were added in a future iteration, `get_conflicts()` could be extended to check whether `task_a.time + timedelta(minutes=task_a.duration) > task_b.time` without changing the rest of the class interface.

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
