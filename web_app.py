import streamlit as st
import matplotlib.pyplot as plt
st.title("Task Scheduler with Dependencies")
if "tasks" not in st.session_state:
    st.session_state.tasks = []
if "execution_order" not in st.session_state:
    st.session_state.execution_order = []
name = st.text_input("Task Name")
priority = st.number_input("Priority (lower = higher)", min_value=1, step=1)
duration = st.number_input("Duration", min_value=1, step=1)
existing_task_names = [t["name"] for t in st.session_state.tasks]
dependency = st.selectbox("Dependency (optional)", ["None"] + existing_task_names)
if st.button("Add Task"):
    if name == "":
        st.warning("Enter task name")
    else:
        st.session_state.tasks.append({
            "name": name,
            "priority": priority,
            "duration": duration,
            "dependency": None if dependency == "None" else dependency
        })
        st.success(f"Task '{name}' added!")
st.subheader("Tasks")
for task in st.session_state.tasks:
    st.write(task)
if st.button("Run Scheduler"):
    tasks = st.session_state.tasks.copy()
    completed = []
    execution_order = []
    while tasks:
        for task in tasks:
            dep = task["dependency"]
            if dep is None or dep in completed:
                execution_order.append(task)
                completed.append(task["name"])
                tasks.remove(task)
                break
        else:
            st.error("⚠️ Circular dependency detected!")
            break
    st.session_state.execution_order = execution_order
if st.session_state.execution_order:
    st.subheader("Execution Order")
    for task in st.session_state.execution_order:
        st.write(f"{task['name']} (Duration: {task['duration']})")
    st.subheader("Execution Timeline (Gantt Chart)")
    current_time = 0
    fig, ax = plt.subplots()
    for task in st.session_state.execution_order:
        start = current_time
        duration = task["duration"]
        ax.barh(task["name"], duration, left=start)
        current_time += duration
    ax.set_xlabel("Time")
    ax.set_ylabel("Tasks")
    ax.set_title("Task Scheduling Gantt Chart")
    st.pyplot(fig)