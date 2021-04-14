# Twin Tummy Discord Bot
Say hi to my twin brother Tummy! Made for fun only.... so far 👀

## Sources
https://realpython.com/how-to-make-a-discord-bot-python/ <br />
https://discord.com/developers  <br />
https://github.com/Rapptz/discord.py   <br />
https://discordpy.readthedocs.io/en/latest/ext/commands/api.html?highlight=ctx#context%60 <br />
https://developer.riotgames.com/ <br />
https://www.youtube.com/watch?v=vQw8cFfZPx0&list=RDCMUCR-zOCvDCayyYy1flR5qaAg&index=7  <br />

## Setting up Virtual Enviornment and Modules
<b>Setting up Python and Virtual Environment</b>  
Install Python online  
Linter for Python on Vscode  

py -m venv venv  
./venv/Scripts/activate  
Run vscode as administrator if needed  

.vscode is vscode using the environment  
.venv is the folder to hold all the packages  

<b>Storing Tokens</b>  
pip install python-dotenv  
.env is a file where I can add tokens in the following format:  
name=token (no spaces)  

<b>.gitignore Edits</b>  
Add .vscode, venv/, .env  
Needed to make sure these files don't get uploaded to github  

<b>Installing Modules</b>   
py -m pip install -U discord.py = installing discord for example   

pip freeze = tells you what you have installed  
pip freeze > requirements.txt = copies over the required modules needed  
pip install -r requirements.txt = for when you need to install everything  

<b>Mistakes and Fixes</b>  
If renamed repo > delete venv > reinstall  
Go to the hidden file .git > config > update url for github  

<b>Shortcuts</b>  
Alt + Shift + F = Auto Format with autopep8  

<b>Misc</b>  
Python Classes Constructors have __ init __ as constructor  
Python Classes need self as parameter  
""" Function Comment """ inside the function

## Bot Features  
<b> League of Legends API </b>  
/opgg

<b> LunchTime </b>
To be continued...
