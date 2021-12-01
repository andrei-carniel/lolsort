class Champion:

    def __init__(self, id = 0, name = "", ban = False):
        self.id = id  # INTEGER PRIMARY KEY AUTOINCREMENT
        self.name = name  # TEXT NOT NULL
        self.ban = ban