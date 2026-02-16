import tkinter as tk

class ModelApp:
    def __init__(self):
        self.planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
        self.counter = 0
    
    def step_up(self):
        self.counter += 1
        if self.counter >= len(self.planets):
            self.counter = 0
    
    def get_values(self):
        return self.planets[self.counter]
    
class ViewApp(tk.Frame):
    def __init__(self, master, on_click):
        super().__init__(master)
        self.pack()

        self.label = tk.Label(self, text="", bg="white", fg="black", width=25, height=3, font=("Arial", 14), relief="solid", bd=2)      
        self.label.pack()

        button = tk.Button(self, text="PRESS", command=on_click)
        button.pack()

    def update_label(self, text):
        self.label.config(text=text)

class ControllerApp:
    def __init__(self, root):
        self.model = ModelApp()
        self.view = ViewApp(root, self.on_click)
        self.update_view()

    def on_click(self):
        self.model.step_up()
        self.update_view()

    def update_view(self):
        value = self.model.get_values()
        self.view.update_label(value)

if __name__ == "__main__":
    root = tk.Tk()
    app = ControllerApp(root)
    root.mainloop()