
```
---------------------------------------------------------------------------------------------------------------------------------
     _______.  ______  __       ___      .__   __. .___________.|| __           __  __  __________      ___     ._______ ._____
    /       | /      ||  |     /   \     |  \ |  | |           |//\  \         /  /|  ||______    |    /   \    |   _   \|  _  \
   |   (----`|  ,----'|  |    /  ^  \    |   \|  | `---|  |----`   \  \   ^   /  / |  |     _/  _/    /  ^  \   |  |_)  || | \  \
    \   \    |  |     |  |   /  /_\  \   |  . `  |     |  |         \  \ / \ /  /  |  |   _/  _/     /  /_\  \  |   ____/| |  ) |
.----)   |   |  `----.|  |  /  _____  \  |  |\   |     |  |          \  v   v  /   |  | _/  _/____  /  _____  \ |  |\  \ | |_/  /
|_______/     \______||__| /__/     \__\ |__| \__|     |__|           \__/^\__/    |__||__________|/__/     \__\|__| \__\|_____/

---------------------------------------------------------------------------------------------------------------------------------
```


# Sciantix'Wizard

A GUI Wizard app to facilitate the use of the Sciantix fission simulation software.
It is made to run on Linux.


## Instalation

### Pre-requisits

Make sure you have python 3.10 or highter installed :

```bash
python3 --version
```

If you don't have it :

```
sudo apt install python3
```

Make sure you have pip 22 or highter installed :

```bash
pip --version
```

If you don't have it :

```
sudo apt install python3-pip
```

### Getting Sciantix'Wizard

Get this app on out github page  :

```bash
git clone https://github.com/sciantix/sciantix-gui.git
```


## How to use it ?

### Opening the app

To open the app, execute the launcher script `Sciantix_Wizzard`, it does not take any arguments :

```bash
./Sciantix_Wizard
```

If you plan on using it often, you can create a symbolic link (shortcut) or add an alias in your `.bashrc` file.

### Using the app

Once launched, you will be presented with a Graphical User Interface (GUI) with tabs :

- The first 4 tabs are the differents input files needed for sciantix to run. You will find in thoses tabs a form-like interface allowing you to fill the input values as you need.

- The 5th tab `Finalize` is to build the input file and run the sciantix simulation.

- The Last 2 tabs are to display and visualize the output of the simulation

The typical use of the app will be :
- Filling the inputs forms
- Runing sciantix
- Inspecting and visualizing the output, maybe copying some of the graphs
- Start again with differents inputs

### Getting the graphs

If you want to use the current graph outside of the gui, it is availible as a .png file at the root of the software.
It is named `plot.png`.

Be warned, it is only the current graph being shown in the GUI.
If you want multiple graphs, you have to copy the `plot.png` file somewhere else for each graphs you want.


### Getting the newly built input files

If you only see 3 files and are missing `input_scaling_factors.txt` it's probably because it's optional. 
You have to go into the 4th tab `Input Scaling Factor` and togle the option to have this file too : if it's red it's off, if it's green it's on.

## Versions

Here is how to read the version numbers :

```
    X . Y . Z
    |   |   └───bug fixes
    |   └───minor versions
    └───major versions
```


## APP architecure

This last section is dedicated to the structure and inner working of the app.

### Generalities

This app is codded in python 3.10, using the PyQt6 GUI Library.
It has been coded on Linux for Linux.

### App structure

The app is build around 2 modules : the gui module (`gui/`) and the classes module (`classes/`). And the simulation software sciantix, which a pre-compiled executable of version 2.2 is included in the `sciantix/` folder.

#### The gui module
It takes care of making the window.
It contains the tabs (`gui/tabs`) submodule that segment each tab in its own class with its own layout and logic to connect to the business logic.

This module act as the frontend of the app.

#### The classes module
It takes care of the business logic and data structure.
It contains 4 submodules:
- The InputFields submodule (`classes/InputFields`) : representation of 1 option/value field that the app will give to it's user
- The InputFiles submodule (`classes/InputFiles`) : structure and setup the fields into 
- The FileAccess submodule (`classes/FileAccess`) : handles accessing files (reading,  printing and ploting)
- The OutputFiles submodule (`classes/OutputFiles`) : representation in memory of the output of Sciantix for the gui

This module act as the backend of the app.

### Config Files

There are 2 config files :
- one for the GUI : `gui/config.py` 
- one for the Business Logic : `classes/config.py` 

### File Tree

```
├─classes/
|   ├─InputFields/
|   |   ├─__init__.py
|   |   ├─InputField.py
|   |   ├─IntervalInputField.py
|   |   └─SetInputField.py
|   ├─InputFiles/
|   |   ├─__init__.py
|   |   ├─InputFile.py
|   |   ├─InputHistory.py
|   |   ├─InputInitialCondition.py
|   |   ├─InputScalingFactor.py
|   |   ├─InputSettings.py
|   |   └─MultiLines.py
|   ├─FileAcess/
|   |   ├─Plotable/
|   |   |   ├─__init__.py
|   |   |   └─Plotable.py
|   |   ├─Printable/
|   |   |   ├─templates/                Representation of how to print a file
|   |   |   ├─__init__.py
|   |   |   └─Printable.py
|   |   ├─Readable/
|   |   |   ├─__init__.py
|   |   |   └─Readable.py
|   |   ├─__init__.py
|   |   └─FileAcess.py
|   ├─OutputFiles/
|   |   ├─__init__.py
|   |   └─OutputFile.py
|   ├─__init__.py
|   └─config.py
├─sciantix/
|   ├─...                               All the input and output .txt files for the simulation
|   └─sciantix.x
├─sciantix/
|   ├─input/                            All the input .txt files for the tests
|   └─output.txt
├─ui/
|   ├─tabs/
|   |   ├─__init__.py
|   |   ├─FinalTab.py
|   |   ├─HistoryTab.py
|   |   ├─InitialConditionTab.py
|   |   ├─OutputTab.py
|   |   ├─ScalingFactorTab.py
|   |   ├─ScrollableTab.py
|   |   ├─SettingsTab.py
|   |   ├─Tab.py
|   |   └─VisualisationTab.py
|   ├─__init__.py
|   ├─config.py
|   └─MainWindow.py
├─.gitignore
├─LICENSE
├─main.py
├─plot.png
├─README.md
├─requirements.txt
├─Sciantix_Wizard                       Launch file
├─tests_input_fields.py                 |
├─tests_input_files.py                  | Make sure that all the logic works properly
└─tests_output_files.py                 |
```
