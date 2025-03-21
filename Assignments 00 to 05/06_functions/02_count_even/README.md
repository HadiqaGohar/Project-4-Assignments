# **🔢 COUNT EVEN NUMBERS - FUNCTION**  

### **📌 Functionality**  
This program counts and prints the number of **even numbers** in a list entered by the user.  

### **📝 How It Works?**  
1. **`count_even(lst)`**  
   - Takes a list as input.  
   - Uses **list comprehension** to count how many numbers are even.  
   - Prints the total count.  

2. **`get_list_of_ints()`**  
   - Asks the user to input numbers **one by one**.  
   - Stops when the user presses **Enter**.  
   - Handles invalid inputs (non-numeric values).  

3. **`main()`**  
   - Calls `get_list_of_ints()` to get user input.  
   - Calls `count_even(lst)` to count and print the even numbers.  

### **🔍 Example Runs**  
#### **✅ Input:**
```
Enter an integer or press enter to stop: 1  
Enter an integer or press enter to stop: 2  
Enter an integer or press enter to stop: 3  
Enter an integer or press enter to stop: 4  
Enter an integer or press enter to stop:   
```
#### **📌 Output:**
```
2
```
(Since `2` and `4` are even numbers)  

🎯 **Try entering different numbers and see the count change!** 🚀
