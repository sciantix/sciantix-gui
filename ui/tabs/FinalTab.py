
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

import datetime
import os

from . import Tab
from .. import config


class FinalTab(Tab.Tab):
    __slots__ = [
        # From the Tab super-class
        "__name",
        "__class",
        "__layout",
        "_option",

        # From the FinalTabs class
        "__classes",
        "__output",
        "__visualisation",
        "__name",
    ]

    def __init__(self, classes, output, visualisation):
        super().__init__("Finalize", None)

        self.__classes       = classes
        self.__output        = output
        self.__visualisation = visualisation
        self.__name          = ""

        self.__setPath(config.DEFAULT_OUTPUT_PATH)


        button = QtWidgets.QPushButton("\nRun the Simulation\n")
        button.clicked.connect(self.__runSciantix)
        self.addItemToLayout(button, 1, 0)

        # little spacers
        self.addItemToLayout(QtWidgets.QLabel(), 0, 0)
        self.addItemToLayout(QtWidgets.QLabel(), 2, 0)


        layout = QtWidgets.QGridLayout()
        box    = QtWidgets.QGroupBox()
        box.setLayout(layout)
        self.addItemToLayout(box, 3, 0)

        layout.addWidget(QtWidgets.QLabel("Name the Simulation"), 0, 0)

        input_name = QtWidgets.QLineEdit()
        input_name.textChanged.connect(self.__setName)
        layout.addWidget(input_name, 0, 1)


        layout = QtWidgets.QGridLayout()
        box    = QtWidgets.QGroupBox()
        box.setLayout(layout)
        self.addItemToLayout(box, 4, 0)

        button = QtWidgets.QPushButton("Import Imput Files")
        button.clicked.connect(lambda : self.__dialog(self.__import))
        layout.addWidget(button, 0, 0)

        button = QtWidgets.QPushButton("Import and Run")
        button.clicked.connect(lambda : self.__dialog(self.__importRun))
        layout.addWidget(button, 0, 1)

        button = QtWidgets.QPushButton("Export Input Files")
        button.clicked.connect(lambda : self.__dialog(self.__export))
        layout.addWidget(button, 0, 2)

        button = QtWidgets.QPushButton("Export Everything")
        button.clicked.connect(lambda : self.__dialog(self.__exportAll))
        layout.addWidget(button, 0, 3)
        

    def __setPath(self, text):
        for cla in self.__classes:
            cla.setPath(text)

        self.__output.setPath(text)

    def __submit(self):
        for cla in self.__classes:
            if cla.getOption():
                cla.print()

    def __runSciantix(self):
        # To clean the input and output files
        os.system(f"rm {config.SIMULATION_PATH}/*.txt")

        self.__setPath(f"{config.SIMULATION_PATH}")
        self.__submit()
        os.system(f"{config.SIMULATION_PATH}/sciantix.x {config.SIMULATION_PATH}/")

        self.__output.read()
    
    def __setName(self, text):
        self.__name = text
    
    def __generateName(self) -> str:
        date_time          = str(datetime.datetime.now()).split('.')[0]
        date_time_formated = date_time.replace(' ', '_').replace('-', '_').replace(':', '_')
        return f"simulation_{date_time_formated}"

    def __dialog(self, function):
        dialog = QtWidgets.QFileDialog()
        dialog.setFileMode(QtWidgets.QFileDialog.FileMode.Directory)
        dialog.setOption(QtWidgets.QFileDialog.Option.ShowDirsOnly, True)
        dialog.setWindowTitle("Select a Directory")
        
        if dialog.exec():
            function(dialog.selectedFiles()[0])
    
    def __import(self, path: str):
        for cla in self.__classes:
            if os.path.exists(f"{path}/{cla.getClassName()}.txt"):
                cla.importFrom(f"{path}/{cla.getClassName()}.txt")
    
    def __importRun(self, path: str):
        self.__import(path)
        self.__runSciantix()
    
    def __export(self, path: str):
        if self.__name:
            name = self.__name
        else:
            name = self.__generateName()

        os.makedirs(f"{path}/{name}")

        for cla in self.__classes:
            cla.exportTo(f"{path}/{name}")
    
    def __exportAll(self, path: str):
        if self.__name:
            name = self.__name
        else:
            name = self.__generateName()

        os.makedirs(f"{path}/{name}")
        os.makedirs(f"{path}/{name}/inputs")
        os.makedirs(f"{path}/{name}/outputs")

        for cla in self.__classes:
            cla.exportTo(f"{path}/{name}/inputs")
        
        self.__output.exportTo(f"{path}/{name}/outputs")
        self.__visualisation.exportGraphs(f"{path}/{name}/outputs")
        