from evernote.api.client import EvernoteClient
from evernote.edam.notestore import NoteStore
import evernote.edam.type.ttypes as Types
from evernote.edam.type.ttypes import NoteSortOrder
from Question import Question
from Presentation import Presentation
import auth

client = EvernoteClient(token = auth.dev_token) # this token will be the
                                                # token of presenter
NOTE_STORE = client.get_note_store()

def get_sorted_questions(guid): # guid of the notebook
    questions = get_questions(guid)
    questions.sort(key = lambda x: x.votes)
    questions.reverse()
    return questions

def get_questions(guid): # guid of the notebook
    questions = []
    noteFilter = NoteStore.NoteFilter(order=NoteSortOrder.UPDATED)
    noteFilter.notebookGuid = guid
    spec = NoteStore.NotesMetadataResultSpec()
    spec.includeTitle = True
    notes = NOTE_STORE.findNotesMetadata(auth.dev_token, noteFilter, 0 , 100, spec)
    for note in notes.notes:
        votes = get_votes(note.guid)
        questions += [ Question(note.title, '', votes,note.guid, NOTE_STORE) ]
    return questions

def get_votes(guid):
    return int(NOTE_STORE.getNoteApplicationDataEntry(auth.dev_token, guid, "votes"))

def get_presentation(guid):
    notebook_title = NOTE_STORE.getNotebook(auth.dev_token, guid).name
    notebook_questions = get_questions(guid)
    return Presentation(notebook_title, notebook_questions, guid)

def make_question(question_text, guid): # guid of the notebook to add to
    note = Types.Note()
    note.title = question_text
    note.content = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
    note.content += '<en-note></en-note>'
    note.notebookGuid = guid
    try:
        note = NOTE_STORE.createNote(note)
    except Exception:
        return None
    NOTE_STORE.setNoteApplicationDataEntry(auth.dev_token, note.guid, "votes", "1")
    question = Question(question_text, '', 1, note.guid, NOTE_STORE)
    return question

def make_presentation(title):
    notebook = Types.Notebook()
    notebook.name = title
    try:
        return NOTE_STORE.createNotebook(auth.dev_token, notebook).guid
    except Exception:
        return None

def gen_student_evernote(notebook_guid, token): # guid of the notebook containing q's
    questions = get_sorted_questions(notebook_guid)
    presentation = get_presentation(notebook_guid)
    new_note_text = ""
    for i in range(5 if len(questions) > 5 else len(questions)):
        new_note_text += "<b>" + questions[i].question + "</b> (" + str(questions[i].votes) + " votes) <br/><br/>"
    note = Types.Note()
    note.title = 'Top Questions from ' + presentation.title
    note.content = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
    note.content += '<en-note>' + new_note_text + '</en-note>'
    client = EvernoteClient(token=token)
    student_note_store = client.get_note_store()
    student_note_store.createNote(token, note)

def get_question_by_guid(guid):
    note = NOTE_STORE.getNote(auth.dev_token, guid, False, False, False, False)
    return Question(note.title, '', get_votes(guid), guid, NOTE_STORE)
