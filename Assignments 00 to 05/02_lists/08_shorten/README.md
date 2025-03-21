# **📌 Shorten List - Python List Trimming Program 🚀**  

This script limits a list to a **maximum length of 3** by removing excess elements. It demonstrates **list manipulation, loops, and user input handling** in Python.  

---

## 📌 **Project Overview**  
- **User inputs** elements into a list.  
- If the list exceeds **3 elements**, the **excess elements are removed** from the end.  
- Removed elements are **printed** as they are removed.  

---

## 🛠️ **How It Works**  

1️⃣ **User Inputs List Elements**  
- Elements are added to a list until the user presses **Enter without typing anything**.  

2️⃣ **Check List Length**  
- If the list has more than **3 elements**, remove extras **one by one** from the end.  

3️⃣ **Print Removed Elements**  
- Each removed element is printed to track what was discarded.  

---

## 📜 **Code Explanation**  

```python
MAX_LENGTH = 3  # Define maximum allowed list length

def shorten(lst):
    while len(lst) > MAX_LENGTH:  # Remove elements if the list is too long
        last_elem = lst.pop()  # Remove last element
        print(last_elem)  # Print removed element

def get_lst():
    lst = []  # Initialize empty list
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":  # Keep collecting input
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop: ")
    return lst

def main():
    lst = get_lst()  # Get user-inputted list
    shorten(lst)  # Call function to shorten the list

if __name__ == '__main__':
    main()
```

### **🔹 `shorten(lst)` - Trimming the List**  
- Uses a **while loop** to check if the list length exceeds **3**.  
- **Removes elements** from the end using `.pop()`.  
- **Prints** each removed element.  

### **🔹 `get_lst()` - Collecting User Input**  
- **Takes user input** and stores it in a list.  
- Stops taking input when the user presses **Enter without typing anything**.  

---

## 🏗️ **Project Structure**  

📂 **Project Directory:**  
```
Project-4-Assignments/Assignments 00 to 05/02_lists/08_shorten/
│── main.py  # Python script to limit list length
```

📄 **File Breakdown:**  
- **`main.py`** → Handles list input and trimming.  

---

## ▶️ **How to Run the Project**  

### 🔧 **Prerequisites**  
Ensure you have **Python installed** on your system.  

### 🏃 **Run the Application**  
```sh
python main.py
```
This will start the script, allowing user input and list shortening.  

---

## 🎯 **Expected Output**  

**Example Run:**  
```
Please enter an element of the list or press enter to stop: apple
Please enter an element of the list or press enter to stop: banana
Please enter an element of the list or press enter to stop: cherry
Please enter an element of the list or press enter to stop: mango
Please enter an element of the list or press enter to stop: orange
Please enter an element of the list or press enter to stop: 
orange
mango
```

### **Final List (After Removing Extra Elements)**
```python
['apple', 'banana', 'cherry']
```

---

## 🛠️ **Customization Options**  

| **Modification** | **How to Implement** |
|-----------------|----------------------|
| Change max list length | Modify `MAX_LENGTH = <new_value>` |
| Print final list after trimming | Add `print(lst)` after `shorten(lst)` |
| Remove elements from the beginning instead of the end | Use `lst.pop(0)` instead of `lst.pop()` |

---

## 🎯 **Learning Outcomes**  
✅ **List manipulation (adding & removing elements)** 📋  
✅ **Using loops & conditions for input handling** 🔄  
✅ **Understanding list size constraints** 🛠️  

---

## 🎯 **Final Thoughts**  
This **Shorten List Program** is a great Python exercise for **list handling, user input processing, and constraints implementation**. 🚀🐍  

🔗 **Perfect for beginners looking to understand list operations in Python!**  
