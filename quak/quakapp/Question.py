import auth

class Question:


    def __init__(self, question, answer, votes, guid, note_store):
        self.NOTE_STORE = note_store
        self.question = question
        self.answer = answer
        self.votes = votes
        self.guid = guid

#    def __init__(self, guid, note_store):
#        self.NOTE_STORE = note_store
#        self.guid = guid
#        note = self.NOTE_STORE.getNote(auth.dev_token, self.guid, False, False, False, False)
#        self.question = note.title
#        self.answer = ""
#        self.sync_vote_count()

    def sync_vote_count(self):
        self.votes = int(self.NOTE_STORE.getNoteApplicationDataEntry(auth.dev_token, self.guid, "votes"))

    def increment_vote_count(self):
        self.sync_vote_count()
        self.NOTE_STORE.setNoteApplicationDataEntry(auth.dev_token, self.guid,"votes", str(self.votes + 1))

    def __repr__(self):
        return "Question: " + self.question + " ; Votes: " + str(self.votes) + " ; guid: " + self.guid;
