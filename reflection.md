# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- The Owner class stores the owner's name and a list of pets they own. It includes methods to add a pet, remove a pet by name, and return the list of pets.

- The Pet class stores a pet's name, species, and a list of tasks. Its methods allow tasks to be added, removed by name, and returned when needed.

- The Task class stores information about a task, including its description, due date, priority, and whether it has been completed. It also has a method to mark the task as complete.

- The Scheduler class creates a schedule using the tasks from an owner's pets. It stores a reference to an owner and includes methods to build and sort the schedule.

- The relationships are one-to-many from Owner to Pet, meaning one owner can have many pets, one-to-many from Pet to Task, meaning one pet can have many tasks, and one-to-one from Scheduler to Owner, meaning each scheduler works with one owner.


**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

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
