import datetime

# Store the next available if for all new notes
last_id = 0

class Note:
    """Represents a note in the notebook. Match against a
       string in searches and store tags for each note."""

    def __init__(self, memo, tags = ""):
        """Initializes a note with memo and optional space-separated tags.
           Automatically set the note's creation date and a unique id."""
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()

        global last_id
        last_id += 1
        self.id = last_id

