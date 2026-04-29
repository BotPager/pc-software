
# Readme
Python pc software for team 22 low cost pager

## Installation
1. Downloaded latest release from github
1. In files app double click application
1. Click allow unverified software
1. Installation complete
## Helpful links for code development
https://python.meshtastic.org/
https://github.com/meshtastic/python/blob/master/meshtastic/protobuf/channel_pb2.pyi
https://github.com/meshtastic/python/blob/master/meshtastic/protobuf/config_pb2.pyi
## Operation Manual
### Device connection
* System will autoconnect fastest when software is started and a gateway/pager is plugged in after.
* Plugging in gateway/pager prior to application start will work however a 10 second delay may occur.
### Team setup
The PC software will automatically attempt to load a teams.txt file in the location where the application was launched from.
Each line of teams.txt is as follows #teamnumber, #pid.
Manual entry of teams is permitted and follows the same order of teamnumber then pid for the 16 teams. Set teams will update the list of teams and write the list to teams.txt. Clicking clear teams will reset the list of teams to blank.
### Automatic

### Manual
Manual mode allows for messaging groups of 4 teams or 1 single team.
The 4 team option uses the first 2 selected teams as the red team and the second 2 as blue. This format is only used for normal messaging and does not include parts requests.
Both buttons allow for the use of selecting arenas 1-8 and parts requests.
### Provisioning
This function currently works with the caveat that threading was not implemented for this function prior to senior design ending. This means the Ui freezes while the pager's settings are changed.
This function sets the device radio  preset to long_moderate. Sets up the primary channel with a non default(not AQ==) key and adds the AQ== channel as secondary. As well to compy with FTC rules regarding bluetooth the ESP32's bluetooth is turned off.
The function grabs the shortname of the pager and tries to add it to the manual teams page starting at the first empty pid entry. If no empty entry it will overwrite entries starting from 0 until it reaches 15. 

