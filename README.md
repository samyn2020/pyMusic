# pyMusic  
🎶 Plays mp3 and wav files from a given directory with python  
____________
Dependencies  
---------------
* Python  
  * https://www.python.org/  
* playsound  
  * https://pypi.org/project/playsound/  
* PySimpleGUI  
  * https://pypi.org/project/PySimpleGUI/  
____________
Features  
---------------
* shuffle  
  * rearranges playlist  
* repeat  
  * replays playlist  
* wait  
  * plays a noise, then waits for user input (enter) to play next song  
* list  
  * prints each song title in its own line  
____________
Notes  
---------------
* The sfx folder and pyMusic.py need to be in the same folder  
* Append features to directory to toggle them (in this case, shuffle and list)  
  * `C:\your\music\directory\?shuffle?list`  
* Leaving the directory blank will cause the player to use the desktop as the chosen directory  
  * typing a folder name that is on your desktop will set that folder as the chosen directory  
* Sometimes a high enough bitrate file will cause a PlaysoundException, which is handled:  
  * plays an alert noise (don't worry, it's not loud)  
  * prints ` | bitrate too high | ` in front of the title  
  * waits for user input to continue  
____________
Upcoming
---------------  
  * - [ ] boombox
    * https://pypi.org/project/boombox/
    * supports more filetypes  
