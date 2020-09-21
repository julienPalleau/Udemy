import os
import json
from uuid import uuid4
from glob import glob

from package.api.constants import NOTES_DIR


def get_notes():
    notes = []
    fichiers = glob(os.path.join(NOTES_DIR, "*.json"))
    for fichier in fichiers:
        with open(fichier, "r") as f:
            node_data = json.load(f)
            note_uuid = os.path.splitext(os.path.basename(fichier))[0]
            note_title = node_data.get("title")
            note_content = node_data.get("content")
            note = Note(uuid=note_uuid, title=note_title, content=note_content)
            notes.append(note)
    return notes


class Note:
    def __init__(self, title="", content="", uuid=None):
        if uuid:
            self.uuid = uuid
        else:
            self.uuid = str(uuid4())

        self.title = title
        self.content = content

    def __repr__(self):
        return f"{self.title} ({self.uuid})"

    def __str__(self):
        return self.title

    @property
    def content(self):
        return self._content  # _content est une variable privee et cela evite une recursion infinie.

    @content.setter  # Permet de controller se que l'on met dans content. Dans ce cas ci on veut uniquement du text.
    def content(self, value):
        if isinstance(value, str):
            self._content = value
        else:
            raise TypeError("Valeur invalide (besoin d'unce chaine de caracteres).")

    def delete(self):
        os.remove(self.path)
        if os.path.exists(self.path):
            return False
        return True

    @property  # faire un propriete, permet d'appeler n.path sans avoir à mettre de () (n.path au lieu de n.path())
    def path(self):
        return os.path.join(NOTES_DIR, self.uuid + ".json")

    def save(self):
        if not os.path.exists(NOTES_DIR):
            os.makedirs(NOTES_DIR)

        data = {"title": self.title, "content": self.content}
        with open(self.path, "w") as f:
            json.dump(data, f, indent=4)


if __name__ == '__main__':
    notes = get_notes()
    print(notes)