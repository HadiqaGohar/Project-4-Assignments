# ⏳ **Project 6: Countdown Timer** ⏰

#### **Description**
This countdown timer allows users to input a duration in seconds. The timer then counts down and displays the remaining time in a `MM:SS` format. Once the timer reaches zero, it prints a message indicating that time is up.

---

#### **Code Overview**

```python
import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer_format = f"{mins:02d}:{secs:02d}"
        print(timer_format, end="\r")
        time.sleep(1)
        seconds -= 1

    print("⏰ Time's up!")

# User se input lena
seconds = int(input("Enter countdown time in seconds: "))
countdown_timer(seconds)
```

---

#### **How It Works**

1. **User Input**: The user is asked to input the number of seconds for the countdown.
2. **Countdown Logic**: The `countdown_timer` function takes the inputted number of seconds and converts it to minutes and seconds using `divmod`.
3. **Display Time**: It displays the countdown in `MM:SS` format. The timer updates every second.
4. **Timer Completion**: When the countdown reaches zero, it prints a "Time's up!" message.

---

#### **Example Output**

```
Enter countdown time in seconds: 120
02:00
01:59
01:58
...
⏰ Time's up!
```

---

#### **Key Features**
- **Real-time countdown**: The time is updated every second.
- **Formatted Output**: Displays the countdown in a clear and easy-to-read `MM:SS` format.
- **End Alert**: Once the timer finishes, it shows a "Time's up!" message.

---
