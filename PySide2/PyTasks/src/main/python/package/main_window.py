from PySide2 import QtWidgets, QtCore, QtGui

import package.api.task

COLORS = {False: (235, 64, 52), True: (160, 237, 83)}


class TaskItem(QtWidgets.QListWidgetItem):
    def __init__(self, name, done, list_widget):
        super().__init__(name)

        self.list_widget = list_widget
        self.done = done
        self.name = name

        self.setSizeHint(QtCore.QSize(self.sizeHint().width(), 25))
        self.list_widget.addItem(self)
        self.set_background_color()

    def toggle_state(self):
        self.done = not self.done
        package.api.task.set_tasks_statut(name=self.name, done=self.done)
        self.set_background_color()

    def set_background_color(self):
        color = COLORS.get(self.done)
        self.setBackgroundColor(QtGui.QColor(*color))  # * means unpacking
        color_str = ", ".join(map(str, color))
        stylesheet = f"""QListView::item:selected {{background: rgb({color_str}); 
                                                    color: rgb(0, 0, 0);}}"""
        self.list_widget.setStyleSheet(stylesheet)


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyTasks")
        self.setup_ui()
        self.get_tasks()

    def setup_ui(self):
        self.create_widgets()
        self.modify_widgets()
        self.create_layouts()
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_widgets(self):
        pass

    def modify_widgets(self):
        self.lw_tasks = QtWidgets.QListWidget()
        self.btn_add = QtWidgets.QPushButton("Add")
        self.btn_clean = QtWidgets.QPushButton("Clean")
        self.btn_quit = QtWidgets.QPushButton("Quit")

    def create_layouts(self):
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.layout_buttons = QtWidgets.QHBoxLayout()

    def add_widgets_to_layouts(self):
        self.main_layout.addWidget(self.lw_tasks)
        self.main_layout.addLayout(self.layout_buttons)

        self.layout_buttons.addWidget(self.btn_add)
        self.layout_buttons.addStretch()  # permet d'avoir le bouton add a gauche et les 2 autres boutons a droite
        # le strech a lieu entre le bouton add et les boutons clean et quit
        self.layout_buttons.addWidget(self.btn_clean)
        self.layout_buttons.addWidget(self.btn_quit)

    def setup_connections(self):
        self.btn_add.clicked.connect(self.add_task)
        self.lw_tasks.itemClicked.connect(lambda lw_item: lw_item.toggle_state())

    def add_task(self):
        task_name, ok = QtWidgets.QInputDialog.getText(self,
                                                       "Ajouter un tache",
                                                       "Nom de la tache :")
        if ok and task_name:
            package.api.task.add_task(name=task_name)
            self.get_tasks()

    def get_tasks(self):
        self.lw_tasks.clear()
        tasks = package.api.task.get_tasks()
        for task_name, done in tasks.items():
            TaskItem(name=task_name, done=done, list_widget=self.lw_tasks)
