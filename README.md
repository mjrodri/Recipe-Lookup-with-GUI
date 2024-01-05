# Recipe Finder

The Recipe Finder is a Python-based GUI application designed to simplify the process of discovering recipes based on user-input food items. Developed using the tkinter library, this application provides an intuitive interface for users to enter a list of ingredients, triggering a search for relevant recipes via the Edamam API.

Features
User-Friendly Interface: The GUI features an easy-to-use entry field for food items and a search button to initiate the recipe search.
API Integration: Utilizes the Edamam API to fetch recipe information based on the user's input.
Error Handling: Provides user-friendly error messages through pop-up alerts in case of missing input.
Getting Started
Clone the repository to your local machine.
bash
Copy code
git clone https://github.com/your-username/RecipeFinder.git
Navigate to the project directory.
bash
Copy code
cd RecipeFinder
Install the required dependencies (tkinter and requests).
bash
Copy code
pip install tk requests
Run the application.
bash
Copy code
python recipe_finder.py
Usage
Launch the application.
Enter a list of food items into the provided text field (comma-separated).
Click the "Search Recipes" button.
View the results in a pop-up window, displaying recipe names and corresponding URLs.
Dependencies
tkinter: Python's standard GUI library for creating interactive interfaces.
requests: Simplifies HTTP requests to the Edamam API for recipe retrieval.
Contributing
Contributions are welcome! Feel free to open issues or pull requests for any improvements or additional features you'd like to see.

License
This project is licensed under the MIT License.
