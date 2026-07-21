
"""
----------------------------------------------------------------------------------------------------------------------------------
     _______.  ______  __      ___     .__   __..___________.|| __           __  __  __________      ___     ._______ ._____
    /       | /      ||  |    /   \    |  \ |  ||           |//\  \         /  /|  ||______    |    /   \    |   _   \|  _  \
   |   (----`|  ,----'|  |   /  ^  \   |   \|  |`---|  |----`   \  \   ^   /  / |  |     _/  _/    /  ^  \   |  |_)  || | \  \
    \   \    |  |     |  |  /  /_\  \  |  . `  |    |  |         \  \ / \ /  /  |  |   _/  _/     /  /_\  \  |   ____/| |  )  |
.----)   |   |  `----.|  | /  _____  \ |  |\   |    |  |          \  v   v  /   |  | _/  _/____  /  _____  \ |  |\  \ | |_/  /
|_______/     \______||__|/__/     \__\|__| \__|    |__|           \__/^\__/    |__||__________|/__/     \__\|__| \__\|_____/

----------------------------------------------------------------------------------------------------------------------------------

    Originally developed by G. Léandre

    Version : 1.4.5
    Year :    2026
    Authors : G. Léandre
"""


import PyQt6.QtWidgets as QtWidgets

from . import Tab


class ImportExportTab(Tab.Tab):
    def __init__(self, name: str, classe):
        super().__init__(name, classe)

        button = QtWidgets.QPushButton("Import")
        button.clicked.connect(self.__import)
        self.addItemToLayout(button, 0, 0)

        button = QtWidgets.QPushButton("Export")
        button.clicked.connect(self.__export)
        self.addItemToLayout(button, 0, 1)


    def __import(self):
        dialog = QtWidgets.QFileDialog()
        dialog.setFileMode(QtWidgets.QFileDialog.FileMode.ExistingFiles)
        dialog.setNameFilter("Text File (*txt)")
        dialog.setWindowTitle("Select a File")
        
        if dialog.exec():
            self._getClass().importData(dialog.selectedFiles()[0])
            self._update_import()

    def __export(self):
        dialog = QtWidgets.QFileDialog()
        dialog.setFileMode(QtWidgets.QFileDialog.FileMode.Directory)
        dialog.setOption(QtWidgets.QFileDialog.Option.ShowDirsOnly, True)
        dialog.setWindowTitle("Select a Directory")
        
        if dialog.exec():
            self._getClass().setPath(dialog.selectedFiles()[0])
            self._getClass().print()
