from datetime import datetime

class Task:
    def __init__(self, id=None, text="", date=datetime.now()):
        self.id = id
        self.text = text
        self.date = date
