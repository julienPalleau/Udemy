from PySide2 import QtWidgets, QtCore, QtGui

from package.image import CustomImage


class Worker(QtCore.QObject):
    def __init__(self, images_to_convert, quality, size, folder):
        super().__init__()
        self.images_to_convert = images_to_convert
        self.quality = quality
        self.size = size
        self.folder = folder

    def convert_images(self):
        for image_lw_item in self.images_to_convert:
            if not image_lw_item.processed:
                image = CustomImage(path=image_lw_item.text(), folder=self.folder)
                image.reduce_image(size=self.size, quality=self.quality)


class MainWindow(QtWidgets.QWidget):
    def __init__(self, ctx):
        super().__init__()
        self.ctx = ctx
        self.setWindowTitle("PyConverter")
        self.setup_ui()

    def setup_ui(self):
        self.create_widgets()
        self.modify_widgets()
        self.create_layouts()
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_widgets(self):
        self.lbl_quality = QtWidgets.QLabel("Qualite:")
        self.spn_quality = QtWidgets.QSpinBox()
        self.lbl_size = QtWidgets.QLabel("Taille:")
        self.spn_size = QtWidgets.QSpinBox()
        self.lbl_dossierOut = QtWidgets.QLabel("Dossier de sortie:")
        self.le_dossierOut = QtWidgets.QLineEdit()
        self.lw_files = QtWidgets.QListWidget()
        self.btn_convert = QtWidgets.QPushButton("Conversion")
        self.lbl_dropInfo = QtWidgets.QLabel("^ Deposez les images sur l'interface")

    def modify_widgets(self):
        css_file = self.ctx.get_resource("style.css")
        with open(css_file, "r") as f:
            self.setStyleSheet(f.read())

        # Alignement
        self.spn_quality.setAlignment(QtCore.Qt.AlignRight)
        self.spn_size.setAlignment(QtCore.Qt.AlignRight)
        self.le_dossierOut.setAlignment(QtCore.Qt.AlignRight)

        # Range
        self.spn_quality.setRange(1, 100)
        self.spn_quality.setValue(75)
        self.spn_size.setRange(1, 100)
        self.spn_size.setValue(50)

        # Divers
        self.le_dossierOut.setPlaceholderText("Dossier de sortie...")
        self.le_dossierOut.setText("reduced")
        self.lbl_dropInfo.setVisible(False)

        self.setAcceptDrops(True)  # on accepte que l'on puisse deposer des element sur l'interface

    def create_layouts(self):
        self.main_layout = QtWidgets.QGridLayout(self)

    def add_widgets_to_layouts(self):
        self.main_layout.addWidget(self.lbl_quality, 0, 0, 1, 1)
        self.main_layout.addWidget(self.spn_quality, 0, 1, 1, 1)
        self.main_layout.addWidget(self.lbl_size, 1, 0, 1, 1)
        self.main_layout.addWidget(self.spn_size, 1, 1, 1, 1)
        self.main_layout.addWidget(self.lbl_dossierOut, 2, 0, 1, 1)
        self.main_layout.addWidget(self.le_dossierOut, 2, 1, 1, 1)
        self.main_layout.addWidget(self.lw_files, 3, 0, 1, 2)
        self.main_layout.addWidget(self.lbl_dropInfo, 4, 0, 1, 2)
        self.main_layout.addWidget(self.btn_convert, 5, 0, 1, 2)

    def setup_connections(self):
        QtWidgets.QShortcut(QtGui.QKeySequence("Delete"), self.lw_files, self.delete_selected_items)
        self.btn_convert.clicked.connect(self.convert_images)

    def convert_images(self):
        print("Conversion activee")
        quality = self.spn_quality.value()
        size = self.spn_size.value() / 100.0
        folder = self.le_dossierOut.text()

        lw_items = [self.lw_files.item(index) for index in range(self.lw_files.count())]
        images_a_convertir = [1 for lw_item in lw_items if not lw_item.processed]
        if not images_a_convertir:
            msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "Aucune image à convertir",
                                            "Toutes les images ont deja ete converties.")
            msg_box.exec_()
            return False

        self.thread = QtCore.QThread(self)

        self.worker = Worker(images_to_convert=lw_items,
                             quality=quality,
                             size=size,
                             folder=folder)

        print("Debug1")
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.convert_images)
        self.thread.start()
        print("Debug2")

    def delete_selected_items(self):
        for lw_item in self.lw_files.selectedItems():
            row = self.lw_files.row(lw_item)
            self.lw_files.takeItem(row)

    def dragEnterEvent(self, event):
        self.lbl_dropInfo.setVisible(True)
        event.accept()

    def dragLeaveEvent(self, event):
        self.lbl_dropInfo.setVisible(False)

    def dropEvent(self, event):
        event.accept()
        for url in event.mimeData().urls():
            self.add_file(path=url.toLocalFile())

        self.lbl_dropInfo.setVisible(False)

    def add_file(self, path):
        items = [self.lw_files.item(index).text() for index in range(self.lw_files.count())]
        if path not in items:
            lw_item = QtWidgets.QListWidgetItem(path)
            lw_item.setIcon(self.ctx.img_unchecked)
            lw_item.processed = False
            self.lw_files.addItem(lw_item)
