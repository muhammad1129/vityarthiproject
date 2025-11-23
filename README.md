# Desktop Wellness Companion (Tkinter)

## Project Overview

    The Desktop Wellness Companion is a lightweight, local Python application designed to combat common issues associated with long hours of digital work, such as eye strain, poor posture, and dehydration.

    Inspired by the Pomodoro Technique, it schedules timely, mandatory breaks, presenting random wellness tips and reminders to help the user maintain physical and mental well-being throughout their workday.

## Features

    -Timed Reminders: Set a custom interval (in minutes) for regular wellness prompts.

    -Wellness Tip Library: Randomly selects from a curated list of tips covering hydration, stretching, posture, mindful breathing, and digital detox.

    -Robust Input Validation: Ensures stable operation by restricting the reminder interval input to whole numbers within a safe range (1 to 120 minutes), preventing crashes or excessive rapid-fire popups.

    -Clean Shutdown: Gracefully cancels all scheduled timers upon closing the application window, ensuring no unexpected dialogs appear later.

    -Simple GUI: Uses tkinter and ttk for a native, straightforward desktop interface.

## 🔒 Security and Robustness Focus

    Since this is a single-user, local application with no network access, the primary focus is on robustness and stability:

    1-Input Sanitation: The input field uses key validation (validate_input) to block all non-numeric characters immediately. The start_reminders function performs a final bounds check to ensure the interval is sensible (between 1 and 120 minutes).

    2-Thread Safety: The application exclusively uses the Tkinter master.after() mechanism for scheduling, ensuring all GUI operations and updates occur safely on the main thread, thus eliminating risks associated with race conditions and deadlocks common with multi-threading.

    3-Hardcoded Data: Wellness tips are stored as immutable Python list data, meaning the content of the reminders cannot be injected or modified by external sources during runtime.

## Prerequisites

    To run this application, you only need Python installed. Tkinter is typically included with standard Python installations (version 3.x).

    -Python 3.x

## How to Run

    1-Save the provided Python code as wellness_companion.py.

    2-Open your terminal or command prompt.

    3-Navigate to the directory where you saved the file.

    4-Run the application using the Python interpreter:

    5-python wellness_companion.py


## Configuration

    The reminder interval is configurable directly within the application window.

    Setting                 Default Value               Description

    Interval (minutes)      25                          The time between each wellness reminder popup.

    You can change the WELLNESS_TIPS list directly in the source code if you wish to customize the content of the reminders.
