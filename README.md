# RPi-Weather-Station-and-Motion-Detection
#
#### Download files, in both SenseHat_Data.py and weather_pictures.py there is a file path that needs to be corrected for the pi to save files in the correct location, the variable is named filePath for SenseHat_Data.py and picPath for weather_pictures.py
#
##### Download senseHat with
###### sudo apt-get install sense-hat
#
##### Enable camera by
###### Raspberry pi application menu -> Preferences -> Raspberry Pi Configuration -> Interfaces, then enable camera
#
##### Make sure python is installed with:
###### sudo apt-get install python
#
##### Also make sure python 3 is installed with:
###### sudo apt-get install python3
#
##### Double check file path variable in both .py files
###### Make sure the file path variable is the correct path for where you want things saved
#
##### Move LXDE into the correct directory with:
###### cp -r /etc/xdg/lxsession ~/.config/
###### Then edit the file with:  sudo nano ~/.config/lxsession/LXDE-pi/autostart
#
##### add the following lines
###### @lxterminal -e file/path/of/launcher_motion.sh
###### @lxterminal -e file/path/of/launcher_SenseHat.sh
#
##### change the file path of the .sh file to the correct path
###### launcher_motion.sh should read:
####### /usr/bin/python file/path/of/weather_pictures.py
###### launcher_SenseHat.sh should read:
####### /usr/bin/python3 file/path/of/SenseHat_Data.py
#### Then save the file and exit, reboot pi 
#
#
#### Send a message or report an issue if it does not work
