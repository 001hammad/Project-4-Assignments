import tkinter as tk  # python built-in gui graphical tool

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

class EraseCanvas:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.pack()

        self.draw_grid()

        # Bind mouse movement
        self.eraser = None
        self.canvas.bind("<Button-1>", self.place_eraser)
        self.canvas.bind("<Motion>", self.move_eraser)

    def draw_grid(self):
        for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
            for col in range(0, CANVAS_WIDTH, CELL_SIZE):
                self.canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="blue", outline="white")

    def place_eraser(self, event):
        # Draw pink eraser on click
        self.eraser = self.canvas.create_rectangle(
            event.x, event.y,
            event.x + ERASER_SIZE,
            event.y + ERASER_SIZE,
            fill="pink"
        )

    def move_eraser(self, event):
        if self.eraser:
            # Move eraser
            self.canvas.coords(
                self.eraser,
                event.x, event.y,
                event.x + ERASER_SIZE,
                event.y + ERASER_SIZE
            )

            # Erase overlapping blue squares
            overlapping = self.canvas.find_overlapping(event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE)
            for item in overlapping:
                if item != self.eraser:
                    self.canvas.itemconfig(item, fill="white")

def main():
    root = tk.Tk()
    root.title("Eraser Canvas - Tkinter")
    app = EraseCanvas(root)
    root.mainloop()

if __name__ == "__main__":
    main()
