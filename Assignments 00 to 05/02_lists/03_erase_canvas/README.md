
# **🖌️ Erase Canvas - Python Tkinter App 🎨**  

This repository contains a **GUI-based Eraser Canvas Application** built with **Tkinter**. It allows users to erase a grid of cells interactively using a draggable eraser. The project demonstrates event handling, canvas manipulation, and basic animations in **Python Tkinter**. 🚀  

## 📌 **Project Overview**  
This application features a **grid-based canvas**, where each cell is initially filled with a blue color. Users can **drag an eraser** over the grid to change the color of the cells to white, simulating an erasing effect.  

---

## 🔹 **Features & Functionalities**  

### 🎨 **Canvas with Grid Cells**  
- The canvas is **400x400 pixels**, divided into **40x40 pixel blue cells**.  
- Each cell is stored in a dictionary for efficient access and modification.  

### 🖱️ **Mouse-controlled Eraser**  
- A **pink eraser** (20x20 pixels) follows the mouse movement when the left button is clicked and dragged.  
- As the eraser moves over a cell, the cell **changes color from blue to white**.  

### 🛠️ **Event Handling with Tkinter**  
- **`<B1-Motion>` event** is used to track mouse movement while holding the left-click.  
- The eraser position updates dynamically to follow the cursor.  

### 🎯 **Customizable Settings**  
- Canvas size, grid size, eraser size, and colors can be easily modified.  
- The eraser color can be changed to different shades for better visibility.  

---

## 🏗️ **Project Structure**  

📂 **Project Directory:**  
```
Project-4-Assignments/Assignments 00 to 05/02_lists/03_erase_canvas/
│── main.py  # Main script for the Eraser Canvas Application
```

📄 **File Breakdown:**  
- **`main.py`** → Contains the complete Tkinter GUI application, including canvas creation, event handling, and eraser logic.  

---

## 🛠️ **How It Works**  

1️⃣ **Initialize Tkinter Window**  
- Creates a **400x400 px canvas** with a **blue grid** using `tk.Canvas()`.  
- Generates a dictionary to store cell references.  

2️⃣ **Draw the Grid**  
- Loops through the canvas dimensions to draw **40x40 px squares** filled with blue color.  

3️⃣ **Create an Eraser**  
- A **pink square (20x20 px)** represents the eraser, initialized at the top-left corner.  

4️⃣ **Mouse Event Handling**  
- `<B1-Motion>` event moves the eraser along with the cursor.  
- The eraser **updates its coordinates dynamically** based on cursor position.  

5️⃣ **Erasing Cells**  
- The function checks **which cells are under the eraser** and changes their fill color to white.  

6️⃣ **Run the Application**  
- The main function initializes the Tkinter window and starts the main loop.  

---

## ▶️ **How to Run the Project**  

### 🔧 **Prerequisites**  
Make sure you have **Python** installed. Tkinter is built into Python, so no additional installations are required.  

### 🏃 **Run the Application**  
```sh
python main.py
```
This will open a **Tkinter window** with a **blue grid** and a draggable eraser. 🎨  

---

## 🎯 **Customization Options**  

You can modify various settings in the `main.py` file:  

| **Setting**  | **Description** | **Default Value** |
|-------------|----------------|------------------|
| `CANVAS_WIDTH` | Width of the canvas | `400 px` |
| `CANVAS_HEIGHT` | Height of the canvas | `400 px` |
| `CELL_SIZE` | Size of each grid cell | `40 px` |
| `ERASER_SIZE` | Size of the eraser | `20 px` |
| `bg="white"` | Background color of the canvas | `"white"` |
| `fill="blue"` | Initial color of grid cells | `"blue"` |
| `fill="pink"` | Eraser color | `"pink"` |

To **change grid size**, update `CELL_SIZE` accordingly.  
To **change eraser size**, modify `ERASER_SIZE`.  

---

## 📌 **Learning Outcomes**  
This project is a great way to learn:  
✅ **GUI programming with Tkinter** 🖼️  
✅ **Handling mouse events in Python** 🖱️  
✅ **Canvas drawing and animations** 🎨  
✅ **Dictionary-based data management** 🔢  

---

## 📜 **Future Enhancements**  
🚀 Add an option to change the eraser size dynamically.  
🚀 Implement a "Reset Canvas" button to refill erased cells.  
🚀 Introduce multiple eraser colors or brush types.  

---

## 🎯 **Final Thoughts**  
This **Eraser Canvas App** is a beginner-friendly **Python GUI project** that demonstrates **event handling, interactive UI design, and drawing on a canvas using Tkinter**. 🐍💡  

🔗 **Perfect for beginners exploring GUI development in Python!** 🚀  

---
