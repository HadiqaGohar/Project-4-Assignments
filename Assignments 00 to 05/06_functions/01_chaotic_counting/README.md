# **🎲 CHAOTIC COUNTING - FUNCTION DESCRIPTION**  

### **🔢 Functionality**  
This program counts from **1 to 10**, but there’s a twist! A random chance determines whether the counting stops early, making it unpredictable.  

### **📝 How It Works?**  
1. **`chaotic_counting()`**  
   - Counts from `1 to 10`, but may stop randomly based on probability.  
   - Calls the `done()` function to check if it should stop.  

2. **`done()`**  
   - Uses a **20% chance** (`DONE_LIKELIHOOD = 0.2`) to return `True`, stopping the count early.  

3. **`main()`**  
   - Prints a message before starting the count.  
   - Calls `chaotic_counting()` and displays "I'm done" at the end.  

### **📌 Possible Output Examples**  
```
I'm going to count until 10 or until I feel like stopping, whichever comes first.  
1  
2  
3  
I'm done  
```
_or_
```
I'm going to count until 10 or until I feel like stopping, whichever comes first.  
1  
2  
3  
4  
5  
6  
7  
8  
9  
10  
I'm done  
```

🎲 **Unpredictable every time! Try running it to see what happens!** 🚀
