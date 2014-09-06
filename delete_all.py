#deletes all notes

from evernote.api.client import EvernoteClient
from evernote.edam.notestore import NoteStore
import evernote.edam.type.ttypes as Types
from evernote.edam.type.ttypes import NoteSortOrder

dev_token = "S=s1:U=8f631:E=14fa4056736:C=1484c543888:P=1cd:A=en-devtoken:V=2:H=3b6da4e14e167fb9d787cf95523bb20b"
client = EvernoteClient(token=dev_token)

NOTE_STORE = client.get_note_store()

def delete_all():
    notebooks = NOTE_STORE.listNotebooks()
    print ('DELETING ALL NOTES')
    for n in notebooks:
        noteFilter = NoteStore.NoteFilter(order=NoteSortOrder.UPDATED)
        spec = NoteStore.NotesMetadataResultSpec()
        spec.includeTitle = True
        notes = NOTE_STORE.findNotesMetadata(dev_token, noteFilter, 0, 100, spec)
        for note in notes.notes:
            deleteNote(dev_token, note.guid)

delete_all()