import tkinter as tk

# Canvas settings
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

class EraserApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.pack()
        
        self.cells = {}  # Store references to cells
        self.create_grid()

        # Create eraser
        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="pink", outline="black")

        # Mouse bindings
        self.canvas.bind("<B1-Motion>", self.move_eraser)  # Drag eraser with left-click

    def create_grid(self):
        """Create a grid of blue cells"""
        for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
            for col in range(0, CANVAS_WIDTH, CELL_SIZE):
                cell = self.canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="blue", outline="black")
                self.cells[(col, row)] = cell

    def move_eraser(self, event):
        """Move the eraser and erase cells"""
        x, y = event.x, event.y
        self.canvas.coords(self.eraser, x, y, x + ERASER_SIZE, y + ERASER_SIZE)
        self.erase_cells(x, y)

    def erase_cells(self, x, y):
        """Erase cells in contact with the eraser"""
        for (col, row), cell in self.cells.items():
            if col < x + ERASER_SIZE and col + CELL_SIZE > x and row < y + ERASER_SIZE and row + CELL_SIZE > y:
                self.canvas.itemconfig(cell, fill="white")  # Change cell color to white

def main():
    root = tk.Tk()
    root.title("Eraser Canvas")
    app = EraserApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
