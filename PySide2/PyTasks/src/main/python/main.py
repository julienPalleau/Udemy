from fbs_runtime.application_context.PySide2 import ApplicationContext, cached_property

import sys

from package.main_window import MainWindow


if __name__ == '__main__':
    appctxt = ApplicationContext()
    window = MainWindow()
    #window.resize(900, 600)
    window.show()
    exit_code = appctxt.app.exec_()
    sys.exit(exit_code)
