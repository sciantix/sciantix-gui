<<<<<<< HEAD
<<<<<<< HEAD
# sciantix-gui
=======
# sciantix-input-builder
A GUI builder for sciantix inputs files
>>>>>>> c7d61c3 (Initial commit)
=======

```
---------------------------------------------------------------------------------------------------------------------------------
     _______.  ______  __       ___      .__   __. .___________.|| __           __  __  __________      ___     ._______ ._____
    /       | /      ||  |     /   \     |  \ |  | |           |//\  \         /  /|  ||______    |    /   \    |   _   \|  _  \
   |   (----`|  ,----'|  |    /  ^  \    |   \|  | `---|  |----`   \  \   ^   /  / |  |     _/  _/    /  ^  \   |  |_)  || | \  \
    \   \    |  |     |  |   /  /_\  \   |  . `  |     |  |         \  \ / \ /  /  |  |   _/  _/     /  /_\  \  |   ____/| |  ) |
.----)   |   |  `----.|  |  /  _____  \  |  |\   |     |  |          \  v   v  /   |  | _/  _/____  /  _____  \ |  |\  \ | |_/  /
|_______/     \______||__| /__/     \__\ |__| \__|     |__|           \__/^\__/    |__||__________|/__/     \__\|__| \__\|_____/

<<<<<<< HEAD
A GUI Wizard to build inputs files for sciantix
>>>>>>> 0612e7e (updated the README)
=======
---------------------------------------------------------------------------------------------------------------------------------
```


# Sciantix'Wizard

A GUI Wizard app to build inputs files for the Sciantix fission simulation software.
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

### Getting Sciantix'Wizard

Get this app on out github page  :

```bash
git clone https://github.com/Zaynn-lea/sciantix-input-builder.git
```


## How to use it ?

### Opening the app

To open the app, execute the launcher script `Sciantix_Wizzard`, it does not take any arguments :

```bash
./Sciantix_Wizard
# or
<Your/Path>/Sciantix_Wizard
```

If you plan on using it often, you can create a symbolic link (shortcut) or add an alias in your `.bashrc` file.

### Using the app

Once launched, you will be presented with a Graphical User Interface (GUI) with 5 tabs :

- Tabs 1 to 4 are the differents input files needed for sciantix to run. You will find in thoses tabs a form-like interface allowing you to fill the input values as you need.

- Tabs 5 `Finalize` is to build the input file and add a custom output path.

### Getting the newly built input files

By default, the input files end up in the `sciantix-input-builder` folder. You can change it in the Finalize tab.

If you only see 3 files and are missing `input_scaling_factors.txt` it's probably because it's optional. 
You have to go into the 4th tab `Input Scaling Factor` and togle the option to have this file too.


## APP architecure

This last section is dedicated to the structure and inner working of the app.

### Generalities

This app is codded in python 3.10, using the PyQt6 GUI Library.
It has been coded on Linux for Linux.

### App structure

The app is build around 2 modules :
- The gui module : `sciantix-input-builder/gui/` 
- The classes module : `sciantix-input-builder/classes/` 

#### The gui module
It takes care of making the window.
It contains the tabs (`sciantix-input-builder/gui/tabs`) submodule that segment each tab in its own class with its own layout and logic to connect to the business logic.

This module act as the frontend of the app.

#### The classes module
It takes care of the business logic and data structure.
It contains 3 submodules:
- The InputFields submodule (`sciantix-input-builder/classes/InputFields`) : representation of 1 option/value field that the app will give to it's user
- The InputFiles submodule (`sciantix-input-builder/classes/InputFiles`) : structure and setup the fields into 
- The printable submodule (`sciantix-input-builder/classes/printable`) : handles outputing to files

This module act as the backend of the app.

### Config Files

There are 2 config files :
- one for the GUI : `sciantix-input-builder/gui/config.py` 
- one for the Business Logic : `sciantix-input-builder/classes/config.py` 

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
|   |   └─InputSettings.py
|   ├─printable/
|   |   ├─templates/                Representation of how to print a file
|   |   ├─__init__.py
|   |   └─Printable.py
|   ├─__init__.py
|   └─config.py
├─ui/
|   ├─tabs/
|   |   ├─__init__.py
|   |   ├─FinalTab.py
|   |   ├─HistoryTab.py
|   |   ├─InitialConditionTab.py
|   |   ├─ScalingFactorTab.py
|   |   ├─SettingsTab.py
|   |   └─Tab.py
|   ├─__init__.py
|   ├─config.py
|   └─MainWindow.py
├─.gitignore
├─main.py
├─README.md
├─Sciantix_Wizard                   Launch file
└─test.py                           Make sure that all the logic works properly
<<<<<<< HEAD
>>>>>>> d75c30d (Drafted the README.md + minor fixes)
=======
```
>>>>>>> e280e7c (oups, formating error in the README)
