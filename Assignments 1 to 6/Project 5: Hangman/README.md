# 🎮 **Project 5: Hangman Game** 💀

#### **Description**
The Hangman game is a word guessing game where the user attempts to guess a hidden word one letter at a time. The game allows a limited number of incorrect guesses (6 in this case). If the user guesses all letters of the word correctly before running out of attempts, they win. If not, the game ends.

---

#### **Code Overview**

```python
import random

def choose_word():
    words = ["python", "hangman", "developer", "programming", "computer"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6

    print("🎩 Welcome to Hangman! 💀")
    
    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter! Try again.")
        elif guess in word:
            guessed_letters.add(guess)
            print("✅ Correct guess!")
        else:
            attempts -= 1
            print(f"❌ Wrong guess! {attempts} attempts left.")
        
        if set(word) == guessed_letters:
            print("\n🎉 Congratulations! You guessed the word:", word)
            return

    print("\n💀 Game Over! The word was:", word)

hangman()
```

---

#### **How It Works**

1. **Choose a Word**: A random word is selected from a predefined list of words.
2. **Display Word**: The word is displayed as underscores (`_`) representing unguessed letters, and correctly guessed letters are shown.
3. **User Guess**: The user is prompted to guess a letter.
4. **Correct Guess**: If the guessed letter is in the word, it is added to the guessed letters, and the word is updated.
5. **Wrong Guess**: If the guessed letter is not in the word, one of the remaining attempts is used up.
6. **Game End**: The game ends if the user guesses all the letters or runs out of attempts. A message is displayed, showing the word and whether the user won or lost.

---

#### **Example Output**

```
🎩 Welcome to Hangman! 💀

Word: _ _ _ _ _ _ _
Guess a letter: p
✅ Correct guess!

Word: p _ _ _ _ _ _
Guess a letter: y
✅ Correct guess!

Word: p y _ _ _ _ _
Guess a letter: z
❌ Wrong guess! 5 attempts left.

...

🎉 Congratulations! You guessed the word: python
```

---

#### **Why Is This Fun?**
🧠 **Brain Challenge**: You have to think of possible letters and form words.  
💥 **Intense**: The pressure of getting guesses right before running out of attempts.  
🎯 **Engaging**: The more words you guess, the better you get!

---
