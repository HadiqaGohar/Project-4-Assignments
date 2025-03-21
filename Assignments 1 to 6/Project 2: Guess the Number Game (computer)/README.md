# 🎮 **Project 2: Guess the Number Game (Computer)** 🤖

#### **Description**  
In this project, the computer attempts to guess the number you're thinking of within a given range (1 to 10). The user provides feedback on whether the guess is too high, too low, or correct, and the computer adjusts its guesses accordingly. It's a fun way to explore how binary search works in practice!

---

#### **Code Overview**

```python
import random

def computer_guess():
    low = 1
    high = 10
    feedback = ""

    print("Think of a number between 1 and 10, and I'll try to guess it! 🤔")

    while feedback != "c":
        guess = random.randint(low, high)
        print(f"My guess is: {guess}")

        feedback = input("Is it too high (h), too low (l), or correct (c)? ").lower()

        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"Yay! I guessed your number {guess} correctly! 🎉")

computer_guess()
```

---

#### **How It Works**  
1. **Initial Setup**: The computer is tasked with guessing a number between 1 and 10.
2. **User Feedback**: The program guesses a random number, and the user provides feedback:
    - **Too high (h)**: The program narrows the range to lower numbers.
    - **Too low (l)**: The program narrows the range to higher numbers.
    - **Correct (c)**: The program celebrates the correct guess.
3. **Binary Search**: By using the feedback, the program continuously adjusts its guesses, effectively using a binary search algorithm.

---

#### **Example Output**

```
Think of a number between 1 and 10, and I'll try to guess it! 🤔
My guess is: 5
Is it too high (h), too low (l), or correct (c)? l
My guess is: 8
Is it too high (h), too low (l), or correct (c)? h
My guess is: 6
Is it too high (h), too low (l), or correct (c)? c
Yay! I guessed your number 6 correctly! 🎉
```

---

#### **Why Is This Fun?**
🤖 **Machine Learning (sort of!)**: The computer "learns" from your feedback and adjusts accordingly.  
🎯 **Efficient Guessing**: It’s a simple example of binary search, which is a great algorithm to learn!  
💻 **Python Practice**: You’ll practice working with loops, conditionals, and user input handling in Python.

---
