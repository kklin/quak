from evernote.api.client import EvernoteClient
from evernote.edam.notestore import NoteStore
import evernote.edam.type.ttypes as Types
from evernote.edam.type.ttypes import NoteSortOrder

dev_token = "S=s1:U=8f631:E=14fa4056736:C=1484c543888:P=1cd:A=en-devtoken:V=2:H=3b6da4e14e167fb9d787cf95523bb20b"
client = EvernoteClient(token=dev_token)

NOTE_STORE = client.get_note_store()

def make_new_question(title, content):
    note = Types.Note()
    note.title = title
    note.content = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
    note.content += '<en-note>' + content + '</en-note>'
    note = NOTE_STORE.createNote(note)
    NOTE_STORE.setNoteApplicationDataEntry(dev_token,note.guid,"votes","1")
    return note.guid

#make_new_question('question2', 'testing')

def get_questions():
    notebooks = NOTE_STORE.listNotebooks()
    for n in notebooks:
        noteFilter = NoteStore.NoteFilter(order=NoteSortOrder.UPDATED)
        spec = NoteStore.NotesMetadataResultSpec()
        spec.includeTitle = True
        notes = NOTE_STORE.findNotesMetadata(dev_token, noteFilter, 0, 100, spec)
        for note in notes.notes:
            print('Title: ' + note.title)
            print('Guid: ' + note.guid)
            # print('Content: ' + NOTE_STORE.getNoteContent(dev_token, note.guid))
            print('Application data: ' +
                    NOTE_STORE.getNoteApplicationDataEntry(dev_token,
                        note.guid, "votes"))
            print('=========================================')

def increment_vote(guid):
    new_vote = get_votes(guid) + 1
    NOTE_STORE.setNoteApplicationDataEntry(dev_token,guid,"votes",
            str(new_vote))

def get_votes(guid):
    return int(NOTE_STORE.getNoteApplicationDataEntry(dev_token, guid, "votes"))

def gen_student_note(guids):
    new_note = ""
    for guid in guids:
        note = NOTE_STORE.getNote(dev_token, guid,False,False,False,False)
        new_note += "<b>" + note.title + "</b> (" + str(get_votes(guid)) + " votes) <br/>"
    make_new_question('Questions from Lecture', new_note)

#get_questions()
#increment_vote("a439e498-2e35-4ce5-a799-d0d329df7439")
#guid = make_new_question('Question 4', 'still testing')
#get_questions()
# increment_vote(guid)
    
#def get_question(id):
    # returns Question object
