import streamlit as st
from datetime import date, time
from pawpal_system import Pet, Owner, Scheduler, Task, RECURRENCE_OPTIONS

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")
st.title("🐾 PawPal+")

# --- Session state init ---
if "owner" not in st.session_state:
    st.session_state.owner = None
if "scheduler" not in st.session_state:
    st.session_state.scheduler = None

# --- Owner setup ---
st.subheader("Owner & Pet")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

if st.button("Set Owner & Pet"):
    pet = Pet(name=pet_name, species=species)
    owner = Owner(name=owner_name)
    owner.add_pet(pet)
    st.session_state.owner = owner
    st.session_state.scheduler = Scheduler(owner=owner)
    st.success(f"Owner '{owner_name}' created with pet '{pet_name}'.")

# --- Task input ---
st.divider()
st.subheader("Add a Task")

if st.session_state.owner is None:
    st.info("Set an owner and pet above before adding tasks.")
else:
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        task_name = st.text_input("Task name", value="Morning Walk")
    with col2:
        task_desc = st.text_input("Description", value="Walk around the block")
    with col3:
        task_hour = st.number_input("Hour (0-23)", min_value=0, max_value=23, value=7)
    with col4:
        priority = st.selectbox("Priority", ["high", "medium", "low"])
    with col5:
        recurrence = st.selectbox("Recurrence", RECURRENCE_OPTIONS)
    with col6:
        due = st.date_input("Due date", value=date.today())

    if st.button("Add Task"):
        task = Task(
            name=task_name,
            description=task_desc,
            time=time(task_hour, 0),
            priority=priority,
            recurrence=recurrence,
            due_date=due,
        )
        st.session_state.owner.get_pets()[0].add_task(task)
        st.success(f"Task '{task_name}' added for {due}.")

# --- Schedule ---
st.divider()
st.subheader("Today's Schedule")

if st.session_state.scheduler is not None:
    scheduler: Scheduler = st.session_state.scheduler
    pets = st.session_state.owner.get_pets()
    pet_names = [p.name for p in pets]

    # --- Controls row ---
    ctrl1, ctrl2, ctrl3 = st.columns(3)
    with ctrl1:
        sort_key = st.radio("Sort by", ["priority", "time"], horizontal=True)
    with ctrl2:
        pet_filter = st.selectbox("Filter by pet", ["All pets"] + pet_names)
    with ctrl3:
        status_filter = st.selectbox("Filter by status", ["Pending", "Completed", "All"])

    if st.button("Generate Schedule"):
        # --- Conflict detection ---
        conflicts = scheduler.get_conflicts()
        if conflicts:
            st.warning("**Scheduling conflicts detected:**")
            for msg in conflicts:
                st.warning(f"  • {msg}")

        # --- Fetch tasks based on filters ---
        if status_filter == "Completed":
            schedule = scheduler.filter_by_status(completed=True)
        elif pet_filter != "All pets" and status_filter == "Pending":
            schedule = scheduler.filter_by_pet(pet_filter, sort_key=sort_key)
        elif status_filter == "All":
            all_tasks = []
            for pet in pets:
                if pet_filter == "All pets" or pet.name == pet_filter:
                    all_tasks.extend(pet.get_tasks())
            schedule = scheduler.sort_tasks(all_tasks, key=sort_key)
        else:
            schedule = scheduler.build_schedule(sort_key=sort_key)

        if not schedule:
            st.info("No tasks found for the selected filters.")
        else:
            for i, task in enumerate(schedule, start=1):
                recur_label = f" | {task.recurrence}" if task.recurrence != "none" else ""
                done_label = " [done]" if task.completion_status else ""
                st.markdown(
                    f"**{i}. [{task.priority.upper()}] {task.name}{done_label}** "
                    f"on {task.due_date} at {task.time.strftime('%I:%M %p')} — "
                    f"{task.description}{recur_label}"
                )

    # --- Mark complete ---
    st.divider()
    st.subheader("Mark Task Complete")
    all_pending = scheduler.build_schedule()
    if all_pending:
        # Build label -> (pet_name, task_name) mapping to handle same-named tasks across pets
        options = {}
        for pet in pets:
            for task in pet.get_tasks():
                if not task.completion_status:
                    label = f"{pet.name}: {task.name} ({task.due_date})"
                    options[label] = (pet.name, task.name)

        selected_label = st.selectbox("Select task to mark done", list(options.keys()))

        if st.button("Mark Complete"):
            pet_n, task_n = options[selected_label]
            next_task = scheduler.mark_task_complete(pet_n, task_n)
            st.success(f"'{task_n}' marked as complete.")
            if next_task is not None:
                st.info(
                    f"Recurring task auto-scheduled: '{next_task.name}' "
                    f"due {next_task.due_date} ({next_task.recurrence})"
                )
    else:
        st.info("No pending tasks to complete.")
