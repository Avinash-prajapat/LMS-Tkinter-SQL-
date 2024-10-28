import tkinter as tk  # Importing tkinter for GUI
from tkinter import messagebox  # Importing messagebox for alert messages

# Book class to store details of a book
class Book:
    def __init__(self, book_id, title, author, category):
        self.book_id = book_id  # Unique identifier for the book
        self.title = title  # Title of the book
        self.author = author  # Author of the book
        self.category = category  # Category or genre of the book
        self.is_available = True  # Initially, the book is available for lending

    # Method to display book details
    def display_info(self):
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, " \
               f"Category: {self.category}, Available: {'Yes' if self.is_available else 'No'}"

# Library class to manage library operations
class Library:
    def __init__(self):
        self.books = []  # List to store all books in the library

    # Method to add a new book to the library
    def add_book(self, book):
        self.books.append(book)  # Append the book to the list of books

    # Method to issue a book based on book_id
    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id and book.is_available:  # Check if book is available
                book.is_available = False  # Mark the book as issued
                return f"Book '{book.title}' issued successfully."
        return "Book not available or invalid ID."  # Message for unavailability or wrong ID

    # Method to return a book based on book_id
    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id and not book.is_available:  # Check if the book was issued
                book.is_available = True  # Mark the book as available
                return f"Book '{book.title}' returned successfully."
        return "Invalid book ID or the book was not issued."  # Error message if invalid ID

    # Method to retrieve all books in the library
    def get_all_books(self):
        if not self.books:  # If no books are available
            return ["No books available in the library."]
        return [book.display_info() for book in self.books]  # Return a list of book details

# GUI Application class
class LibraryGUI:
    def __init__(self, root):
        self.library = Library()  # Create an instance of Library

        root.title("Library Management System")  # Set the window title
        # Welcome message
        welcome_label = tk.Label(root, text="Welcome to the Library Management System!", font=("Arial", 16))
        welcome_label.pack(pady=10)  # Display welcome message with padding

        # Add Book Section
        self.add_frame = tk.Frame(root)  # Frame for adding books
        self.add_frame.pack(pady=10)

        tk.Label(self.add_frame, text="Book ID:").grid(row=0, column=0, padx=5)  # Label for Book ID
        self.book_id_entry = tk.Entry(self.add_frame)  # Entry field for Book ID
        self.book_id_entry.grid(row=0, column=1, padx=5)  # Place entry field in the grid

        tk.Label(self.add_frame, text="Title:").grid(row=1, column=0, padx=5)  # Label for Title
        self.title_entry = tk.Entry(self.add_frame)  # Entry field for Title
        self.title_entry.grid(row=1, column=1, padx=5)  # Place entry field in the grid

        tk.Label(self.add_frame, text="Author:").grid(row=2, column=0, padx=5)  # Label for Author
        self.author_entry = tk.Entry(self.add_frame)  # Entry field for Author
        self.author_entry.grid(row=2, column=1, padx=5)  # Place entry field in the grid

        tk.Label(self.add_frame, text="Category:").grid(row=3, column=0, padx=5)  # Label for Category
        self.category_entry = tk.Entry(self.add_frame)  # Entry field for Category
        self.category_entry.grid(row=3, column=1, padx=5)  # Place entry field in the grid

        self.add_button = tk.Button(self.add_frame, text="Add Book", command=self.add_book)  # Button to add book
        self.add_button.grid(row=4, columnspan=2, pady=10)  # Place button in the grid

        # Issue and Return Section
        self.action_frame = tk.Frame(root)  # Frame for issuing and returning books
        self.action_frame.pack(pady=10)

        tk.Label(self.action_frame, text="Book ID:").grid(row=0, column=0, padx=5)  # Label for Book ID
        self.action_id_entry = tk.Entry(self.action_frame)  # Entry field for action Book ID
        self.action_id_entry.grid(row=0, column=1, padx=5)  # Place entry field in the grid

        self.issue_button = tk.Button(self.action_frame, text="Issue Book", command=self.issue_book)  # Button to issue book
        self.issue_button.grid(row=1, column=0, pady=10)  # Place button in the grid

        self.return_button = tk.Button(self.action_frame, text="Return Book", command=self.return_book)  # Button to return book
        self.return_button.grid(row=1, column=1, pady=10)  # Place button in the grid

        # Display Books Section
        self.books_frame = tk.Frame(root)  # Frame for displaying books
        self.books_frame.pack(pady=10)

        self.display_button = tk.Button(self.books_frame, text="Display Books", command=self.display_books)  # Button to display books
        self.display_button.pack()  # Place button in the frame

        self.books_list = tk.Listbox(self.books_frame, width=80, height=10)  # Listbox to show all books
        self.books_list.pack()  # Place listbox in the frame

    # Method to add a new book
    def add_book(self):
        try:
            book_id = int(self.book_id_entry.get())  # Get Book ID from entry
            title = self.title_entry.get()  # Get Title from entry
            author = self.author_entry.get()  # Get Author from entry
            category = self.category_entry.get()  # Get Category from entry

            # Check if any field is empty
            if not title or not author or not category:
                raise ValueError("All fields are required.")  # Raise error if fields are empty

            new_book = Book(book_id, title, author, category)  # Create a new book object
            self.library.add_book(new_book)  # Add the book to the library
            messagebox.showinfo("Success", f"Book '{title}' added successfully.")  # Show success message

            self.clear_entries()  # Clear the entry fields after adding
        except ValueError as e:
            messagebox.showerror("Error", str(e))  # Show error message for invalid input

    # Method to issue a book
    def issue_book(self):
        try:
            book_id = int(self.action_id_entry.get())  # Get Book ID from action entry
            message = self.library.issue_book(book_id)  # Issue the book and get message
            messagebox.showinfo("Info", message)  # Show info message
        except ValueError:
            messagebox.showerror("Error", "Invalid Book ID.")  # Show error message for invalid input

    # Method to return a book
    def return_book(self):
        try:
            book_id = int(self.action_id_entry.get())  # Get Book ID from action entry
            message = self.library.return_book(book_id)  # Return the book and get message
            messagebox.showinfo("Info", message)  # Show info message
        except ValueError:
            messagebox.showerror("Error", "Invalid Book ID.")  # Show error message for invalid input

    # Method to display all books in the Listbox
    def display_books(self):
        self.books_list.delete(0, tk.END)  # Clear the Listbox
        books = self.library.get_all_books()  # Get the list of books
        for book_info in books:  # Loop through the list of books
            self.books_list.insert(tk.END, book_info)  # Insert each book detail into the Listbox

    # Method to clear input entries after adding a book
    def clear_entries(self):
        self.book_id_entry.delete(0, tk.END)  # Clear the Book ID entry
        self.title_entry.delete(0, tk.END)  # Clear the Title entry
        self.author_entry.delete(0, tk.END)  # Clear the Author entry
        self.category_entry.delete(0, tk.END)  # Clear the Category entry

# Main program to run the GUI
if __name__ == "__main__":
    root = tk.Tk()  # Create the main application window
    app = LibraryGUI(root)  # Create an instance of the LibraryGUI class
    root.mainloop()  # Start the GUI event loop
