import tkinter as tk                                                            #GUI: tkinter for the desktop interface.
from tkinter import ttk, messagebox
import random                                                                   #Random Selection: Choosing random tips/reminders.
import time                                                                     #Scheduling: Python's threading and time.sleep for timed intervals.
import threading

REMINDER_INTERVAL_MINUTES = 25                                                  #Default interval for a Pomodoro-style break
INITIAL_INTERVAL_MS = REMINDER_INTERVAL_MINUTES * 60 * 1000                     #Convert to milliseconds

WELLNESS_TIPS = [                                                               # A list of wellness tips and actions
    ("Hydration Reminder", "Time to grab a glass of water!"),
    ("Stretch Break", "Stand up, stretch your arms overhead, and roll your shoulders."),
    ("Eye Rest", "Look away from the screen for 20 seconds at something 20 feet away"),
    ("Mindful Minute", "Take 60 seconds to close your eyes and focus only on your breath."),
    ("Posture Check", "Sit up straight! Are your feet flat and your screen at eye level?"),
    ("Walk Around", "Do a quick 2-minute walk around your room or desk area."),
    ("Productivity Pause", "Take 2-minute nap and recall your progress up till now"),
    ("Wrist and Finger Exercise", "Gently rotate your wrists and stretch your fingers to prevent strain."),
    ("Digital Detox", "Put your phone facedown for the next 5 minutes. No notifications!"),
    ("Breathing Exercise", "Try 4-7-8 breathing: Inhale for 4, hold for 7, Exhale for 8."),
    ("Quick Tidy", "Spend 60 seconds organizing your immediate desk area for better focus."),
    ("Shoulder Release", "Perform 5 shoulder rolls backward and 5 forward to release tension.") ]

class WellnessApp:                                                              #Main application class for the desktop wellness reminder.
    def __init__(self, master):
        self.master = master
        master.title("Wellness Companion")
        master.resizable( False, False)                                         #Prevent the main window from being resizable
        
        style = ttk.Style()                                                     #Apply a simple theme
        style.configure('TFrame', background="#5df4c4")
        style.configure('TButton', font=('Inter', 12), padding=5)
        style.configure('TLabel', font=('Inter', 12), background="#e0e8e3")

        self.is_running = False
        self.interval_ms = INITIAL_INTERVAL_MS
        self.timer_id = None                                                    #To hold the ID of the scheduled Tkinter event

        main_frame = ttk.Frame(master, padding="15 15 15 15")                   #Setup Main Frame
        main_frame.pack(fill='both', expand=True)

        #Title
        ttk.Label(main_frame, text="Desktop Wellness Reminder", font=('Inter', 14, 'bold'), foreground='#333').grid(row=0, column=0, columnspan=2, pady=10)
        
        # Status Label
        self.status_text = tk.StringVar(value="Status: Ready to start")
        ttk.Label(main_frame, textvariable=self.status_text, font=('Inter', 10, 'italic'), foreground="#113556").grid(row=1, column=0, columnspan=2, pady=(0, 15))

        # Interval Input
        ttk.Label(main_frame, text="Interval (minutes):", foreground='#555').grid(row=2, column=0, sticky='w', padx=5, pady=5)
        
        self.interval_var = tk.StringVar(value=str(REMINDER_INTERVAL_MINUTES))
        interval_entry = ttk.Entry(main_frame, textvariable=self.interval_var, width=10)
        interval_entry.grid(row=2, column=1, sticky='ew', padx=5, pady=5)
        
        # Buttons
        self.start_button = ttk.Button(main_frame, text="Start Reminders", command=self.start_reminders, style='TButton')
        self.start_button.grid(row=3, column=0, sticky='ew', padx=5, pady=10)

        self.stop_button = ttk.Button(main_frame, text="Stop Reminders", command=self.stop_reminders, state=tk.DISABLED, style='TButton')
        self.stop_button.grid(row=3, column=1, sticky='ew', padx=5, pady=10)

        # Protocol for handling window closing
        master.protocol("WM_DELETE_WINDOW", self.on_closing)

    def start_reminders(self):
        """Starts the timer loop for reminders."""
        try:
            minutes = int(self.interval_var.get())
            if minutes <= 0:
                raise ValueError
            self.interval_ms = minutes * 60 * 1000
            
            self.is_running = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.status_text.set(f"Status: Running (Every {minutes} mins)")
            self.schedule_next_reminder()                                           #Start the first timer
            
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a positive whole number for the interval in minutes.")

    def stop_reminders(self):
        """Stops the timer loop."""
        self.is_running = False
        if self.timer_id:
            self.master.after_cancel(self.timer_id)                                 #Cancel the scheduled event
            self.timer_id = None
        
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.status_text.set("Status: Stopped")

    def schedule_next_reminder(self):
        """Schedules the next show_reminder call using Tkinter's event loop."""
        if self.is_running:
            self.timer_id = self.master.after(self.interval_ms, self.show_reminder) #scheduling the function call after interval_ms
            print(f"Next reminder scheduled in {self.interval_ms / (60 * 1000)} minutes.")# Log for debugging/confirmation


    def show_reminder(self):
        """Pops up the reminder message box."""
        if not self.is_running:
            return

        # 1. Select a random tip
        title, message = random.choice(WELLNESS_TIPS)

        # 2. Pop up the message
        # Use a non-blocking dialog (simple info box) so it doesn't halt the main loop
        messagebox.showinfo(title, message)
        
        # 3. Schedule the next reminder right after the current one has been displayed
        self.schedule_next_reminder()

    def on_closing(self):
        """Handles closing the window cleanly."""
        self.stop_reminders()
        self.master.destroy()

if __name__ == "__main__":                                                      #Main Execution
    print("Wellness Reminder App Starting...")                                  #Tkinter requires the main thread for GUI operations
    root = tk.Tk()                                                              #Note: Using Tkinter's `after()` method is preferred over `threading.Timer`
    app = WellnessApp(root)                                                     #for scheduling GUI updates, as it ensures all operations run safely in the main .thread
    root.mainloop()