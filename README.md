# RPi-Weather-Station-and-Motion-Detection
#
#### Download files, in both SenseHat_Data.py and weather_pictures.py there is a file path that needs to be corrected for the pi to save files in the correct location, the variable is named filePath for SenseHat_Data.py and picPath for weather_pictures.py
#
##### Second download LXDE
###### Then edit the file with $ sudo nano ~/.config/lxsession/LXDE-pi/autostart
#
##### add the following lines
###### @lxterminal -e file/path/of/launcher_motion.sh
###### @lxterminal -e file/path/of/launcher_SenseHat.sh
#
#### Then save the file and exit, reboot pi and test if it works
