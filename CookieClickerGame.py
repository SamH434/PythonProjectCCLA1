import tkinter as tk
from tkinter import font

#This is a new branch
class CookieClickerGame:
    def __init__(self, master):
        # Initialize the game
        self.master = master
        master.title("Cookie Clicker")

        # Initialize score, cookies per click/second, and items owned
        self.score = 0
        self.cookies_per_click = 1
        self.cookies_per_sec = 0
        self.cursors = 0
        self.workers = 0
        self.factories = 0

        # Create cookie button
        self.cookie_button = tk.Button(master, text="Cookie", command=self.click_cookie, bg="black", fg="white", font=("Arial", 30, "bold"))
        self.cookie_button.config(width=10, height=3)  # Adjust button size
        self.cookie_button.grid(row=0, column=0, padx=10, pady=10)  # Add padding

        # Create label to display score
        self.score_label = tk.Label(master, text="Score: 0", font=("Arial", 12, "bold"))
        self.score_label.grid(row=0, column=1, padx=10, pady=10)  # Add padding

        # Create frame for unlock buttons
        self.unlock_frame = tk.Frame(master)
        self.unlock_frame.grid(row=0, column=2, rowspan=3, padx=10, pady=10)  # Add padding

        # Create buttons to unlock items
        self.unlock_cursor_button = tk.Button(self.unlock_frame, text="Cursor - 10", command=self.buy_cursor, font=("Times", 20, "bold"))
        self.unlock_cursor_button.grid(row=0, column=0, padx=10, pady=5)  # Add padding

        self.unlock_worker_button = tk.Button(self.unlock_frame, text="Worker - 25", command=self.buy_worker, font=("Times", 20, "bold"))
        self.unlock_worker_button.grid(row=1, column=0, padx=10, pady=5)  # Add padding

        self.unlock_factory_button = tk.Button(self.unlock_frame, text="Factory - 50", command=self.buy_factory, font=("Times", 20, "bold"))
        self.unlock_factory_button.grid(row=2, column=0, padx=10, pady=5)  # Add padding

        self.unlock_factory_button = tk.Button(self.unlock_frame, text="Granny - 100", command=self.buy_factory, font=("Times", 20, "bold"))
        self.unlock_factory_button.grid(row=2, column=0, padx=10, pady=5)  # Add padding

        # Create label to display items owned
        self.items_label = tk.Label(master, text="Cursors: 0\nWorkers: 0\nFactories: 0", font=("Arial", 12, "bold"))
        self.items_label.grid(row=1, column=1, padx=10, pady=10, sticky="n")  # Add padding and set alignment

        # Start the game
        self.update_score()
        self.update_items()

    # Function to handle clicking the cookie
    def click_cookie(self):
        self.score += self.cookies_per_click
        self.update_score()

    # Function to buy a cursor
    def buy_cursor(self):
        if self.score >= 10:
            self.score -= 10
            self.cookies_per_sec += 1
            self.cursors += 1
            self.update_score()
            self.update_items()
            self.master.after(5000, self.generate_cookies)

    # Function to buy a worker
    def buy_worker(self):
        if self.score >= 20:
            self.score -= 20
            self.cookies_per_sec += 10
            self.workers += 1
            self.update_score()
            self.update_items()
            self.master.after(5000, self.generate_cookies)

    # Function to buy a factory
    def buy_factory(self):
        if self.score >= 50:
            self.score -= 50
            self.cookies_per_sec += 15
            self.factories += 1
            self.update_score()
            self.update_items()
            self.master.after(5000, self.generate_cookies)

        # Function to buy grannys
    def buy_factory(self):
        if self.score >= 50:
            self.score -= 50
            self.cookies_per_sec += 750
            self.factories += 1
            self.update_score()
            self.update_items()
            self.master.after(5000, self.generate_cookies)

    # Function to generate cookies every 5 seconds
    def generate_cookies(self):
        self.score += self.cookies_per_sec
        self.update_score()
        self.master.after(5000, self.generate_cookies)

    # Function to update the score label
    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")

    # Function to update the items label
    def update_items(self):
        self.items_label.config(text=f"Cursors: {self.cursors}\nWorkers: {self.workers}\nFactories: {self.factories}")

# Create the main window
root = tk.Tk()
root.geometry("600x300")  # Set window size

# Get the window width and height
window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()

# Calculate position x and y for the window to be centered
position_x = int(root.winfo_screenwidth() / 2 - window_width / 2)
position_y = int(root.winfo_screenheight() / 2 - window_height / 2)

# Set the window to be centered
root.geometry(f"+{position_x}+{position_y}")

# Create an instance of the game
game = CookieClickerGame(root)

# Start the GUI event loop
root.mainloop()
