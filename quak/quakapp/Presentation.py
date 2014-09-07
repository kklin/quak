class Presentation:

    def __init__(self, title, questions, guid):
        self.title = title
        self.questions = questions
        self.guid = guid

    def __repr__(self):
        return "Title: " + self.title + " ; GUID: " + self.guid
