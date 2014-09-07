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
    return questions

def get_questions(guid): # guid of the notebook
    questions = []
    noteFilter = NoteStore.NoteFilter(order=NoteSortOrder.UPDATED)
    noteFilter.notebookGuid = guid
    spec = NoteStore.NotesMetadataResultSpec()
    spec.includeTitle = True
    notes = NOTE_STORE.findNotesMetadata(auth.dev_token, noteFilter, 0 , 100, spec)
    for note in notes.notes:
        questions += [ Question(note.guid, NOTE_STORE) ]
    return questions

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
    question = Question(note.guid, NOTE_STORE)
    return question

def make_presentation(title):
    notebook = Types.Notebook()
    notebook.name = title
    try:
        return NOTE_STORE.createNotebook(auth.dev_token, notebook).guid
    except Exception:
        return None

def gen_student_evernote(notebook_guid): # guid of the notebook containing q's
    questions = get_sorted_questions()
    new_note = ""
    for question in questions:
        new_note += "<b>" + question.question + "</b> (" + str(question.votes)
        + " votes) <br/><br/>"
    # get student's oauth and add to their account

def get_question_by_guid(guid):
    return Question(guid, NOTE_STORE)
