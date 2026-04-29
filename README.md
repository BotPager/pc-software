
# Readme
Python pc software for team 22 low cost pager

# Installation
1. Downloaded latest release from github
1. In files app double click application
1. Click allow unverified software
1. Installation complete

# Development environment
## Helpful links for code development
https://python.meshtastic.org/
https://github.com/meshtastic/python/blob/master/meshtastic/protobuf/channel_pb2.pyi
https://github.com/meshtastic/python/blob/master/meshtastic/protobuf/config_pb2.pyi
## Installation
1. Install QtCreator from https://www.qt.io/development/tools/qt-creator-ide
1. Clone the repository
1. Enter directory
3. Create and Enter a virtual environment .venv or using your standard python install type Python "python -m pip install requirements.txt"

### Alternate option
https://devenv.sh/
This repository provides a devenv.nix file this is useful if the user is running NixOs or another linux distribution. It provides the required libraries and QTCreator. The pyside6 library that ships however is missing the wheel that contains the ability to update the ui.py so a sepeate pyside6 install is reuqired to convert the PCUI.ui file to a .py file. As such this is not a recommended option unless the user is running Nixos for development. 
## UI Development
QT documetation: https://doc.qt.io/qtforpython-6/
The UI should be edited by opening PCUI.ui in QTCreator. 
### Icons
Add icons and other images to the ./App/Icons folder
The resources.qrc file is strucured as follows and is used to refrence the icons
```
<RCC>
    <qresource prefix="/">
        <file>icons/green-led-on.png</file>
        <file>icons/led-red-on.png</file>
    </qresource>
</RCC>
```
After adding the entry to resources.qrc generate the required rc_resources.py file by running ```pyside6-rcc icons.qrc -o rc_icons.py```

### Converting .Ui edits to python .py
After editing the .ui file convert it to PCUI.py by running ```pyside6-uic PCUI.ui > ui_PCUI.py```

# Operation Manual
## Device connection
* System will autoconnect fastest when software is started and a gateway/pager is plugged in after.
* Plugging in gateway/pager prior to application start will work however a 10 second delay may occur.
## Team setup
The PC software will automatically attempt to load a teams.txt file in the location where the application was launched from.
Each line of teams.txt is as follows #teamnumber, #pid.
Manual entry of teams is permitted and follows the same order of teamnumber then pid for the 16 teams. Set teams will update the list of teams and write the list to teams.txt. Clicking clear teams will reset the list of teams to blank.
## Automatic

## Manual
Manual mode allows for messaging groups of 4 teams or 1 single team.
The 4 team option uses the first 2 selected teams as the red team and the second 2 as blue. This format is only used for normal messaging and does not include parts requests.
Both buttons allow for the use of selecting arenas 1-8 and parts requests.
## Provisioning
This function currently works with the caveat that threading was not implemented for this function prior to senior design ending. This means the Ui freezes while the pager's settings are changed.
This function sets the device radio  preset to long_moderate. Sets up the primary channel with a non default(not AQ==) key and adds the AQ== channel as secondary. As well to compy with FTC rules regarding bluetooth the ESP32's bluetooth is turned off.
The function grabs the shortname of the pager and tries to add it to the manual teams page starting at the first empty pid entry. If no empty entry it will overwrite entries starting from 0 until it reaches 15. 

