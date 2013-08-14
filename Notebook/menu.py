import sys
from notebook import Note, Notebook

class Menu:
    """Display a menu and respond to choices when run."""
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
                 "1": self.show_notes,
                 "2": self.search_notes,
                 "3": self.add_note,
                 "4": self.modify_note,
                 "5": self.quit
                 }

    def display_menu(self):
        print("""
        Notebook Menu
            
        1. Show all Notes
        2. Search Notes
        3. Add Note
        4. Modify Note
        5. Quit
        """)
    
    def run(self):
        """Display the menu and respond to the choices."""
        self.display_menu()