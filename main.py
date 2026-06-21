from datetime import time
from pawpal_system import Owner, Pet, Task, Scheduler

owner = Owner(name="Jordan")

mochi = Pet(name="Mochi", species="dog")
luna = Pet(name="Luna", species="cat")

mochi.add_task(Task(
    name="Morning Walk",
    description="30-minute walk around the block",
    time=time(7, 0),
    priority="high",
))
mochi.add_task(Task(
    name="Evening Feed",
    description="One cup of dry food",
    time=time(18, 0),
    priority="low",
))
luna.add_task(Task(
    name="Litter Box",
    description="Clean and refill litter box",
    time=time(19, 0),
    priority="medium",
))

owner.add_pet(mochi)
owner.add_pet(luna)

scheduler = Scheduler(owner=owner)
schedule = scheduler.build_schedule()

print("=== Today's Schedule ===")
for i, task in enumerate(schedule, start=1):
    status = "done" if task.completion_status else "pending"
    print(f"{i}. [{task.priority.upper()}] {task.name} at {task.time.strftime('%I:%M %p')} — {task.description} ({status})")
