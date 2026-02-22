class Book:
    """A class to represent a book."""
    
    def __init__(self, title, author, year):
        """
        Initialize a Book object.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            year (int): The year of publication
        """
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):
        """Return a formatted string representation of the book."""
        return f"{self.title} by {self.author} ({self.year})"
    
    def get_age(self):
        """Calculate and return the age of the book based on publication year."""
        current_year = 2025
        return current_year - self.year


class EBook(Book):
    """A class to represent an electronic book, inheriting from Book."""
    
    def __init__(self, title, author, year, file_size):
        """
        Initialize an EBook object.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            year (int): The year of publication
            file_size (int): The file size in megabytes
        """
        super().__init__(title, author, year)
        self.file_size = file_size
    
    def __str__(self):
        """Return a formatted string representation of the ebook including file size."""
        parent_str = super().__str__()
        return f"{parent_str} - {self.file_size} MB"


if __name__ == "__main__":
    # minimal demo when run as a script
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    print(book1)