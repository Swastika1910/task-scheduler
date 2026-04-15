# Task Scheduler with Dependencies

This is a simple project I built to understand how task scheduling works when there are priorities and dependencies between tasks.

The idea is that some tasks can only run after others are completed, and the scheduler should handle that properly while also considering priority.
---
## What this project does
* Lets you create tasks with:
  * name
  * priority
  * duration
  * dependency (optional)
* Runs tasks in the correct order
* Makes sure dependencies are completed first
* Detects if tasks are stuck because of circular dependencies
* Shows execution order
* In the web version, it also displays a Gantt chart
---
## Different versions

I tried implementing the same logic in different ways:

* CLI version → basic terminal-based scheduler
* Tkinter GUI → simple desktop interface
* Streamlit app → web interface with visualization
---
## How to run

First install dependencies:

```bash
pip install -r requirements.txt
```
Then you can run any version:

**CLI**
```bash
python task_scheduler.py
```
**GUI**
```bash
python uischeduler.py
```
**Web App**
```bash
streamlit run web_app.py
```
---

## How it works (in short)
* Tasks are stored in a priority queue
* The scheduler keeps checking if a task’s dependency is completed
* If not, it delays that task
* If tasks keep getting delayed, it detects a deadlock

---
## Why I made this

I built this project while learning about:

* Operating Systems (task scheduling)
* Data structures like heaps
* How dependencies affect execution order

---
## Tech used
* Python
* Streamlit
* Tkinter
* Matplotlib
---
## Author
Swastika Rajput
