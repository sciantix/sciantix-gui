
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

    Version : 1.4.4
    Year :    2026
    Authors : G. Léandre
"""


import PyQt6.QtCore    as QtCore
import PyQt6.QtWidgets as QtWidgets

from . import config
from . import tabs


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, classes):
        super().__init__()

        self.__tab_list = QtWidgets.QTabWidget()
        
        self.setWindowTitle(config.WINDOW_TITLE)
        self.setFixedSize(QtCore.QSize(config.WINDOW_WIDTH, config.WINDOW_HEIGHT))

        # Passing the business logic to the Tabs
        self.__createTabs(classes)

        self.__load_stylesheet()


    def __createTabs(self, classes):
        class_list = [
            # Passing the business logic classes to the corresponding Tabs
            tabs.SettingsTab(classes.InputSettings()),
            tabs.InitialConditionTab(classes.InputInitialCondition()),
            tabs.HistoryTab(classes.InputHistory()),
            tabs.ScalingFactorTab(classes.InputScalingFactor()),
        ]

        for cla in class_list:
            cla.addToTabList(self.__tab_list)

        output = tabs.OutputTab(classes.OutputFile())
        tabs.FinalTab(class_list, output).addToTabList(self.__tab_list)
        output.addToTabList(self.__tab_list)
        tabs.VisualisationTab(output).addToTabList(self.__tab_list)
        
        self.setCentralWidget(self.__tab_list)
    
    def __load_stylesheet(self):
        with open(config.STYLESHEET_PATH, 'r') as stylesheet:
            self.setStyleSheet(stylesheet.read())
