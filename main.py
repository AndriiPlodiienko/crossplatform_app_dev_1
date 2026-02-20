import tkinter as tk

class ModelApp:
    def __init__(self):
        self.planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
        self.counter = 0
    
    def step_up(self):
        self.counter += 1
        if self.counter >= len(self.planets):
            self.counter = 0
    
    def step_down(self):
        self.counter -= 1
        if self.counter < 0:
            self.counter = len(self.planets) - 1
    
    def reset(self):
        self.counter = 0
    
    def get_values(self):
        return self.planets[self.counter]
    
class ViewApp(tk.Frame):
    def __init__(self, master, on_back_click, on_forward_click, on_reset_click):
        super().__init__(master)
        self.pack()

        self.label = tk.Label(self, text="", bg="white", fg="black", width=25, height=3, font=("Arial", 14), relief="solid", bd=2)      
        self.label.pack()

        button_frame = tk.Frame(self)
        button_frame.pack()

        back_button = tk.Button(button_frame, text="Back", command=on_back_click, width=10)
        back_button.pack(side=tk.LEFT, padx=5)

        forward_button = tk.Button(button_frame, text="Forward", command=on_forward_click, width=10)
        forward_button.pack(side=tk.LEFT, padx=5)

        reset_button = tk.Button(button_frame, text="Reset", command=on_reset_click, width=10)
        reset_button.pack(side=tk.LEFT, padx=5)

    def update_label(self, text):
        self.label.config(text=text)

class ControllerApp:
    def __init__(self, root):
        self.model = ModelApp()
        self.view = ViewApp(root, self.on_back_click, self.on_forward_click, self.on_reset_click)
        self.update_view()

    def on_back_click(self):
        self.model.step_down()
        self.update_view()

    def on_forward_click(self):
        self.model.step_up()
        self.update_view()

    def on_reset_click(self):
        self.model.reset()
        self.update_view()

    def update_view(self):
        value = self.model.get_values()
        self.view.update_label(value)

if __name__ == "__main__":
    root = tk.Tk()
    app = ControllerApp(root)
    root.mainloop()