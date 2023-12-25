```python
import tkinter as tk
from design_suggestions import DesignSuggestions

class UserInterface:
    def __init__(self, root, data_path, model_path):
        self.root = root
        self.design_suggestions = DesignSuggestions(data_path, model_path)
        self.create_widgets()

    def create_widgets(self):
        self.user_input_label = tk.Label(self.root, text="Enter your preferences:")
        self.user_input_label.pack()

        self.user_input_entry = tk.Entry(self.root)
        self.user_input_entry.pack()

        self.submit_button = tk.Button(self.root, text="Submit", command=self.get_suggestions)
        self.submit_button.pack()

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

    def get_suggestions(self):
        user_input = self.user_input_entry.get()
        design_suggestion = self.design_suggestions.get_design_suggestions(user_input)
        self.result_label.config(text=f"Suggested Design: {design_suggestion}")

if __name__ == "__main__":
    root = tk.Tk()
    app = UserInterface(root, "data_path", "model_path")
    root.mainloop()
```
