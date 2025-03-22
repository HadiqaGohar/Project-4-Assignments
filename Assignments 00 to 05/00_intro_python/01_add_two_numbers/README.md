# **📝 01_add_two_numbers – Improved Addition Program** 🚀  

This Python script takes two numbers as user input, adds them together, and displays the result. The updated version includes enhancements for better **error handling, user experience, and readability.** Let's break it down in detail!  

---

## **🔍 Old Code Explanation**  

### **🔹 How the Old Code Works**
1️⃣ **Defines `main()` Function:** Runs the program logic.  
2️⃣ **Takes User Input:** Accepts two numbers using `input()`.  
3️⃣ **Performs Addition:** Adds the two numbers.  
4️⃣ **Displays Output:** Prints the sum.  
5️⃣ **Executes When Run Directly:** Uses `if __name__ == '__main__':` to ensure the script runs only when executed directly.  

---

## **🔄 New Code - Key Enhancements & Explanation**  

```python
from termcolor import colored
```
✅ **Why Import `termcolor`?**  
This library is used to **add colors to text output**, improving readability in the terminal.  

```python
print(colored("\n\t\t\t +-+-+ Sum of two numbers +-+-+ \n", "light_magenta"))
```
✅ **Enhanced User Interface**  
Instead of plain text, **formatted and colored headings** make the output visually appealing.  

---

### **1️⃣ Why Use `while True`?**
```python
while True:
    try:
        value1 = int(input(colored("Enter the first number: ", "light_cyan")))
        break
    except ValueError:
        print(colored("❌ Invalid input! Please enter a valid number.", "red"))
```
✅ **Purpose:**  
- Ensures the user **enters only valid integers** before proceeding.  
- **Keeps asking** until a valid number is entered.  

✅ **Why Use `try-except`?**  
- Prevents the program from **crashing** if a user enters text instead of a number.  
- **Handles errors gracefully** by displaying a user-friendly message.  

💡 **Repeating this logic for `value2` ensures both numbers are valid before moving forward!**  

---

### **2️⃣ Addition & Displaying the Result**
```python
total_value = value1 + value2
print(colored(f"The total value is {total_value}.", "yellow"))
print(colored("\n\t\t\t +-+-+ End of the program +-+-+ \n", "light_magenta"))
```
✅ **Why Use Colored Output?**  
- `yellow` makes the **final sum stand out**.  
- Adds a **closing message** to indicate the program has finished execution.  

---

### **3️⃣ Why Use `if __name__ == '__main__':`?**
```python
if __name__ == '__main__':
    sum()
```
✅ **Why Not `if __name__ == '__sum__':`?**  
- `__name__` is a **built-in variable** that Python uses to determine whether a script is being **run directly or imported**.  
- The correct built-in value is `'__main__'`, **not `__sum__`**, which is why using `__sum__` would **not work**!  

---

## **🛠️ Summary of Improvements**  
🔹 **✔️ Error Handling:** Prevents invalid inputs.  
🔹 **🔄 Loops for Validation:** Ensures only valid numbers are used.  
🔹 **🎨 Colored Text Output:** Improves UI.  
🔹 **📜 Cleaner Code Structure:** Easier to read and understand.  

This enhanced version makes the script **more robust, user-friendly, and visually appealing!** 🚀
