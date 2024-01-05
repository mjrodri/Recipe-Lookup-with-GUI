import tkinter as tk
from tkinter import messagebox
import requests

class RecipeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Recipe Finder")

        # Create GUI elements
        self.label = tk.Label(root, text="Enter foods (comma-separated):")
        self.label.pack(pady=10)

        self.food_entry = tk.Entry(root, width=40)
        self.food_entry.pack(pady=10)

        self.search_button = tk.Button(root, text="Search Recipes", command=self.search_recipes)
        self.search_button.pack(pady=10)

    def search_recipes(self):
        # Get user input
        foods = self.food_entry.get().strip()

        if not foods:
            messagebox.showerror("Error", "Please enter at least one food item.")
            return

        # Make API request to Edamam
        api_key = "YOUR_EDAMAM_API_KEY"  # Replace with your actual API key
        base_url = "https://api.edamam.com/search"
        params = {
            "q": foods,
            "app_id": "YOUR_EDAMAM_APP_ID",  # Replace with your actual app ID
            "app_key": api_key,
        }

        response = requests.get(base_url, params=params)
        data = response.json()

        # Display recipe information (customize this part based on Edamam API response format)
        recipes = data.get("hits", [])
        if not recipes:
            messagebox.showinfo("Results", "No recipes found.")
        else:
            results_text = "\n".join([f"{hit['recipe']['label']}\n{hit['recipe']['url']}" for hit in recipes])
            messagebox.showinfo("Results", results_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = RecipeApp(root)
    root.mainloop()
