# 🔐 **Project 7: Random Password Generator** 🔑

#### **Description**
This project generates random passwords based on the user's input. It allows the user to specify the number of passwords to generate and the desired length for each password. The generated passwords include a mix of uppercase letters, lowercase letters, digits, and special characters for enhanced security.

---

#### **Code Overview**

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# User input
num_passwords = int(input("Enter number of passwords to generate: "))
password_length = int(input("Enter password length: "))

print("\nGenerated Passwords:")
for _ in range(num_passwords):
    print(generate_password(password_length))
```

---

#### **How It Works**

1. **Password Generation**:
   - The `generate_password` function creates a random password by selecting characters from a combination of uppercase letters, lowercase letters, digits, and punctuation.
   - The `random.choice` method is used to select a random character from the set, and this process is repeated for the specified length.
   
2. **User Input**:
   - The program asks the user for two inputs:
     - The number of passwords to generate (`num_passwords`).
     - The desired length of each password (`password_length`).
   
3. **Output**:
   - The program then generates and prints the specified number of random passwords with the given length.

---

#### **Example Output**

```
Enter number of passwords to generate: 3
Enter password length: 12

Generated Passwords:
n7Zk5Tg!4@NQ
l#Y3svB%0Wrp
mP&8qxL^2Vdk
```

---

#### **Key Features**
- **Customizable Length**: The user can specify the length of each password.
- **Multiple Passwords**: The user can generate multiple passwords at once.
- **Strong Passwords**: The generated passwords contain a mix of characters, ensuring they are strong and secure.

---
