
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


import PyQt6.QtCore    as QtCore
import PyQt6.QtWidgets as QtWidgets

from . import Tab


# For now it's just copied code from the ScrollableTab and the ImportExportTab
#   In the futur, try to make have only 2 interfaces/super-class :
#   one for Scrollable and one for ImportExport
class ScrollableIETab(Tab.Tab):
    def __init__(self, name: str, classe, box: bool= False):
        super().__init__(name, classe)

        self.__group_box = QtWidgets.QGroupBox()
        self.__group_box.setLayout(self._getLayout())

        self.__scroll = QtWidgets.QScrollArea()
        self.__scroll.setWidget(self.__group_box)
        self.__scroll.setWidgetResizable(True)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.__scroll)

        if box:
            top_layout = QtWidgets.QGridLayout()
            top_box    = QtWidgets.QGroupBox()
            top_box.setLayout(top_layout)
            self.addItemToLayout(top_box, 0, 0)

        button = QtWidgets.QPushButton("Import")
        button.clicked.connect(self.__import)
        if box:
            top_layout.addWidget(button, 0, 0)
        else:
            self.addItemToLayout(button, 0, 0)

        button = QtWidgets.QPushButton("Export")
        button.clicked.connect(self.__export)
        if box:
            top_layout.addWidget(button, 0, 1)
        else:
            self.addItemToLayout(button, 0, 1)


    def __import(self):
        dialog = QtWidgets.QFileDialog()
        dialog.setFileMode(QtWidgets.QFileDialog.FileMode.ExistingFiles)
        dialog.setNameFilter("Text File (*txt)")
        dialog.setWindowTitle("Select a File")
        
        if dialog.exec():
            self._getClass().importData(dialog.selectedFiles()[0])
            
            for i, name in enumerate(self._getClass().getOptionsNames()):
                self.__value_labels[i].setText(str(self._getClass().getValueByName(name)))

    def __export(self):
        dialog = QtWidgets.QFileDialog()
        dialog.setFileMode(QtWidgets.QFileDialog.FileMode.Directory)
        dialog.setOption(QtWidgets.QFileDialog.Option.ShowDirsOnly, True)
        dialog.setWindowTitle("Select a Directory")
        
        if dialog.exec():
            self._getClass().setPath(dialog.selectedFiles()[0])
            self._getClass().print()
