from PySide2 import QtWidgets, QtGui

from package.api.note import Note, get_notes

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyNotes")

        self.setup_ui()
        self.populate_notes()

    def setup_ui(self):
        self.create_widgets()
        self.create_layouts()
        self.modify_widgets()
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_widgets(self):
        self.btn_createNote = QtWidgets.QPushButton("Creer une note")
        self.lw_notes = QtWidgets.QListWidget()
        self.te_contenu = QtWidgets.QTextEdit()

    def modify_widgets(self):
        pass

    def create_layouts(self):
        self.main_layout = QtWidgets.QGridLayout(self)

    def add_widgets_to_layouts(self):
        self.main_layout.addWidget(self.btn_createNote, 0, 0, 1, 1)
        self.main_layout.addWidget(self.lw_notes, 1, 0, 1, 1)
        self.main_layout.addWidget(self.te_contenu, 0, 1, 2, 1)

    def setup_connections(self):
        self.btn_createNote.clicked.connect(self.create_note)
        self.te_contenu.textChanged.connect(self.save_note)
        self.lw_notes.itemSelectionChanged.connect(self.populate_note_content)
        QtWidgets.QShortcut(QtGui.QKeySequence("Delete"), self.lw_notes, self.delete_selected_note)

    # END UI

    def add_note_to_listwidget(self, note):
        lw_item = QtWidgets.QListWidgetItem(note.title)
        lw_item.note = note
        self.lw_notes.addItem(lw_item)

    def create_note(self):
        titre, resultat = QtWidgets.QInputDialog.getText(self, "Ajouter une note", "Titre: ")
        if resultat and titre:
            note = Note(title=titre)
            note.save()
            self.add_note_to_listwidget(note)

    def delete_selected_note(self):
        print("Suppression de la note")

    def populate_notes(self):
        notes = get_notes()
        for note in notes:
            self.add_note_to_listwidget(note)

    def populate_note_content(self):
        print("Charegement du contenu de la note")

    def save_note(self):
        print("Sauvegarde du contenu de la note")
